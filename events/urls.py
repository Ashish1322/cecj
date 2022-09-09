"""cecday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # Urls for returning events details and handling post request of forms
 # CECJ-CODATHON 
    path('break-the-strategy',views.break_strategy,name='break_strategy'), #CECJ-CODATHON 
    path('technical-presentation',views.technical_presentation,name='technical_presentation'),
    path('tech-quiz', views.tech_quiz,name='tech_quiz'),
    path('project-display', views.project_display,name='project_display'),
    path('rangoli', views.rangoli,name='rangoli'),
    path('autocad', views.autocad,name='autocad'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('robolympics',views.robolympics,name="robolympics"),
    path('techcharades',views.techcharades,name="techcharades"),
    path('technical-collage',views.techcollage,name="techcollage"),
    path('floating-boat',views.floatingboat,name="floatingboat"),
    path('group-discussion',views.gd,name="gd"),
    path('master-minds',views.masterminds,name="masterminds"),
    path('mech-relay',views.mechrelays,name="mechrelays"),
    path('survey-scout',views.survey,name="survey"),
    path('technical-quiz-ce',views.techquizce,name="techquizce"),
    path('b-plan',views.bplan,name="bplan"),



    path('break-the-strategy-register',views.break_strategy_register,name='break_strategy_register'), #CECJ-CODATHON 
    path('technical-presentation-register', views.technical_presentation_register,name='technical_presentation_register'),
    path('project-display-register', views.project_display_register,name='project_display_register'),
    path('mechrelay-register', views.mechrealy_register,name='mechrelay_register'),
    path('masterminds-register', views.masterminds_register,name='masterminds_register'),
    path('servey-scout-register', views.survey_register,name='surveyscout_register'),
    path('technical-quiz-ce-register', views.tech_quiz_ce,name='techquizce_register'),
    path('robolympics-register', views.robolympics_register,name='robolympics_register'),
    path('tech-charades-register', views.techcharades_register,name='techcharades_register'),
    path('tech-collage-register', views.techcollage_register,name='techcollage_register'),
    path('tech-quiz-register', views.tech_quiz_register,name='tech_quiz_register'),
    path('autocad-register', views.autocad_register,name='autocad_register'),
    path('floating-concrete-register', views.floatingboat_register,name='floatingboat_register'),
    path('group-discussion-register', views.gd_register,name='gd_register'),
    path('b-plan-register', views.bplan_register,name='bplan_register'),


]
