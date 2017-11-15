#!/usr/bin/env python
# -*- coding: utf-8 -*-

import endpoints
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from protorpc import remote

import jwt
import time

from CustomExceptions import NotFoundException

from messages import EmailPasswordMessage, TokenMessage, CodeMessage, Token, TokenKey, MessageNone
from messages import EmpresaInput, EmpresaUpdate, EmpresaList
from messages import TweetInput, TweetUpdate, TweetList
from messages import UserInput, UserUpdate, UserList
from messages import ProductInput, ProductUpdate, ProductList
from messages import DeveloperInput, DeveloperUpdate, DeveloperList
from messages import VideogameInput, VideogameUpdate, VideogameList
from messages import PublisherInput, PublisherUpdate, PublisherList
from messages import GenreInput, GenreUpdate, GenreList

from endpoints_proto_datastore.ndb import EndpointsModel

import models
from models import validarEmail
from models import Empresa, Usuarios, Tweet, Product, Developer, Videogame, Publisher, Genre


###############
# Publishers
###############
@endpoints.api(name='publishers_api', version='v1', description='publishers endpoints')
class PublishersApi(remote.Service):

######## Add Publishers ##########
  @endpoints.method(PublisherInput, CodeMessage, path='publishers/insert', http_method='POST', name='publishers.insert')
  def publisher_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id']) #el usuario que registro este dev
      
      myPub = Publisher()

      if myPub.publisher_m(request, user.key) == 0:
        codigo = 1
      else:
        codigo = -3

      message = CodeMessage(code=codigo, message='Publisher added')
   
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

######## List Publishers ##########
  @endpoints.method(Token, PublisherList, path='publishers/list', http_method='POST', name='publishers.list')
  def publisher_list(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = PublisherList(code=1) # crea objeto mensaje
      lstBd = Publisher.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(PublisherUpdate(token='', entityKey = i.entityKey,
                                #empresa_key=user.empresa_key.urlsafe(),
                                nameA = i.nameA,
                                location = i.location,
                                year = i.year,
                                logo = i.logo))
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = PublisherList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = PublisherList(code=-2, data=[]) #token expiro
    return message

######## Get one Publisher ##########
  @endpoints.method(TokenKey, PublisherList, path='publishers/get', http_method='POST', name='publishers.get')
  def publisher_get(cls, request):
    try:                 
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      publisherentity = ndb.Key(urlsafe = request.entityKey)
      publisher = Publisher.get_by_id(publisherentity.id())
      
      lista = []  #crea lista
      lstMessage = PublisherList(code=1) # crea objeto mensaje
      lista.append(PublisherUpdate(token='', 
                                 entityKey= publisher.entityKey,
                                 #empresa_key = user.empresa_key.urlsafe(),
                                 nameA = publisher.nameA,
                                 location = publisher.location,
                                 year = publisher.year,
                                 logo = publisher.logo))
      lstMessage.data = lista #ASIGNA a la salida la lista
      message = lstMessage
    
    except jwt.DecodeError:
      message = PublisherList(code=-1, data=[]) #token invalido
    
    except jwt.ExpiredSignatureError:
      message = PublisherList(code=-2, data=[]) #token expiro
    
    return message
    

######## Update Publisher ##########  
  @endpoints.method(PublisherUpdate, CodeMessage, path='publishers/update', http_method='POST', name='publishers.update')
  def publisher_update(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      publisher = Publisher()

      # empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
      if publisher.publisher_m(request, user.key) == 0:
        codigo = 1
      
      else:
        codigo = -3
      
      message = CodeMessage(code = 1, message='Sus cambios han sido guardados exitosamente')
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message='Token expired')
    return message    
    
    
######## Delete Publisher ##########    
  @endpoints.method(TokenKey, CodeMessage, path='publishers/delete', http_method='POST', name='publishers.delete')
  def publisher_remove(cls, request):
    try:

      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      publisherEntity = ndb.Key(urlsafe = request.entityKey)#Obtiene el elemento dado el EntityKey
      publisherEntity.delete()#BORRA
      message = CodeMessage(code = 1, message = 'Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')

    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message


###############
# Developers
###############
@endpoints.api(name='developers_api', version='v1', description='developers endpoints')
class DevelopersApi(remote.Service):

######## Add Developers ##########
  @endpoints.method(DeveloperInput, CodeMessage, path='developers/insert', http_method='POST', name='developers.insert')
  def developer_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id']) #el usuario que registro este dev
      
      myDev = Developer()

      if myDev.developer_m(request, user.key) == 0:
        codigo = 1
      else:
        codigo = -3

      message = CodeMessage(code=codigo, message='Developer added')
   
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

######## List Developers ##########
  @endpoints.method(Token, DeveloperList, path='developers/list', http_method='POST', name='developers.list')
  def developer_list(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = DeveloperList(code=1) # crea objeto mensaje
      lstBd = Developer.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(DeveloperUpdate(token='', entityKey = i.entityKey,
                                #empresa_key=user.empresa_key.urlsafe(),
                                nameA = i.nameA,
                                location = i.location,
                                year = i.year,
                                logo = i.logo))
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = DeveloperList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = DeveloperList(code=-2, data=[]) #token expiro
    return message

######## Get one Developer ##########
  @endpoints.method(TokenKey, DeveloperList, path='developers/get', http_method='POST', name='developers.get')
  def developer_get(cls, request):
    try:                 
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      developerentity = ndb.Key(urlsafe = request.entityKey)
      developer = Developer.get_by_id(developerentity.id())
      
      lista = []  #crea lista
      lstMessage = DeveloperList(code=1) # crea objeto mensaje
      lista.append(DeveloperUpdate(token='', 
                                 entityKey= developer.entityKey,
                                 #empresa_key = user.empresa_key.urlsafe(),
                                 nameA = developer.nameA,
                                 location = developer.location,
                                 year = developer.year,
                                 logo = developer.logo))
      lstMessage.data = lista #ASIGNA a la salida la lista
      message = lstMessage
    
    except jwt.DecodeError:
      message = DeveloperList(code=-1, data=[]) #token invalido
    
    except jwt.ExpiredSignatureError:
      message = DeveloperList(code=-2, data=[]) #token expiro
    
    return message
    

######## Update Developer ##########  
  @endpoints.method(DeveloperUpdate, CodeMessage, path='developers/update', http_method='POST', name='developers.update')
  def developer_update(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      developer = Developer()

      # empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
      if developer.developer_m(request, user.key) == 0:
        codigo = 1
      
      else:
        codigo = -3
      
      message = CodeMessage(code = 1, message='Sus cambios han sido guardados exitosamente')
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message='Token expired')
    return message    
    
    
######## Delete Developer ##########    
  @endpoints.method(TokenKey, CodeMessage, path='developers/delete', http_method='POST', name='developers.delete')
  def developer_remove(cls, request):
    try:

      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      developerEntity = ndb.Key(urlsafe = request.entityKey)#Obtiene el elemento dado el EntityKey
      developerEntity.delete()#BORRA
      message = CodeMessage(code = 1, message = 'Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')

    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message
    

###############
# Videogames
###############
@endpoints.api(name='videogames_api', version='v1', description='videogames endpoints')
class VideogamesApi(remote.Service):

######## Add Videogames ##########
  @endpoints.method(VideogameInput, CodeMessage, path='videogames/insert', http_method='POST', name='videogames.insert')
  def videogame_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id']) #el usuario que registro este dev
      
      myVideogame = Videogame()

      if myVideogame.videogame_m(request, user.key) == 0:
        codigo = 1
      else:
        codigo = -3

      message = CodeMessage(code=codigo, message='Videogame added')
   
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

######## List Videogames ##########
  @endpoints.method(Token, VideogameList, path='videogames/list', http_method='POST', name='videogames.list')
  def videogame_list(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = VideogameList(code=1) # crea objeto mensaje
      lstBd = Videogame.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(VideogameUpdate(token='', entityKey = i.entityKey,
                                #empresa_key=user.empresa_key.urlsafe(),
                                title = i.title,
                                developer = i.developer,
                                publisher = i.publisher,
                                year = i.year,
                                description = i.description,
                                genre = i.genre,
                                image = i.image))
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = VideogameList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = VideogameList(code=-2, data=[]) #token expiro
    return message

######## Get one Videogame ##########
  @endpoints.method(TokenKey, VideogameList, path='videogames/get', http_method='POST', name='videogames.get')
  def videogame_get(cls, request):
    try:                 
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      videogameentity = ndb.Key(urlsafe = request.entityKey)
      videogame = Videogame.get_by_id(videogameentity.id())
      
      lista = []  #crea lista
      lstMessage = VideogameList(code=1) # crea objeto mensaje
      lista.append(VideogameUpdate(token='', 
                                 entityKey= videogame.entityKey,
                                 #empresa_key = user.empresa_key.urlsafe(),
                                 title = videogame.title,
                                 developer = videogame.developer,
                                 publisher = videogame.publisher,
                                 year = videogame.year,
                                 description = videogame.description,
                                 genre = videogame.genre,
                                 image = videogame.image))
      lstMessage.data = lista #ASIGNA a la salida la lista
      message = lstMessage
    
    except jwt.DecodeError:
      message = VideogameList(code=-1, data=[]) #token invalido
    
    except jwt.ExpiredSignatureError:
      message = VideogameList(code=-2, data=[]) #token expiro
    
    return message
    

######## Update Videogame ##########  
  @endpoints.method(VideogameUpdate, CodeMessage, path='videogames/update', http_method='POST', name='videogames.update')
  def videogame_update(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      videogame = Videogame()

      # empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
      if videogame.videogame_m(request, user.key) == 0:
        codigo = 1
      
      else:
        codigo = -3
      
      message = CodeMessage(code = 1, message='Sus cambios han sido guardados exitosamente')
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message='Token expired')
    return message    
    
    
######## Delete Videogame ##########    
  @endpoints.method(TokenKey, CodeMessage, path='videogames/delete', http_method='POST', name='videogames.delete')
  def videogame_remove(cls, request):
    try:

      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      videogameEntity = ndb.Key(urlsafe = request.entityKey)#Obtiene el elemento dado el EntityKey
      videogameEntity.delete()#BORRA
      message = CodeMessage(code = 1, message = 'Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')

    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message


###############
# Genres
###############
@endpoints.api(name='genres_api', version='v1', description='genres endpoints')
class GenresApi(remote.Service):

######## Add Genres ##########
  @endpoints.method(GenreInput, CodeMessage, path='genres/insert', http_method='POST', name='genres.insert')
  def genre_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id']) #el usuario que registro este dev
      
      myGen = Genre()

      if myGen.genre_m(request, user.key) == 0:
        codigo = 1
      else:
        codigo = -3

      message = CodeMessage(code=codigo, message='Genre added')
   
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

######## List Genres ##########
  @endpoints.method(Token, GenreList, path='genres/list', http_method='POST', name='genres.list')
  def genre_list(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = GenreList(code=1) # crea objeto mensaje
      lstBd = Genre.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(GenreUpdate(token='', entityKey = i.entityKey,
                                #empresa_key=user.empresa_key.urlsafe(),
                                nameA = i.nameA,
                                description = i.description))
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = GenreList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = GenreList(code=-2, data=[]) #token expiro
    return message

######## Get one Genre ##########
  @endpoints.method(TokenKey, GenreList, path='genres/get', http_method='POST', name='genres.get')
  def genre_get(cls, request):
    try:                 
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      genreentity = ndb.Key(urlsafe = request.entityKey)
      genre = Genre.get_by_id(genreentity.id())
      
      lista = []  #crea lista
      lstMessage = GenreList(code=1) # crea objeto mensaje
      lista.append(GenreUpdate(token='', 
                                 entityKey= genre.entityKey,
                                 #empresa_key = user.empresa_key.urlsafe(),
                                 nameA = genre.nameA,
                                 description = genre.description))
      lstMessage.data = lista #ASIGNA a la salida la lista
      message = lstMessage
    
    except jwt.DecodeError:
      message = GenreList(code=-1, data=[]) #token invalido
    
    except jwt.ExpiredSignatureError:
      message = GenreList(code=-2, data=[]) #token expiro
    
    return message
    

######## Update Genre ##########  
  @endpoints.method(GenreUpdate, CodeMessage, path='genres/update', http_method='POST', name='genres.update')
  def developer_update(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      genre = Genre()

      # empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
      if genre.genre_m(request, user.key) == 0:
        codigo = 1
      
      else:
        codigo = -3
      
      message = CodeMessage(code = 1, message='Sus cambios han sido guardados exitosamente')
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message='Token expired')
    return message    
    
    
######## Delete Genre ##########    
  @endpoints.method(TokenKey, CodeMessage, path='genres/delete', http_method='POST', name='genres.delete')
  def genre_remove(cls, request):
    try:

      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      genreEntity = ndb.Key(urlsafe = request.entityKey)#Obtiene el elemento dado el EntityKey
      genreEntity.delete()#BORRA
      message = CodeMessage(code = 1, message = 'Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')

    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message


###############
# Products
###############
@endpoints.api(name='products_api', version='v1', description='products endpoints')
class ProductsApi(remote.Service):

  ######## Add products ##########
  @endpoints.method(ProductInput, CodeMessage, path='products/insert', http_method='POST', name='products.insert')
  def product_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])
      
      myProduct = Product()

      if myProduct.product_m(request, user.key) == 0:
        codigo = 1
      else:
        codigo = -3

      message = CodeMessage(code=codigo, message='Product added')
   
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

  @endpoints.method(TokenKey, ProductList, path='products/get', http_method='POST', name='products.get')
  def product_get(cls, request):
    try:                 
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      productentity = ndb.Key(urlsafe = request.entityKey)
      product = Product.get_by_id(productentity.id()) #obtiene usuario
      
      lista = []  #crea lista
      lstMessage = ProductList(code=1) # crea objeto mensaje
      lista.append(ProductUpdate(token='', 
                                 entityKey= product.entityKey,
                                 #empresa_key = user.empresa_key.urlsafe(),
                                 code = product.code,
                                 description = product.description,
                                 urlImage = product.urlImage)) # agrega a la lista

      lstMessage.data = lista #ASIGNA a la salida la lista
      message = lstMessage
    
    except jwt.DecodeError:
      message = UserList(code=-1, data=[]) #token invalido
    
    except jwt.ExpiredSignatureError:
      message = UserList(code=-2, data=[]) #token expiro
    
    return message


######## list products ##########

  @endpoints.method(Token, ProductList, path='products/list', http_method='POST', name='products.list')
  def product_list(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = ProductList(code=1) # crea objeto mensaje
      lstBd = Product.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(ProductUpdate(token='', entityKey = i.entityKey,
                                #empresa_key=user.empresa_key.urlsafe(),
                                code = i.code,
                                description = i.description,
                                urlImage = i.urlImage)) # agrega a la lista
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = ProductList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = ProductList(code=-2, data=[]) #token expiro
    return message

  @endpoints.method(ProductUpdate, CodeMessage, path='products/update', http_method='POST', name='products.update')
  #siempre lleva cls y request
  def product_update(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      product = Product()

      # empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
      if product.product_m(request, user.key) == 0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
        codigo = 1
      
      else:
        codigo = -3
        #la funcion josue_m puede actualizar e insertar
        #depende de la ENTRADA de este endpoint method
      
      message = CodeMessage(code = 1, message='Sus cambios han sido guardados exitosamente')
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message='Invalid token')
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message='Token expired')
    return message

  @endpoints.method(TokenKey, CodeMessage, path='products/delete', http_method='POST', name='products.delete')
  #siempre lleva cls y request
  def product_remove(cls, request):
    
    try:

      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      productEntity = ndb.Key(urlsafe = request.entityKey)#Obtiene el elemento dado el EntitKey
      productEntity.delete()#BORRA
      message = CodeMessage(code = 1, message = 'Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')

    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message

###############
# Usuarios
###############
@endpoints.api(name='usuarios_api', version='v1', description='usuarios endpoints')
class UsuariosApi(remote.Service):
###############get the info of one########
 @endpoints.method(TokenKey, UserList, path='users/get', http_method='POST', name='users.get')
 def users_get(cls, request):
  try:                 
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   userentity = ndb.Key(urlsafe=request.entityKey)
   user = Usuarios.get_by_id(userentity.id()) #obtiene usuario
            #user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = UserList(code=1) # crea objeto mensaje
   lista.append(UserUpdate(token='', 
    entityKey= user.entityKey,
    #empresa_key = user.empresa_key.urlsafe(),
    email = user.email))
   lstMessage.data = lista#ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = UserList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = UserList(code=-2, data=[]) #token expiro
  return message


########################## list###################
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
  @endpoints.method(Token, UserList, path='users/list', http_method='POST', name='users.list')
  def lista_usuarios(cls, request):
    try:
      token = jwt.decode(request.tokenint, 'secret')  #checa token
      user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
      lista = []  #crea lista
      lstMessage = UserList(code=1) # crea objeto mensaje
      lstBd = Usuarios.query().fetch() # recupera de base de datos
      
      for i in lstBd: # recorre
        lista.append(UserUpdate(token='',
        entityKey=i.entityKey,
        #empresa_key=user.empresa_key.urlsafe(),
        email=i.email)) # agrega a la lista
      
      lstMessage.data = lista # la manda al messa
      message = lstMessage #regresa
      
    except jwt.DecodeError:
      message = UserList(code=-1, data=[]) #token invalido
    except jwt.ExpiredSignatureError:
      message = UserList(code=-2, data=[]) #token expiro
    
    return message

  @endpoints.method(TokenKey, CodeMessage, path='users/delete', http_method='POST', name='users.delete')
  #siempre lleva cls y request
  def user_remove(cls, request):
    try:
      
      token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      usersentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
      usersentity.delete()#BORRA
      message = CodeMessage(code=1, message='Succesfully deleted')
    
    except jwt.DecodeError:
      message = CodeMessage(code=-2, message='Invalid token')
    
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code=-1, message='Token expired')
    
    return message

# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
  @endpoints.method(UserInput, CodeMessage, path='users/insert', http_method='POST', name='users.insert')
  def user_add(cls, request):
    try:
      token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
      user = Usuarios.get_by_id(token['user_id'])
    
      if validarEmail(request.email) == False: #checa si el email esta registrado
                       #empresakey = ndb.Key(urlsafe=request.empresa_key) #convierte el string dado a entityKey
        if user.usuario_m(request, user.empresa_key) == 0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
          codigo = 1
        
        else:
          codigo = -3
                         #la funcion josue_m puede actualizar e insertar
                         #depende de la ENTRADA de este endpoint method
        message = CodeMessage(code = codigo, message = 'Succesfully added')
    
      else:
        message = CodeMessage(code = -4, message = 'El email ya ha sido registrado')
    
    except jwt.DecodeError:
      message = CodeMessage(code = -2, message = 'Invalid token')
    
    except jwt.ExpiredSignatureError:
      message = CodeMessage(code = -1, message = 'Token expired')
    
    return message


##login##

 @endpoints.method(EmailPasswordMessage, TokenMessage, path='users/login', http_method='POST', name='users.login')
 def users_login(cls, request):
  try:
   user = Usuarios.query(Usuarios.email == request.email).fetch() #obtiene el usuario dado el email
   if not user or len(user) == 0: #si no encuentra user saca
    raise NotFoundException()
   user = user[0] 
   key = user.email#user.entityKey#.urlsafe() # regresa como mensaje la key del usuario
   if not user.verify_password(request.password): # checa la contrasena
    raise NotFoundException()

   token = jwt.encode({'user_id': user.key.id(), 'exp': time.time() + 43200}, 'secret') #crea el token que dura 43200 segundos
   message = TokenMessage(code=1, message=key, token=token ) # regresa token #CAMBIO: token como tercer parametro en lugar de segundo, para hacer match en la definición de messages.py, debe ser lo mismo, ¿no?
  except NotFoundException:
   message = TokenMessage(code=-1, message='Wrong username or password', token=None )
  return message

##update##
# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(UserUpdate, CodeMessage, path='users/update', http_method='POST', name='users.update')
#siempre lleva cls y request
 def user_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
   if user.usuario_m(request, empresakey)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

###########################
#### Empresa
###########################

## Google Cloud Endpoint
@endpoints.api(name='empresas_api', version='v1', description='empresas REST API')
class EmpresasApi(remote.Service):


# get one

 @endpoints.method(TokenKey, EmpresaList, path='empresa/get', http_method='POST', name='empresa.get')
#siempre lleva cls y request
 def empresa_get(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      #Obtiene el elemento dado el entityKey
   empresaentity = ndb.Key(urlsafe=request.entityKey)
      #CREA LA SALIDA de tipo JosueInput y le asigna los valores, es a como se declaro en el messages.py
      #empresaentity.get().empresa_key.urlsafe() para poder optener el EntityKey
     ##### ejemplo real
    ####### message = EmpresaList(code=1, data=[EmpresaUpdate(token='Succesfully get', nombre_empresa=empresaentity.get().nombre_empresa, empresa_key=empresaentity.get().empresa_key.urlsafe(), entityKey=empresaentity.get().entityKey)])
   message = EmpresaList(code=1, data = [EmpresaUpdate(token='Succesfully get',
    entityKey = empresaentity.get().entityKey,
    codigo_empresa=empresaentity.get().codigo_empresa, 
    nombre_empresa = empresaentity.get().nombre_empresa)])

  except jwt.DecodeError:
   message = EmpresaList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = EmpresaList(code=-2, data=[])
  return message




 @endpoints.method(TokenKey, CodeMessage, path='empresa/delete', http_method='POST', name='empresa.delete')
#siempre lleva cls y request
 def empresa_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   empresaentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   empresaentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


# insert
 @endpoints.method(EmpresaInput, CodeMessage, path='empresa/insert', http_method='POST', name='empresa.insert')
#siempre lleva cls y request
 def empresa_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario models.py 
   myempresa = Empresa()
   if myempresa.empresa_m(request)==0: 
    codigo=1
   else:
		codigo=-3
      	      #la funcion josue_m puede actualizar e insertar
	      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Succesfully added')
      #else:
	    #  message = CodeMessage(code=-4, message='Succesfully added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(EmpresaUpdate, CodeMessage, path='empresa/update', http_method='POST', name='empresa.update')
#siempre lleva cls y request
 def empresa_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN 
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      #empresakey = ndb.Key(urlsafe=request.empresa_key)#convierte el string dado a entityKey
   myempresa = Empresa()
   if myempresa.empresa_m(request)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# list
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, EmpresaList, path='empresa/list', http_method='POST', name='empresa.list')
#siempre lleva cls y request
 def empresa_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   #if user.importante==1 or user.importante==2:
   lista = [] #crea lista para guardar contenido de la BD
   lstMessage = EmpresaList(code=1) #CREA el mensaje de salida
   lstBdEmpresa = Empresa.query().fetch() #obtiene de la base de datos
   for i in lstBdEmpresa: #recorre la base de datos
             #inserta a la lista creada con los elementos que se necesiten de la base de datos
             #i.empresa_key.urlsafe() obtiene el entityKey
	     #lista.append(ClientesUpdate(token='', nombre=i.nombre, status=i.status, empresa_key=i.empresa_key.urlsafe(), entityKey=i.entityKey))
    lista.append(EmpresaUpdate(token='', 
     entityKey = i.entityKey,
     codigo_empresa=i.codigo_empresa, 
     nombre_empresa = i.nombre_empresa))
      
   lstMessage.data = lista #ASIGNA a la salida la lista
   message = lstMessage
      #else:
      #    message = EmpresaList(code=-3, data=[])
  except jwt.DecodeError:
   message = EmpresaList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = EmpresaList(code=-2, data=[])
  return message


###########################
#### Tweets
###########################

@endpoints.api(name='tweet_api', version='v1', description='tweet REST API')
class TweetApi(remote.Service):
# get one
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, TweetList, path='tweet/get', http_method='POST', name='tweet.get')
#siempre lleva cls y request
 def tweet_get(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      #Obtiene el elemento dado el entityKey
   tweetentity = ndb.Key(urlsafe=request.entityKey)
      #CREA LA SALIDA de tipo JosueInput y le asigna los valores, es a como se declaro en el messages.py
      #josuentity.get().empresa_key.urlsafe() para poder optener el EntityKey
   message = TweetList(code=1, data=[TweetUpdate(token='Succesfully get',
    entityKey=tweetentity.get().entityKey,
    #empresa_key=teamentity.get().empresa_key.urlsafe(), 
    title=tweetentity.get().title, 
    description=tweetentity.get().description, 
    urlImage=tweetentity.get().urlImage)])
  except jwt.DecodeError:
   message = TweetList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = TweetList(code=-2, data=[])
  return message


# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='tweet/delete', http_method='POST', name='tweet.delete')
#siempre lleva cls y request
 def tweet_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   tweetentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   tweetentity.delete()#BORRA
   message = CodeMessage(code=0, message='tweet deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# list
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, TweetList, path='tweet/list', http_method='POST', name='tweet.list')
#siempre lleva cls y request
 def tweet_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = [] #crea lista para guardar contenido de la BD
   lstMessage = TweetList(code=1) #CREA el mensaje de salida
   lstBd = Tweet.query().fetch() #obtiene de la base de datos
   for i in lstBd: #recorre la base de datos
    #inserta a la lista creada con los elementos que se necesiten de la base de datos
    #i.empresa_key.urlsafe() obtiene el entityKey
	     
    lista.append(TweetUpdate(token='', 
     entityKey=i.entityKey, 
     #empresa_key=i.empresa_key.urlsafe(),
     title=i.title, 
     decription=i.decription, 
     urlImage=i.urlImage))
   lstMessage.data = lista #ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = TweetList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = TweetList(code=-2, data=[])
  return message

# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TweetInput, CodeMessage, path='tweet/insert', http_method='POST', name='tweet.insert')
#siempre lleva cls y request
 def tweet_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de
   mytweet = Tweet()
   if mytweet.tweet_m(request, user.empresa_key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
          #la funcion josue_m puede actualizar e insertar
          #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Tweet added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TweetUpdate, CodeMessage, path='tweet/update', http_method='POST', name='tweet.update')
#siempre lleva cls y request
 def tweet_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   empresakey = ndb.Key(urlsafe=user.empresa_key.urlsafe())#convierte el string dado a entityKey
   mytweet = Tweet()
   if mytweet.tweet_m(request, empresakey)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='tweet updated')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


application = endpoints.api_server([UsuariosApi, EmpresasApi, TweetApi, ProductsApi, DevelopersApi, VideogamesApi, PublishersApi, GenresApi], restricted=False)

