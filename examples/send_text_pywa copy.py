import asyncio
from whatsapp_ai.adapters.pywa_adapter import PyWaAdapter


from dotenv import load_dotenv

load_dotenv()


async def main():
    adapter = PyWaAdapter()
    recipient = "33668957467"  # Remplace par ton numéro de test

    # Envoi d'un message texte simple
    response = await adapter.send_text_message(
        to=recipient, text="Hello via PyWa Adapter! 🚀"
    )
    print("Texte envoyé:", response)


if __name__ == "__main__":
    asyncio.run(main())
