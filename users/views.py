from rest_framework.generics import CreateAPIView


class LoginView(CreateAPIView):
    serializer_class = None

    def post(self, request, *args, **kwargs):
        pass


class LogoutView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        pass
