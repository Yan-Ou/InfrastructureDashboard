from django.contrib import admin
from dailyhealth.models import Report, General, Capacity, Backup, BYOL, Alarm, Wrong, SDRS, Affinity,Snapshot, Zombie, Clone, CDROM, Removed, StorageIO, Reservation

# Register your models here.
admin.site.register(Report)
admin.site.register(General)
admin.site.register(Capacity)
admin.site.register(Backup)
admin.site.register(BYOL)
admin.site.register(Alarm)
admin.site.register(Wrong)
admin.site.register(SDRS)
admin.site.register(Affinity)
admin.site.register(Snapshot)
admin.site.register(Zombie)
admin.site.register(Clone)
admin.site.register(CDROM)
admin.site.register(Removed)
admin.site.register(StorageIO)
admin.site.register(Reservation)