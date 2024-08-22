from django.test import TestCase
from django.urls import reverse
from .models import Article

class ArticleTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crea un artículo de prueba que estará disponible para todas las pruebas
        cls.article = Article.objects.create(
            title="Test Article",
            content="This is a test article."
        )

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_list.html')
        self.assertContains(response, "Test Article")

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertContains(response, self.article.title)

    def test_article_create_view(self):
        response = self.client.post(reverse('article_create'), {
            'title': 'New Article',
            'content': 'This is a new article.'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de crear
        self.assertEqual(Article.objects.count(), 2)

    def test_article_update_view(self):
        response = self.client.post(reverse('article_update', args=[self.article.id]), {
            'title': 'Updated Article',
            'content': 'This is an updated article.'
        })
        self.assertEqual(response.status_code, 302)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Article')

    def test_article_delete_view(self):
        response = self.client.post(reverse('article_delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 0)

