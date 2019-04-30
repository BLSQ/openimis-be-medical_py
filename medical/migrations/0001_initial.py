# Generated by Django 2.1.8 on 2019-04-05 08:15

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(db_column='ItemID', primary_key=True, serialize=False)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('code', models.CharField(db_column='ItemCode', max_length=6)),
                ('name', models.CharField(db_column='ItemName', max_length=100)),
                ('type', models.CharField(db_column='ItemType', max_length=1)),
                ('package', models.CharField(blank=True, db_column='ItemPackage', max_length=255, null=True)),
                ('price', models.DecimalField(db_column='ItemPrice', decimal_places=2, max_digits=18)),
                ('care_type', models.CharField(db_column='ItemCareType', max_length=1)),
                ('frequency', models.SmallIntegerField(blank=True, db_column='ItemFrequency', null=True)),
                ('pat_cat', models.SmallIntegerField(db_column='ItemPatCat')),
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom')),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('audit_user_id', models.IntegerField(db_column='AuditUserID')),
                ('row_id', models.BinaryField(blank=True, db_column='RowID', null=True)),
            ],
            options={
                'db_table': 'tblItems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(db_column='ServiceID', primary_key=True, serialize=False)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('category', models.CharField(blank=True, db_column='ServCategory', max_length=1, null=True)),
                ('code', models.CharField(db_column='ServCode', max_length=6)),
                ('name', models.CharField(db_column='ServName', max_length=100)),
                ('type', models.CharField(db_column='ServType', max_length=1)),
                ('level', models.CharField(db_column='ServLevel', max_length=1)),
                ('price', models.DecimalField(db_column='ServPrice', decimal_places=2, max_digits=18)),
                ('care_type', models.CharField(db_column='ServCareType', max_length=1)),
                ('frequency', models.SmallIntegerField(blank=True, db_column='ServFrequency', null=True)),
                ('pat_cat', models.SmallIntegerField(db_column='ServPatCat')),
                ('validity_from', core.fields.DateTimeField(blank=True, db_column='ValidityFrom', null=True)),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('audit_user_id', models.IntegerField(blank=True, db_column='AuditUserID', null=True)),
                ('row_id', models.BinaryField(blank=True, db_column='RowID', null=True)),
            ],
            options={
                'db_table': 'tblServices',
                'managed': False,
            },
        ),
    ]