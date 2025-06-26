from django.db import models
from django.conf import settings


class DanzaEstilo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    descripcion = models.TextField()
    referentes = models.CharField(max_length=300)
    año = models.CharField(max_length=20)
    video_url = models.URLField()

    def __str__(self):
        return self.nombre
    
    @property
    def video_embed_url(self):
        """
        Convierte una URL normal de YouTube a formato embed.
        Ejemplo: https://www.youtube.com/watch?v=ABC123 → https://www.youtube.com/embed/ABC123
        """
        if "youtube.com/watch?v=" in self.video_url:
            video_id = self.video_url.split("v=")[-1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in self.video_url:
            video_id = self.video_url.split(".be/")[-1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.video_url 

   