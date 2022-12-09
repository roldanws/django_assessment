from django.urls import path
from .views import SignUpView, BienvenidaView, SignInView,SignOutView
from django.contrib.auth.decorators import login_required


administrator_patterns = ([
    path('', login_required(BienvenidaView.as_view()), name='bienvenida'),
    #path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('login/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    
],'administrator')



