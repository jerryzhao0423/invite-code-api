from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Invitation


class UserListSerializer(serializers.ModelSerializer):
    invite_code = serializers.CharField(source='invitation.invite_code', read_only=True)
    invite_input = serializers.CharField(source='invitation.invite_input', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'invite_code', 'invite_input']


class InvitationSerializer(serializers.ModelSerializer):
    invite_code = serializers.CharField(read_only=True)
    invite_input = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Invitation
        fields = ('id', 'username', 'invite_code', 'invite_input', 'is_invited', 'credit')

    def validate(self, data):
        invite_input = data.get('invite_input', None)
        if invite_input == '':
            return data
        else:
            invited = Invitation.objects.filter(invite_code=invite_input)
            if not invited.exists():
                raise ValidationError('wrong code')
            data['is_invited'] = True
            data['credit'] += 1
            return data
