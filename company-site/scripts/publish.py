"""Copy only known generated pages from a checked build; preserve root seller and domain."""
from pathlib import Path
import argparse,json,shutil,subprocess
R=Path(__file__).resolve().parents[2]; S=R/'company-site'; O=S/'dist-production'
a=argparse.ArgumentParser();a.add_argument('--check',action='store_true');args=a.parse_args()
config=json.loads((S/'site.config.json').read_text())
files=[p for p in O.rglob('*') if p.is_file() and p.relative_to(O).as_posix() not in ['app-ads.txt','CNAME','.build.json']]
assert (O/'app-ads.txt').read_bytes()==(R/'app-ads.txt').read_bytes(),'Seller file differs; rebuild from current root'
assert (O/'CNAME').read_text().strip()==(R/'CNAME').read_text().strip(),'Domain differs; do not change Pages configuration'
if args.check:
 errors=[str(p.relative_to(O)) for p in files if not (R/p.relative_to(O)).exists() or p.read_bytes()!=(R/p.relative_to(O)).read_bytes()]
 if errors:raise SystemExit('Generated root files differ: '+', '.join(errors))
 print('Generated root files, seller file and custom domain match')
else:
 subprocess.run(['git','fetch','origin','master'],cwd=R,check=True)
 ancestor=subprocess.run(['git','merge-base','--is-ancestor','origin/master','HEAD'],cwd=R)
 if ancestor.returncode:raise SystemExit('Remote master has newer changes. Merge/rebase, rebuild and check before publishing.')
 for p in files:
  target=R/p.relative_to(O);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 print('Updated generated root files; review and commit them with the source changes')
