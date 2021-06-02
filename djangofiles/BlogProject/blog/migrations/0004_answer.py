# Generated by Django 2.2.1 on 2019-05-23 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answer_content', models.TextField(max_length=50000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.TextField(max_length=20)),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Question')),
            ],
        ),
    ]
