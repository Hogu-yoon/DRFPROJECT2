# Generated by Django 4.0.5 on 2022-06-17 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_article_category_alter_article_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_article', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500, verbose_name='댓글')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='blog.article')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
