
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from article.models import Article
from article.models import User_1 , LikeByUser
import MySQLdb
import smtplib
import hashlib
#import easygui
# Create your views here.

u_name='a'
u_mail='a'
u_id=0
flag=0


def articles(request):
	articles = Article.objects.all()
	context = {'articles':articles}
	return render(request,'articles.html',context)



def article(request,article_id):
	if 'userid' in request.session:
		article = get_object_or_404(Article,pk=article_id)
		imageUrl= str(article.image)
		imageName = (imageUrl.split('/'))[3]
		context = {'imageName':imageName,'article':article}
		return render(request,'article.html',context)

	else:
		return HttpResponse('Dear user please Login or Regist in our site')




def likeArticle(request,article_id):
	article = Article.objects.get(pk=article_id)
	try:
		checkUser=LikeByUser.objects.get(userLike=0,articleId=article_id,userId_id=u_id)
		article.like +=1
		article.save()
		checkUser.userLike=1
		checkUser.save()
		#return HttpResponseRedirect('http://127.0.0.1:8000/article/get/{0}/'.format(article_id))
		return HttpResponse('like try')
	except:
		try :
			checkUserLike=LikeByUser.objects.get(userLike=1,articleId=article_id,userId_id=u_id)
			return HttpResponse('like before except try')
		except :
			addUser=LikeByUser(userLike=1,articleId_id=article_id, userId_id=u_id)	
			addUser.save()
			article.like +=1
			article.save()
			return HttpResponse('like  except try except')
		
def unlikeArticle(request,article_id):
	article = Article.objects.get(pk=article_id)
	try:
		checkUser=LikeByUser.objects.get(userLike=1,articleId=article_id,userId_id=u_id)
		article.like -=1
		article.save()
		checkUser.userLike=0
		checkUser.save()
		#return HttpResponseRedirect('http://127.0.0.1:8000/article/get/{0}/'.format(article_id))
		return HttpResponse('unlike try')
	except:
		try :
			checkUserLike=LikeByUser.objects.get(userLike=0,articleId=article_id,userId_id=u_id)
			return HttpResponse('unlike before except try')
		except :
			addUser=LikeByUser(userLike=0,articleId_id=article_id, userId_id=u_id)	
			addUser.save()
			article.like -=1
			article.save()
			return HttpResponse('unlike  except try except')


def comments(request):
	onArticle=[]
	onComment=[]
	allComment=[]
	
	comments = Comment.objects.all()
	for comment in comments:
		
		if comment.onComment == 0:
			onArticle.append(comment)
		else:
			onComment.append(comment)

	for comment in onArticle:
		allComment.append(comment)
		for oncomment in onComment:
		 	if oncomment.commentId == comment.id:
				allComment.append(oncomment)

	return render(request,'comments.html',{'allComment' : allComment})



#def article(request,article_id=1):
	#if 'userid' in request.session:
	#	article = get_object_or_404(Article,pk=article_id)
	#	return render(request,'article.html',{'article':article})
	#else:
	#	return HttpResponse('Dear user please Login or Regist in our site')


def reg(request):
	global flag
	flag=1
	return render(request,'reg.html')

def save(request):
	checkExists=0
	name=(request.POST['firstname'])
	mail=(request.POST['E-mail'])
	pas=request.POST['password']
	md5_object = hashlib.md5()
	md5_object.update(pas.encode("utf-8"))
	secret_code = md5_object.hexdigest()
	try:
		checkName = User_1.objects.get(user_name=name)
		checkEmail=User_1.objects.get(email=mail)
		if checkName or checkEmail :
			return render(request,'reg.html')
			
		else :
			m=User_1(user_name=name,email=mail,password=secret_code)	
			m.save()
			global u_id
			u_id=m.id
			request.session['userid']=u_id
			checkExists=1
	except:
		m=User_1(user_name=name,email=mail,password=secret_code)	
		m.save()
		global u_id
		u_id=m.id
		request.session['userid']=u_id
		checkExists=1
		#mail.send_mail(sender="engy.elmoshrify@gmail.com",
			      #to="rababelzen@yahoo.com",
			      #subject="Your account has been approved",
			      #body=""" hello
		#""")
	if checkExists==1 :
		sender = 'rababzein2012@gmail.com'
		receivers = ['engy.elmoshrify@gmail.com']

		message = """From: From Person <rababelzen@yahoo.com>
		To: To Person <rababelzen@yahoo.com>
		Subject: SMTP e-mail test

		This is a test e-mail message.
		"""

		try:
		   smtpObj = smtplib.SMTP('localhost')
		   smtpObj.sendmail(sender, receivers, message)         
		   return HttpResponse('Successfully sent email')
	
		#except SMTPException:
		except :
		   return HttpResponse('Error: unable to send email')



def check(request) :
	myName=request.POST['usrname']
	myPassword=request.POST['psw']
	md5_object = hashlib.md5()
	md5_object.update(myPassword.encode("utf-8"))
	secret_code = (md5_object.hexdigest())

	try :
		myuser =(User_1.objects.get(user_name=myName , password=secret_code))
 		if myuser:
			global u_name
			u_name=myuser.user_name
			global u_id
			u_id=myuser.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})
	except:
		return HttpResponse('Sorry Our Dear User May Entered Wrong Password ,User Name Or regist in our site ')
		

def checkfb(request):
	user_name = request.user.username
	email = request.user.email
	fid = request.user.id
	global u_name
	global u_mail
	u_name=user_name
	u_mail=email
	if flag==1:
		context={'name':user_name ,'mail':email}
		return render(request,'facepaswd.html',context)
	elif flag==2:
		return HttpResponseRedirect('http://localhost:8000/savefblogin/')

	else:
		return HttpResponse(" error")

def savefb(request):
	pas = request.POST['passw']
	md5_object = hashlib.md5()
	md5_object.update(pas.encode("utf-8"))
	secret_code = md5_object.hexdigest()
	try:
		checkName = User_1.objects.get(user_name=u_name)
		checkEmail=User_1.objects.get(email=u_mail)
		if checkName or checkEmail :
			return HttpResponse("Dear user you registered in our site before")
		else :
			you=User_1(user_name=u_name,email=u_mail,password=secret_code,logWithFb=1)
			you.save()
			global u_id
			u_id=you.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})
	except:
			you=User_1(user_name=u_name,email=u_mail,password=secret_code,logWithFb=1)
			you.save()
			global u_id
			u_id=you.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})


def savefblogin(request):
	try:
		checkName = User_1.objects.get(user_name=u_name)
		checkEmail=User_1.objects.get(email=u_mail)
		if checkName or checkEmail :
			global u_id
			u_id=checkName.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})
		else :
			you=User_1(user_name=u_name,email=u_mail,logWithFb=1)
			you.save()
			global u_id
			u_id=you.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})
	except:
			you=User_1(user_name=u_name,email=u_mail,logWithFb=1)
			you.save()
			global u_id
			u_id=you.id
			request.session['userid']=u_id
			return render(request,'welcome.html',{'name':u_name,})
	
def login(request):
	global flag
	flag=2
	return render(request,'login.html')

def home(request):
	
	return render(request,'home.html')

def logout(request):
	del request.session['userid']
	return HttpResponse("bye ya user")
	#return HttpResponse('hello'+str(new_user.id))
