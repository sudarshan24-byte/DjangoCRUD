from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player

# Create your views here.
def index(request):
    players = Player.objects.all()

    return render(request, 'data.html', {'players':players})

def add_data(request):

    if request.method=="POST":
         # data fetch
        player_name = request.POST.get("player_name")
        country = request.POST.get("country")
        team = request.POST.get("team")
        # player_id = request.POST.get("player_id")
        category = request.POST.get("category")
        player_type = request.POST.get("player_type")
        bowler_type = request.POST.get("bowler_type")

    # set data
        p = Player()
        p.pName = player_name
        p.country = country
        p.team = team
        # p.player_id = player_id
        p.category = category
        p.pType = player_type
        p.bType = bowler_type

    # save
        p.save()

        return redirect('/data')
    
    return render(request, 'add-data.html')


def delete_data(request, id):
    ply = Player.objects.get(pk=id)
    ply.delete()
    # print(id)
    return redirect('/data')

def update_data(request, id):
    ply = Player.objects.get(pk=id)
    return render(request, 'update-data.html', {
        'ply':ply
    })

def update_player(request, id):
    if request.method == 'POST':
        player_name = request.POST.get("player_name")
        country = request.POST.get("country")
        team = request.POST.get("team")
        # player_id = request.POST.get("player_id")
        category = request.POST.get("category")
        player_type = request.POST.get("player_type")
        bowler_type = request.POST.get("bowler_type")

        ply = Player.objects.get(pk=id)
        ply.pName = player_name
        ply.country = country
        ply.team = team
        ply.category = category
        ply.pType = player_type
        ply.bType = bowler_type

        ply.save()

    return redirect('/data')