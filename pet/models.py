from django.db import models

# Create your models here.

class PetOwnerModel(models.Model):
    name = models.CharField(verbose_name="Ad Soyad", max_length=255)
    phone = models.CharField(verbose_name="Telefon No", max_length=13)
    email = models.EmailField(verbose_name="E-Posta")
    address = models.TextField(verbose_name="Adres", max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def howManyPets(self):
        return len(self.petmodel_set.all())

    

class PetModel(models.Model):
    owner = models.ForeignKey(PetOwnerModel, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Hayvanın Adı", max_length=255)
    genre = models.CharField(verbose_name="Hayvanın Türü", max_length=255)
    genus = models.CharField(verbose_name="Hayvanın Cinsi", max_length=255)
    age = models.FloatField(verbose_name="Hayvanın Yaşı")
    detail = models.TextField(verbose_name="Hayvan Hakkında Açıklamalar", max_length=1000)
    
    def __str__(self):
        return self.name


