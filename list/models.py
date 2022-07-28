from django.db import models

# item model
class Item(models.Model):
    name = models.CharField(max_length=75, blank=False, null=False)
    complete = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return str(self.name)
