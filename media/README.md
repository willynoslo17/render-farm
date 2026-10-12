# media-tools.yml — `event_type: "media"`
POST https://api.github.com/repos/willynoslo17/render-farm/dispatches (same headers as README)
{"event_type":"media","client_payload":{"job":"upscale","inputs":["https://res.cloudinary.com/yiq9yzmu/image/upload/v1/ml/prod/foto1.jpg"],"scale":"4","commercial":"true","job_id":"m1","callback_url":"https://hook.eu1.make.com/..."}}
Jobs: raw2jpg | panorama | office2pdf (format pdf|pptx) | marp (pdf|pptx) | slidev (pdf|pptx) | mux (mkv|mp4) | upscale (scale 2|3|4) | interpolate (2x fps, first 60 s) | bg_remove (model u2net|isnet) | resize (size px, format jpg|png|webp)
inputs: 1-30 https://res.cloudinary.com/yiq9yzmu/... URLs only. Outputs -> Cloudinary ml/media. Callback (n8n/Make only): {job,task,urls,ok,commercial,fallback_reason}.
commercial=true (default): isnet refused -> u2net. GFPGAN is not available (and must never be used on the owner's face).
