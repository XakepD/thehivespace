# Generated by Django 3.0.5 on 2023-01-29 19:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category2',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MN', 'Men'), ('WM', 'Women'), ('UN', 'Unisex'), ('KD', 'Kids'), ('UW', 'Underwear'), ('JK', 'Jacket'), ('ST', 'Suit'), ('TR', 'Trouser'), ('SH', 'Shirt'), ('SN', 'Sneakers'), ('PJ', 'Pyjamas'), ('SE', 'Shoe'), ('JN', 'Jean'), ('SR', 'Short'), ('HD', 'Hoodie')], max_length=3),
        ),
    ]
