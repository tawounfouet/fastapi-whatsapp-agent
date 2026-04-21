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
import asyncio
from whatsapp_ai.adapters.pywa_adapter import PyWaAdapter
from dotenv import load_dotenv
from pywa_async.types.callback import Button, URLButton

load_dotenv()


async def main():
    adapter = PyWaAdapter()
    recipient = "33668957467"  # Remplace par ton numéro de test

    # Envoi d'un message avec boutons interactifs
    # buttons = [
    #     Button(text="Oui"),
    #     Button(text="Non"),
    #     URLButton(text="Voir le site", url="https://openai.com"),
    # ]

    # buttons = [
    #     Button("Oui"),
    #     Button("Non"),
    #     URLButton(text="Voir le site", url="https://openai.com"),
    # ]
    buttons = [
    Button("Oui", "oui"),
    Button("Non", "non"),
    #URLButton("Voir le site", "https://openai.com")
]
    response = await adapter.wa.send_message(
        to=recipient, text="Veux-tu continuer ?", buttons=buttons
    )
    print("Message avec boutons envoyé:", response)

    # buttons = [
    #         URLButton("Voir le site", "https://openai.com")
    # ]
    # response = await adapter.wa.send_message(
    #     to=recipient,
    #     text="Clique sur le bouton ci-dessous pour visiter le site !",
    #     buttons=buttons
    # )
    # print("Message avec bouton URL envoyé:", response)


if __name__ == "__main__":
    asyncio.run(main())
