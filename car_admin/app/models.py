from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='марка')
    model = models.CharField(max_length=50, verbose_name='модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'