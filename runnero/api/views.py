from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerProfileOrReadOnly, IsObjectOwner
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
from .models import (
    UserProfile,
    Challenge,
    UserActiveChallenge,
    UserDoneChallenge,
    Prize,
    UserPrize
)
from .serializers import (
    UserProfileSerializer,
    ChallengeSerializer,
    UserActiveChallengeSerializer,
    UserDoneChallengeSerializer,
    PrizeSerializer,
    UserPrizeSerializer,
    RegisterSerializer
)


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class UserProfileRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated & IsOwnerProfileOrReadOnly]

    def put(self, request, *args, **kwargs):
        return Response(status=401, data='PUT method not allowed')


class ChallengeList(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]


class ChallengeRetrieve(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated]


class UserActiveChallengeCreate(generics.CreateAPIView):
    serializer_class = UserActiveChallengeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if self.request.user.id != request.data.get("user"):
            return Response(status=409)
        else:
            return self.create(request, *args, **kwargs)


class UserActiveChallengeRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserActiveChallenge.objects.all()
    serializer_class = UserActiveChallengeSerializer
    permission_classes = [IsAuthenticated & IsObjectOwner]


class UserDoneChallengeListCreate(generics.ListCreateAPIView):
    serializer_class = UserDoneChallengeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserDoneChallenge.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if self.request.user.id != request.data.get("user"):
            return Response(status=409)
        else:
            return self.create(request, *args, **kwargs)


class PrizeList(generics.ListAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]


class PrizeRetrieve(generics.RetrieveAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]


class UserPrizeListCreate(generics.ListCreateAPIView):
    serializer_class = UserPrizeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPrize.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if self.request.user.id != request.data.get("user"):
            return Response(status=409)
        else:
            return self.create(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
