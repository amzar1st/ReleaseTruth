"""Prepare pinned evidence commitments. Does not submit or decide a review."""
import argparse
import hashlib
import json
import urllib.request


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent':'ReleaseTruth-manifest/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def build(repo, base, head, notes):
    comp = json.loads(get(f'https://api.github.com/repos/{repo}/compare/{base}...{head}'))
    hashes = {}
    for f in comp['files']:
        for side, commit in [('b',base),('h',head)]:
            if (side == 'b' and f['status'] == 'added') or (side == 'h' and f['status'] == 'removed'):
                continue
            hashes[side+':'+f['filename']] = hashlib.sha256(get(f'https://raw.githubusercontent.com/{repo}/{commit}/{f["filename"]}')).hexdigest()
    hashes['h:'+notes] = hashlib.sha256(get(f'https://raw.githubusercontent.com/{repo}/{head}/{notes}')).hexdigest()
    return {'repo':repo,'base':base,'head':head,'notes':notes,'hashes':hashes}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    for key in ['repo','base','head','notes']: p.add_argument(key)
    a = p.parse_args()
    print(json.dumps(build(a.repo,a.base,a.head,a.notes),sort_keys=True,separators=(',',':')))
