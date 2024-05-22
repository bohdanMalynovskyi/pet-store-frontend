from rest_framework.authtoken.models import Token


class TokenStrategy:
    @classmethod
    def obtain(cls, user):
        token, created = Token.objects.get_or_create(user=user)
        return {
            'access': token.key,
            'user': user
        }
