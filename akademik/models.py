from django.db import models

from master.models import Dosen, Mahasiswa, Ruang


SEMESTER_CHOICES = (
    (1, "Ganjil"),
    (2, "Genap")
)


class Periode(models.Model):
    periode = models.CharField(blank=False, null=True, max_length=10)
    semester = models.PositiveSmallIntegerField(blank=False, null=True, choices=SEMESTER_CHOICES)

    class Meta:
        verbose_name = 'periode'
        verbose_name_plural = 'periode'

    def __str__(self):
        semester_string = None
        if self.semester:
            semester_string = SEMESTER_CHOICES[self.semester][1]
        return f"{semester_string}, {self.periode}"


class MataKuliah(models.Model):
    nama = models.CharField(blank=False, null=True, max_length=50)
    kode = models.CharField(blank=False, null=True, max_length=10)
    sks = models.PositiveSmallIntegerField(blank=False, null=True)
    matkul_prasyarat = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'mata kuliah'
        verbose_name_plural = 'mata kuliah'

    def __str__(self):
        return self.nama


HARI_CHOICES = (
    (1, "Senin"),
    (2, "Selasa"),
    (3, "Rabu"),
    (4, "Kamis"),
    (5, "Jum'at"),
    (6, "Sabtu"),
    (7, "Minggu")
)

class Jadwal(models.Model):
    dosen = models.ForeignKey(Dosen, null=True, blank=False, on_delete=models.SET_NULL)
    mata_kuliah = models.ForeignKey(MataKuliah, null=True, blank=False,on_delete=models.SET_NULL)
    hari = models.PositiveSmallIntegerField(choices=HARI_CHOICES, null=True, blank=False)
    jam_mulai = models.TimeField(blank=False, null=True)
    jam_selesai = models.TimeField(blank=False, null=True)
    ruang = models.ForeignKey(Ruang, blank=False, null=True, on_delete=models.SET_NULL)
    kuota_peserta = models.PositiveIntegerField(blank=False, null=True)
    periode = models.ForeignKey(Periode, blank=False, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'jadwal'
        verbose_name_plural = 'jadwal'

    @property
    def jadwal(self):
        jam_mulai = self.jam_mulai.strftime("%H:%M")
        jam_selesai = self.jam_selesai.strftime("%H:%M")
        return f"{HARI_CHOICES[self.hari][1]}, {jam_mulai}-{jam_selesai}"

    def __str__(self):
        return f"{self.mata_kuliah} | {self.dosen} | {self.jadwal}"


class KRS(models.Model):
    periode = models.ForeignKey(Periode, blank=False, null=True, on_delete=models.SET_NULL)
    mahasiswa = models.ForeignKey(Mahasiswa, blank=False, null=True, on_delete=models.SET_NULL)
    jadwal = models.ManyToManyField(
        Jadwal,
        blank=True,
    )
    class Meta:
        verbose_name = 'krs'
        verbose_name_plural = 'krs'

    def __str__(self):
        return f"{self.mahasiswa} - {self.periode}"
