from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
import feedparser
import re
from django.contrib.auth.decorators import login_required
import simplejson
from blog.models import *
from django.db.models import Max
from blog.forms import *
import connections
compid = 0
count = 1
def boom(request):
	maxid = Post.objects.aggregate(Max('id'))
	mid =maxid['id__max']
	data = {}
	temp = compid
	if not compid == mid:
		data['recent'] = Post.objects.get(id = mid).title
		data['count'] = mid - temp 
		global compid
		compid = mid  
	else :
		data = {}
	response = simplejson.dumps(data)
	return HttpResponse(response,content_type='application/json')
	 
			
	#post = Post.objects.get(id = mid)
	
	#data['a'] = post.title
	#response = simplejson.dumps(data)
	'''newkey=0
	data={i : Post.objects.get(id = i).title for i in range(mid,mid-5,-1) }
	for i in range(mid,mid-5,-1):
		data[newkey] = data.pop(i)
		newkey = newkey + 1'''
	

def registration(request):
	allusers = auth.models.User.objects.all()
	name = request.POST['name']
	flag = False
	for i in allusers:
		if i.username == name :
			flag = True			
	response = {}
	response['check'] = flag
	r=simplejson.dumps(response)
	if flag:
		return HttpResponse(r,content_type ='application/json')
	else:
		first = request.POST['first']
		last = request.POST['last']
		email = request.POST['email']
		passw = request.POST['pass']
		#about = request.POST['about']
		#url = request.POST['url']
		user = auth.models.User.objects.create_user(name,email,passw)
		#user = User(username=name,email=email,password=passw),about=about,url=url)
		user.last_name = last
		user.first_name = first
		user.save()
		T.objects.create(user=user)
		authuser = auth.authenticate(username=name,password=passw)
		auth.login(request,authuser)
		return HttpResponse(r,content_type ='application/json')
		#return HttpResponseRedirect('/home/')

def getoptional(request):
	return render(request,'addons.html')		

def saveoptional(request):
	obj = Moreinfo()
	user = User.objects.get(username=request.user.username)
	obj.user = user
	obj.save()
	try:
		if request.POST['url']:
			obj.url = request.POST['url']
			obj.save()
		if request.POST['quote']:
			obj.quote = request.POST['quote']
			obj.save()
		if request.POST['about']:	
			obj.about = request.POST['about']
			obj.save()
		if request.FILES['image']:	
			obj.image = request.FILES['image']
			obj.save()

	except MultiValueDictKeyError:
		pass		
	return HttpResponseRedirect('/profile/')	

	
def login_page(request):
	
	return render(request,'login.html')

def show(request):
	d = feedparser.parse('http://www.espnfc.com/barclays-premier-league/23/rss') 
	check = request.user.is_authenticated()
	if check:
		display = request.user.username
	else :
		display = False
	#d = feedparser.parse('http://www.espncricinfo.com/rss/livescores.xml')
	arr=[]
	for i in range(len(d['entries'])):
		arr.append(d['entries'][i]['title'])
	images = []
	articles = []
	for i in range(len(d['entries'])):
		
		
		temp = d['entries'][i]['links']
		if len(temp) > 1:
			images.append(temp[1]['href'])
		articles.append(d['entries'][i]['summary'])	
	'''try:
		for i in range(len(d['entries'])):
		
		
				temp = d['entries'][i]['links'][1]
				if 'href' in temp.keys():
					images.append(temp) 
	except:
		pass'''
		#if temp.find('.jpg'):

		#	images.append(temp)	
	#for i in arr:
	#	a,b=i.split('v')
	#	x = re.split('\d',a)
	#	a = x[0].strip()
	#	x = re.split('\d',b)
	#	b = x[0].strip()
	'''scores = []	
	teams = []
	for i in arr:
		a,b = i.split('v')
	for i in arr:
		for j in i.split():
			if j[0].isdigit():
				scores.append(j)
			elif j[0]=='v' or j[0]=='*':
				del j;	
			else :
				teams.append(j) '''	
	final = zip(images,articles)			
	maxid = Post.objects.aggregate(Max('id'))
	mid =maxid['id__max']
	global compid 
	compid = mid
	titles = [Post.objects.get(id = i).title for i in range(mid,mid-5,-1)]
	return render(request,'home.html', {'len':4,'titles' : titles,'images':images,'articles':articles,'final':final})#,{'f':arr,'a':images,'d':display})#'scores':scores,'teams':teams,})

#@login_required(redirect_field_name=None)
def login(request):
	if not request.user.is_authenticated():
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
			auth.login(request, user)
			name = request.user.username
			first = request.user.first_name
			last = request.user.last_name
			email = request.user.email
			date = request.user.date_joined
			user = auth.models.User.objects.get(username=username)
			posts = Post.objects.filter(author = user)
			more = Moreinfo.objects.get(user=user)
			following = T.objects.get(user=user).follows.all().count()
			followed_by = user.follows.all().count()
			glist = []
			for i in posts:
				glist.append((i,PostView.objects.filter(post=i).count()))
			if len(glist) >= 5  :
				glist = glist[len(glist)-5 : len(glist)]
			length = len(glist)
			a  = PostView.objects.aggregate(Max('id'))
			obj	= PostView.objects.get(id=a['id__max'])
			return render(request, 'welcome.html', {'name':name,'first':first,'last':last,'email':email,'date':date,'more':more,
													'posts' : posts,'glist' : glist,'length' : length, 'num' : posts.count(),
													'obj' : obj,'following' : following, 'followed_by' : followed_by})
			# Redirect to a success page.

			#return HttpResponseRedirect(request.POST.get('next','/profile/'))			
		else:
			# Show an error page
			return HttpResponse("fail")
	else :
			name = request.user.username
			first = request.user.first_name
			last = request.user.last_name
			email = request.user.email
			date = request.user.date_joined
			author = auth.models.User.objects.get(username=name)
			posts = Post.objects.filter(author = author)
			more = Moreinfo.objects.get(user=author)
			following = T.objects.get(user=author).follows.all().count()
			followed_by = author.follows.all().count()
			glist = []
			for i in posts:
				glist.append((i,PostView.objects.filter(post=i).count()))
			if len(glist) >= 5  :
				glist = glist[len(glist)-5 : len(glist)]
			length = len(glist)
			a  = PostView.objects.aggregate(Max('id'))
			obj	= PostView.objects.get(id=a['id__max']) 		
			# Redirect to a success page.
			return render(request, 'welcome.html', {'name':name,'first':first,'last':last,'obj' : obj,'following' : following, 'followed_by' : followed_by,
				'email':email,'date':date,'posts' : posts,'more' : more,'glist' : glist,'length' : length,'num' : posts.count()})
			


	

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/home/')

def register(request):
	return render(request,'registration.html')


def changepassword(request):
	user = auth.models.User.objects.get(username=request.user.username)	
	pwd = request.POST['password']
	user.set_password(pwd)
	user.save()
	auth.login(request,auth.authenticate(username=request.user.username,password=pwd))
	return HttpResponseRedirect('/home/')

@login_required(redirect_field_name=None)
def change(request):

	return render(request,"change_password.html")


def publicprofile(request,name):
	puser = auth.models.User.objects.get(username=name)
	
	more = Moreinfo.objects.get(user=puser)
	posts = Post.objects.filter(author = puser)
	tags = Tags.objects.aggregate(Max('id'))
	tagid = tags['id__max']
	#tag = [Tags.objects.get(id = i).tag for i in range(tagid,tagid-8,-1)]
	followers=[]
	for i in puser.follows.all():
		followers.append(i.user)
	current_user = 	auth.models.User.objects.get(username=request.user.username)
	if current_user in followers:
		val = "Following"
	else : 
		val = "Follow"	
	rand = range(3);
	return render(request,'profile.html',{'puser' : puser, 'posts' : posts,'val' : val,
					'rand' : rand,'more':more, 'followers' : len(followers),'count' :posts.count()} )

def lol(request):
	clc = request.GET['clc']
	val = request.GET['tr']
	user = auth.models.User.objects.get(username=request.user.username)
	#change_dict = {"first":user.first_name,"last":user.last_name,"email":user.email}
	#change_dict[clc] = val
	if clc == "first":
		user.first_name = val
	elif clc == "last":
		user.last_name = val
	elif clc == "email":
		user.email = val
	user.save()
	data = {'val' : val}
	d = simplejson.dumps(data)
	return HttpResponse(d,content_type="application/json")

def saveimage(request):
	i = request.FILES['image']
	obj = Imageup(image=i)
	obj.save()
	#return HttpResponseRedirect(obj.image.url)
	return render(request,'uploadedimage.html',{'img' : obj})

def check(request,status):
	post = Post.objects.get(id=int(status))
	tag_list = request.GET.getlist('tags')

	for i in tag_list:
		if i :
			Tags.objects.create(tag=i,post = post)

	return HttpResponse("success")	

def follow(request,name,status):
	if int(status) == 0 :
		loggedin_user = User.objects.get(username=request.user.username)
		viewed_user = User.objects.get(username=name)
		query = T.objects.get(user = loggedin_user)
		query.follows.add(viewed_user)
		query.save()
		
	else :
		loggedin_user = User.objects.get(username=request.user.username)
		viewed_user = User.objects.get(username=name)
		query = T.objects.get(user = loggedin_user)
		query.follows.remove(viewed_user)
		query.save()

	val = simplejson.dumps({})
	return HttpResponse(val,content_type='application/json')




	def notify(request):
		user = User.objects.get(username=request.user.username)
		followers = user.follows.all()
		temp = len(followers)
