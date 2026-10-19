# Review-ready evidence

## Public on-chain execution

- [Contract / source / read methods](https://explorer-studio.genlayer.com/address/0x003f2bA80D09604c7b131f99FB4EFD5a3136cBbD)
- [Finalized deployment](https://explorer-studio.genlayer.com/tx/0x1d0f59eaf7bf21fe224e9d1b0c9b48c1c0ca52abb810c24371f5fc080aa84480)
- [Finalized Full Consensus review, input and equivalence output](https://explorer-studio.genlayer.com/tx/0x50a3009dc8abbd80c848a77c41a87bda52fb4415658a2180786ef67014db84b5)
- [Exact deployed source commit](https://github.com/amzar1st/ReleaseTruth/blob/d283037163583bc3cf234eb2de2869c536c6c27c/contracts/release_truth.py)
- [Version-bound release comparison](https://github.com/amzar1st/ReleaseTruth/compare/223f9d88535192545aa4aa031c1e4d12194a1d87...64c44f87de81d6c00a8bf764876ae6e81142ab71)
- [Base authorization code](https://github.com/amzar1st/ReleaseTruth/blob/223f9d88535192545aa4aa031c1e4d12194a1d87/demo/access.py)
- [Head authorization code](https://github.com/amzar1st/ReleaseTruth/blob/64c44f87de81d6c00a8bf764876ae6e81142ab71/demo/access.py)
- [Published misleading notes at head](https://github.com/amzar1st/ReleaseTruth/blob/64c44f87de81d6c00a8bf764876ae6e81142ab71/demo/RELEASE_NOTES.md)

The release is a deliberately adversarial fictional fixture. It is not an accusation about a real project's release. Code now permits all callers, while notes claim publishing remains admin-only. Finalized verdict: **MISLEADING**.

## Preserved artifacts

| Artifact | What it proves |
|---|---|
| [Manifest](../evidence/manifest.json) | Exact repository, base/head commits, notes path and four content commitments submitted live. |
| [Finalized review](../evidence/finalized-review.json) | Actual Finalized-state read, including source quotes, explanations and deterministic decision hash. |
| [Integrity verification](../evidence/integrity.json) | Local source = GitHub source = Explorer source; recomputed request and decision hashes. |
| [Explorer source export](../evidence/explorer-source.py) | Byte-for-byte exported deployed source. |
| [Deployment overview](../evidence/deployment-overview.txt) | Public Explorer deployment state and input source. |
| [Review overview](../evidence/review-overview.txt) | Public finalized status, Normal mode, successful execution and MISLEADING equivalence output. |
| [Consensus view](../evidence/consensus-view.txt) | Observed public consensus data: 3 agree votes, 2 idle; not a claim of five successful validators. |
| [Full Consensus screenshot](../evidence/full-consensus-finalized.jpg) | Public finalized review transaction with mode, result, input and outcome. |
| [Tests](../evidence/tests.txt) | 38 direct-mode tests passed. |
| [GenVM check](../evidence/genvm-check.txt) | Lint passed and pinned-SDK validation passed; 3 public methods. |
| [Type check](../evidence/typecheck.txt) | No type errors. |

Request ID: `0f9578e9a8cf84b092c7f25735ff6680dd8b2cbc06b6fd1e06917635150c941b`.

Decision hash: `595e19d21ba3b70544cbd2bd639c506b8817141c201b2b4101c7cc7fcdb6ff01`.

Policy hash: `fedf0a0b84c3981ae1a326cc23c8a0f6bc1e065237a73776fb4f1920fa59eb81`.

Source SHA-256: `b72593d1b103ad0f09cd70fc8a4cff01c108538479af7eef2ed9d76d8727cb55`.

## Test scope

Adversarial checks cover invalid hosts/paths/commit IDs, manifest hashes and omission, mutated/oversized/unavailable evidence, non-ancestor/head mismatch, compare truncation, duplicate files, unsupported renames, fabricated quotes, malformed/oversized model fields, classification coverage, unknown enum values, unassessable claims, all four outcomes, validator dissent/error, independent fingerprint rechecking, equivalent prose, duplicate write prevention, canonical hashes, policy reads, bounded retry caps and inconclusive recovery. Prompt-injection tests verify guard construction and conservative handling with controlled mock outputs, not empirical model immunity. Direct tests are not substituted for live consensus.
