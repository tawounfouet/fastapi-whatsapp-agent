import os
from pywa_async import WhatsApp as PyWa
from pywa_async.types.templates import TemplateLanguage


class PyWaAdapter:
    """
    Wrapper autour de PyWa pour l'utiliser comme backend
    à la place du WhatsAppClient natif.
    """

    def __init__(self):
        self.wa = PyWa(
            phone_id=os.getenv("WHATSAPP_PHONE_NUMBER_ID"),
            token=os.getenv("WHATSAPP_ACCESS_TOKEN"),
        )

    async def send_text_message(self, to: str, text: str):
        """Envoie un message texte simple."""
        return await self.wa.send_message(to=to, text=text)

    async def send_template_message(
        self,
        to: str,
        template_name: str,
        language_code: str = "en_US",
        params=None,
    ):
        """Envoie un message template avec paramètres."""
        return await self.wa.send_template(
            to=to,
            name=template_name,
            language=TemplateLanguage(language_code),
            params=params,
        )

    async def send_image(self, to: str, image_url: str, caption: str = None):
        """Envoie une image."""
        return await self.wa.send_image(to=to, image=image_url, caption=caption)

    async def send_document(
        self, to: str, document_url: str, filename: str = None, caption: str = None
    ):
        """Envoie un document."""
        return await self.wa.send_document(
            to=to, document=document_url, filename=filename, caption=caption
        )

    async def send_audio(self, to: str, audio_url: str):
        """Envoie un fichier audio."""
        return await self.wa.send_audio(to=to, audio=audio_url)

    async def send_video(self, to: str, video_url: str, caption: str = None):
        """Envoie une vidéo."""
        return await self.wa.send_video(to=to, video=video_url, caption=caption)

    async def send_location(
        self,
        to: str,
        latitude: float,
        longitude: float,
        name: str = None,
        address: str = None,
    ):
        """Envoie une localisation."""
        return await self.wa.send_location(
            to=to, latitude=latitude, longitude=longitude, name=name, address=address
        )

    async def mark_as_read(self, message_id: str):
        """Marque un message comme lu."""
        return await self.wa.mark_message_as_read(message_id=message_id)
