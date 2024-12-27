from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                'user_id', 'first_name',
                'last_name', 'email',
                'password_hash', 'phone_number',
                'role', 'created_at'
        ]

class ConversationSerializer(serializers.ModelSerializer):
    participants_id = UserSerializer(many=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'created_at']

    def get_messages(self, obj):
        messages = Message.objects.filter(conversation=obj)
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        if len(data.get('participants', [])) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")

        return data

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.CharField(source='sender_id.user_id', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'message_body', 'sent_at']
