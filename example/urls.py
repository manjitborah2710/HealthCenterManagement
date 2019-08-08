from django.conf.urls import url
from example import views
from django.views.generic import RedirectView

ADMIN_URL = 'http://127.0.0.1:8000/admin'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^signin/$', views.SignInPageView.as_view(), name='signin'),
    # url(r'^patient_details/$', views.PatientDetailPageView.as_view(), name='patient_details'),
    url(r'^pharmacist_screen/$', views.PharmacistPageView.as_view(), name='Dashboard'),
    url(r'^stman_screen/$', views.StockManagerPageView.as_view(), name='Requisition'),
    url(r'^patient_history/$', views.PatientHistoryPageView.as_view(), name='PatientHistory'),
    url(r'^getMedicines/$', views.getMedicines, name="medicines"),
    url(r'^new_prescription/$', views.DoctorPageView.as_view(), name='Prescription'),
    url(r'^stock_medicines/$', views.StockPageView.as_view(), name='Stock_medicine'),
    url(r'^getPatient/$', views.getPatient, name="patients"),
    url(r'^getPatientDetail/$', views.getPatientDetail, name="patientdetails"),
    url(r'^getMedicineList/$', views.getMedicineList, name="medlist"),
    url(r'^getMedDetail/$', views.getMedDetail, name="meddetail"),
    url(r'^getMedicinesPrescription/$', views.getMedicinesPrescription, name="medList"),
    url(r'^savePrescriptionMedicine/$', views.savePrescriptionMedicine, name="saving"),
    url(r'^saveNewPrescription/$', views.saveNewPrescription, name="savingNewPres"),
    url(r'^prescription/$', views.PrescriptionPageView.as_view(),name="Template")
]