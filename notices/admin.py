from django.contrib import admin
from notices.models import Notice

admin.site.register(Notice)
#admin.site.register(Contact)
#admin.site.register(Location)
#admin.site.register(Comment)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'body', 'notice', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('title', 'commenter', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)