"""Offline verification of preserved deployment commitments (no network or models)."""
import ast
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
canon = lambda value: json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
sha = lambda value: hashlib.sha256(value).hexdigest()
source = (root/'contracts/release_truth.py').read_bytes()
assert source == (root/'evidence/explorer-source.py').read_bytes()
assert sha(source) == 'b72593d1b103ad0f09cd70fc8a4cff01c108538479af7eef2ed9d76d8727cb55'
r = json.loads((root/'evidence/finalized-review.json').read_text())
decision = r.pop('decision_hash')
assert decision == sha(canon(r).encode())
assert r['request_id'] == sha(canon({k:r[k] for k in ['manifest','policy_hash','attempt']}).encode())
tree = ast.parse(source)
policy = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'POLICY' for t in n.targets))
assert r['policy_hash'] == sha(policy.encode())
assert r['manifest'] == json.loads((root/'evidence/manifest.json').read_text())
assert r['result']['outcome'] == 'MISLEADING'
print('PASS: source identity, policy hash, request hash, decision hash, manifest and finalized verdict')
