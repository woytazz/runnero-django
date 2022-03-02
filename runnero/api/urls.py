from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from .views import (
    UserProfileList,
    UserProfileRetrieveUpdate,
    ChallengeList,
    ChallengeRetrieve,
    UserActiveChallengeCreate,
    UserActiveChallengeRetrieveDestroy,
    UserDoneChallengeListCreate,
    PrizeList,
    PrizeRetrieve,
    UserPrizeListCreate,
    RegisterView
)

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='all_profiles-list'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdate.as_view(), name='profiles-retrieve-update'),

    path('challenges/', ChallengeList.as_view(), name='all_challenges-list'),
    path('challenges/<int:pk>/', ChallengeRetrieve.as_view(), name='challenge-retrieve'),
    path('active/', UserActiveChallengeCreate.as_view(), name='active_challenge-create'),
    path('active/<int:pk>/', UserActiveChallengeRetrieveDestroy.as_view(), name='active_challenge-retrieve-destroy'),
    path('done/', UserDoneChallengeListCreate.as_view(), name='done_challenge-list-create'),

    path('prizes/', PrizeList.as_view(), name='all_prizes-list'),
    path('prizes/<int:pk>/', PrizeRetrieve.as_view(), name='prize-retrieve'),
    path('userprizes/', UserPrizeListCreate.as_view(), name='user_prizes-list-create'),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register')
]
