# Generated by Django 2.2.7 on 2019-11-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191026_0930'),
        ('course', '0011_remove_course_student_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='course',
            name='queue',
        ),
        migrations.AlterField(
            model_name='description',
            name='name',
            field=models.CharField(max_length=180, unique=True),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInformation')),
            ],
            options={
                'ordering': ['ticket_number'],
            },
        ),
    ]