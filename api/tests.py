from django.test import TestCase

from .models import Message


# Create your tests here.
class MessageModelTest(TestCase):
    def setUp(self):
        self.messages = [
            Message.objects.create(author_email="test1@mail.com", text="How r u?"),
            Message.objects.create(
                author_email="test2@mail.com", text="Oh Im fine! and u?"
            ),
            Message.objects.create(author_email="test3@mail.com", text="Spam"),
        ]

    def test_message_creating(self):
        message_qs = Message.objects.all()

        self.assertEqual(len(message_qs), 3)
        self.assertEqual(message_qs[0], self.messages[0])
        self.assertEqual(message_qs[1], self.messages[1])
        self.assertEqual(message_qs[2], self.messages[2])

    def test_message_deleting(self):
        Message.objects.filter(pk=self.messages[0].id).delete()
        message_qs = Message.objects.all()

        self.assertEqual(len(message_qs), 2)
        self.assertTrue(self.messages[0] not in message_qs)

    def test_message_updating(self):
        message_to_update = Message.objects.get(pk=self.messages[1].id)
        message_to_update.text = "Some new text"
        message_to_update.save()

        updated_message = Message.objects.get(pk=self.messages[1].id)

        self.assertEqual(updated_message.text, "Some new text")
        self.assertNotEqual(updated_message.create_date, updated_message.update_date)
