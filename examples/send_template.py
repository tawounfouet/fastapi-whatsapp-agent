import asyncio
from whatsapp_ai import WhatsAppClient, WhatsAppConfig


async def main():
    config = WhatsAppConfig()
    client = WhatsAppClient(config)

    recipient = "33668957467"  # Numéro au format international sans +
    template_name = "hello_world"  # Remplace par le nom exact de ton template dans Meta Business Manager
    language_code = "en_US"  # Code de langue correspondant au template

    # hello_world n'a pas de paramètres dynamiques, components=[] ou omis
    try:
        response = await client.send_template_message(
            to=recipient,
            template_name=template_name,
            language_code=language_code,
        )
        print("Template message sent:", response)
    except Exception as e:
        print("Failed to send template message:", e)


if __name__ == "__main__":
    asyncio.run(main())
