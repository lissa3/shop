from djoser.serializers import UserCreateSerializer as UCSer
from django.contrib.auth import  get_user_model



User = get_user_model()

class UserCreateSerializer(UCSer):
    class Meta(UCSer.Meta):
        model = User
        fields = ['id','email','first_name','last_name','password']

