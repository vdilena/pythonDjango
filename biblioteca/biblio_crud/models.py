from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn_code = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField
    created = models.DateTimeField(auto_now=True)

    # Clase interna para ejecutar configuraciones en la tabla, como el orden
    class Metadata:
        ordering = ['-created']

    # Redefinimos el toString del objeto, asi podemos identificarlo facilmente en el debugging
    def __str__(self):
        return self.title

