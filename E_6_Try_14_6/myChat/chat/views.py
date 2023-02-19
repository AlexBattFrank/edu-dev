# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from requests import Response
# from rest_framework import generics, permissions, status
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import api_view
# from rest_framework.filters import OrderingFilter, SearchFilter
# from django.shortcuts import render, redirect
# from rest_framework.generics import get_object_or_404
#
# from .filters import MessageFilter
# from .models import UserProfile, Room, Message
# from .serializers import UserSerializer, UserProfileSerializer, RoomSerializer, MessageSerializer
# from .forms import UserProfileForm
#
#
# def home(request):
#     return render(request, 'home.html')
#
#
# @api_view(['POST'])
# def create_message(request, room_id):
#     room = get_object_or_404(Room, id=room_id)
#     serializer = MessageSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user, room=room)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # registration view
# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # user profile views
# @login_required
# def profile(request):
#     user_profile = request.user.profile
#     return render(request, 'profile.html', {'user_profile': user_profile})
#
#
# def profile_edit(request):
#     user_profile = request.user.profile
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated!')
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=user_profile)
#
#     return render(request, 'edit_profile.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('rooms')
#         else:
#             return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
#     else:
#         return render(request, 'registration/login.html')
#
#
# @login_required
# def edit_profile(request):
#     user_profile = request.user.profile
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#         return render(request, 'edit_profile.html', {'form': form})
#     else:
#         form = UserProfileForm(instance=user_profile)
#     return render(request, 'edit_profile.html', {'form': form})
#
#
# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)
#         return Response({'detail': 'Successfully logged in.'})
#     else:
#         return Response({'detail': 'Invalid credentials.'}, status=400)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class RoomList(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         members = [self.request.user]
#         serializer.save(members=members)
#
#
# class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class MessageList(generics.ListAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_class = MessageFilter
#     ordering_fields = ['timestamp']
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(room__name=self.request.query_params.get('room'))
#
#
# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
#     filterset_class = MessageFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from requests import Response
from rest_framework import generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from .filters import MessageFilter
from .models import UserProfile, Room, Message
from .serializers import UserSerializer, UserProfileSerializer, RoomSerializer, MessageSerializer
from .forms import UserProfileForm


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


@api_view(['POST'])
def create_message(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, room=room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# registration view
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user profile views
@login_required
def profile(request):
    user_profile = request.user.profile
    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('rooms')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'registration/login.html')


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'detail': 'Successfully logged in.'})
    else:
        return Response({'detail': 'Invalid credentials.'}, status=400)


class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        members = [self.request.user]
        serializer.save(members=members)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MessageFilter
    ordering_fields = ['timestamp']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(room__name=self.request.query_params.get('room'))


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = MessageFilter
