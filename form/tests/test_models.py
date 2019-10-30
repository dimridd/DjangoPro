import pytest
from django.test import TestCase
from form.models import UserDetail as Entry


class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(email="dimri32@gmail.com")
        self.assertEqual(str(entry), entry.email)


class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(email='')
        self.assertEqual(str(entry), entry.email)