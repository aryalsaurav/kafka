from django.db import models

# Create your models here.
EMOTION_CHOICES = (("happy","happy"),
    ("sad","sad"),
    ("angry","angry"),
    ("neutral","neutral")
)
GENDER_CHOICES =  (("male","male"),
    ("female","female"),
    ("other","other")
    )

class FaceEmbade(models.Model):
    age = models.IntegerField(default=0)
    emotion = models.CharField(choices=EMOTION_CHOICES,max_length=10)
    gender  = models.CharField(choices=GENDER_CHOICES,max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
