# Generated by Django 4.2.11 on 2024-04-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignment", "0002_remove_course_id_alter_course_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="course",
            name="code",
            field=models.CharField(max_length=20),
        ),
    ]
