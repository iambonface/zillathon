from django.contrib import admin
from . models import Genre, Language, Book, BookInstance, Author

# Register your models here.
# admin.site.register(Genre)
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
#Make Book instance and book info in same page
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    readonly_fields=('slug',)

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    #Creating section titiles
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #Organize the list display
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
