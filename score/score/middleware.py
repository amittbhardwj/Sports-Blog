from blog.models import ExtendedUser

class Auth(object):
    def process_request(self, request):
        request.__class__.user = ExtendedUser()
        return None