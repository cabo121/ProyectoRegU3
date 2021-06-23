from django.db import models

class electricas (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nombre

class manuales (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nombre

class neumaticas (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nombre

