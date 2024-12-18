from django.db import models


# Create your models here.
class Prodi(models.Model):

    class Meta:
        verbose_name = 'prodi'
        verbose_name_plural = 'prodi'
        indexes = [
            models.Index(fields=['nama']),
            models.Index(fields=['kode']),
        ]
 
    nama = models.CharField(blank=False, null=True, max_length=50)
    kode = models.CharField(blank=False, null=True, max_length=10)

    def __str__(self):
        return self.nama


JENIS_KELAMIN_CHOICES = (
    ('l','Laki-laki'),
    ('p','perempuan'),
)

class Mahasiswa(models.Model):
    class Meta:
        verbose_name = 'mahasiswa'
        verbose_name_plural = 'mahasiswa'
        indexes = [
            models.Index(fields=['nama']),
            models.Index(fields=['nim']),
        ]

    nama = models.CharField(blank=False, null=True, max_length=50)
    nim = models.CharField(blank=False, null=True, max_length=15)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
    tgl_lahir = models.DateField(null=True, blank=True)
    prodi = models.ForeignKey(Prodi, blank=True, null=True, on_delete=models.SET_NULL)
    # log -> keamanan
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # updated_by = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama


class Dosen(models.Model):
    class Meta:
        verbose_name = 'dosen'
        verbose_name_plural = 'dosen'
        indexes = [
            models.Index(fields=['nama']),
            models.Index(fields=['nid']),
        ]

    nama = models.CharField(blank=False, null=True, max_length=50)
    nid = models.CharField(blank=False, null=True, max_length=15)
    tgl_lahir = models.DateField(null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
    prodi = models.ForeignKey(Prodi, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nama


# Create your models here.
class Ruang(models.Model):
    class Meta:
        verbose_name = 'ruang'
        verbose_name_plural = 'ruang'
        indexes = [
            models.Index(fields=['nama']),
            models.Index(fields=['kode']),
        ]

    nama = models.CharField(blank=False, null=True, max_length=50)
    kode = models.CharField(blank=False, null=True, max_length=10)

    def __str__(self):
        return self.nama
