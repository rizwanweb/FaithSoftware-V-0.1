
from django.urls import path

from . import views



urlpatterns = [
    path('jobcalculation/<str:pk>', views.CalculationSheetPDF.as_view(), name='calculationsheet'),
    path('pidcalculation/<str:pk>', views.PIDCalculationSheetPDF.as_view(), name='pidcalculationsheet'),
    path('jobsreport/', views.JobsReportPDF.as_view(), name='jobsreport'),
    path('streport/', views.STReportPDF.as_view(), name='streport'),
    path('billreport/<int:pk>', views.BillReportPDF.as_view(), name='billreport'),

    path('pidbillreport/<int:pk>', views.PIDBillReportPDF.as_view(), name='pidbillreport'),

    #Letters

    path('damagewaive/<str:pk>', views.DamageWaivePDF.as_view(), name='damagewaive'),
    path('piddamagewaive/<str:pk>', views.PIDDamageWaivePDF.as_view(), name='piddamagewaive'),
    path('jobrefund/', views.JobRefundReportPDF.as_view(), name='jobrefund'),


    #DO Authority Letters
    path('authority_letter/<str:pk>', views.DOAuthorityLetterPDF.as_view(), name='authority_letter'),


    #DO UNDERTAKINGS
    path('do_undertaking/<str:pk>', views.DOUndertakingPDF.as_view(), name='do_undertaking'),
]
