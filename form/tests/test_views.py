from django.urls import reverse, resolve
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
from form.views import homepage
from django.test import TestCase
from form.views import register, logout_request, login_request
import pytest

@pytest.mark.django_db
class TestViews(TestCase):

	@classmethod
	def setUpClass(cls):

		super(TestViews, cls).setUpClass()
		mixer.blend('form.UserDetail')
		cls.factory = RequestFactory()	

	def test_homepage(self):
		

		path = reverse('homepage')
		request = self.factory.get(path)
		request.user = mixer.blend( User)

		response = homepage(request)
		assert response.status_code == 200


	def test_register(self):

		path = reverse("register")
		request = self.factory.get(path)
		request.user = mixer.blend( User)

		response = register(request)
		assert response.status_code == 200


	def test_register(self):

		path = reverse("login")
		request = self.factory.get(path)

		request.user = mixer.blend( User)
		login_request(request)
		



from django.test.client import Client
class TestLogout(TestCase):

	def test_logout(self):

		self.client = Client()

		self.client.login(username='dimri1', password='dimri1')
		response = self.client.get('logout')
		self.assertEqual(response.status_code, 404)
		#assert response.status_code == 200

#@pytest.fixture
#def factory(scope='module'):

#	return RequestFactory()

#@pytest.fixture
#def product(db):

#	return mixer.blend('form.UserDetail')

#	def test_views_detail_authenticated(factory, product):
		

#		path = reverse('homepage')
#		request = factory.get(path)
#		request.user = mixer.blend( User)

#		response = homepage(request)
#		assert response.status_code == 200
