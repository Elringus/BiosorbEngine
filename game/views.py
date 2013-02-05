from django.http import HttpResponse
from django.contrib.auth.models import User
from game.models import Player

def auth(request):
    reqUser = request.POST.get('username')
    reqPass = request.POST.get('password')
    if User.objects.filter(username=reqUser).exists():
        user = User.objects.get(username=reqUser)
        player = Player.objects.get(user=user)
        if user.check_password(reqPass) and player.allowGame:
            return HttpResponse("auth-ok\n" + str(player.pk) + "\n" + str(player.level))
        else:
            return HttpResponse("auth-failed")
    else:
        return HttpResponse("auth-failed")

def get_playerlist(request):
    players = Player.objects.all()
    response = ""
    for player in players: response += "%s %s \n" % (player.user.username, str(player.level))
    return HttpResponse(response)

def up_level(request):
    playerID = int(request.POST.get('playerID'))
    player = Player.objects.get(pk=playerID)
    player.level += 1
    player.save()
    return HttpResponse("levelup-ok")


