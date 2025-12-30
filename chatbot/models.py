from django.db import models

class FAQ(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question[:60]


class ChatLog(models.Model):
    user_message = models.TextField()
    intent = models.CharField(max_length=100)
    risk = models.CharField(max_length=20)
    route = models.CharField(max_length=50)
    reply = models.TextField()
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user_message[:40]}..."
