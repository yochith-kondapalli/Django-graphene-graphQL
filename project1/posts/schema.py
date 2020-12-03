
import graphene
from graphene_django import DjangoObjectType

from .models import Blog
from .models import Author
from .models import Comment
from .models import Entry


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class EntryType(DjangoObjectType):
    class Meta:
        model = Entry

class Query(graphene.ObjectType):
    allblogs = graphene.List(BlogType)
    allauthors = graphene.List(AuthorType)
    allcomments = graphene.List(CommentType)
    allentries = graphene.List(EntryType)
    def resolve_allblogs(self, info, **kwargs):
        return Blog.objects.all()
    def resolve_allauthors(self, info, **kwargs):
        return Author.objects.all()
    def resolve_allcomments(self, info, **kwargs):
        return Comment.objects.all()
    def resolve_allentries(self, info, **kwargs):
        return Entry.objects.all()


# Create a  New Blog

class CreateBlog(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    tagline = graphene.String()


    class Arguments:
        name = graphene.String()
        tagline = graphene.String()

  
    def mutate(self, info, name, tagline):
        blog1 = Blog(name=name, tagline = tagline)
        blog1.save()

        return CreateBlog(
            	id=blog1.id,
            	name=blog1.name,
            	tagline=blog1.tagline,
        )

class CreateAuthor(graphene.Mutation):
	name = graphene.String()
	email = graphene.String()

	class Arguments:
		name = graphene.String()
		email = graphene.String()
	def mutate(self, info, name, email):
		author1 = Author(name=name, email=email)
		author1.save()
	
		return CreateAuthor(name=author1.name, email = author1.email,)

class CreateComment(graphene.Mutation):
	text = graphene.String()
	name = graphene.String()
	
	class Arguments:
		text = graphene.String()
		name = graphene.String()
	def mutate(self, info, text, name):
		comment1 = Comment(text=text, name=name)
		comment1.save()

		return CreateComment(text=comment1.text, name = comment1.name,)

# Mutation Method

class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    create_author = CreateAuthor.Field()
    create_comment = CreateComment.Field()

