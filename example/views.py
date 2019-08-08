# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import json
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from example.forms import SignInForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from doctor.models import *
from django.http import HttpResponse
from django.http import JsonResponse

# from django.utils import simplejson
# A view class
class HomePageView(TemplateView):
    template_name = "index.html"
    # to define get request
    def get(self, request):
        '''
            For the index page or homepage
            1. Get the list of Doctors from DB
                self.doctors = HealthCentreStaff.objects.filter(staff_type='Doctor').values()
            2. Get the list of Medicines and Tests similarly
            3. Render the index page and sends the doctors, medicines and tests as
                return render(request, self.template_name, {
                    "doctors" : self.doctors,
                    "tests" : self.tests,
                    "medicines" : self.medicines
                })
        '''
        self.doctors = HealthCentreStaff.objects.filter(staff_type='DR').values()
        self.medicines = Medicine.objects.all().values()
        paginator = Paginator(self.medicines, 15) # Show 25 medicines per page
        page = request.GET.get('page')
        try:
            self.medicines = paginator.page(page)
        except PageNotAnInteger:
            self.medicines = paginator.page(1)
        except EmptyPage:
            self.medicines = paginator.page(paginator.num_pages)
        
        return render(request, self.template_name, {
            "doctors" : self.doctors,
            "medicines" : self.medicines
            })

class SignInPageView(TemplateView):
    template_name = "signin.html"

class PrescriptionPageView(TemplateView):
    template_name = "prescriptionTemplate.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class StockPageView(TemplateView):
    template_name = "stock_medicines.html"

class StockManagerPageView(TemplateView):
    template_name = "stman_screen.html"

class DoctorPageView(TemplateView):
    template_name = "new_prescription.html"

class PharmacistPageView(TemplateView):
    template_name = "pharmacist_screen.html"
    def get(self, request):
        self.pres = Prescription.objects.filter(issued=False).values()
        return render(request, self.template_name,{"pres" : self.pres})

class PatientHistoryPageView(TemplateView):
    template_name = "patientHistory.html"

def savePrescriptionMedicine(request):
    if request.method=='POST' and request.is_ajax():
        try:
            psno = request.POST['psno']
            mid = request.POST['mid']
            issue = request.POST['issue']
            if issue is "true":
                issue = True
            else:
                issue = False
            pid = MedicineIssue.objects.get(prescription_serial_no=psno, medicine_id=mid)
            pid.issue_status = issue
            pid.medicine_quantity_issued = request.POST['qnt']
            pid.non_issue_reason = request.POST['reason']
            pid.save()
            prescription = Prescription.objects.get(prescription_serial_no=psno)
            prescription.issued = True
            prescription.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except MedicineIssue.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getPatient(request):
        
    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text:
            search_text = request.GET['search_text']
            statuss = StudentRecord.objects.filter(person_id__icontains=search_text).values('person_id','name')[:10]
        else:
            statuss = []
    return render(request, 'ajax-search.html', {'statuss':statuss})

def getPatientDetail(request):
        
    if request.method == "GET":
        search_text = request.GET['pid']
        if search_text:
            search_text = request.GET['pid']
            person = StudentRecord.objects.filter(person_id=search_text).values('person_id','name','category').first()
        else:
            person = {}
    return JsonResponse({'person': person})

def getMedicineList(request):
        
    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text:
            search_text = request.GET['search_text']
            statuss = Medicine.objects.filter(medicine_name__icontains=search_text).values('medicine_name')[:10]
        else:
            statuss = []
    return render(request, 'ajax-search2.html', {'statuss':statuss})

def getMedDetail(request):

    if request.method == "GET":
        search_text = request.GET['mid']
        if search_text:
            search_text = request.GET['mid']
            med = Medicine.objects.filter(medicine_name=search_text).values('medicine_id','medicine_name','manufacturing_company','quantity','category').first()
        else:
            med = []
    return JsonResponse({'med_details': med})

def getMedicinesPrescription(request):
    
    if request.method == "GET":
        search_text = request.GET['search_text']
        med = []
        if search_text:
            search_text = request.GET['search_text']
            temp = Medicine.objects.values('medicine_name')
            for xx in temp:
                med.append(xx['medicine_name'])
        else:
            med = []
    return render(request, 'medicineList.html', {'med':med})

def getMedicines(request):
    if request.method == 'POST':
        post_id = request.POST['psno']
        posts = post_id.split(",")
        lis = []
        for x in posts:
            if x:
                temp = list(MedicineIssue.objects.filter(prescription_serial_no = x).values())
                for j in temp:
                    # lis.append(j)
                    temp2 = Medicine.objects.filter(medicine_id = j['medicine_id_id']).values_list('medicine_name').first()
                    j['medicine_name'] = temp2
                lis.append(temp)
            else:
                continue       
        return JsonResponse({'lis' : lis})
    else:
        return HttpResponse("Request method is not a POST")


def saveNewPrescription(request):
    if request.method == 'POST':
        newPres = Prescription()
        newPres.prescription_serial_no = "1002"
        newPres.patient_id_id = request.POST['personid']
        newPres.doctor_id_id = "1001"
        newPres.issued = False
        newPres.save()

        newPresPatientRecord = PatientRecord()
        newPresPatientRecord.prescription_serial_no_id = "1002"
        newPresPatientRecord.doctor_id_id = "1001"
        newPresPatientRecord.patient_id_id = request.POST['personid']
        newPresPatientRecord.complaint = request.POST['complaint']
        newPresPatientRecord.diagnosis = request.POST['diagnosis']
        newPresPatientRecord.test_result = "Yet to arive!"
        newPresPatientRecord.follow_up_date = "2019-08-26"
        newPresPatientRecord.isDependant = False
        newPresPatientRecord.testRecommended = False
        newPresPatientRecord.save()

        medlis = request.POST['medlist']
        medlist = medlis.split(",")
        medqn = request.POST['medqnt']
        medqnt = medqn.split(",")
        temp2 = 0
        for temp1 in medlist:
            if temp1 != "":
                newPresMed = MedicineIssue()
                newPresMed.prescription_serial_no_id = "1002"
                newPresMed.medicine_id_id = temp1
                newPresMed.medicine_quantity_prescribed = medqnt[temp2]
                newPresMed.issue_status = False
                newPresMed.non_issue_reason = ""
                newPresMed.save()
                temp2 = temp2 + 1

        return HttpResponse("Success!")
    else:
        return HttpResponse("Failed")


# def getPatientPreviousRecord(request):
#     if request.method == "GET":
#         name = request.GET['name']
#         pid = request.GET['pid']
#         temp = list(PatientRecord)


# def autocompleteModel(request):
    # search_qs = IndividualRecord.objects.filter(name__startswith=request.REQUEST['search'])
    # results = []
    # return render(request, self.template_name, {"form" : form})

