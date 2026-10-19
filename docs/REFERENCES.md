# Official references consulted

Checked 2026-10-19:

- https://docs.genlayer.com/developers/intelligent-contracts/first-intelligent-contract
- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
- https://docs.genlayer.com/developers/intelligent-contracts/testing
- https://docs.genlayer.com/api-references/genlayer-test
- https://docs.genlayer.com/api-references/genlayer-linter
- https://docs.genlayer.com/understand-genlayer-protocol/core-concepts/optimistic-democracy/finality
- https://github.com/genlayerlabs/genvm-linter
- https://docs.github.com/en/rest/commits/commits#compare-two-commits

SDK dependency is pinned to the runner also used by Studio's current storage template. The web SDK's actual response field is `status`; some prose examples use `status_code`. SDK validation and direct tests check the pinned implementation.
