from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        tooLarge = 300
        if img.height > tooLarge or img.width > tooLarge:
            output_size = (tooLarge, tooLarge)
            img.thumbnail(output_size)
            img.save(self.image.path)
