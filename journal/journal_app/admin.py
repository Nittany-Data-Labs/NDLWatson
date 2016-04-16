from django.contrib import admin

# Register your models here.
from .models import JournalEntry, ProcessedEntry, UserProfile



class ProcessedEntryInline(admin.StackedInline):
    model = ProcessedEntry
    extra = 3


class JournalEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ProcessedEntryInline]

admin.site.register(JournalEntry, JournalEntryAdmin)
admin.site.register(UserProfile)
