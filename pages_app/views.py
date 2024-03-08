from django.shortcuts import render

# Create your views here.
weekdays_by_dayname = {
    'Dushanba': ['Dushanba','Понедельник','Monday','Lundi','Lunes'],
    'Seshanba': ['Seshanba','Вторник','Tuesday','Mardi','Martes'],
    'Chorshanba':['Chorshanba','Среда','Wednesday','Mercredi','Miércoles'],
    'Payshanba': ['Payshanba','Четверг','Thursday','Jeudi','Jueves'],
    'Juma': ['Juma','Пятница','Friday','Vendredi','Viernes'],
    'Shanba': ['Shanba','Суббота','Saturday','Samedi','Sábado'],
    'Yakshanba': ['Yakshanba','Воскресенье','Sunday','Dimanche','Domingo']
}
weekdays_by_lang = {
    'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
    'ru': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
    'eng': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'fr': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'is': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
}

# functions for views  


languages=['Uzbekcha','Ruscha','Inglizcha', 'Fransuzcha','Ispancha']
def index(request):
    global weekdays_by_dayname
    return render(request,template_name='index.html',context={'all_days': weekdays_by_dayname,'languages': languages})
def uz(request):
    global weekdays_by_lang
    return render(request, template_name='uz.html', context={'names':weekdays_by_lang.get("uz")})
def eng(request):
    global weekdays_by_lang
    return render(request, template_name='eng.html', context={'names':weekdays_by_lang.get("eng")})
def ru(request):
    global weekdays_by_lang
    return render(request, template_name='ru.html', context={'names':weekdays_by_lang.get("ru")})