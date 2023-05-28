from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    num_games = Games.objects.all().count()
    num_companys = Companys.objects.all().count()
    num_genres = Genre.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
 

    return render(
        request,
        'index.html',
        context= {'num_games':num_games, 'num_companys':num_companys, 'num_genres':num_genres, 'num_visits': num_visits}

    )

class GamesListView(generic.ListView):
    model = Games
    paginate_by = 10

class GamesDetailView(generic.DetailView):
    model = Games

    def game_detail_view(request, pk):
        try:
            game_id=Games.objects.get(pk=pk)
        except:
            raise Http404("Game does not exist")
        
        return render(
            request,
            'catalog/games_detail.html',
            context={'game':game_id})

class CompanysListView(generic.ListView):
    model = Companys

class CompanyDetailView(generic.DetailView):
    model = Companys

    def company_detail_view(request, pk):
        try:
            company_id=Companys.objects.get(pk=pk)
        except:
            raise Http404("Company does not exist")
        
        return render(
            request,
            'catalog/companys_detail.html',
            context={'company':company_id})
    

class AddedGamesByUserListView(LoginRequiredMixin,generic.ListView):
    model = GameLibrarys
    template_name ='catalog/game_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return GameLibrarys.objects.filter(borrower=self.request.user).order_by('time_add')
    