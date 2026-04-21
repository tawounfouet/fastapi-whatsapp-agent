import logging

import uvicorn
from fastapi.responses import JSONResponse

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
