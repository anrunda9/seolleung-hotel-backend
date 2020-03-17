from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'bathrooms',
            },
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'beds',
            },
        ),
        migrations.CreateModel(
            name='Bedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'beddings',
            },
        ),
        migrations.CreateModel(
            name='BedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Bed')),
            ],
            options={
                'db_table': 'bed_types',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Comfort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'comforts',
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('is_weekend', models.BooleanField(null=True)),
                ('is_holiday', models.BooleanField(null=True)),
                ('is_season', models.BooleanField(null=True)),
                ('custom_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'dates',
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'entertainments',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='FnBService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'fnb_services',
            },
        ),
        migrations.CreateModel(
            name='Furnishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'furnishings',
            },
        ),
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'laundries',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('offer', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'packages',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Branch')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomIconicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_parking', models.BooleanField(null=True)),
                ('free_wifi', models.BooleanField(null=True)),
                ('non_smoking', models.BooleanField(null=True)),
                ('room_square_meter', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('room_square_meter_py', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('tv', models.BooleanField(null=True)),
                ('refrigerator', models.BooleanField(null=True)),
                ('bed_type', models.ManyToManyField(null=True, through='room.BedType', to='room.Bed')),
            ],
            options={
                'db_table': 'room_iconic_infos',
            },
        ),
        migrations.CreateModel(
            name='RoomInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Bathroom')),
                ('bedding', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Bedding')),
                ('comfort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Comfort')),
                ('entertainment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Entertainment')),
                ('fnb_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.FnBService')),
                ('furnishing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Furnishing')),
                ('laundry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Laundry')),
            ],
            options={
                'db_table': 'room_informations',
            },
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'safeties',
            },
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'views',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('iconic_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomIconicInfo')),
                ('room_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomInformation')),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='RoomPackagePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Package')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Room')),
            ],
            options={
                'db_table': 'room_package_prices',
            },
        ),
        migrations.AddField(
            model_name='roominformation',
            name='safety',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Safety'),
        ),
        migrations.AddField(
            model_name='roominformation',
            name='view',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.View'),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=500)),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomType')),
            ],
            options={
                'db_table': 'room_images',
            },
        ),
        migrations.CreateModel(
            name='RoomDatePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Date')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Room')),
            ],
            options={
                'db_table': 'room_date_prices',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='package',
            field=models.ManyToManyField(null=True, through='room.RoomPackagePrice', to='room.Package'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomType'),
        ),
        migrations.AddField(
            model_name='branch',
            name='facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Facility'),
        ),
        migrations.AddField(
            model_name='bedtype',
            name='iconic_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomIconicInfo'),
        ),
    ]
