# Generated by Django 2.1.4 on 2019-01-06 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TagRealmAssociation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('last_used', models.DateTimeField(blank=True, null=True)),
                ('realm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realms.Realm')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='realms',
            field=models.ManyToManyField(through='tags.TagRealmAssociation', to='realms.Realm'),
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tagrealmassociation',
            unique_together={('tag', 'realm')},
        ),
    ]