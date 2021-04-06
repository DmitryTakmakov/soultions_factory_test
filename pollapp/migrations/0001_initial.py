# Generated by Django 2.2.10 on 2021-04-04 21:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='идентификатор')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('start_date', models.DateTimeField(verbose_name='дата и время начала')),
                ('finish_date', models.DateTimeField(verbose_name='дата и время окончания')),
                ('description', models.CharField(max_length=256, verbose_name='описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
            ],
        ),
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='идентификатор')),
                ('question_text', models.CharField(max_length=256, verbose_name='текст вопроса')),
                ('question_type', models.CharField(choices=[('TXT', 'ответ текстом'), ('MULT', 'ответ с выбором нескольких вариантов'), ('SING', 'ответ с выбором одного варианта')], default='TXT', max_length=4, verbose_name='тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='PollsUsers',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='идентификатор')),
                ('user_answer', models.CharField(blank=True, max_length=512, verbose_name='ответ пользователя')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answered_polls', to='pollapp.Poll', verbose_name='идентификатор опроса')),
                ('poll_question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answered_questions', to='pollapp.PollQuestion', verbose_name='идентификатор вопроса')),
            ],
        ),
    ]
