# Generated by Django 5.0 on 2024-01-07 16:57

import django.db.models.deletion
import product.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='catalog')),
                ('gender', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'catalog',
                'verbose_name_plural': 'catalogs',
                'db_table': 'catalog',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name of material')),
                ('fit', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materials',
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='compound')),
                ('percentage', models.CharField(max_length=4, verbose_name='percentage')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compounds', to='product.material')),
            ],
            options={
                'verbose_name': 'compound',
                'verbose_name_plural': 'compounds',
                'db_table': 'compound',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('discount', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='discount')),
                ('style', models.CharField(max_length=64, verbose_name='style')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='update date')),
                ('description', models.TextField(verbose_name='description')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_products', to='product.material', verbose_name='material')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=8, verbose_name='size')),
                ('color', models.CharField(max_length=8, verbose_name='color')),
                ('available', models.PositiveSmallIntegerField(verbose_name='available')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='product.product')),
            ],
            options={
                'verbose_name': 'parameter',
                'verbose_name_plural': 'parameters',
                'db_table': 'parameter',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=product.models.get_upload_to, verbose_name='image')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_bought', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product review',
                'verbose_name_plural': 'product reviews',
                'db_table': 'product_review',
            },
        ),
        migrations.CreateModel(
            name='SubCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='sub catalog')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_catalogs', to='product.catalog')),
            ],
            options={
                'verbose_name': 'sub catalog',
                'verbose_name_plural': 'sub catalogs',
                'db_table': 'sub_catalog',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.subcatalog', verbose_name='category'),
        ),
    ]
