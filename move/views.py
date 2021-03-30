from django.shortcuts import render, get_object_or_404
from .models import Move

def all_moves(request):
    move_count = Move.objects.count
    moves = Move.objects.order_by('moved_in')
    return render(request, 'move/all_moves.html', {'moves':moves})

def detail(request, move_id):
    move = get_object_or_404(Move, pk=move_id)
    return render(request, 'move/detail.html', {'move':move})
