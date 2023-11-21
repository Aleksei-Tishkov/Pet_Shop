from django.contrib.sitemaps import Sitemap

from Blog.services import get_published_posts, get_post_tags


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return get_published_posts()

    def lastmod(self, obj):
        return obj.time_updated


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return get_post_tags()

