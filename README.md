# render-farm (Remotion + Blender, free on GitHub Actions)

Trigger from Make (HTTP module) or n8n (HTTP Request):

POST https://api.github.com/repos/willynoslo17/render-farm/dispatches
Headers: Authorization: Bearer <fine-grained PAT, this repo only, Contents: read/write>
         Accept: application/vnd.github+json
Body (Remotion):
{"event_type":"remotion","client_payload":{"composition":"Main","props":{"title":"Hola"},"job_id":"123","callback_url":"https://<n8n>/webhook/render-done"}}
Body (Blender):
{"event_type":"blender","client_payload":{"scene":"blender/scene.blend","start":1,"end":120,"job_id":"124","callback_url":"..."}}

Output: uploaded to Cloudinary (cloud yiq9yzmu, unsigned preset ml_unsigned); URL POSTed to callback_url.

Setup still needed: `remotion/` project (npx create-video@latest), a `blender/scene.blend`.
Limits: public repo = unlimited free minutes, 4 vCPU/16 GB runner; private = 2,000 min/mo, 2 vCPU/7 GB. Max 6 h per job. No GPU.
Note: public repo means code + logs are public; never put secrets in payloads/logs.
