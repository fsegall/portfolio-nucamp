# Generated by Django 4.2 on 2023-05-17 02:26

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0013_remove_expense_track_balance_expense_and_more'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='expense',
            name='track_balance_expense',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='income',
            name='track_balance_income',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='expense',
            trigger=pgtrigger.compiler.Trigger(name='track_balance_expense', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO trackers_balance (current_balance, previous_balance, transaction_date, customer, transaction_id) VALUES (0.0, 0.0, now(), NEW.customer, NEW.expense_id);', hash='9dd94b765b75ce849f3407fd089b2111362302e9', level='STATEMENT', operation='INSERT', pgid='pgtrigger_track_balance_expense_58998', table='trackers_expense', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='income',
            trigger=pgtrigger.compiler.Trigger(name='track_balance_income', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO trackers_balance (current_balance, previous_balance, transaction_date, customer, transaction_id) VALUES (0.0, 0.0, now(), NEW.customer, NEW.income_id;', hash='cac429aa68dec2e98e3dd11691fa37c1379db388', level='STATEMENT', operation='INSERT', pgid='pgtrigger_track_balance_income_f59ce', table='trackers_income', when='AFTER')),
        ),
    ]
