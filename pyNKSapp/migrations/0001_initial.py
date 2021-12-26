# Generated by Django 3.1 on 2021-12-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('fee', models.CharField(max_length=20)),
                ('advance_fee', models.CharField(max_length=20)),
                ('req_percentage', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'degree',
            },
        ),
        migrations.CreateModel(
            name='institutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=50)),
                ('ins_photo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'institutes',
            },
        ),
        migrations.CreateModel(
            name='number_of_students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_students', models.IntegerField()),
            ],
            options={
                'db_table': 'number_of_students',
            },
        ),
        migrations.CreateModel(
            name='signupdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_stu_id', models.IntegerField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('reenterpassword', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('prev_edu_percentage', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'signupdetails',
            },
        ),
        migrations.CreateModel(
            name='staff_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'staff_details',
            },
        ),
        migrations.CreateModel(
            name='student_enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=25)),
                ('course', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'student_enroll',
            },
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('seats_available', models.IntegerField(max_length=50)),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.degree')),
                ('institute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.institutes')),
            ],
            options={
                'db_table': 'specialization',
            },
        ),
        migrations.AddField(
            model_name='institutes',
            name='chairman_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.signupdetails'),
        ),
        migrations.CreateModel(
            name='enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.degree')),
                ('institute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.institutes')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.specialization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.signupdetails')),
            ],
            options={
                'db_table': 'enrolled',
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='institute_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyNKSapp.institutes'),
        ),
    ]
