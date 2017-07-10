from rest_framework import generics
from rest_framework import permissions
from snippets.models import Snippet
from snippets.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = UserSerializer
