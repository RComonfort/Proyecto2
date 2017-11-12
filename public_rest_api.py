import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from google.appengine.api import images
from google.appengine.ext import blobstore
import cloudstorage
import mimetypes
import json
import os
import jinja2

from models import Empresa
from models import Usuarios
from models import Videogame
from models import Developer
from models import Publisher
from models import Genre
from models import Tweet

jinja_env = jinja2.Environment(
 loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class DemoClass(object):
 pass

def MyClass(obj):
 return obj.__dict__


class GetTweetsHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myTweets = Tweet.query(Tweet.empresa_key == myEmpKey)

     myList = []
     for i in myTweets:
      myObj = DemoClass()
      myObj.title = i.title
      myObj.description = i.description
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetVideogamesHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_user = self.request.get('user')
     objemp = Usuarios.query(Usuarios.email == id_user).get() #No se puede evaluar en base a key cno este metodo
     strKey = objemp.key.urlsafe() 
     ownerKey = ndb.Key(urlsafe=strKey) 
     
     myEntities = Videogame.query(Videogame.user_key == ownerKey)

     myList = []
     for i in myEntities:
      myObj = DemoClass()
      
      myObj.title = i.title
      myObj.developer = i.developer
      myObj.publisher = i.publisher
      myObj.year = i.year
      myObj.description = i.description
      myObj.genre = i.genre
      myObj.image = i.image
      
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetPublishersHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_user = self.request.get('user')
     objemp = Usuarios.query(Usuarios.email == id_user).get()
     strKey = objemp.key.urlsafe() 
     ownerKey = ndb.Key(urlsafe=strKey) 
     
     myEntities = Publisher.query(Publisher.user_key == ownerKey)

     myList = []
     for i in myEntities:
      myObj = DemoClass()
      
      myObj.nameA = i.nameA
      myObj.location = i.location
      myObj.year = i.year
      myObj.logo = i.logo
      
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)
     
class GetDevelopersHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_user = self.request.get('user')
     objemp = Usuarios.query(Usuarios.email == id_user).get()
     strKey = objemp.key.urlsafe() 
     ownerKey = ndb.Key(urlsafe=strKey) 
     
     myEntities = Developer.query(Developer.user_key == ownerKey)

     myList = []
     for i in myEntities:
      myObj = DemoClass()
      
      myObj.nameA = i.nameA
      myObj.location = i.location
      myObj.year = i.year
      myObj.logo = i.logo
      
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)     

class GetGenresHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_user = self.request.get('user')
     objemp = Usuarios.query(Usuarios.email == id_user).get()
     strKey = objemp.key.urlsafe() 
     ownerKey = ndb.Key(urlsafe=strKey) 
     
     myEntities = Genre.query(Genre.user_key == ownerKey)

     myList = []
     for i in myEntities:
      myObj = DemoClass()
      
      myObj.nameA = i.nameA
      myObj.description = i.description
      
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string) 

###########################################################################     


class UpHandler(webapp2.RequestHandler):
    def _get_urls_for(self, file_name):
        
     bucket_name = app_identity.get_default_gcs_bucket_name()
     path = os.path.join('/', bucket_name, file_name)
     real_path = '/gs' + path
     key = blobstore.create_gs_key(real_path)
     try:
      url = images.get_serving_url(key, size=0)
     except images.TransformationError, images.NotImageError:
      url = "http://storage.googleapis.com{}".format(path)

     return url


    def post(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     bucket_name = app_identity.get_default_gcs_bucket_name()
     uploaded_file = self.request.POST.get('uploaded_file')
     file_name = getattr(uploaded_file, 'filename', None)
     file_content = getattr(uploaded_file, 'file', None)
     real_path = ''

     if file_name and file_content:
      content_t = mimetypes.guess_type(file_name)[0]
      real_path = os.path.join('/', bucket_name, file_name)

      with cloudstorage.open(real_path, 'w', content_type=content_t,
       options={'x-goog-acl': 'public-read'}) as f:
       f.write(file_content.read())

      key = self._get_urls_for(file_name)
      self.response.write(key)


class LoginHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('login.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)


class TweetHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('tweet.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class VideogameHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('videogame.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
    
class PublisherHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('publisher.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
    
class DeveloperHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('developer.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
    
class GenreHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('genre.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class MainHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('index.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/tweets', TweetHandler),
    ('/up', UpHandler),
    ('/videogames', VideogameHandler),
    ('/publishers', PublisherHandler),
    ('/developers', DeveloperHandler),
    ('/genres', GenreHandler),
    ('/gettweets', GetTweetsHandler),
    ('/getvideogames', GetVideogamesHandler),
    ('/getpublishers', GetPublishersHandler),
    ('/getdevelopers', GetDevelopersHandler),
    ('/getgenres', GetGenresHandler)
], debug = True)
