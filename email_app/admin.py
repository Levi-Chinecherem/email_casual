# email_app/admin.py
from django.contrib import admin
from .models import EmailInfo

class EmailInfoAdmin(admin.ModelAdmin):
    list_display = ('to_email', 'company_name', 'message_content')
    search_fields = ('to_email', 'company_name')
    list_filter = ('company_name',)

    fieldsets = (
        ('Email Information', {
            'fields': ('to_email', 'company_name', 'message_content'),
        }),
    )

    def has_add_permission(self, request):
        # Disable the ability to add new entries from the admin interface
        return False

admin.site.register(EmailInfo, EmailInfoAdmin)

# Update Django admin site header, title, and index title
admin.site.site_header = 'O Sender Admin'
admin.site.site_title = 'O Sender Admin Portal'
admin.site.index_title = 'Welcome to O Sender - Send Company Mails to Your Friends and Pretend to Own a Company'
