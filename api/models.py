from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    @property
    def mydish(self):
        return self.dishes_set.all()


class Dishes(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.TextField()
    foodimg = models.ImageField(upload_to='food_img', null=True, blank=True)
    created_by = models.CharField(max_length=250)

    def __str__(self):
        return self.name
        
    @property
    def ingredient(self):
        return self.ingredients_set.all()

class Ingredients(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    rules = models.CharField(max_length = 400)

    def __str__(self):
        return self.rules
