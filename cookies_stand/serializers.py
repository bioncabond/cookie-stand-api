from rest_framework import serializers
from .models import Cookies


class CookiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookies
        fields = "__all__"
