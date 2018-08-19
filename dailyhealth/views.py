from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from dailyhealth.models import Report, General, Capacity, Backup, BYOL, Affinity, Alarm, Wrong, SDRS, Zombie,Clone, Snapshot

# Create your views here.

report_index = Report.objects.get_or_create(created = date.today())[0]
backcup_list = Backup.objects.filter(report_date=report_index)

def index(request):
	general_list = General.objects.order_by('-report_date')[0]
	context_dict = {'generals': general_list, 'backups': backcup_list}
	return render(request, 'dailyhealth/index.html', context_dict)

def capacity(request):
	capacity_list = Capacity.objects.filter(report_date=report_index)
	context_dict = {'capacities': capacity_list}
	return render(request, 'dailyhealth/capacity.html', context_dict)