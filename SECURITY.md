# Security model

## Trust boundaries

GitHub HTTPS provides repository/commit namespace authority, not signed author identity. Raw commit URLs plus required SHA-256 commitments prevent silently changed evidence. The compare response provides the complete changed-file set for the pinned range; full contents replace potentially truncated patches. More than eight files is refused (well below GitHub's 300-file compare response limit). Compare commit pagination/truncation is refused by exact count checks and the 20-commit cap. A base that is not the merge base is refused. API rate limiting or unavailable commits yields inconclusive.

Callers cannot supply arbitrary hosts, query strings, fragments, encoded path separators or traversal segments. URL components have restrictive ASCII formats. There are no caller-controlled policy instructions, external tool calls by the LLM, executable snippets, money movements or privileged mutation methods.

## AI and consensus

Code, comments and release notes are untrusted data, including fake system messages. The instruction policy precedes JSON-encoded evidence and explicitly disallows following evidence instructions. Exact output schemas, enum validation, coverage, literal quotations and deterministic precedence reduce the model's authority. They do not mathematically prove semantic correctness. Each validator repeats the actual evidence retrieval and classification. Equivalence compares decision-critical fields, not arbitrary prose or schema validity alone. Any malformed response becomes INCONCLUSIVE; an independent validator that reaches a definitive answer will disagree with it.

All files must be classified, including documentation/specification changes. Multiple changes within a file use conservative precedence: uncertainty, contradiction, omission, documentation, non-material. Global unassessable note claims force inconclusive. False but assessable claims can still produce misleading. Literal quotes prove source presence, not entailment; entailment remains a validator judgment.

## State and availability

Canonical JSON and SHA-256 commitments provide deterministic identifiers. The decision hash includes accepted leader prose; it need not be identical across different runs with equivalent prose. Records are append-only. Duplicate requests revert. Reads do not trigger external work. No timestamps, random IDs, mutable tags or off-chain AI result endpoints determine state.

A transaction that fails to reach consensus does not create a successful review record. Finalized INCONCLUSIVE is a genuine negative availability/coverage result and never an attestation of accuracy. It is immutable in this version, including transient failures. Do not build irreversible financial decisions on a single review. Quotas bound each request; aggregate spam costs are a network/application concern. Response-size checks occur after the web runtime fetches the response and do not bound transport bandwidth by themselves.

Supported evidence is small UTF-8 regular source/spec text. Renames, submodules, symlink semantics, generated artifacts, runtime dependencies outside the comparison and binary releases are not certified. A model unable to establish behavior from the supplied files must choose uncertainty. No security audit, publisher-signature verification, artifact signing, execution or reproducible-build claim is made.

Report issues through a repository issue with a minimal public reproduction; never include credentials.
