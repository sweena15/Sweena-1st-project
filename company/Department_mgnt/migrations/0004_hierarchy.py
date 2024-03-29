# Generated by Django 5.0.1 on 2024-01-21 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department_mgnt', '0003_remove_dept_dep_head'),
        ('Employee_mgnt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hierarchy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='Employee_mgnt.employee')),
                ('manager', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='Employee_mgnt.employee')),
                ('teamleader', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teamleader', to='Employee_mgnt.employee')),
            ],
        ),
    ]
