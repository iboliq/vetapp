from django.test import TestCase
from .models import PetModel, PetOwnerModel
# Create your tests here.

class PetAppTestCase(TestCase):
    def setUp(self):
        petOwnerModel = PetOwnerModel.objects.create(
            name="Test Owner",
            phone="+905554443322",
            email="test@testmail.com",
            address="test address"
        )
        PetModel.objects.create(
            owner=petOwnerModel,
            name="Test",
            genre="Kedi",
            genus="Tekir",
            age=2,
            detail="Hayvan hakkında test açıklaması."
        )
    
    def testhowManyPets(self):
        petOwnerModel = PetOwnerModel.objects.get(name="Test Owner")
        self.assertEqual(petOwnerModel.howManyPets(), 1)


