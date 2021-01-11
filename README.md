This is internship project of implementation of GraphQL Blog service
using the following tech stack.

python – 3.9.0

django – 3.1.3

graphene\_django – 2.13.0

This package provides couple of query and mutation examples of GraphQL
schema:

For detailed technical walkthrough, read TUTORIAL.

Overview of the project:

For this Blog project, the following models are created.

**Blog, Author, Comment, Entry**

A sample **models.py** file is given below:

*from django.db import models*

*from datetime import date*

*\# Create your models*

*class Blog(models.Model):*

*name = models.CharField(max\_length=100)*

*tagline = models.TextField()*

*def \_\_str\_\_(self):*

*return self.name*

*class Author(models.Model):*

*name = models.CharField(max\_length=100)*

*email = models.EmailField()*

*def \_\_str\_\_(self):*

*return self.name*

*class Comment(models.Model):*

*text = models.CharField(max\_length=100)*

*name = models.TextField()*

*def \_\_str\_\_(self):*

*return self.text*

*class Entry(models.Model):*

*blog = models.ForeignKey(Blog, on\_delete=models.CASCADE)*

*headline = models.CharField(max\_length=100)*

*body\_text = models.TextField()*

*date\_created = models.DateField(default=date.today)*

*authors = models.ManyToManyField(Author)*

*comments = models.ManyToManyField(Comment)*

*def \_\_str\_\_(self):*

*return self.headline *

A reference **schema.py** file is given below.

*import graphene*

*from graphene\_django import DjangoObjectType*

*from .models import BPost*

*from .models import Comment*

*class BPostType(DjangoObjectType):*

*class Meta:*

*model = BPost*

*class CommentType(DjangoObjectType):*

*class Meta:*

*model = Comment*

*class SearchResult(graphene.Union):*

*class Meta:*

*types = (BPostType, CommentType)*

*class Query(graphene.ObjectType):*

*bposts = graphene.List(BPostType)*

*bpost\_by\_id = graphene.Field(BPostType, id = graphene.Int())*

*bcomments = graphene.List(CommentType)*

*searchid = graphene.List(SearchResult, id=graphene.Int())*

*def resolve\_bposts(self, info, \*\*kwargs):*

*return BPost.objects.all()*

*def resolve\_bcomments(self, info, \*\*kwargs):*

*return Comment.objects.all()*

*def resolve\_bpost\_by\_id(self, info, id):*

*return BPost.objects.get(pk=id)*

*def resolve\_searchid(self, info, id):*

*posts = BPost.objects.all()*

*comments = Comment.objects.all()*

*return posts*

*\# Create New Post*

*class CreateBPost(graphene.Mutation):*

*id = graphene.Int()*

*title = graphene.String()*

*description = graphene.String()*

*dateCreated = graphene.Date()*

*author = graphene.String()*

*class Arguments:*

*title = graphene.String()*

*description = graphene.String()*

*dateCreated = graphene.Date()*

*author = graphene.String()*

*def mutate(self, info, title, description, dateCreated, author):*

*bpost = BPost(title=title, description=description, dateCreated =
dateCreated, author = author)*

*bpost.save()*

*return CreateBPost(*

*id=bpost.id,*

*title=bpost.title,*

*description=bpost.description,*

*dateCreated = bpost.dateCreated,*

*author = bpost.author,*

*)*

*\# Update a post*

*class UpdateBPost(graphene.Mutation):*

*class Arguments:*

*title = graphene.String(required=True)*

*description = graphene.String()*

*dateCreated = graphene.Date()*

*author = graphene.String()*

*id = graphene.ID()*

*\# The class attributes define the response of the mutation*

*bpostu = graphene.Field(BPostType)*

*def mutate(self, info, id, title, description, dateCreated, author):*

*bpostu = BPost.objects.get(pk=id)*

*bpostu.title = title*

*bpostu.description = description*

*bpostu.dateCreated = dateCreated*

*bpostu.author = author*

*bpostu.save()*

*\# Notice we return an instance of this mutation*

*return UpdateBPost(bpostu=bpostu)*

*\# Delete a post*

*class DeleteBPost(graphene.Mutation):*

*idDeleted = graphene.String()*

*class Arguments:*

*id = graphene.ID()*

*\# The class attributes define the response of the mutation*

*bpostd = graphene.Field(BPostType)*

*def mutate(self, info, id):*

*bpostd = BPost.objects.get(pk=id)*

*bpostd.delete()*

*\# Notice we return an instance of this mutation*

*return DeleteBPost(id)*

*\# Create New Comment*

*class CreateBComment(graphene.Mutation):*

*id = graphene.Int()*

*postid = graphene.Int()*

*text = graphene.String()*

*author = graphene.String()*

*class Arguments:*

*postid = graphene.Int()*

*text = graphene.String()*

*author = graphene.String()*

*def mutate(self, info, postid, text, author):*

*bcomment = Comment(postid = postid, text=text, author = author)*

*bcomment.save()*

*return CreateBComment(*

*id=bcomment.id,*

*postid=bcomment.postid,*

*text=bcomment.text,*

*author = bcomment.author,*

*)*

*\# Update a Comment*

*class UpdateBComment(graphene.Mutation):*

*class Arguments:*

*postid = graphene.Int()*

*text = graphene.String(required=True)*

*author = graphene.String()*

*id = graphene.ID()*

*\# The class attributes define the response of the mutation*

*bcommentu = graphene.Field(CommentType)*

*def mutate(self, info, id, postid, text, author):*

*bcommentu = Comment.objects.get(pk=id)*

*bcommentu.postid = postid*

*bcommentu.text = text*

*bcommentu.author = author*

*bcommentu.save()*

*\# Notice we return an instance of this mutation*

*return UpdateBComment(bcommentu=bcommentu)*

*\# Delete a Comment*

*class DeleteBComment(graphene.Mutation):*

*idDeleted = graphene.String()*

*class Arguments:*

*id = graphene.ID()*

*\# The class attributes define the response of the mutation*

*bcommentd = graphene.Field(CommentType)*

*def mutate(self, info, id):*

*bcommentd = Comment.objects.get(pk=id)*

*bcommentd.delete()*

*\# Notice we return an instance of this mutation*

*return DeleteBComment(id)*

*class Mutation(graphene.ObjectType):*

*create\_bpost = CreateBPost.Field()*

*update\_bpost = UpdateBPost.Field()*

*delete\_bpost = DeleteBPost.Field()*

*create\_bcomment = CreateBComment.Field()*

*update\_bcomment = UpdateBComment.Field()*

*delete\_bcomment = DeleteBComment.Field()*

***To use this github repository:***

Follow the following steps.

1.  Create a virtual environment

> \$ python -m venv /usr/projects/venv
>
> \$ /usr/projects/venv/scripts/activate
>
> \$ cd /usr/projects/venv

1.  Download the repository

    \$ git clone
    https://github.com/yochith-kondapalli/Django-graphene-graphQL

2.  Install python and other requirements

> \$ pip install -r requirements.txt

1.  Database activation

    \$ cd project1

    \$ ./manage.py migrate

    Now you can start loading the data by the Django shell. Or you can
    start the webserver and use graphql.

    To start the web server.

    \$ ./manage.py runserver

    For further guidance, read through the TUTORIAL.
