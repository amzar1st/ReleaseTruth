# GenLayer Intelligent Contracts submission

**Title:** ReleaseTruth: Version-Bound Release Note Verification

**One line:** A GenLayer Intelligent Contract that verifies release notes against commit-pinned code changes through independent validator consensus.

**Notes / Description (926 characters):**

ReleaseTruth is a standalone GenLayer Intelligent Contract that verifies release notes against complete, commit-pinned GitHub code/spec changes. Validators independently retrieve both source versions and notes, verify SHA-256 commitments and apply an immutable review policy. Custom equivalence requires matching evidence fingerprints, per-file classifications and verdicts. Outcomes are ACCURATE, MATERIAL_OMISSIONS, MISLEADING or INCONCLUSIVE. It includes bounded inputs, literal citation checks, injection-aware prompts, deterministic decision hashes, immutable records and two bounded retries after inconclusive results. All 38 tests, GenVM lint/SDK validation and type checks pass. A real Studio Full Consensus review finalized MISLEADING for a fictional release that removed an admin check while claiming authorization was unchanged. Deployed source matches GitHub byte for byte. Evidence and limitations are documented.

Repository: https://github.com/amzar1st/ReleaseTruth

Contract: https://explorer-studio.genlayer.com/address/0x003f2bA80D09604c7b131f99FB4EFD5a3136cBbD

See [all evidence URLs and hashes](EVIDENCE.md) and [deployment details](DEPLOYMENT.md). The source commit is d283037163583bc3cf234eb2de2869c536c6c27c. The final packaging commit is the commit containing this document and the preserved evidence; contract source is unchanged.
