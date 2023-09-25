from django.test import TestCase

from ..models import File


class TestModels(TestCase):
    def test_File(self):
        file_1 = File.objects.create(
            file='/uploads/sample.txt',
        )
        self.assertIs('/uploads/sample.txt', file_1.__str__())
