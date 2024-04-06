from rest_framework import serializers
from .models import Professor ,Assistant ,User
from lesson.models import Term



#get User professors serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'national_code')

#get and post professors serializers
class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


#update and delete professors serializers
class UpdateDeleteProfessorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Professor
        fields = ('user','faculty', 'field_of_study', 'order')


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
        

# class TermSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Term
#         fields = '__all__'
