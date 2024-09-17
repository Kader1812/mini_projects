from django.urls import path
# from . import views
from .views import InsertView,CheckData,GetData


urlpatterns = [
    # path('userpage/',UserPage.as_view(),name="user"),
    # path('userpage/first',UserLogin.as_view(),name="page")
    # path('customview/',CustomView.as_view(),name='connection'),
    # path('user/',UserWorld.as_view(),name="orm_method"),
    # path('page/',ExportToExcel.as_view(),name="excel_format"),
    # path('word/',ExportToExcel1.as_view(),name="changed_vers0.1")
    # path('date/',DateImport2.as_view(),name="date.getting")
    # path('pws/',CursorJoinUpdate.as_view(),name="pws_sheet"),
    # path('excel/',CursorExportExcel.as_view(),name="final_excel_sheet"),
    # path('ptm/',ProductionTest.as_view(),name="ptmdata"),
    path('insert/',InsertView.as_view(),name='insert_func'),
    path('check/',CheckData.as_view(),name="check"),
    path('get/',GetData.as_view(),name="get_data")


]
