from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    # The following doesn't seem to work to get checkboxes
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_max_num(self, request, obj=None, **kwargs):
        return Category.objects.count()


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'categories':
    #         kwargs["queryset"] = Category.objects.filter(author=request.user)
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    
admin.site.register(Category, CategoryAdmin)


