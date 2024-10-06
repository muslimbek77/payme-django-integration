from django.db import models

class Order(models.Model):
	customer_name = models.CharField(max_length=255)  
	amount = models.DecimalField(max_digits=10, decimal_places=2)  
	created_at = models.DateTimeField(auto_now_add=True)  

	def __str__(self):
			return f"Order by {self.customer_name} - {self.amount} USD"