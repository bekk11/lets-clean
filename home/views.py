from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'home/index.html'

    def get(self, request):
        return Response({'page': "Home"})
