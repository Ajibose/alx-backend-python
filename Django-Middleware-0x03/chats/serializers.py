from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                'user_id', 'first_name',
                'last_name', 'email',
                'password', 'phone_number',
                'role', 'created_at'
        ]

class ConversationSerializer(serializers.ModelSerializer):
    participants_id = serializers.PrimaryKeyRelatedField(
            many=True, queryset=User.objects.all()
    )
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'messages', 'created_at']

    def get_messages(self, obj):
        messages = Message.objects.filter(sender_id__in=obj.participants_id.all())
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        participants_id = data.get('participants_id', [])

        if len(data.get('participants_id', [])) < 2:
            raise serializers.ValidationError("A conversation must have at least tiwo participants.")

        participants = User.objects.filter(user_id__in=participants_id)
        if len(participants) != len(participants_id):
            raise serializers.ValidationError("One or more participant IDs are invalid.")

        return data

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.CharField(source='sender_id.user_id', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'message_body', 'sent_at']
