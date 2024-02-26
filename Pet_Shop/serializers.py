from rest_framework import serializers

from User.models import UserTheme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTheme
        fields = '__all__'

