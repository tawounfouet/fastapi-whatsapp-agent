import logging

import uvicorn
from fastapi.responses import HTMLResponse, JSONResponse

from whatsapp_ai.ai.openai_provider import OpenAIProvider
from whatsapp_ai.client import WhatsAppClient
from whatsapp_ai.config import WhatsAppConfig
from whatsapp_ai.memory import InMemoryStore
from whatsapp_ai.router import MessageRouter
from whatsapp_ai.webhook import WebhookReceiver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = WhatsAppConfig()
client = WhatsAppClient(config)

memory = InMemoryStore() if config.openai_api_key else None
ai_provider = OpenAIProvider(config) if config.openai_api_key else None

router = MessageRouter(client=client, ai_provider=ai_provider, memory=memory)
webhook_receiver = WebhookReceiver(config=config, router=router)
app = webhook_receiver.get_app()


@app.get("/health")
def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})


@app.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    html = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>WhatsApp AI Agent</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 48px 56px;
      max-width: 480px;
      width: 100%;
      text-align: center;
    }
    .icon { font-size: 56px; margin-bottom: 20px; }
    h1 { font-size: 1.8rem; font-weight: 700; margin-bottom: 8px; }
    .subtitle { color: #94a3b8; font-size: 0.95rem; margin-bottom: 32px; }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #166534;
      color: #4ade80;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 99px;
      margin-bottom: 36px;
    }
    .dot {
      width: 7px; height: 7px;
      background: #4ade80;
      border-radius: 50%;
      animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.3; }
    }
    .links { display: flex; flex-direction: column; gap: 12px; }
    a.btn {
      display: block;
      padding: 13px 20px;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      transition: opacity 0.15s;
    }
    a.btn:hover { opacity: 0.85; }
    .btn-primary { background: #25d366; color: #000; }
    .btn-secondary { background: #1e40af; color: #fff; }
    .btn-outline {
      background: transparent;
      border: 1px solid #475569;
      color: #94a3b8;
    }
    .footer { margin-top: 32px; font-size: 0.75rem; color: #475569; }
  </style>
</head>
<body>
  <div class="card">
    <div class="icon">💬</div>
    <h1>WhatsApp AI Agent</h1>
    <p class="subtitle">FastAPI · WhatsApp Cloud API · OpenAI</p>
    <div class="badge">
      <span class="dot"></span>
      Service opérationnel
    </div>
    <div class="links">
      <a class="btn btn-primary" href="/docs">📄 Swagger UI — Documentation API</a>
      <a class="btn btn-secondary" href="/redoc">📘 ReDoc — Documentation alternative</a>
      <a class="btn btn-outline" href="/health">🩺 Health check</a>
    </div>
    <p class="footer">fastapi-whatsapp.awounfouet.com</p>
  </div>
</body>
</html>
"""
    return HTMLResponse(content=html)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
