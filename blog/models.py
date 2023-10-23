from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='')
    cost=models.PositiveIntegerField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class TvShow(models.Model):
    CHOISE_ACT =(
        ('ДА', 'ДА'),
        ('НЕТ','НЕТ')
    )


    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='film/')
    act = models.CharField(max_length=100, choices=CHOISE_ACT)
    cost = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)