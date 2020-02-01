################################################################################
from django.db import models
from django.urls import reverse
################################################################################

# Create your models here.
################################################################################
class CommonInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()
    order = models.IntegerField(verbose_name=u'orden',default=0)

    class Meta:
        abstract = True

    #Add the __str__ function to see the name in the admin
    def __str__(self):
        return self.name
################################################################################


################################################################################
class Reason(CommonInfo):
    pass
################################################################################


################################################################################
class Category(CommonInfo):
    description = models.TextField(verbose_name=u'descripción')

    #Add the __str__ function to see the name in the admin
    def __str__(self):
        return self.name
################################################################################


################################################################################
class Prodcut(models.Model):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')
    category = models.ForeignKey(
        Category,
        verbose_name='categoría',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
    #Add the __str__ function to see the name in the admin
    def __str__(self):
        return self.name
################################################################################


################################################################################
class Activity(Prodcut):
    reasons = models.ManyToManyField(Reason, verbose_name='tags', blank=True)
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)

    #Add the __str__ function to see the name in the admin
    def __str__(self):
        return self.name
################################################################################


################################################################################
class Box(Prodcut):
    activities = models.ManyToManyField(Activity)
    price = models.IntegerField(verbose_name='precio de venta')
    purchase_available = models.BooleanField(
        verbose_name='disponible venta individual', default=False)

################################################################################
