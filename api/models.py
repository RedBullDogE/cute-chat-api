from django.core.exceptions import ValidationError
from django.db import models


class Message(models.Model):
    """
    Message Model that describes message entity in the chat.
    """

    author_email = models.EmailField()
    text = models.CharField(max_length=100, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.text == "":
            raise ValidationError("Message text should not be empty")
