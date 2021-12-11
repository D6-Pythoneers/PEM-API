from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["username"] = user.username
        token["name"] = user.name
        token["role"] = user.role
        token["sid"] = user.school_id
        token["nid"] = user.nid
        token["eid"] = user.eid
        token["qualification"] = user.qualification
        token["directorate"] = user.directorate
        return token


class MyTokenObtainPairCustomView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
