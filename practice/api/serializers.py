from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # This includes all fields of the Post model


        # fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at'] # This includes specific fields of the Post model

        # exclude = ['updated_at'] # This excludes specific fields of the Post model    

        # read_only_fields = ['created_at', 'updated_at'] # This makes specific fields read-only

    