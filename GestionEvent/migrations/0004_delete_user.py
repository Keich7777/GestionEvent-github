# Generated by Django 4.2.7 on 2024-02-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionEvent', '0003_utilisateur_alter_user_nom_alter_user_prenom_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
