from django.db import models

from trading.core.models import UserAudit


class Journal(UserAudit):
    open_time = models.DateTimeField()
    ticker = models.CharField(max_length=64)
    side = models.CharField(max_length=64)
    entry_price = models.DecimalField(max_digits=10, decimal_places=8)
    close_price = models.DecimalField(max_digits=10, decimal_places=8)
    details = models.TextField()

    def __str__(self):
        return f"{self.open_time} - {self.ticker}"