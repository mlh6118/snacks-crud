from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnacksTestPages(TestCase):
    """
    Tests each page's status and template usage.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            title="Reese's", description="Chocolate peanut butter cups",
            purchaser=self.user)

    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_detail_page_status_code(self):
        url = reverse('snack_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_template(self):
        url = reverse("snack_detail", args=[1])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_create_page_status_code(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_create_page_template(self):
        url = reverse("snack_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_create.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_update_page_status_code(self):
        url = reverse('snack_update', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_update_page_template(self):
        url = reverse("snack_update", args=[1])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_update.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_delete_page_status_code(self):
        url = reverse('snack_delete', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_delete_page_template(self):
        url = reverse("snack_delete", args=[1])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_delete.html")
        self.assertTemplateUsed(response, "base.html")

    """
    Test each element of a snack on each page.
    """
    def test_string_representation(self):
        self.assertEqual(str(self.snack), f'Reese\'s: \t\t Chocolate peanut '
                                          f'butter cups')

    def test_string_representation_fail(self):
        self.assertIsNot(str(self.snack), 'Reese\'s')

    def test_string_representation_title(self):
        self.assertEqual(str(self.snack.title), 'Reese\'s')

    def test_string_representation_title_fail(self):
        self.assertIsNot(str(self.snack.title), 'Reeses')

    def test_string_representation_description(self):
        self.assertEqual(str(self.snack.description), 'Chocolate peanut butter '
                                                      'cups')

    def test_string_representation_description_fail(self):
        self.assertIsNot(str(self.snack.description), 'Yummy!')

    def test_string_representation_purchaser(self):
        self.assertEqual(str(self.snack.purchaser), 'tester')

    def test_string_representation_purchaser_fail(self):
        self.assertIsNot(str(self.snack.purchaser), 'admin')


class FormTests(TestCase):
    """
    Test the forms.
    """
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            title="Reese's", description="Chocolate peanut butter cups",
            purchaser=self.user)

    def test_snack_create_title_field(self):
        self.assertEqual(self.snack.title, "Reese\'s")

    def test_snack_create_description_field(self):
        self.assertEqual(self.snack.description, "Chocolate peanut butter cups")

    def test_snack_create_purchaser_field(self):
        self.assertEqual(self.snack.purchaser.username, "tester")

    def test_snack_update_title_field(self):
        self.assertEqual(self.snack.title, "Reese\'s")

    def test_snack_update_description_field(self):
        self.assertEqual(self.snack.description, "Chocolate peanut butter cups")

    def test_snack_update_purchaser_field(self):
        self.assertEqual(self.snack.purchaser.username, "tester")


class ButtonTests(TestCase):
    """
    Test the buttons on all pages.
    """
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            title="Reese's", description="Chocolate peanut butter cups",
            purchaser=self.user)

    def test_snack_create_invalid_form_view(self):
        pass