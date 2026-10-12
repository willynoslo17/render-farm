# Streaming (Azure VM) — not deployed
`OME_HOST_IP=<ip> docker compose up -d` (OvenMediaEngine) or `docker compose --profile zlm up -d` (ZLMediaKit).
Before exposing publicly: TLS reverse proxy (Caddy/nginx) in front of 3333/80, firewall RTMP 1935 to the encoder's IP only,
stream-key auth (OME AdmissionWebhooks / ZLM on_publish hook), ZLM api secret set via env/secret file (never committed),
keep images pinned by digest, update monthly. OvenMediaEngine AGPL-3.0: use unmodified.
Players: `players/dplayer.html`, `players/xgplayer.html` (SRI-pinned CDN), embed in the website.
