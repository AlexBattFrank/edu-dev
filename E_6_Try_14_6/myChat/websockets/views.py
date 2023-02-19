from django.shortcuts import render


def my_websocket(request):
    return render(request, 'websockets/my_websocket.html')
