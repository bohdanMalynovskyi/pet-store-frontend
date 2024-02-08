from django.db import models


class AnimalCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = "animal categories"
        verbose_name = "animal category"

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    animal_category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE, null=False, blank=False,
                                        related_name='product_categories')

    class Meta:
        verbose_name_plural = "product categories"
        verbose_name = "product category"

    def __str__(self):
        return f'{self.animal_category.name} - {self.name}'


class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False, blank=False,
                                         related_name='subcategories')

    class Meta:
        verbose_name_plural = "subcategories"
        verbose_name = "subcategory"

    def __str__(self):
        return f'{self.product_category.animal_category.name} - {self.product_category.name} - {self.name}'
