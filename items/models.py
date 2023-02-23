from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(max_length=150, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Price")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Итем"
        verbose_name_plural = "Итемы"

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
