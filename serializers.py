from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.HyperLinkedModelSerializer):
	class Meta:
		model=Post
		fiels=('title','published_date')