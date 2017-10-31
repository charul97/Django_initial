from rest_framework import serializers
from blog.models import Post

class PostSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Post
		fields=('title','published_date','created_date')