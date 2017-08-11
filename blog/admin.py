from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display=["title","published_date","created_date","text"]
	list_display_links=["published_date"]
	list_editable=["text"]
	list_filter=["published_date"]
	search_fields =["title"]

	class Meta:
		model=Post

admin.site.register(Post,PostModelAdmin)

