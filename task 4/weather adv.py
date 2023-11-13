import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'cf45402b55cb605ab961ee6029dc2a2e'  # Replace with your OpenWeatherMap API key

def get_weather():
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the response contains valid data
        if data['cod'] != '404':
            # Extract relevant weather information
            main = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Update labels with weather information
            weather_label.config(text=f'Weather: {main} - {description}')
            temp_label.config(text=f'Temperature: {temperature}°C')
            humidity_label.config(text=f'Humidity: {humidity}%')
            wind_label.config(text=f'Wind Speed: {wind_speed} m/s')
        else:
            messagebox.showerror('Error', 'City not found. Please check your input.')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {e}')

# Create the main window
root = tk.Tk()
root.title('Weather App')

# Create input field and search button
city_label = tk.Label(root, text='City:')
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)
search_button = tk.Button(root, text='Search', command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Create labels to display weather information
weather_label = tk.Label(root, text='')
weather_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')
temp_label = tk.Label(root, text='')
temp_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w')
humidity_label = tk.Label(root, text='')
humidity_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w')
wind_label = tk.Label(root, text='')
wind_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w')

# Run the main event loop
root.mainloop()
