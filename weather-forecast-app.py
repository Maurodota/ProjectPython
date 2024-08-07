import tkinter as tk
import requests

# Função para obter a previsão do tempo
def get_weather(city):
    api_key = 'your_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather = response.json()
    
    if weather.get('cod') != 200:
        return "City not found."
    
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    
    return f'Temperature: {temp}°C\nDescription: {desc}'

# Configurar interface gráfica
def show_weather():
    city = city_text.get()
    weather = get_weather(city)
    weather_label.config(text=weather)

root = tk.Tk()
root.title("Weather App")

city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()

weather_button = tk.Button(root, text="Get Weather", command=show_weather)
weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
