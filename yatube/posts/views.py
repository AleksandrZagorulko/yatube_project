from django.http import HttpResponse

# Create your views here.
def index(request):
    # Main page.
    return HttpResponse('Главная страница лучшей в мире соцсети yatube')


def group_posts(request):
    # Group posts page.
    return HttpResponse('Гениальные изречения, явления и тп наших пользователей из группировок')
