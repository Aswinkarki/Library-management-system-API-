# Generated by Django 5.1.6 on 2025-02-23 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
        ('Students', '0003_alter_student_user'),
        ('Transactions', '0003_transactionmodel_book_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Books.book'),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='book_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Students.student'),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='student_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='transaction_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='transaction_type',
            field=models.CharField(choices=[('borrow', 'Borrow'), ('return', 'Return')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
