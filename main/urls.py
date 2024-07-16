from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('count/', views.progress_count, name="count"),
    path('amount/', views.progress_amount, name="amount"),
    path('report/', views.report, name="report"),
    #forms path
    path('barsik-lakshya/', views.barsik_lakshya, name="barsik-lakshya"),
    path('forms/namuna-bibaran', views.namuna_bibaran, name="namuna"),
    path('forms/anugaman-bibaran/', views.anugaman, name="anugaman"),
    path('forms/logobitaran/', views.logobitaran, name="logobitaran"),
    path('forms/namuna-bisleysan/', views.namuna_bisleysan, name="namuna-bisleysan"),
    path('forms/prayogsala-bisleysan/', views.prayogsala_bisleysan, name="prayogsala-bisleysan"),
    path('forms/khadya-patrajari/', views.khadya1, name="khadya1"),
    path('forms/khadya-nabikaran/', views.khadya2, name="khadya2"),
    path('forms/udyog/', views.udyog, name="udyog"),
    path('forms/aayat/', views.aayat, name="aayat"),
    path('forms/export/',views.export,name='export'),
    path('forms/bhansar-chali/',views.bhansar_chali_nikasi,name='bhansar_chali'),
    path('forms/ujuri/', views.ujuri, name="ujuri"),
    path('forms/khadya-prasodhan/', views.khadya_prasodhan, name="khadya-prasodhan"),
    path('forms/barsik-budget/', views.barsik_budget, name="barsik_budget"),
    path('forms/quarterly-budget/', views.quarterely_budget, name="quarterely_budget"),
    path('forms/masik-expenses/', views.masik_expense, name="masik_expense"),
    path('forms/masik-rajaswo/', views.rajaswo, name="rajaswo"),
    path('forms/masik-pragati/', views.masik_pragati, name="masik-pragati"),
    #details form path--table list
    path('forms/details/anugaman/', views.detail_anugaman, name="d-anugaman"),
    path('forms/details/gunasho/', views.detail_gunasho, name="d-gunasho"),
    path('forms/details/hotel/', views.detail_hotel, name="d-hotel"),
    path('forms/details/mudha/', views.detail_mudha, name="d-mudha"),
    path('forms/details/rbpa-fruits/', views.rbpa_fruits, name="d-rbpa-fruits"),
    path('forms/details/rbpa-vegetables/', views.rbpa_vegetables, name="d-rbpa-vegetables"),
    path('forms/details/registration/', views.detail_registration, name="d-registration"),
    path('forms/details/renew/', views.detail_renew, name="d-renew"),
    path('forms/details/udyog/', views.detail_udyog, name="d-udyog"),
    #reports path
    path('report/khadya-act/', views.khadyaact_report, name="khadya-act-report"),
    path('report/anugaman/', views.anugaman_report, name="anugaman-report"),
    path('report/hotel/', views.hotel_report, name="hotel-report"),
    path('report/khadya/', views.khadya_report, name="khadya-report"),
    path('report/prayogsala/', views.prayogsala_report, name="prayogsala-report"),
    path('report/rbpa/', views.rbpa_report, name="rbpa-report"),
    path('report/import-export/', views.importexport_report, name="import-export-report"),
    path('report/gunasho/', views.gunasho_report, name="gunasho-report"),
    path('report/patrakar/', views.patrakar_report, name="patrakar-report"),
    path('report/patrajari/', views.patrajari_report, name="patrajari-report"),
    path('report/renew/', views.renew_report, name="renew-report"),
    path('report/udyog/', views.udyog_report, name="udyog-report"),
    # path('report/finance/', views.finance_report, name="finance-report"),
    #Budget Report
    path('report/yearly-budget/', views.yearly_budget, name="yearly-budget-report"),
    path('report/quarterely-budget/', views.quarterely_budget_report, name="quarterely-budget-report"),
    #Expense Report
    path('report/monthly-expense/', views.monthly_expense_report, name="monthly-expense-report"),
    path('report/quarterely-expense/', views.quarterely_expense_report, name="quarterely-expense-report"),
    path('report/yearly-expense/', views.yearly_expense_report, name="yearly-expense-report"),
    # Rajaswo Report
    path('report/monthly-rajaswo-report/', views.monthly_rajaswo_report, name="monthly-rajaswo-report"),
    path('report/quarterely-rajaswo/', views.quarterely_rajaswo_report, name="quarterely-rajaswo-report"),
    path('report/yearly-rajaswo/', views.yearly_rajaswo_report, name="yearly-rajaswo-report"),
    
    #view path
    path('detail/khadyaact/<int:id>/', views.khadyaact_view, name="khadyaact-view"),
    path('detail/anugaman/<int:id>/', views.anugaman_view, name="anugaman-view"),
    path('detail/hotel/<int:id>/', views.hotel_view, name="hotel-view"),
    path('detail/khadya/<int:id>/', views.khadya_view, name="khadya-view"),
    path('detail/prayogsala/<int:id>/', views.prayogsala_view, name="prayogsala-view"),
    path('detail/rbpr/<int:id>/', views.rbpa_view, name="rbpa-view"),
    path('detail/import-export/<int:id>/', views.importexport_view, name="import-export-view"),
    path('detail/gunasho/<int:id>/', views.gunasho_view, name="gunasho-view"),
    path('detail/patrakar/<int:id>/', views.patrakar_view, name="patrakar-view"),
    path('detail/patrajari/<int:id>/', views.patrajari_view, name="patrajari-view"),
    path('detail/renew/<int:id>/', views.renew_view, name="renew-view"),
    path('detail/udyog/<int:id>/', views.udyog_view, name="udyog-view"),
    path('detail/finance/<int:id>/', views.finance_view, name="finance-view"),
    path('detail/monthly/<int:id>/', views.monthly_view, name="monthly-view"),
    #edit path
    path('edit/khadyaact/<int:id>/', views.khadyaact_edit, name="namunabibaran-edit"),
    path('edit/anugaman/<int:id>/', views.anugaman_edit, name="anugaman-edit"),
    path('edit/hotel/<int:id>/', views.hotel_edit, name="hotel-edit"),
    path('edit/khadya/<int:id>/', views.khadya_edit, name="khadya-edit"),
    path('edit/prayogsala/<int:id>/', views.prayogsala_edit, name="prayogsala-edit"),
    path('edit/rbpa/<int:id>/', views.rbpa_edit, name="rbpa-edit"),
    path('edit/import-export/<int:id>/', views.importexport_edit, name="importexport-edit"),
    path('edit/gunasho/<int:id>/', views.gunasho_edit, name="gunasho-edit"),
    path('edit/patrakar/<int:id>/', views.patrakar_edit, name="patrakar-edit"),
    path('edit/patrajari/<int:id>/', views.patrajari_edit, name="patrajari-edit"),
    path('edit/renew/<int:id>/', views.renew_edit, name="renew-edit"),
    path('edit/udyog/<int:id>/', views.udyog_edit, name="udyog-edit"),
    # path('edit/finance/<int:id>/', views.finance_edit, name="finance-edit"),
    path('edit/monthly/<int:id>/', views.monthly_edit, name="monthly-edit"),
    #delete path
    path('khadyaact/delete/<int:id>/', views.khadyaact_report_delete, name="khadyaact-delete"),
    path('anugaman/delete/<int:id>/', views.anugaman_report_delete, name="anugaman-delete"),
    path('hotel/delete/<int:id>/', views.hotel_report_delete, name="hotel-delete"),
    path('khadya/delete/<int:id>/', views.khadyaact_report_delete, name="khadya-delete"),
    path('prayogsala/delete/<int:id>/', views.prayogsala_report_delete, name="prayogsala-delete"),
    path('rbpr/delete/<int:id>/', views.rbpa_report_delete, name="rbpa-delete"),
    path('import-export/delete/<int:id>/', views.importexport_report_delete, name="import-export-delete"),
    path('gunasho/delete/<int:id>/', views.gunasho_report_delete, name="gunasho-delete"),
    path('patrakar/delete/<int:id>/', views.patrakar_report_delete, name="patrakar-delete"),
    path('patrajari/delete/<int:id>/', views.patrajari_report_delete, name="patrajari-delete"),
    path('renew/delete/<int:id>/', views.renew_report_delete, name="renew-delete"),
    path('udyog/delete/<int:id>/', views.udyog_report_delete, name="udyog-delete"),
    # path('finance/delete/<int:id>/', views.finance_report_delete, name="finance-delete"),
    path('monthly/delete/<int:id>/', views.monthly_report_delete, name="monthly-delete"),
    #remarks and verify path
    path('khadyaact/remarks/<int:id>/', views.khadyaact_remarks, name="khadyaact-remarks"),
    path('anugaman/remarks/<int:id>/', views.anugaman_remarks, name="anugaman-remarks"),
    path('hotel/remarks/<int:id>/', views.hotel_remarks, name="hotel-remarks"),
    path('prayogsala/remarks/<int:id>/', views.prayogsala_remarks, name="prayogsala-remarks"),
    path('rbpr/remarks/<int:id>/', views.rbpa_remarks, name="rbpa-remarks"),
    path('import-export/remarks/<int:id>/', views.importexport_remarks, name="import-export-remarks"),
    path('gunasho/remarks/<int:id>/', views.gunasho_remarks, name="gunasho-remarks"),
    path('patrakar/remarks/<int:id>/', views.patrakar_remarks, name="patrakar-remarks"),
    path('patrajari/remarks/<int:id>/', views.patrajari_remarks, name="patrajari-remarks"),
    path('renew/remarks/<int:id>/', views.renew_remarks, name="renew-remarks"),
    path('udyog/remarks/<int:id>/', views.udyog_remarks, name="udyog-remarks"),
    # path('finance/remarks/<int:id>/', views.finance_remarks, name="finance-remarks"),
    path('monthly/remarks/<int:id>/', views.monthly_remarks, name="monthly-remarks"),
]