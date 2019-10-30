from django.urls import reverse, resolve
from form import views

class TestUrls:

	def test_detail_urls(self):

		path = reverse('homepage')

		assert resolve(path).view_name == 'homepage'
	

	def test_detail_urls1(self):

		path = reverse('register')
		assert resolve(path).view_name == 'register'


	def test_detail_urls2(self):

		path = reverse('logout')
		assert resolve(path).view_name == 'logout'


	def test_detail_urls3(self):

		path = reverse('login')
		assert resolve(path).view_name == 'login'	
	


