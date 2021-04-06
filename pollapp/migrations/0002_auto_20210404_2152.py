# Generated by Django 2.2.10 on 2021-04-04 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pollapp', '0001_initial'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollsusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_polls', to='userapp.PollUser', verbose_name='идентификатор пользователя'),
        ),
        migrations.AddField(
            model_name='pollquestion',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='pollapp.Poll', verbose_name='идентификатор опроса'),
        ),
    ]