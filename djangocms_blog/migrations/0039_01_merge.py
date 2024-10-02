from django.db import migrations

"""
Merge migration to fix our tree
"""


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_blog", "0038_post_featured_post"),
        ("djangocms_blog", "0038_post_media"),
    ]

    operations = []
