# Generated by Django 4.1.6 on 2023-02-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EVBunk_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bunk_name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('company_address', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to='documents/', verbose_name='Upload Image')),
            ],
        ),
        migrations.CreateModel(
            name='Public_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=2000)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to='documents/', verbose_name='Upload Image')),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_name', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('', 'Select'), ('Available', 'Available'), ('Booked', 'Booked')], max_length=30, null=True)),
                ('bunk_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.evbunk_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_battery', models.CharField(max_length=200, unique=True)),
                ('battery_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('slot_status', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('', 'Select'), ('Approved', 'Approve'), ('Rejected', 'Reject')], max_length=30, null=True)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=200, unique=True)),
                ('notes', models.TextField(blank=True, max_length=2000, null=True)),
                ('amount', models.CharField(max_length=30)),
                ('payment_status', models.CharField(max_length=30)),
                ('bunk_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.evbunk_detail')),
                ('slot_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.slot_detail')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.public_detail')),
            ],
        ),
    ]
