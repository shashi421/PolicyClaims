from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from claim.views import ClaimViewList,ClaimViewDetail,ClaimStatusDetail
from claim import views

urlpatterns = [
 #   path('claims/', ClaimViewList.as_view()),
  #  path('claims/<int:pk>/', ClaimViewDetail.as_view()),
   # path('claimstatus/<int:pk>/',ClaimStatusDetail.as_view()),
    path('createclaim/',views.createclaim),
    path('updateclaim/',views.updateclaim),
    path('getclaims/',views.getclaims),
    path('getclaimsforadmin/',views.getclaimsforadmin),




]

urlpatterns = format_suffix_patterns(urlpatterns)

