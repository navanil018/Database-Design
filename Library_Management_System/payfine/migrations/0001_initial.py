# Generated by Django 2.0.5 on 2019-10-25 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(db_column='Isbn', max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('availability', models.IntegerField(db_column='Availability')),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookAuthors',
            fields=[
                ('author_id', models.AutoField(db_column='Author_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'book_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookLoans',
            fields=[
                ('loan_id', models.AutoField(db_column='Loan_id', primary_key=True, serialize=False)),
                ('date_out', models.DateField(blank=True, db_column='Date_out', null=True)),
                ('due_date', models.DateField(blank=True, db_column='Due_date', null=True)),
                ('date_in', models.DateField(blank=True, db_column='Date_in', null=True)),
            ],
            options={
                'db_table': 'book_loans',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('card_id', models.AutoField(db_column='Card_id', primary_key=True, serialize=False)),
                ('ssn', models.CharField(db_column='Ssn', max_length=9, unique=True)),
                ('bname', models.CharField(blank=True, db_column='Bname', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'borrower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('author', models.ForeignKey(db_column='Author_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='payfine.BookAuthors')),
                ('name', models.CharField(db_column='Name', max_length=255)),
            ],
            options={
                'db_table': 'authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('loan', models.ForeignKey(db_column='Loan_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='payfine.BookLoans')),
                ('fine_amt', models.FloatField(db_column='Fine_amt')),
            ],
            options={
                'db_table': 'fines',
                'managed': False,
            },
        ),
    ]
