import tkinter as tk
from tkinter import font
import requests

# - 42.16
HEIGHT = 700
WIDTH = 800

# - Extremely helpful: https://www.tutorialspoint.com/python/python_gui_programming.htm
# - Video: https://youtu.be/D8-snVfekto
# - APIs on any sort of site or server is a way to communicate with the server. Get and push info.
# - api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test_function(entry):
    print("This is the entry!", entry)

# - 368d62b8a2988c73fd0e22a50f52f111

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (F) %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information.'
    return final_str

def get_weather(city):
    weather_key = '368d62b8a2988c73fd0e22a50f52f111'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather = response.json()

    label['text'] = format_response(weather)

    print(weather['name']) # - name object
    print(weather['weather'][0]['description']) # - First entry, description of weather object
    print(weather['main']['temp']) # - temp of main object.

# - Now, we want to format these values.

root = tk.Tk()

# - Everything between this and mainloop is the app

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # - This defines us a bigger window. Decided to add b/c below.*
canvas.pack() # - Puts the canvas into play. Gives a bigger window.

background_image = tk.PhotoImage(file='bg.png') # - Assigns a variable to the image
background_label = tk.Label(root, image=background_image) # - Assigns a label to the root with the background image.
background_label.place(relwidth=1, relheight=1) # - Spans the document with the background image

frame = tk.Frame(root, bg='blue', bd=5) # - Borderspace is 5
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get())) # - Lambda defined at run time. Temp stored in mem then disposed of.
button.place(relx=0.7, relheight=1, relwidth=0.3) # - Space betw entry and button.

lower_frame = tk.Frame(root, bg='blue', bd=10) # - Borderspace is 10
lower_frame.place(relx=0.5, rely=0.25, relwidth = 0.75, relheight=0.6, anchor='n') # Starts quarter way down. Height bigger. Anchor north to center.

label = tk.Label(lower_frame, font=('Courier', 16))
label.place(relwidth=1 , relheight=1)

print(tk.font.families())

root.mainloop()