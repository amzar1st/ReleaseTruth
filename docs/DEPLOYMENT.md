# Deployment and reproduction

## Verified deployment

- Network: public GenLayer Studio / StudioNet sandbox, not production mainnet.
- Account: Studio built-in `0xd8E6cE9057215C5d48A7d7cFd756c0E0f75fC8C4`.
- Contract: `0x003f2bA80D09604c7b131f99FB4EFD5a3136cBbD`.
- Source commit: `d283037163583bc3cf234eb2de2869c536c6c27c`.
- Source path: `contracts/release_truth.py` (11,209 UTF-8 bytes).
- Source SHA-256: `b72593d1b103ad0f09cd70fc8a4cff01c108538479af7eef2ed9d76d8727cb55`.
- [Deployment transaction](https://explorer-studio.genlayer.com/tx/0x1d0f59eaf7bf21fe224e9d1b0c9b48c1c0ca52abb810c24371f5fc080aa84480): FINALIZED, SUCCESS, Normal mode, 5 initial validators, zero rotations.
- [Review transaction](https://explorer-studio.genlayer.com/tx/0x50a3009dc8abbd80c848a77c41a87bda52fb4415658a2180786ef67014db84b5): FINALIZED, SUCCESS, Accepted, Normal mode, 5 initial validators, zero rotations.
- [Contract and deployed source](https://explorer-studio.genlayer.com/address/0x003f2bA80D09604c7b131f99FB4EFD5a3136cBbD).

The exact source was pasted into Studio, copied back and compared, then deployed once. The public Explorer Code tab was subsequently exported as `evidence/explorer-source.py` and compared byte-for-byte with the local source and the raw GitHub source at the source commit. All matched. Final documentation commits do not change contract code. To identify the complete submission snapshot, use the GitHub commit containing this document (`git rev-parse HEAD` after checking out that commit). The final package commit is also supplied in the submission response; a commit cannot embed its own hash.

## Reproduce the live demonstration

1. Open the contract in Explorer and select Contract > Read Contract. Or use Studio's deployed instance and select Finalized state.
2. Call `get_review` with `0f9578e9a8cf84b092c7f25735ff6680dd8b2cbc06b6fd1e06917635150c941b`.
3. Observe `result.outcome = MISLEADING`, `reason = REVIEWED`, and two CONTRADICTED file findings. Code changed from `return is_admin` to `return True` despite notes denying an authorization change.
4. Compare the exact input in `evidence/manifest.json` with the review transaction's decoded input.
5. Inspect transaction Consensus data. The recorded vote map is **3 agree, 2 idle**, not five unanimous successful executions. Two validator entries have idle/error receipts; the network nevertheless accepted and finalized the transaction. Preserve this distinction when describing evidence.

For a new review, prepare a manifest using `python tools/build_manifest.py owner/repo BASE_SHA HEAD_SHA RELEASE_NOTES_PATH`. Deploy the same contract source (no constructor parameters), select Normal (Full Consensus), disable Simulation Mode, and call `review(manifest_json, 0)`. A duplicate successful request reverts. Attempts 1 and 2 require their previous attempt to have finalized as INCONCLUSIVE. Never use a failed or pending transaction as evidence of a result.

## Verification commands

```sh
python -m pip install -r requirements-dev.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
genvm-lint check contracts/release_truth.py
genvm-lint typecheck contracts/release_truth.py
sha256sum contracts/release_truth.py evidence/explorer-source.py
python tools/verify_evidence.py
```

The official direct testing suite auto-loads a plugin in some environments. Disabling pytest plugin auto-load and explicitly loading its direct plugin in `tests/conftest.py` avoids duplicate registration. If the testing suite requests an obsolete `genvm-universal.tar.xz` asset URL for the latest release, reuse the official archive already downloaded by genvm-lint: copy `~/.cache/genvm-linter/genvm-universal-v0.3.0-rc7.tar.xz` into `~/.cache/gltest-direct/` under the same filename. No SDK code modifications are required. This environment needed that cache reuse.

Studio is a shared sandbox. Its consensus is meaningful development evidence, not proof of production validator economics or irreversible mainnet settlement. Public sandbox data may eventually be reset; the repository preserves source, manifest, finalized record, observed transaction text and screenshot.
