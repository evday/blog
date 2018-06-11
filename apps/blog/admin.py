from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article,Category,Tag


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',) #给content字段添加富文本

admin.site.register(Article,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
