from django.http import HttpResponse
from django.contrib.auth.models import User

def auth(request):
    reqUser = request.POST.get('username')
    reqPass = request.POST.get('password')
    if User.objects.filter(username=reqUser).exists():
        user = User.objects.get(username=reqUser)
        if user.check_password(reqPass) and user.get_profile().allowGame:
            return HttpResponse("auth-ok\n" + str(user.pk) + "\n" + str(user.get_profile().score))
        else:
            return HttpResponse("auth-failed")
    else:
        return HttpResponse("auth-failed")

def get_scorelist(request):
    players = User.objects.all()
    response = ""
    for player in players: response += "%s %s \n" % (player.username, str(player.get_profile().score))
    return HttpResponse(response)

def add_score(request):
    userID = int(request.POST.get('userID'))
    user = User.objects.get(pk=userID)
    playerProfile = user.get_profile()
    playerProfile.score += 2
    playerProfile.save()


