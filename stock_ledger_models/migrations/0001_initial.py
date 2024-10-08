# Generated by Django 3.2 on 2022-06-13 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YEAR', models.PositiveIntegerField(null=True)),
                ('YEAR_START', models.DateField(null=True)),
                ('CURR_MONTH', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('CURR_MONTH_START', models.DateField(null=True)),
                ('CURR_MONTH_END', models.DateField(null=True)),
                ('CURR_WEEK', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(7)])),
                ('CURR_WEEK_START', models.DateField(null=True)),
                ('CURR_WEEK_END', models.DateField(null=True)),
                ('LAST_MONTH', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)])),
                ('LAST_MONTH_START', models.DateField(null=True)),
                ('LAST_MONTH_END', models.DateField(null=True)),
                ('LAST_WEEK', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(7)])),
                ('LAST_WEEK_START', models.DateField(null=True)),
                ('LAST_WEEK_END', models.DateField(null=True)),
                ('SYSTEM_DATE', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('CLASS', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CLASS_DESC', models.CharField(max_length=40, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('CURRENCY', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('CURRENCY_DESC', models.CharField(max_length=60, null=True)),
                ('EFFECTIVE_DATE', models.DateField()),
                ('EXCHANGE_RATE', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='date_range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YEAR', models.PositiveIntegerField(null=True)),
                ('MONTH_START', models.DateField(null=True)),
                ('WEEK_START', models.DateField(null=True)),
                ('MONTH_END', models.DateField(null=True)),
                ('WEEK_END', models.DateField(null=True)),
                ('MONTH_NO', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)])),
                ('WEEK_NO', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12)])),
                ('DAILY_DATE', models.DateField(null=True)),
                ('WEEK_CLOSE_IND', models.CharField(max_length=1)),
                ('DAY_CLOSE_IND', models.CharField(max_length=1)),
                ('MONTH_CLOSE_IND', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('DEPT', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('DEPT_DESC', models.CharField(max_length=40, null=True)),
                ('ACC_METHOD', models.CharField(choices=[(1, 'Direct Cost'), (2, 'Retail Inventory')], max_length=1)),
                ('PURCHASE_TYPE', models.CharField(choices=[(0, 'Normal Merchandise'), (1, 'Consignment Stock'), (2, 'Concession Items')], max_length=1)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GL_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRIMARY_ACCOUNT', models.PositiveIntegerField()),
                ('SET_OF_BOOKS_ID', models.PositiveIntegerField()),
                ('SEGMENT1', models.CharField(max_length=5, null=True)),
                ('SEGMENT2', models.CharField(max_length=5, null=True)),
                ('SEGMENT3', models.CharField(max_length=5, null=True)),
                ('SEGMENT4', models.CharField(max_length=5, null=True)),
                ('SEGMENT5', models.CharField(max_length=5, null=True)),
                ('SEGMENT6', models.CharField(max_length=5, null=True)),
                ('SEGMENT7', models.CharField(max_length=5, null=True)),
                ('CURRENCY', models.CharField(max_length=3, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('LOCATION', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('LOCATION_NAME', models.CharField(max_length=50, null=True)),
                ('LOCATION_TYPE', models.CharField(choices=[('S', 'Store'), ('W', 'Warehouse')], max_length=1)),
                ('STATUS', models.CharField(choices=[('A', 'Active'), ('C', 'Closed')], max_length=1)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('LAST_UPDATE_ID', models.CharField(max_length=25, null=True)),
                ('UPDATE_DATETIME', models.DateTimeField(auto_now=True)),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.currency')),
            ],
        ),
        migrations.CreateModel(
            name='sl_control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CONTROL_IND', models.CharField(max_length=1, null=True)),
                ('PROGRAM_NAME', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stg_trn_data',
            fields=[
                ('TRAN_SEQ_NO', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('PROCESS_IND', models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1)),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('PACK_QTY', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('PACK_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('PACK_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('AREF', models.CharField(max_length=1, null=True)),
                ('CURRENCY', models.CharField(max_length=3)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('REV_NO', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('REV_TRN_NO', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stg_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stg_location_type', to='stock_ledger_models.location')),
            ],
        ),
        migrations.CreateModel(
            name='SubClass',
            fields=[
                ('SUBCLASS', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('SUBCLASS_DESC', models.CharField(max_length=40, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
            ],
        ),
        migrations.CreateModel(
            name='trn_data_rev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_POST_DATE', models.DateField(null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('TOTAL_TRN_COST', models.PositiveIntegerField(null=True)),
                ('TOTAL_TRN_RETAIL', models.PositiveIntegerField(null=True)),
                ('REF_NO_1', models.PositiveIntegerField(null=True)),
                ('REF_NO_2', models.PositiveIntegerField(null=True)),
                ('REF_NO_3', models.PositiveIntegerField(null=True)),
                ('REF_NO_4', models.PositiveIntegerField(null=True)),
                ('UPDATE_DATETIME', models.DateTimeField(auto_now=True)),
                ('CREATE_ID', models.CharField(max_length=25)),
                ('REV_NO', models.IntegerField()),
                ('REV_TRN_NO', models.IntegerField()),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trn_rev_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trn_rev_location_type', to='stock_ledger_models.location')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.CreateModel(
            name='trn_data_history',
            fields=[
                ('PROCESS_IND', models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1)),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_POST_DATE', models.DateField(null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('SELLING_UOM', models.CharField(max_length=3)),
                ('PACK_QTY', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('PACK_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('PACK_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('REV_NO', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('REV_TRN_NO', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('ARCHIVE_DATETIME', models.DateTimeField()),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock_ledger_models.currency')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_location_type', to='stock_ledger_models.location')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.CreateModel(
            name='trn_data',
            fields=[
                ('PROCESS_IND', models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1)),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_POST_DATE', models.DateField(null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('SELLING_UOM', models.CharField(max_length=3)),
                ('PACK_QTY', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('PACK_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('PACK_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('REV_NO', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('REV_TRN_NO', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock_ledger_models.currency')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trn_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trn_location_type', to='stock_ledger_models.location')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.CreateModel(
            name='transaction_data_expl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('CREATE_ID', models.CharField(max_length=25)),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock_ledger_models.currency')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='txn_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='txn_location_type', to='stock_ledger_models.location')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.CreateModel(
            name='stg_fin_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SET_OF_BOOKS_ID', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('ACCOUNTING_DATE', models.DateField(null=True)),
                ('TRN_DATE', models.DateField(null=True)),
                ('EXCHANGE_RATE', models.DecimalField(decimal_places=4, max_digits=20)),
                ('DEBIT_AMOUNT', models.DecimalField(decimal_places=4, max_digits=20)),
                ('CREDIT_ACCOUNT', models.DecimalField(decimal_places=4, max_digits=20)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('PRIMARY_ACCOUNT', models.PositiveIntegerField(null=True)),
                ('PRIMARY_CURR_CODE', models.CharField(max_length=3)),
                ('PRIMARY_DEBIT_AMT', models.DecimalField(decimal_places=4, max_digits=20)),
                ('PRIMARY_CREDIT_AMT', models.DecimalField(decimal_places=4, max_digits=20)),
                ('CURRENCY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.currency')),
            ],
        ),
        migrations.CreateModel(
            name='pndg_dly_rollup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROCESS_IND', models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1)),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_NO', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(max_length=10, null=True)),
                ('TRN_POST_DATE', models.DateField()),
                ('TRN_DATE', models.DateField()),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10)),
                ('QTY', models.PositiveIntegerField()),
                ('SELLING_UOM', models.CharField(max_length=3, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('PACK_QTY', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('PACK_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('PACK_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REV_NO', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('REV_TRN_NO', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('CREATE_ID', models.CharField(max_length=25)),
                ('ARCHIVE_DATETIME', models.DateTimeField()),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock_ledger_models.currency')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pndg_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pndg_location_type', to='stock_ledger_models.location')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.CreateModel(
            name='item_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEM', models.CharField(max_length=25)),
                ('ITEM_PARENT', models.CharField(max_length=25, null=True)),
                ('ITEM_GRANDPARENT', models.CharField(max_length=25, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('SELLING_UOM', models.CharField(max_length=3, null=True)),
                ('STATUS', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted'), ('C', 'Discontinued')], max_length=1)),
                ('STATUS_UPDATE_DATE', models.DateField(null=True)),
                ('ITEM_SOH', models.DecimalField(decimal_places=4, max_digits=20)),
                ('SOH_UPDATE_DATETIME', models.DateField(null=True)),
                ('SHIPPED_QTY', models.PositiveIntegerField()),
                ('RESERVED_QTY', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('RTV_QTY', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('EXPECTED_QTY', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('RECEIVED_QTY', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('LAST_UPDATE_ID', models.CharField(max_length=25, null=True)),
                ('UPDATE_DATETIME', models.DateTimeField(auto_now=True)),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_location_type', to='stock_ledger_models.location')),
            ],
        ),
        migrations.CreateModel(
            name='ITEM_DTL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEM', models.CharField(max_length=25)),
                ('ITEM_PARENT', models.CharField(max_length=25, null=True)),
                ('ITEM_GRANDPARENT', models.CharField(max_length=25, null=True)),
                ('PACK_IND', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], max_length=1)),
                ('ITEM_LEVEL', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('TRAN_LEVEL', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('DIFF1', models.CharField(max_length=15, null=True)),
                ('DIFF2', models.CharField(max_length=15, null=True)),
                ('STATUS', models.CharField(choices=[('A', 'Active'), ('D', 'Disabled')], max_length=1)),
                ('ITEM_DESC', models.CharField(max_length=100)),
                ('SELLING_UOM', models.CharField(max_length=3, null=True)),
                ('ORIGINAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('ORIGINAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('LAST_UPDATE_ID', models.CharField(max_length=25, null=True)),
                ('UPDATE_DATETIME', models.DateTimeField(auto_now=True)),
                ('CLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.class')),
                ('DEPT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept')),
                ('SUBCLASS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.subclass')),
            ],
        ),
        migrations.CreateModel(
            name='err_trn_data',
            fields=[
                ('PROCESS_IND', models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1)),
                ('ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM', models.CharField(max_length=25, null=True)),
                ('REF_ITEM_TYPE', models.CharField(choices=[('P', 'PACK'), ('U', 'UPC')], max_length=1, null=True)),
                ('TRN_DATE', models.DateField(auto_now=True)),
                ('TRN_TYPE', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=10, null=True)),
                ('QTY', models.PositiveIntegerField(null=True)),
                ('PACK_QTY', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('PACK_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('PACK_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('UNIT_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_COST', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('TOTAL_RETAIL', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('REF_NO1', models.CharField(max_length=10, null=True)),
                ('REF_NO2', models.CharField(max_length=10, null=True)),
                ('REF_NO3', models.CharField(max_length=10, null=True)),
                ('REF_NO4', models.CharField(max_length=10, null=True)),
                ('CREATE_ID', models.CharField(max_length=25, null=True)),
                ('CREATE_DATETIME', models.DateTimeField(auto_now_add=True)),
                ('REV_TRN_NO', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('ERR_MSG', models.CharField(choices=[('SALES', 'SALES'), ('RETURNS', 'RETURNS'), ('PO', 'PO'), ('TRANSFER', 'TRANSFER')], max_length=100)),
                ('ERR_SEQ_NO', models.IntegerField()),
                ('CURRENCY', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stock_ledger_models.currency')),
                ('LOCATION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='err_location_name', to='stock_ledger_models.location')),
                ('LOCATION_TYPE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='err_location_type', to='stock_ledger_models.location')),
                ('TRAN_SEQ_NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_ledger_models.stg_trn_data')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='DEPT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_ledger_models.dept'),
        ),
    ]
