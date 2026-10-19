# ReleaseTruth

A standalone GenLayer Intelligent Contract that checks published release notes against complete, version-bound source changes. GenLayer is the adjudicator: each validator fetches GitHub evidence independently, verifies commitments and assesses the locked review policy. There is no frontend or centralized AI verdict service.

## What it returns

| Outcome | Meaning |
|---|---|
| ACCURATE | All changes in this bounded comparison are non-material or correctly disclosed; every notes claim is assessable. |
| MATERIAL_OMISSIONS | At least one material change is missing, without a detected contradiction. |
| MISLEADING | At least one release-note assertion contradicts a material code/spec change. |
| INCONCLUSIVE | Evidence, coverage or interpretation is inadequate. This is never an approval. |

Uncertainty takes precedence over all definitive outcomes. Otherwise contradiction takes precedence over omission. Per-file classifications and grounded quotations remain available for inspection.

## API

- `review(manifest_json: str, attempt: int = 0) -> str`: permissionless review; returns content-addressed request ID. Each ID is immutable and cannot be overwritten.
- `get_review(request_id: str) -> str`: canonical JSON record, or empty string if missing.
- `get_policy() -> str`: the policy and its SHA-256 commitment. Policy is fixed in the deployed source, with no administrative override.

Manifest schema:

```json
{"repo":"owner/project","base":"40 lowercase hex characters","head":"40 lowercase hex characters","notes":"RELEASE_NOTES.md","hashes":{"b:src/file.py":"64 lowercase hex SHA-256","h:src/file.py":"64 lowercase hex SHA-256","h:RELEASE_NOTES.md":"64 lowercase hex SHA-256"}}
```

`b:` is the base version; `h:` is the head. Supply every existing side of every changed file plus head release notes. Added files have only `h:`, removed files only `b:`. Unexpected or missing hashes are rejected as inconclusive. `tools/build_manifest.py` prepares the exact manifest from GitHub; validators independently repeat retrieval and verification. Only full immutable commit IDs are accepted, never moving tags, branches or caller URLs.

## Evidence and consensus

The GitHub compare endpoint establishes the ancestor relationship and complete bounded file list. Returned base, merge-base, final head and commit count must match. Every changed file is fetched in full at both versions, so truncated diff patches are never used. Exact HTTPS GitHub URLs are constructed internally from validated components. SHA-256 checks bind raw UTF-8 content to the manifest. GitHub serves as the source authority; this does not prove a human identity, signed publisher approval, binary reproducibility or tag ownership.

Each validator independently fetches the comparison, code/spec files and notes, verifies all hashes, and calls its own model with the same immutable policy. The custom equivalence function requires exact agreement on evidence fingerprint, failure reason, outcome and every changed file's classification. Quotations and explanatory prose may differ. Model output must satisfy exact schema, full file coverage, bounded explanations and literal source citation checks. Disagreement rejects consensus; it is not silently converted into an accepted verdict.

The request hash commits the canonical manifest, policy hash and attempt number. Attempts 1 and 2 require the preceding immutable record to be INCONCLUSIVE; definitive outcomes cannot be retried. The decision hash commits the complete canonical record before adding `decision_hash`, including findings. Consumers must check the transaction is finalized and `result.outcome`, not just record existence or transaction submission.

## Bounds

At most 20 commits, 8 changed files, 17 hash entries, 12,000 manifest characters, 160,000 compare-response bytes, 12,000 bytes per file and 48,000 total source bytes. Renames, binary/non-UTF-8 evidence, oversized files, unsupported change statuses and incomplete comparisons are inconclusive. Paths use a conservative ASCII allowlist. This intentionally targets small auditable releases, not arbitrary monorepo releases.

## Run checks

```sh
python -m pip install -r requirements-dev.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
genvm-lint check contracts/release_truth.py
```

See [Security](SECURITY.md), [deployment](docs/DEPLOYMENT.md), [official sources](docs/REFERENCES.md) and [live evidence](docs/EVIDENCE.md). Direct-mode tests use official GenLayer SDK mocks; they are separate from live Full Consensus evidence.

## Integration and limitations

This is a reusable read primitive for release gates, dependency monitors or governance workflows. No token transfers, upgrades or hidden owner privileges are present. Consumers choose their own consequences. Evidence is public; do not submit secrets. A source review does not execute tests or prove absence of vulnerabilities. Correlated LLM errors, prompt injection and GitHub availability remain risks. A finalized inconclusive record is retained, not rewritten. Up to two sequential retries allow recovery without replacing history. After all three attempts are inconclusive, this deployment will not accept further retries of the same manifest.
