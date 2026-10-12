# Modal GPU for avatar-gpu

Account: GitHub `willynoslo17` (created 2026-10-12).

## One-time setup (no secrets in this public repo)
1. In Modal dashboard create a token.
2. Add GitHub Actions secrets on `willynoslo17/render-farm` only: `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET`.
3. Locally (or in CI): `modal token set` / use those env vars.
4. Deploy: `modal deploy avatar/modal/app.py` (app name `ml-avatar-gpu`).

Runner stays isolated: only pinned weights from `weights.lock`, allowlisted Cloudinary media, callback only to n8n/Make.
