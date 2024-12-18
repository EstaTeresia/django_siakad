from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import (
    Periode,
    MataKuliah,
    Jadwal,
    KRS
)


@admin.register(Periode)
class PeriodeAdmin(ModelAdmin):
    pass


@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    pass


@admin.register(Jadwal)
class JadwalAdmin(ModelAdmin):
    list_display = ("mata_kuliah", "dosen", "jadwal", "ruang")


@admin.register(KRS)
class KRSAdmin(ModelAdmin):

    filter_horizontal = ("jadwal",)
    list_display = ("periode", "mahasiswa",)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "jadwal":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs["queryset"] = qs.select_related("dosen", "mata_kuliah", "ruang", "periode")
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)


# @admin.register(Jadwal)
# class JadwalAdmin(ModelAdmin):
#     pass
