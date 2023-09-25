from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


@api_view(['POST'])
@transaction.atomic
def upload_file(request):
    file_serializer = FileSerializer(data=request.data)

    if file_serializer.is_valid():
        uploaded_file = file_serializer.save()

        try:
            # Определяем тип файла на основе его расширения
            file_extension = uploaded_file.file.name.split('.')[-1].lower()

            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                uploaded_file.file_type = 'image'
                uploaded_file.save()
            elif file_extension in ['txt', 'csv']:
                uploaded_file.file_type = 'text'
                uploaded_file.save()
            # Другие условия для обработки других типов файлов

            # Запуск задачи celery для обработки файла
            transaction.on_commit(
                lambda: process_file.delay(uploaded_file.id)
            )
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            # Обработка ошибок
            return Response(
                {
                    'error': 'Не удается определить тип файла',
                    'detail': str(ex)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

