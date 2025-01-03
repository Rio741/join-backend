from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


from rest_framework import serializers
import re

class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # def validate_username(self, value):
    #     # Überprüfen, ob der Benutzername aus genau zwei Wörtern besteht
    #     if len(value.split()) != 2:
    #         raise serializers.ValidationError("Der Benutzername muss aus genau zwei Wörtern bestehen, Vorname und Nachname.")
        
    #     # Optional: Überprüfen, ob der Benutzername nur Buchstaben und Leerzeichen enthält (keine Sonderzeichen)
    #     if not re.match(r'^[A-Za-zÄÖÜäöüß\s]+$', value):
    #         raise serializers.ValidationError("Der Benutzername darf nur Buchstaben und Leerzeichen enthalten.")
        
    #     return value

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']

        if pw != repeated_pw:
            raise serializers.ValidationError({'error':'password dont match'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account

    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            # Benutzer anhand der E-Mail finden
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'Benutzer mit dieser E-Mail existiert nicht.'})

        # Benutzer authentifizieren
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError({'password': 'Ungültige Login-Daten.'})

        data['user'] = user
        return data