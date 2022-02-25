import pytest

@pytest.mark.django_db
def test_home_page_is_accessible(client):
   response = client.get('/')
   assert response.status_code == 200

def test_admin_url_redirects_to_login_page_if_not_authenticated(client):
   response = client.get('/admin')
   assert response.status_code == 301

@pytest.mark.django_db
def test_user_can_not_access_admin_page(client, django_user_model):
   email = "user@test.com"
   password = "password"
   user = django_user_model.objects.create_user(email=email, password=password)
   client.force_login(user)
   response = client.get('/admin/')
   assert response.status_code == 302

@pytest.mark.django_db
def test_superuser_can_access_admin_page(admin_client, django_user_model):
   email = "admin@test.com"
   password = "password"
   user = django_user_model.objects.create_superuser(email=email, password=password)
   admin_client.force_login(user)
   response = admin_client.get('/admin/')
   assert response.status_code == 200