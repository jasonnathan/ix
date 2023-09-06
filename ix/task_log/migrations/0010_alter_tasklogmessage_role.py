# Generated by Django 4.2.2 on 2023-08-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_log", "0009_uppercase_msg_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasklogmessage",
            name="role",
            field=models.CharField(
                choices=[
                    ("SYSTEM", "SYSTEM"),
                    ("ASSISTANT", "ASSISTANT"),
                    ("USER", "USER"),
                ],
                max_length=16,
            ),
        ),
    ]