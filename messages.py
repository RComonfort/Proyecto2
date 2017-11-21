#!/usr/bin/env python
# -*- coding: utf-8 -*-

from protorpc import messages
from protorpc import message_types

class MessageNone(messages.Message):
    inti = messages.StringField(1)
# Input messages
#Recibe el token para validar
class Token(messages.Message):
    tokenint = messages.StringField(1, required=True)
    #entityKey = messages.StringField(2, required=False)
    #fromurl = messages.StringField(3)

#Recibe el token y un entityKey de cualquier base de datos para validar
class TokenKey(messages.Message):
    tokenint = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    #fromurl = messages.StringField(3)

#Recibe el email y contrasena para la creacion de token
class EmailPasswordMessage(messages.Message):
    email = messages.StringField(1, required=True)
    password = messages.StringField(2, required=True)

# Output messages
#regresa un token
class TokenMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)
    token = messages.StringField(3)

#regresa mensajes de lo ocurrido
class CodeMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)

#USERS
class UserInput(messages.Message):
    token = messages.StringField(1) 
    empresa_key = messages.StringField(2)
    email = messages.StringField(3)
    password = messages.StringField(4)

class UserUpdate(messages.Message):
    token = messages.StringField(1)
    email = messages.StringField(2)
    password = messages.StringField(3)
    entityKey = messages.StringField(4, required=True)

class UserList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(UserUpdate, 2, repeated=True)


######Empresa########

#Mensaje de Entrada y Salida para la base de datos Empresa
class EmpresaInput(messages.Message):
    token = messages.StringField(1, required=True) 
    codigo_empresa = messages.StringField(2)
    nombre_empresa = messages.StringField(3)


class EmpresaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    codigo_empresa = messages.StringField(3)
    nombre_empresa = messages.StringField(4)

#regresa una lista para la base de datos Empresa
class EmpresaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo EmpresaUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(EmpresaUpdate, 2, repeated=True)

######Tweet########

#Mensaje de Entrada y Salida para Tweets
class TweetInput(messages.Message):
    token = messages.StringField(1, required=True) 
    title = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class TweetUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    title = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class TweetList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(TweetUpdate, 2, repeated=True)

########Product########

#Mensaje de Entrada y Salida para Tweets
class ProductInput(messages.Message):

    token = messages.StringField(1, required=True) 
    code = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

class ProductUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    code = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class ProductList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(ProductUpdate, 2, repeated=True)
    
    
######## Developer ########

#Input and output messages for developers
class DeveloperInput(messages.Message):

    token = messages.StringField(1, required=True) #???
    
    user_key = messages.StringField(2)
    nameA = messages.StringField(3)
    location = messages.StringField(4)
    year = messages.StringField(5)
    logo = messages.StringField(6)

#Update message for developer
class DeveloperUpdate(messages.Message):

    token = messages.StringField(1, required=True)
    
    entityKey = messages.StringField(2)
    nameA = messages.StringField(3)
    location = messages.StringField(4)
    year = messages.StringField(5)
    logo = messages.StringField(6)

#Returns a list for the DB of dev
class DeveloperList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(DeveloperUpdate, 2, repeated=True)
    
    
    
######## Videogame ########

#Input and output messages for Videogame
class VideogameInput(messages.Message):

    token = messages.StringField(1, required=True) #???
    
    user_key = messages.StringField(2)
    title = messages.StringField(3)
    developer = messages.StringField(4)
    publisher = messages.StringField(5)
    year = messages.StringField(6)
    description = messages.StringField(7)
    genre = messages.StringField(8)
    image = messages.StringField(9)
    

#Update message for Videogame
class VideogameUpdate(messages.Message):

    token = messages.StringField(1, required=True) #???
    
    entityKey = messages.StringField(2)
    title = messages.StringField(3)
    developer = messages.StringField(4)
    publisher = messages.StringField(5)
    year = messages.StringField(6)
    description = messages.StringField(7)
    genre = messages.StringField(8)
    image = messages.StringField(9)

#Returns a list for the DB of dev
class VideogameList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(VideogameUpdate, 2, repeated=True)
    

######## Publisher ########    
    
#Input and output messages for developers
class PublisherInput(messages.Message):

    token = messages.StringField(1, required=True) #???
    
    user_key = messages.StringField(2)
    nameA = messages.StringField(3)
    location = messages.StringField(4)
    year = messages.StringField(5)
    logo = messages.StringField(6)

#Update message for developer
class PublisherUpdate(messages.Message):

    token = messages.StringField(1, required=True)
    
    entityKey = messages.StringField(2)
    nameA = messages.StringField(3)
    location = messages.StringField(4)
    year = messages.StringField(5)
    logo = messages.StringField(6)

#Returns a list for the DB of dev
class PublisherList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(PublisherUpdate, 2, repeated=True)
    
    
######## Genre ########    
    
#Input and output messages for genres
class GenreInput(messages.Message):

    token = messages.StringField(1, required=True) #???
    user_key = messages.StringField(2)
    
    nameA = messages.StringField(3)
    description = messages.StringField(4)


#Update message for genre
class GenreUpdate(messages.Message):

    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2)
    
    nameA = messages.StringField(3)
    description = messages.StringField(4)

#Returns a list for the DB of dev
class GenreList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(GenreUpdate, 2, repeated=True)
