import time

from celery import shared_task

from .models import File


@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        # Определите тип файла и выполните соответствующую обработку
        match file.file_type:
            case 'image':
                # Обработка изображений
                # time.sleep(5)
                print('Обработка изображений')
            case 'text':
                # Обработка текстовых файлов
                # time.sleep(5)
                print('Обработка текстовых файлов')
            # Другие условия для обработки других типов файлов

        file.processed = True
        file.save()
    except Exception:
        raise FileExistsError
