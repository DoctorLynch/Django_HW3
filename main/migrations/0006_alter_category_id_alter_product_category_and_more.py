# Generated by Django 4.2.5 on 2023-09-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.SlugField(max_length=150, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.SlugField(max_length=150, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
