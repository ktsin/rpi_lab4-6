from django.contrib import admin
import book_shop.models as md


# Register your models here.
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('id', 'category_id', 'authors', 'name', 'publish_date', 'price')


admin.site.register(md.Book)
admin.site.register(md.BookOutcome)
admin.site.register(md.BookIncome)
admin.site.register(md.KnowledgeCategory)
admin.site.register(md.Author)
