# Generated by Django 4.1 on 2023-04-30 15:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addrees',
            options={'verbose_name_plural': 'Addrees'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ticket', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('star', models.IntegerField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('addrees', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.addrees')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='core.category')),
            ],
        ),
    ]
