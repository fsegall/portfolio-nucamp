# Generated by Django 4.2 on 2023-05-12 13:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('due_date', models.DateField(default=None)),
                ('is_salary', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trackers.category')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trackers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('due_date', models.DateField(default=None)),
                ('is_bill', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trackers.category')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trackers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_balance', models.FloatField(default=0.0)),
                ('previous_balance', models.FloatField(default=None)),
                ('transaction_date', models.DateTimeField()),
                ('expense_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trackers.expense')),
                ('income_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trackers.income')),
            ],
        ),
    ]
