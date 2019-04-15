import json

from django.urls import reverse

from rest_framework import status

from authors.apps.authentication.models import User
from authors.apps.articles.models import Article

from .test_base import BaseTestClass
from authors.apps.authentication.tests.test_base import BaseTestClass as BTC


class TestUserRoutes(BaseTestClass):

    def test_create_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        response = self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_articles(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        response = self.client.get(
            reverse('article:create_article'),
            format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_one_articles(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.get(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)

    def test_slug_does_not_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.get(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-t-trai-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Not found.', str(response.data))

    def test_delete_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.delete(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Article has been deleted', str(response.data))

    def test_update_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.put(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            data=self.update_data,
            format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_article_no_slug(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.delete(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon77"}),
            format='json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Not found.', str(response.data))

    def test_update_article_no_slug(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.put(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon88"}),
            data=self.update_data,
            format='json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Not found.', str(response.data))

    def test_show_read_time(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.get(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.data['read_time']), "less than 1 min")

    def test_show_read_time_more_than_a_minute(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article,
            format='json')
        response = self.client.get(
            reverse(
                'article:get_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.data['read_time']), "4 mins")

    def test_share_facebook_link(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.post(
            reverse(
                'article:share_facebook',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)

    def test_share_twitter_link(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.post(
            reverse(
                'article:share_twitter',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)

    def test_share_article_via_mail(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        response = self.client.post(
            reverse(
                'article:share_email',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            data=self.email_share,
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your article has been shared successfully',
                      str(response.data))
        self.assertIn(
            'Your article has been shared successfully', str(
                response.data))

    def test_get_all_tags(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data2,
            format='json')
        resp = self.client.get(
            reverse('articles:get_tags'), format='json')
        self.assertEqual(resp.status_code, 200)

    def test_no_tags_available(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(
            reverse('article:create_article'),
            data=self.article_data,
            format='json')
        resp = self.client.get(
            reverse('articles:get_tags'), format='json')
        self.assertIn('there are no tags available', str(resp.data))

    def test_post_rating_article_unauthorized(self):
        response = self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.6}))
        error = {"detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, 403)
        self.assertEqual(error, response.data)

    def test_post_rating_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(reverse('article:create_article'),
                         data=self.article_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header3)
        response = self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.6}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual('4.6', response.data['rating'])

    def test_post_rating_article_same_authour(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(reverse('article:create_article'),
                         data=self.article_data, format='json')
        response = self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.6}))
        message = {
            'error': ['Rate an article that does not belong to you, Please']}
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message, response.data['errors'])

    def test_post_rating_article_exists(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(reverse('article:create_article'),
                         data=self.article_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header3)
        self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.6}))
        response = self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.7}))
        message = {"error": ['Article rating already exists, Please']
                   }
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['errors'], message)

    def test_get_rated_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(reverse('article:create_article'),
                         data=self.article_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header3)
        self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.7}))
        response = self.client.get(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('4.7', response.data['rating'])

    def test_get_rated_article_unauthorized(self):
        response = self.client.get(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            format='json')
        error = {"detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, 403)
        self.assertEqual(error, response.data)

    def test_updated_rated_article(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        self.client.post(reverse('article:create_article'),
                         data=self.article_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header3)
        self.client.post(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.7}))
        response = self.client.patch(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.8}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual('4.8', response.data['rating'])

    def test_updated_rated_article_unauthorized(self):
        response = self.client.patch(
            reverse(
                'article:rate_article',
                kwargs={
                    'slug': "how-to-train-your-dragon"}),
            content_type='application/json', data=json.dumps({'rating': 4.6}))
        error = {"detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, 403)
        self.assertEqual(error, response.data)
