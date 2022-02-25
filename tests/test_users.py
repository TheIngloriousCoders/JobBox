import pytest

@pytest.mark.django_db
def test_create_a_new_user(django_user_model):
   email = "user@test.com"
   password = "password"
   django_user_model.objects.create_user(email=email, password=password)
   assert django_user_model.objects.get(email=email) is not None

@pytest.mark.django_db
def test_create_a_super_user(django_user_model):
   email = "superuser@test.com"
   password = "password"
   django_user_model.objects.create_superuser(email=email, password=password)
   assert django_user_model.objects.get(email=email).is_superuser