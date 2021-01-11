***Tutorial***

In this project, we will use **python** and **Django**. We will use
**SQLite** file based database.

We want to implement **GraphQL** server. The module **Graphene-Django**
has built in support for the GraphQL implemention.

Also we will use **GraphiQL** (Graph-i-QL), to have the Visual
Playground for testing our Schema.

Reference Web Links:

<https://docs.djangoproject.com/en/3.1/topics/db/queries/>

<https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/>

Software Needed: python, Django, Graphene-Django

python – 3.9.0

django – 3.1.3

graphene\_django – 2.13.0

Django-filter, Django-graphql-jwt

1.  Open a command prompt on your UNIX/Linux System, make sure that
    “python” is your PATH.

    \$ python

    Python 3.9.0

    &gt;&gt;&gt;

2.  Now before, we install Django, we will start Virtual Environment
    Shell

\$ pwd

/usr/projects

\$ python -m venv /usr/projects/venv1

Now, activate the virtual environment venv1

\$ /usr/projects/ven1/scripts/activate

…

ven1&gt;

1.  Install Django by using pip for that.

ven1&gt; pip install django graphene\_django

1.  Check the Django version.

ven1&gt; python -m django --version

1.  Start the new web project.

\$ django-admin startproject project1

\[The directory called “project1” is created”\]

\$ cd project1/project1

1.  Django separates the project into *apps*. Think about each app as a
    divisional section of our project.

    Create an app called “posts”

    In the project1 directory, create the first app.

    \$ django-admin startapp posts

    \[“posts” directory is created \]

2.  Next step is make the main Project “project1” configuration file to
    include the new app “apps”, which we just created. We also need to
    add graphene\_django.

Edit the file project1/project1/settings.py and add the
‘graphene\_django’ and ‘posts’ entries at the end of INSTALLED\_APPS

INSTALLED\_APPS = (

*\# After all the existing entries*

'graphene\_django’,

‘posts’,

)

1.  Create the database file in /usr/projects/ven1/project1

\$ python manage.py migrate

\[Notice “db.sqlite3” file is created, which is the database file\]

1.  Before we go ahead and work with models, let us test our Django
    installation once.

    Run the web server on localhost by the following command.

    \$ python manage.y runserver

    …..

    To test whether, the webserver is running or not, open a web browser
    and type the following in the URL toolbar.

    http://localhost :8000

    You will notice a “Django successful installation” message.

    Now, go back to the command window, and we will stop the web
    server running.

    Control + Break to STOP the web server.

2.  So far we created a Project, and then an App and then we created an
    empty database file.

    Now let us create some “web blog post s”. For maintaining identity
    and relationships, let us create the following four models.

    Blog, Author, Comment and Entry.

    Django relies on “Models” as a medium for our data to be stored in
    the database. Each model is defined with the fields, it needs. Here
    we have four models and their fields are defined in the
    file project1/posts/models.py.

    \$ cd posts

    \[ In the app directory , “models.py” file exists already\]

    Edit the models.py and add the following entries into it.

    from django.db import models

    from datetime import date

    \# Create your models

    class Blog(models.Model):

    name = models.CharField(max\_length=100)

    tagline = models.TextField()

    def \_\_str\_\_(self):

    return self.name

    class Author(models.Model):

    name = models.CharField(max\_length=100)

    email = models.EmailField()

    def \_\_str\_\_(self):

    return self.name

    class Comment(models.Model):

    text = models.CharField(max\_length=100)

    name = models.TextField()

    def \_\_str\_\_(self):

    return self.text

    class Entry(models.Model):

    blog = models.ForeignKey(Blog, on\_delete=models.CASCADE)

    headline = models.CharField(max\_length=100)

    body\_text = models.TextField()

    date\_created = models.DateField(default=date.today)

    authors = models.ManyToManyField(Author)

    comments = models.ManyToManyField(Comment)

    def \_\_str\_\_(self):

    return self.headline

3.  Go back the project1 directory.

\$ python manage.py makemigrations

\$ python manage.py migrate

1.  Now, let us do an Interactive way of storing and reading the data
    from the Database file.

We will use **Django Shell**.

ven1&gt; python manage.py shell

…

&gt;&gt;&gt;

1.  Create some models

The following code to be run in the Django Shell.

&gt;&gt;&gt;

from posts.models import Blog

from posts.models import Author

from posts.models import Comment

from posts.models import Entry

Blog.objects.create(name=”Sunday”, tagline=”Good Morning, Sunday”)

Blog.objects.create(name=”Monday”, tagline=”Good Morning, Monday”)

Blog.objects.create(name=”Tuesday”, tagline=”Good Morning,Tuesday”)

Blog.objects.create(name=”Wednesday”, tagline=”Good Morning, Wednesday”)

Blog.objects.create(name=”Thursday”, tagline=”Good Morning, Thursday”)

Blog.objects.all()

Author.objects.create(name=”John”, email=<john@mailserver.com>)

Author.objects.create(name=”Robert”, email=<robert@mailserver.com>)

Author.objects.create(name=”Will”, email=<will@mailserver.com>)

Author.obects.all()

Comment.objects.create(text=”Good Job”, name=”Jinny”)

Comment.objects.create(text=”Rightly Said”, name=”Sara”)

Comment.objects.create(text=”Wrong Notion Here”, name=”Mary”)

Comment.objects.create(text=”Wonderful Idea”, name=”Smith”)

Comment.objects.all()

\[The “date\_created” field for entry, it takes the Current Date. And
also the Django date format by default is “Year-Month-Date” form\]

1.  Now work with Django API for database by querying, filtering and
    adding, deleting the records.

&gt;&gt;&gt; b1 = Blog.objects.get(pk=1)

&gt;&gt;&gt; b2 = Blog.objects.get(pk=2)

&gt;&gt;&gt; b3 = Blog.objects.get(pk=3)

&gt;&gt;&gt; b4 = Blog.objects.get(pk=4)

&gt;&gt;&gt; b5=Blog.obejcts.get(pk=5)

&gt;&gt;&gt; a1 = Author.objects.get(pk=1)

&gt;&gt;&gt; a2 = Author.objects.get(pk=2)

&gt;&gt;&gt; a3 = Author.objects.get(pk=3)

&gt;&gt;&gt; c1 = Comment.objects.get(pk=1)

&gt;&gt;&gt; c2 = Comment.objects.get(pk=2)

&gt;&gt;&gt;c3 = Comment.objects.get(pk=3)

\[Now create first Entry \]

&gt;&gt;&gt; Entry.objects.create(blog=b1, headline=”Sunday News”)

&gt;&gt;&gt; e1 = Entry.objects.get(pk=1)

\[Now add authors and comments\]

&gt;&gt;&gt; e1.authors.add(a1,a2)

&gt;&gt;&gt;e1.comments.add(c1)

&gt;&gt;&gt;e1.comments.all()

&gt;&gt;&gt;e1.comments.add(c2,c3)

&gt;&gt; e1. comments.all()

\[To delete the third comment, first you to retrieve it\]

&gt;&gt;&gt; e1. comments.get(pk=3).delete()

&gt;&gt;&gt;e1.comments.all()

\[Now add another Entry\]

&gt;&gt;&gt; Entry.objects.create(blog=b2, headline=”Monday News”)

&gt;&gt;&gt; e2 = Entry.objects.get(pk=2)

&gt;&gt;&gt; e2.authors.add(a3)

&gt;&gt;&gt; e2.authors.add(a2)

&gt;&gt;&gt; e2.authors.all()

&gt;&gt;&gt; e2.comments.add(c4, c3)

&gt;&gt;&gt; e2.comments.all()

\[Now let us create an Entry with blog b1 only. So we will have two
entry records with blog b1\]

&gt;&gt;&gt; Entry.objects.create(blog=b1, headline=”New Sunday News…”)

&gt;&gt;&gt;e3 = Entry.objects.get(pk=3)

&gt;&gt;&gt; e3.authors.add(a1)

&gt;&gt;&gt;e3.authors.add(a3)

&gt;&gt;&gt;e3.comments.add(c1,c2)

&gt;&gt;&gt;e3.comments.all()

\[Now from entry, let us try to probe the blog deatails\]

&gt;&gt;&gt; e1.blog.tagline

&gt;&gt;&gt; e1.blog.id

&gt;&gt;&gt; e2.blog.name

\[Let us do some reverse lookup from Blog field of Entry\]

&gt;&gt; b1.entry\_set.all()

\[The above command looks for all the entry records, where b1 is the
blog\]

&gt;&gt; b1.entry\_set.count()

\[The above command gives you the number Entry records where b1 is
defined as the blog\]

\[Add the entry from Blog object\]

&gt;&gt;&gt;b2.entry\_set.add(e2)

\[The above command adds b1 (Blog 2) to the entry object 2\]

&gt;&gt;&gt; e2.blog

\[This gives you the number Entry records where b1 is defined as the
blog\]

\[Now, let us filter out elements from all objects, using the key word
“filter”\]

&gt;&gt;&gt; Entry.objects.filter(blog\_\_name = ‘Sunday’)

\[The above command filters out all the entry elements with blog whose
name is starting with “Sunday”. Note the \_\_\[double underscore\] to
access the fileds.\]

&gt;&gt;&gt; Entry.objects.filter(blog\_\_name\_\_startswith = “Sun”)

\[‘startswith’ keyword looks for the name of the blog entries starting
with “Sun”\]

&gt;&gt;&gt; Entry.objects.filter(blog\_\_name\_\_contains = “un”)

\[‘contains’ keyword looks for the ‘un’ in the blog name\]

&gt;&gt;&gt; Entry.objects.filter(blog\_\_name =
“Sunday”).filter(blog\_\_tagline\_\_startswith = “Good”)

\[The above query filters from the filtered output of the first Query\]

&gt;&gt;&gt; Entry.objects.exlcude(blog\_\_name = “Sunday”)

\[The above command lists all the entries where the blog name is not
exactly equal to “Sunday”\]

&gt;&gt;&gt; Entry.objects.filter(blog\_\_name\_\_icontains = “news”)

\[ ‘I’ before ‘contains’ or ‘startswith’ or ‘endswith’ makes the query
case insensitive \]

\[Now let us do some queries from Blog Objects side\]

&gt;&gt;&gt; Blog.objects.all()

&gt;&gt;&gt; Blog.objects.filter(entry\_\_headline\_\_icontains =
“news”)

\[ icontains – for case insensitive search \]

&gt;&gt;&gt; Blog.objects.filter(entry\_\_authors\_\_name=”John”)

\[ Lists all the entries with an author name matching exactly as
“John”\]

&gt;&gt;&gt; Blog.objects.filter(Entry\_\_comments\_\_text\_\_contains =
“Good”)

\[The above command finds all the entries where the comments are having
a word “Good” in them\]

&gt;&gt;&gt; Ctrl + Z

\[Exit the Django Shell \]

1.  Now let us create our first GraphQL Schema

Before we edit schema.py file, we have to define it in the settings.py
file.

In project1/project1/settings.py file, add the following at the end.

GRAPHENE = {

'SCHEMA': 'project1.schema.schema',

}

Now to edit the schema.py file.

Create a file called schema.py in project1/posts/schema.py.

Add the following Query and Mutation.

import graphene

from graphene\_django import DjangoObjectType

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

def resolve\_allblogs(self, info, \*\*kwargs):

return Blog.objects.all()

def resolve\_allauthors(self, info, \*\*kwargs):

return Author.objects.all()

def resolve\_allcomments(self, info, \*\*kwargs):

return Comment.objects.all()

def resolve\_allentries(self, info, \*\*kwargs):

return Entry.objects.all()

\# Create a New Blog

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

\# Mutation Method

class Mutation(graphene.ObjectType):

create\_blog = CreateBlog.Field()

1.  The above schema.py file is created in the “posts” app folder. We
    have to create another schema.py file in our project directory
    linking that schema to this one.

Create a file project1/project1/schema.py

Add the following entries in that.

import graphene

import posts.schema

class Query(posts.schema.Query, graphene.ObjectType):

pass

class Mutation(posts.schema.Mutation, graphene.ObjectType):

pass

schema = graphene.Schema(query=Query, mutation=Mutation)

Note: This query just inherits the query defined before. This way, you
are able to keep every part of the schema isolated in the apps.

1.  GraphiQL:

To enable GraphiQL, we will add the following code to the urls.py file

project1/project1/urls.py is the path. The new URL for “graphql”, add it
to “admin” which is already present in the urlpatterns.

... *\# code*

from django.views.decorators.csrf import csrf\_exempt

from graphene\_django.views import GraphQLView

urlpatterns = \[

path('graphql/', csrf\_exempt(GraphQLView.as\_view(graphiql=True))),

\]

1.  Now start the webserver.

ven1&gt; python manage.py runserver

1.  Now test the GraphQL schema.

    The GraphQL endpoint is given by the url.

    <http://localhost:8000/graphql>

    Try the query: \[ Note; you can optionally add “query” before the
    following query \]

    {

    allblogs {

    id

    name

    tagline

    }

    }

    For all entries, authors and all comments.

    {

    allentries {

    blog {

    name

    tagline

    }

    headline

    dateCreated

    bodyText

    authors {

    name

    email

    }

    comments {

    text

    name

    }

    }

    }

    Now, let us try a Mutation.

    *mutation {*

    *createBlog(name: "Friday", tagline: "Good Morning, Friday"){*

    *id*

    *name*

    *tagline*

    *}*

    *}*

    And again, query back to see whether the new record is added or not.

2.  After testing, stop the web server

    CTRL + BREAK to stop the server running on command line.

3.  Now go out of the virtual environment

Venv1 &gt; deactivate

…

\$
