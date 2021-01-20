# Generated by Django 3.1.5 on 2021-01-19 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='combine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combine_name', models.CharField(max_length=45)),
                ('combine_telephone_number', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_price', models.CharField(max_length=45)),
                ('purchase_price', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('birthday', models.CharField(max_length=45)),
                ('login', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='weekly_prices_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_selling_price', models.CharField(max_length=45)),
                ('new_purchase_price', models.CharField(max_length=45)),
                ('id_prices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.prices')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=45)),
                ('product_sort', models.CharField(max_length=45)),
                ('product_group', models.CharField(max_length=45)),
                ('amount_of_product', models.CharField(max_length=45)),
                ('id_combine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.combine')),
            ],
        ),
        migrations.AddField(
            model_name='prices',
            name='id_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.product'),
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=45)),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='combine',
            name='id_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.employee'),
        ),
        migrations.AddField(
            model_name='combine',
            name='id_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.location'),
        ),
    ]