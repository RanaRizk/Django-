from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	like = models.IntegerField(default=0)
	image = models.ImageField(upload_to = "static/images/article") 
	published = models.BooleanField(default=False)


class User_1(models.Model):
	user_name= models.CharField(max_length=100)
	password= models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	image = models.ImageField(upload_to = "static/images/user") 
	logWithFb = models.BooleanField(default=False)


class Comment(models.Model):
	articleId = models.ForeignKey(Article)
	userId = models.ForeignKey(User_1)
	onComment = models.BooleanField(default=False)
	like = models.IntegerField(default=0)
	body = models.TextField()
	commentId = models.IntegerField(default=0)


class TagOnArticle(models.Model):
	articleId = models.ForeignKey(Article)
	tag = models.CharField(max_length=200)
	


class LikeByUser(models.Model):
	articleId = models.ForeignKey(Article)
	userId = models.ForeignKey(User_1)
	userLike = models.IntegerField(default=0)









