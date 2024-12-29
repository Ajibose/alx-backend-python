import uuid
from rest_framework import viewsets
from .models import Message, Conversation
from .serializers import MessageSerializer, Converserialzer
from rest_framework.response import Response
# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        conversation_id = data.get('conversation_id');
        if conversation_id:
            try:
                uuid_obj = uuid.UUID(conversation_id, version=4)
            except ValueError:
                return Response(
                        {"error": "Invalid conversation_id. It must be a valid UUID"},
                        status=status.HTTP_400_BAD_REQUEST,
                )

            if Conversation.objects.filter(conversation_id=conversation_id).exists:
                return Response(
                        {"error": "ID already exist"},
                        status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    query_set = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        message_id = data.get('message_id');

        if message_id:
            try:
                uuid_obj = uuid.UUID(message_id, version=4)
            except ValueError:
                Response(
                        {"error": "Invalid conversation_id. It must be a valid UUID"}
                        status: status.HTTP_400_BAD_REQUEST
                )

            if Message.objects.filter(message_id=message_id).exists:
                return Response(
                        {"error": "ID already exist"},
                        status=status.HTTP_400_BAD_REQUEST 
                )

        if (!data.get('message_body') or data.get('message_body') == ""):
            return Response(
                    {"error": "Message body must be provided and not empty"}
                    status: status.HTTP_400_BAD_REQUEST
            )

        data.sender_id = request.user.user_id

        serializer = self.get_serializer(data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
