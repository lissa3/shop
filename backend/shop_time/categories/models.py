from django.db import models
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=200,unique=True)  
    slug = AutoSlugField(populate_from='name',unique=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            db_index=True,
                            related_name='children'
                            )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

