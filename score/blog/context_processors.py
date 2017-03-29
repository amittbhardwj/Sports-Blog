from django.contrib.auth.models import User


def userdetails(request):
	flag = False
	if request.user.is_authenticated():
		flag = True
		user = User.objects.get(username=request.user.username)
		return {'user':user, 'flag' : flag}
	else : 
		return {'flag' : flag}	
	