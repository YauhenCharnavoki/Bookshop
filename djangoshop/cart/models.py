from django.db import models


class Purchase(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 13)
    email = models.CharField(max_length = 255, blank=True, null = True)
    city = models.CharField(max_length = 255, blank=True, null = True)
    address = models.CharField(max_length = 255, blank=True, null = True)
    card_number = models.CharField(max_length = 16)
    card_term= models.CharField(max_length = 5)
    cvv = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s purchase."
