from django.shortcuts import render
from models import *
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.contrib.comments.models import Comment
# Create your views here

@login_required(redirect_field_name=None)
def writepost(request):
	
	return render(request,'blog/write.html')
	
@login_required(redirect_field_name=None)
def createpost(request,value):
	author = User.objects.get(username=request.user.username)
	title = request.POST['title']
	post = request.POST['content']
	if int(value) == 0:
		obj = Post(title = title,author=author,post=post)
		obj.save()
		num = len(Post.objects.filter(author=author))
		return render(request,'blog/congrats.html',{'num':num,'obj' : obj})
	else :
		obj = Post(title = title,author=author,post=post,is_draft=True)
		obj.save()
		return HttpResponseRedirect("/dashboard/")	
	
	

def displaypost(request,name,title):
	post = Post.objects.get(title=title)
	if not PostView.objects.filter(post=post,session=request.session.session_key):
		view = PostView(post=post,user=request.user.username,session=request.session.session_key)
		view.save()
	count = PostView.objects.filter(post=post).count()
	a  = PostView.objects.aggregate(Max('id'))
	obj	= PostView.objects.get(id=a['id__max'])
	comment = Comment.objects.filter(object_pk = post.id)
	img = []
	users = []
	for i in comment:
		luser = User.objects.get(id = i.user_id )
		users.append(luser)
		user = Moreinfo.objects.get(user = luser)
		img.append(user)

	return render(request,'blog/post.html',{'post':post,'count' : count,'obj' : obj,'img' : img,'mixed' : zip(comment,img,users)})

@login_required(redirect_field_name=None)
def dashboard(request):
	user = User.objects.get(username=request.user.username)
	posts = Post.objects.filter(author = user)
	more = Moreinfo.objects.get(user = user)
	return render(request,'blog/dashboard.html',{'posts' : posts,'more' : more})