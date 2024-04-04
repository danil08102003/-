from django.db import models

# Create your models here.


class Catigories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URl')



    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return f'{self.name}'



class Projects(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URl')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name = 'Изображение')
    budget = models.DecimalField( default=0.00, max_digits=7, decimal_places=2, verbose_name = 'Бюджет')
    discount = models.DecimalField( default=0.00, max_digits=7, decimal_places=2, verbose_name = 'Скидка в %')
    quantity = models.PositiveIntegerField( default=0, verbose_name = 'Количество')
    category = models.ForeignKey(to=Catigories, on_delete=models.CASCADE, verbose_name = 'Категория')
    start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)



    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


    def __str__(self):
        return  f'{self.name} Количество - {self.quantity}'
    

    def display_id(self):
        return f"{self.id:05}"
    



def sell_price(self):
    if self.discount:
      
        return round(self.budget - self.budget*self.discount/100, 2)
    return self.budget

    
    


