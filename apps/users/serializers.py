from apps.users.models import User
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        filds = ["id", "phone", 'name']
        read_only_fields = ["id"]


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        filds = ['id', 'phone', 'name', 'password']

        def create(self, validated_date):
            user = User.objects.create(
                phone=validated_date['phone'],
                password=validated_date['password'],
                name=validated_date['name']
            )
            return user


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone = attrs.get(phone)
        password = attrs.get("password")

        if phone and password:
            user = authenticate(username=phone, password=password)
            if not user:
                raise serializers.ValidationError("Невурный телефон")

            else:
                raise serializers.ValidationError("Видите телефон парол")

            attrs['user'] = user
            return attrs
