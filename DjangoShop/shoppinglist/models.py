from django.db import models

# Create your models here.
# If I make changes in here I can run: python manage.py makemigrations
# Then to apply the changes I run: python manage.py migrate
class ShoppingList(models.Model):
  shoppping_list_name = models.CharField(max_length=200)
  create_date = models.DateTimeField('date created')

  def __str__(self):
      return self.shoppping_list_name


class Item(models.Model):
  shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
  item_name = models.CharField(max_length=200)
  quantity = models.IntegerField(default=1)
  purchased = models.BooleanField()

  def __str__(self):
    return f"{self.item_name} {self.quantity}"
