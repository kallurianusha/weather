from django.shortcuts import render

import requests
def weather(request):
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5e111b026977db152b5857df21ce06dd"
        
        x = requests.get(url)
        y = x.json()
        context = {
            'c_name' : f"City_name:{y['name']}",
            'Temperature': f"Temperature: {y['main']['temp']} F",
            'Pressure': f"Pressure: {y['main']['pressure']}",
            'Humidity': f"Humidity: {y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
        }

        return render(request, 'index.html', context)
    return render(request, 'index.html')