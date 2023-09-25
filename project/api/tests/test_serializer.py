from django.test import TestCase

from ..models import File
from ..serializers import FileSerializer


class TestFileSerializer(TestCase):
    def test_ok(self):
        file_1 = File.objects.create(
            file='/uploads/sample.txt',
            file_type='text'
        )
        file_2 = File.objects.create(
            file='/uploads/sample.png',
            file_type='image'
        )
        data = FileSerializer([file_1, file_2], many=True).data
        expected_data = [
            {
                'id': file_1.id,
                'file': '/uploads/sample.txt',
                'uploaded_at': str(file_1.uploaded_at).
                replace(' ', 'T').
                replace('+00:00', 'Z'),
                'processed': False,
                'file_type': 'text'
            },
            {
                'id': file_2.id,
                'file': '/uploads/sample.png',
                'uploaded_at': str(file_2.uploaded_at).
                replace(' ', 'T').
                replace('+00:00', 'Z'),
                'processed': False,
                'file_type': 'image'
            }
        ]
        self.assertEquals(expected_data, data)
