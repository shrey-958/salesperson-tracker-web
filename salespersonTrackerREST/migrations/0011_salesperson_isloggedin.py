# Generated by Django 2.2.10 on 2020-04-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("salespersonTrackerREST", "0010_auto_20200329_1250")]

    operations = [
        migrations.AddField(
            model_name="salesperson",
            name="isLoggedin",
            field=models.BooleanField(default=False),
        )
    ]
