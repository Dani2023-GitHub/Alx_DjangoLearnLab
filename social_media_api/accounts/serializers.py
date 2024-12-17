from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    # Adding a password field for user creation
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.CharField()  # Token will be generated upon user creation

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']
        read_only_fields = ['followers']

    def create(self, validated_data):
        # Extract the password field and remove it from validated_data
        password = validated_data.pop('password', None)

        # Create the user using the get_user_model()
        user = get_user_model().objects.create_user(**validated_data)

        if password:
            user.set_password(password)  # Set the user's password securely
            user.save()

        # Create a token for the user
        token = Token.objects.create(user=user)
        
        # Add the token to the user's serialized response
        user.token = token.key
        
        return user
