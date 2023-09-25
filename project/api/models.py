from django.db import models, transaction
# from .tasks import process_file  # Это задача Celery для обработки файла


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    file_type = models.CharField(max_length=50, blank=True)  # Поле для хранения типа файла

    def __str__(self):
        return f'{self.file.name}'

    # @transaction.atomic
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     transaction.on_commit(lambda: process_file.delay(self.id))
