# Generated by Django 5.1.3 on 2024-12-04 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0008_rename_periode_akademik_kelas_periode'),
        ('master', '0002_mahasiswa_jenis_kelamin_mahasiswa_tgl_lahir_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kelas',
            new_name='Jadwal',
        ),
        migrations.AlterModelOptions(
            name='jadwal',
            options={'verbose_name': 'jadwal', 'verbose_name_plural': 'jadwal'},
        ),
    ]
