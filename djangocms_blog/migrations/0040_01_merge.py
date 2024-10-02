from django.db import migrations

"""
Merge migration to fix our tree
"""


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_blog", "0040_post_featured_post"),
        ("djangocms_blog", "0040_post_include_in_rss"),
    ]

    operations = []
