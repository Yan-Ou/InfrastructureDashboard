from django.db import models

# Create your models here.

class Report(models.Model):
	created = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.created)

class General(models.Model):
	report_date = models.ForeignKey(Report)
	activeVM_count = models.IntegerField(default=0)
	migrate_count = models.IntegerField(default=0)
	inactive_count = models.IntegerField(default=0)
	cluster_count = models.IntegerField(default=0)
	dcluster_count = models.IntegerField(default=0)
	datastore_count = models.IntegerField(default=0)
	host_count = models.IntegerField(default=0)
	template_count = models.IntegerField(default=0)
	VM_count = models.IntegerField(default=0)

	def __unicode__(self):
		return unicode(self.report_date)
		pass 


class Capacity(models.Model):
	report_date = models.ForeignKey(Report)
 	cluster = models.CharField(max_length=128)
 	host = models.CharField(max_length=128)
 	VM_count = models.CharField(max_length=128)
 	CPU_total = models.CharField(max_length=128)
 	CPU_allocated = models.CharField(max_length=128)
 	RAM_total = models.CharField(max_length=128)
 	RAM_allocated = models.CharField(max_length=128)
 	CPU_available = models.CharField(max_length=128)
 	RAM_available = models.CharField(max_length=128)
 	CPU_reserve = models.CharField(max_length=128)
 	RAM_reserve = models.CharField(max_length=128)

 	def __unicode__(self):
 		return self.cluster

class Backup(models.Model):
	report_date = models.ForeignKey(Report)
	VMName = models.CharField(max_length=128)
	LastBackedup = models.CharField(max_length=128)
	HoursSinceLastBackup = models.CharField(max_length=128)
	MediaServer = models.CharField(max_length=128)
	NBPolicy = models.CharField(max_length=128)

	def __unicode__(self):
		return self.VMName

class BYOL(models.Model):
	report_date = models.ForeignKey(Report)
	VM = models.CharField(max_length=128)
	cluster = models.CharField(max_length=128)

	def __unicode__(self):
		return self.cluster

class Alarm(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	Type = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class Wrong(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	Host = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class SDRS(models.Model):
	report_date = models.ForeignKey(Report)
	VM = models.CharField(max_length=128)
	Enabled = models.CharField(max_length=128)
	cluster = models.CharField(max_length=128)

	def __unicode__(self):
		return self.VM

class Affinity(models.Model):
	report_date = models.ForeignKey(Report)
	VM1 = models.CharField(max_length=128)
	VM2 = models.CharField(max_length=128)
	VMsOnSameHost = models.CharField(max_length=128)
	VMsInSameCluster = models.CharField(max_length=128)

	def __unicode__(self):
		return self.VM1

class Snapshot(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	NumberofSnapshot = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class Zombie(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	Message = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class Clone(models.Model):
	report_date = models.ForeignKey(Report)
	CreatedTime = models.CharField(max_length=128)
	UserName = models.CharField(max_length=128)
	Message = models.CharField(max_length=128)

	def __unicode__(self):
		return self.CreatedTime

class CDROM(models.Model):
	report_date = models.ForeignKey(Report)
	VM = models.CharField(max_length=128)

	def __unicode__(self):
		return self.VM

class Removed(models.Model):
	report_date = models.ForeignKey(Report)
	CreatedTime = models.CharField(max_length=128)
	UserName = models.CharField(max_length=128)
	Message = models.CharField(max_length=255)

	def __unicode__(self):
		return self.CreatedTime

class StorageIO(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	IOControl = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class Reservation(models.Model):
	report_date = models.ForeignKey(Report)
	Name = models.CharField(max_length=128)
	CPURes = models.CharField(max_length=128)
	MemRes = models.CharField(max_length=128)

	def __unicode__(self):
		return self.Name

class VMAX(models.Model):
	report_date = models.ForeignKey(Report)
	symmID = models.CharField(max_length=128)
	virtual_used = models.IntegerField(default=0)
	virtual_total= models.IntegerField(default=0)
	physical_used = models.IntegerField(default=0)
	physical_total = models.IntegerField(default=0)
	EFD_name = models.CharField(max_length=128)
	EFD_total = models.IntegerField(default=0)
	EFD_free = models.IntegerField(default=0)
	EFD_used = models.IntegerField(default=0)
	EFD_full = models.IntegerField(default=0)
	EFD_sub = models.IntegerField(default=0)
	FC_name = models.CharField(max_length=128)
	FC_total = models.IntegerField(default=0)
	FC_free = models.IntegerField(default=0)
	FC_used = models.IntegerField(default=0)
	FC_full = models.IntegerField(default=0)
	FC_sub = models.IntegerField(default=0)
	SATA_name = models.CharField(max_length=128)
	SATA_total = models.IntegerField(default=0)
	SATA_free = models.IntegerField(default=0)
	SATA_used = models.IntegerField(default=0)
	SATA_full = models.IntegerField(default=0)
	SATA_sub = models.IntegerField(default=0)

