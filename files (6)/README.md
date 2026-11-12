# SPEED CRISIS
1. Copy ALL your .glb files (exact names, unchanged) into the `assets/` folder.
2. Push this folder to a GitHub repo -> Settings > Pages > deploy from branch (root).
   Files over 100 MB are rejected by GitHub: use Git LFS for big GLBs (Pages serves LFS files poorly, so shrink them with gltf-transform if needed).
3. Open the Pages URL once online; the service worker then caches everything for offline play. Add to Home Screen on phones.
Fully offline from first load: download three@0.160.0 `build/three.module.js` and `examples/jsm/loaders/GLTFLoader.js` + `utils/BufferGeometryUtils.js` into `libs/` and edit the importmap in index.html.
Test locally: `python3 -m http.server` (GLBs will not load from file://).
To add cars/tracks: add a line to CARS / TRACKS / LEVELS at the top of the script in index.html.

## Render.com
Best: New > **Static Site**, connect the repo, Build Command: leave empty, Publish Directory: `.`
If you already made a **Web Service**: Build Command `pip install -r requirements.txt`, Start Command `python server.py`.

## File sizes
Every file is max 24 MB. Big models are split into `name.glb.part01, .part02, ...` and listed in `assets/manifest.json`; the game joins them automatically. Keep all parts + manifest.json together in `assets/`.
