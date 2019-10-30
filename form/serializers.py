
from rest_framework import serializers
from form.models import UserDetail

class SnippetSerializers(serializers.ModelSerializer):

	class Meta:

		model = UserDetail
		fields = ['First_Name', 'Last_Name', 'email', 'date_joined', 'is_active', 'is_admin']

