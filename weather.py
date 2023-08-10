import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main_data = data["main"]
        weather_info = data["weather"][0]
        weather_description = weather_info["description"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        
        return weather_description, temperature, humidity
    else:
        return None, None, None

def show_weather():
    city_name = entry_city.get()
    if city_name:
        weather_description, temperature, humidity = get_weather_data(api_key="00f8649c9e333e69cc1bda9b6d9ce75f", city_name=city_name)
        if weather_description and temperature and humidity:
            result_text.set(f"Weather in {city_name}: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
        else:
            messagebox.showerror("Error", f"City '{city_name}' not found or API key is invalid.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

root = tk.Tk()
root.title("My Weather App")
root.geometry("400x200")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_city = tk.Label(frame, text="Enter city name:")
label_city.grid(row=0, column=0, sticky="w")

entry_city = tk.Entry(frame, width=30)
entry_city.grid(row=0, column=1)

button_get_weather = tk.Button(frame, text="Get Weather", command=show_weather)
button_get_weather.grid(row=1, column=0, columnspan=2)

result_text = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_text)
label_result.grid(row=2, column=0, columnspan=2)

root.mainloop()
