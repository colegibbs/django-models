from django.test import TestCase
from django.urls import reverse
from .models import Snacks
from django.contrib.auth import get_user_model

class SnacksTest(TestCase):
  def setUp(self):
    user = get_user_model().objects.create(username="tester",password="tester")
    Snacks.objects.create(name="rake", purchaser=user, description="description")

  def test_snack_list_status_code(self):
    url = reverse("snack_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_snack_list_template(self):
    url = reverse("snack_list")
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_snack_page_template(self):
    url = reverse("snack_detail", args=(1,))
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_detail.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_snack_page_status_code(self):
    url = reverse("snack_detail",args=(1,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)


