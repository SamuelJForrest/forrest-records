from django.test import TestCase
from django.urls import reverse, resolve
from .models import Blog, BlogPage
from .forms import BlogForm
from .views import *

# Model tests


class TestBlogModels(TestCase):
    """
    Test Blog and BlogPage models
    """

    def test_create_blogpage(self):
        blog = BlogPage.objects.create(
            title='Another blog',
            subtitle='Can you believe it?'
        )
        self.assertTrue(blog.title, blog.subtitle)

    def test_create_blog(self):
        blog = Blog.objects.create(
            title='Test blog'
        )
        self.assertTrue(blog.title)


# Url tests


class TestBlogUrls(TestCase):
    """
    Tests status of blog URLs
    """

    def test_all_blog_posts_url(self):
        """
        Tests all blogs page
        """
        url = reverse('blog')
        self.assertEqual(resolve(url).func, all_blog_posts)

    def test_blog_detail_url(self):
        """
        Tests single blog urls
        """
        url = reverse('blog_detail', args=[1])
        self.assertEqual(resolve(url).func, blog_detail)

    def test_add_blog_url(self):
        """
        Tests add blog url
        """
        url = reverse('add_blog')
        self.assertEqual(resolve(url).func, add_blog)

    def test_edit_blog_url(self):
        """
        Tests edit blog page
        """
        url = reverse('edit_blog', args=[1])
        self.assertEqual(resolve(url).func, edit_blog)

    def test_delete_blog_url(self):
        """
        Tests delete blog url
        """
        url = reverse('delete_blog', args=[1])
        self.assertEqual(resolve(url).func, delete_blog)

    def test_blog_warning_url(self):
        """
        Tests blog warning pages
        """
        url = reverse('blog_warning', args=[1])
        self.assertEqual(resolve(url).func, blog_warning)

    def test_feature_blog_url(self):
        """
        Tests feature blog url
        """
        url = reverse('feature_blog', args=[1])
        self.assertEqual(resolve(url).func, feature_blog)


# Form tests


class TestBlogForms(TestCase):
    """
    Tests the blog forms
    """
    def test_add_blog_form(self):
        """
        Tests add blog
        """
        form = Blog({
            'title': 'Another blog'
        })
        self.assertTrue(form)
