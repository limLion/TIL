from rest_framework import serializers 
from .models import Review
from users.serializers import TinyUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    
    user = TinyUserSerializer(read_only=True) # 관계 확장을 위해서 / user 데이터가 유저가 주면 안됨.
    
    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating"
        )