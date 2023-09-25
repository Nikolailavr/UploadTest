import shutil

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import File
from ..serializers import FileSerializer


class TestAPI(TestCase):

    def test_get_files(self):
        file_1 = File.objects.create(
            file='/uploads/sample.txt',
            file_type='text'
        )
        file_2 = File.objects.create(
            file='/uploads/sample.png',
            file_type='image'
        )
        url = reverse('api:get_files')
        response = self.client.get(url)
        serializer = FileSerializer([file_1, file_2], many=True).data
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(serializer, response.data)

    def test_upload_file_fail(self):
        response = self.client.post(reverse('api:upload_file'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_file(self):
        file = SimpleUploadedFile(
            name='sample.txt',
            content=b'Sample text'
        )
        response = self.client.post(
            reverse('api:upload_file'), {'file': file}
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['file'], '/uploads/sample.txt')
        self.assertEquals(len(File.objects.all()), 1)
        file = SimpleUploadedFile(
            name='sample.png',
            content=b'1',
            content_type='image/png'
        )
        response = self.client.post(
            reverse('api:upload_file'), {'file': file}
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['file'], '/uploads/sample.png')
        self.assertEquals(len(File.objects.all()), 2)
        shutil.rmtree('uploads/', ignore_errors=True)
