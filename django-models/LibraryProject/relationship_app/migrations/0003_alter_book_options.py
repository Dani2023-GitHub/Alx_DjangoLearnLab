# Generated by Django 5.1.2 on 2024-11-14 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'can add a book'), ('can_edit_book', 'can edit a book'), ('can_delete_book', 'can delete a book')]},
        ),
    ]
