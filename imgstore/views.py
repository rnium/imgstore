from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PhotoSerializer

class PhotoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save()
            photo_url = request.build_absolute_uri(photo.image.url)
            return Response({'photo_url': photo_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
