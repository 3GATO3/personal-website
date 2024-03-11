from django.db import models
from django.db.models.constraints import UniqueConstraint

class Country(models.Model):
    name = models.CharField(max_length=100)

class Indicator(models.Model):
    name = models.CharField(max_length=200)

class DebtData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.FloatField()  # Assuming debt values are numeric
    
    
    debt_type = models.CharField(max_length=50, choices=[
        ('central_government', "Central Government Debt"),
        ('general_government', 'General Government Debt'),
        ('household', 'Household Debt'),
        ('non_financial_corporate', 'Non Financial Corporate Debt'),
        ('private','Private debt')
    ])
    class Meta:
        constraints = [
            UniqueConstraint(fields=['country', 'indicator', 'year', 'debt_type'], name='unique_debt_record')
        ]