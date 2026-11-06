# Car Games company site

The public website and its editable source live in this repository. GitHub Pages serves `master` from the repository root at https://www.cargamesinc.com. Keep `CNAME`, `.nojekyll`, the current Pages settings and enforced HTTPS in place.

## Editing and rebuilding

Python 3.12 is sufficient; there are no package dependencies or external build services.

```sh
SITE_MODE=production BUILD_DIR=dist-production python3 company-site/scripts/build.py
BUILD_DIR=dist-production python3 company-site/scripts/check.py
python3 company-site/scripts/publish.py --check
```

Edit `company-site/content/` for copy and store mappings, `company-site/scripts/generate.py` for page templates, and `company-site/assets/site.css` for styling. The family navigation source is vendored in `company-site/scripts/studio_family/`; it requires no private repository. Frozen legal fragments are checked against `company-site/evidence/preserved-files.json`; review legal changes explicitly and update their digests only when approved.

To publish a reviewed source change, start from current `master`, build and check, then run `python3 company-site/scripts/publish.py`. This fetches current `master` and refuses a checkout missing newer upstream commits. Review the generated root diff, commit source plus generated output, and submit a PR. CI verifies reproducibility and links. Merge deploys through the existing Pages branch workflow. Rebuild after rebasing; never force push a stale deployment over newer root files.

## Seller file workflow

Margaret can continue editing **the root `app-ads.txt` directly in GitHub**. It is the only canonical seller file. There is no source duplicate, frozen seller digest or automatic workflow that republishes an older copy. Every build reads the current root file, and the publish helper verifies its bytes while excluding it from writes. Seller-only edits need no website rebuild. Also keep root `CNAME` edits separate: the helper checks the domain and never writes that file.

## Publication scope and provenance

Only the selected site generator, content, existing website assets, build/check helpers and this guide were consolidated. No private repository history, captures, internal audits or unrelated company tools were copied. The 16 game artwork files and styles are byte-identical copies of assets already published in this repository; this consolidation adds no new third-party artwork. Store metadata describes the company's four apps. Existing legal and trademark fragments are retained verbatim. No blanket license is granted to game artwork, trademarks or legal content.

A pre-publication review of selected text found no credentials, private keys, local account paths or private repository references. Public support contacts, store IDs, seller IDs and existing legal notices remain intentional public content. Original Wix captures and reference artwork were excluded; legacy Wix CSS class names within unchanged legal fragments remain to preserve those fragments.

The project has no runtime or build dependency on the former private monorepo. The source and all required build components are included here. Generated staging folders and local validation reports are ignored.
