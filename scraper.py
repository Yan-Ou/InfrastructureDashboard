import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcs_dashboard.settings")
django.setup()

from bs4 import BeautifulSoup
import urllib2
from datetime import date

from dailyhealth.models import Report, General, Capacity, Backup, BYOL, Affinity, Alarm, Wrong, SDRS, Snapshot, Zombie, Clone, CDROM, Removed, Reservation, StorageIO


page = urllib2.urlopen("http://172.24.3.79")
soup = BeautifulSoup(page)

divs=soup.find_all(lambda x:x.name == 'div' and 'id' in x.attrs)

report_index = Report.objects.get_or_create(created = date.today())[0]

def populate(*args):
	i=1
	result = []
	for arg in args:
		arg = str(cols[i].get_text())
		i+=1
		result.append(arg)
	return result
	
report_list = {'General', 'Capacity', 'Backup', 'BYOL', 'Affinity', 'Alarm', 'wrong', 'SDRS','Snapshot', 'Zombie','Clone','Violation', 'Removed', 'I/O', 'Reservation'}

for div in divs:
	report_name = "".join (filter (lambda x: x in str(div['id']), report_list))
	if report_name == 'General':
		print report_name
		tables = div.find_all('td')
		general = General.objects.get_or_create(report_date=report_index)[0]
		general.activeVM_count = tables[0].get_text()
		general.migrate_count = tables[1].get_text()
		general.inactive_count = tables[2].get_text()
		general.cluster_count = tables[3].get_text()
		general.dcluster_count = tables[4].get_text()
		general.datastore_count = tables[5].get_text()
		general.host_count = tables[6].get_text()
		general.template_count = tables[7].get_text()
		general.VM_count = tables[8].get_text()
		general.save()

	elif report_name == 'Capacity':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			capacity = Capacity.objects.get_or_create(report_date=report_index, cluster=cols[0].get_text())[0]
			capacity.host,capacity.VM_count,capacity.CPU_total,capacity.CPU_allocated,capacity.RAM_total, capacity.RAM_allocated, capacity.CPU_available, capacity.RAM_available,capacity.CPU_reserve,capacity.RAM_reserve = [str(item) for item in populate(capacity.host,capacity.VM_count,capacity.CPU_total,capacity.CPU_allocated,capacity.RAM_total, capacity.RAM_allocated, capacity.CPU_available, capacity.RAM_available, capacity.CPU_reserve,capacity.RAM_reserve)]
			capacity.save()

	elif report_name == 'Backup':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			backup = Backup.objects.get_or_create(report_date=report_index, VMName=cols[0].get_text())[0]
			backup.LastBackedup,backup.HoursSinceLastBackup,backup.MediaServer,backup.NBPolicy = [str(item) for item in populate(backup.LastBackedup,backup.HoursSinceLastBackup,backup.MediaServer,backup.NBPolicy)]
			backup.save()

	elif report_name == 'BYOL':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			byol = BYOL.objects.get_or_create(report_date=report_index, VM=cols[0].get_text())[0]
			byol.cluster = cols[1].get_text()
			byol.save()

	elif report_name == 'Affinity':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			affinity = Affinity.objects.get_or_create(report_date=report_index, VM1=cols[0].get_text())[0]
			affinity.VM2, affinity.VMsOnSameHost, affinity.VMsInSameCluster = [str(item) for item in populate(affinity.VM2, affinity.VMsOnSameHost, affinity.VMsInSameCluster)]
			affinity.save()

	elif report_name == 'Alarm':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols= table.find_all('td')
			alarm = Alarm.objects.get_or_create(report_date=report_index, Name=cols[0].get_text())[0]
			alarm.Type = cols[1].get_text()
			alarm.save()

	elif report_name == 'wrong':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			wrong = Wrong.objects.get_or_create(report_date=report_index,Name=cols[0].get_text())[0]
			wrong.Host = cols[1].get_text()
			wrong.save()

	elif report_name == 'SDRS':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			sdrs = SDRS.objects.get_or_create(report_date=report_index, VM=cols[0].get_text())[0]
			sdrs.Enabled, sdrs.cluster = [str(item) for item in populate(sdrs.Enabled,sdrs.cluster)]
			sdrs.save()

	elif report_name == 'Snapshot':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			snapshot = Snapshot.objects.get_or_create(report_date=report_index,Name=cols[0].get_text())[0]
			snapshot.NumberofSnapshot = cols[1].get_text()
			snapshot.save()

	elif report_name == 'Zombie':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			zombie = Zombie.objects.get_or_create(report_date=report_index, Name=cols[0].get_text())[0]
			zombie.Message = cols[1].get_text()
			zombie.save()

	elif report_name == 'Clone':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			clone = Clone.objects.get_or_create(report_date=report_index, CreatedTime=cols[0].get_text())[0]
			clone.UserName, clone.Message = [str(item) for item in populate(clone.UserName,clone.Message)]
			clone.save()

	elif report_name == 'Violation':
		print report_name
		tables = div.find_all('tr')[2:]
		for table in tables:
			cdrom = CDROM.objects.get_or_create(report_date=report_index, VM= table.get_text())[0]
			cdrom.save()

	elif report_name == 'Removed':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			removed = Removed.objects.get_or_create(report_date=report_index, CreatedTime=cols[0].get_text())[0]
			removed.UserName, removed.Message = [str(item) for item in populate(removed.UserName,removed.Message)]
			removed.save()

	elif report_name == 'I/O':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			storageio = StorageIO.objects.get_or_create(report_date=report_index, Name=cols[0].get_text())[0]
			storageio.IOControl = cols[1].get_text()
			storageio.save()

	elif report_name == 'Reservation':
		print report_name
		tables = div.find_all('tr')[1:]
		for table in tables:
			cols = table.find_all('td')
			reservation = Reservation.objects.get_or_create(report_date=report_index, Name=cols[0].get_text())[0]
			reservation.CPURes, reservation.MemRes = [str(item) for item in populate(reservation.CPURes, reservation.MemRes)]
			reservation.save()

