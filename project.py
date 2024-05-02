#Suhani Varute

import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *


#read csv data
def read_weather_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            place = row['Place']
            temp_9am_fahrenheit = int(row['Temperature (9am)'])
            temp_12pm_fahrenheit = int(row['Temperature (12pm)'])
            temp_3pm_fahrenheit = int(row['Temperature (3pm)'])
            weather = row['Weather']
            if place not in data:
                data[place] = {'temperatures': [], 'weather': []}
            data[place]['temperatures'].append((temp_9am_fahrenheit, temp_12pm_fahrenheit, temp_3pm_fahrenheit))
            data[place]['weather'].append(weather)
    return data

#animation
def animate_temperature_graph(data, place):
    if place not in data:
        print("Sorry, weather information for {} is not available.".format(place))
        return
    temperatures = data[place]['temperatures']
    times_of_day = ['9am', '12pm', '3pm']
    days = range(1, len(temperatures) + 1)

    fig, ax = plt.subplots(figsize=(10, 6))  #set the larger figure
    ax.set_facecolor('#E6E6FA')  

    # Define colors for the lines
    line_colors = ['#8A2BE2', '#32CD32', '#4169E1']  # Purple, green, and blue

    line_styles = ['-', '--', ':']  
    markers = ['o', 's', '^']  
    
    for i in range(len(times_of_day)):
        line, = ax.plot([], [], lw=2, linestyle=line_styles[i], color=line_colors[i], marker=markers[i], markersize=8)
    
    ax.set_xlabel('Time of Day') #axis label
    ax.set_ylabel('Temperature (°F)')
    ax.set_title('Temperature Trend Over 3 Days for {}'.format(place))
    ax.set_xlim(0, len(temperatures))
    ax.set_ylim(0, 100)
    ax.set_xticks(range(len(times_of_day)))  #setting axis ticks
    ax.set_xticklabels(times_of_day)  #Setting the custom tick labels for x-axis

    def init():
        for line in ax.lines:
            line.set_data([], [])
        return ax.lines

    def update(frame):
        for i, line in enumerate(ax.lines):
            x_data = list(range(len(temperatures)))
            y_data = [temps[frame] for temps in temperatures]  #Access temperature values for the current time in the day
            line.set_data(x_data, y_data)
            if i == frame:
                line.set_linestyle('--')
            else:
                line.set_linestyle('-')
        return ax.lines

    ani = FuncAnimation(fig, update, frames=len(times_of_day), init_func=init, blit=True)
    plt.show()


    def update(frame):
        for i, line in enumerate(ax.lines):
            x_data = list(range(len(temperatures)))
            y_data = [temps[frame] for temps in temperatures]  #Access temperature values for the current time in the day
            line.set_data(x_data, y_data)
            if i == frame:
                line.set_linestyle('--')
            else:
                line.set_linestyle('-')
        return ax.lines

    ani = FuncAnimation(fig, update, frames=len(times_of_day), init_func=init, blit=True)
    plt.show()


#welcome message and input for city selecting
def main():
    #read the weather data in csv
    file_path = 'weather_data.csv'
    weather_data = read_weather_data(file_path)
    
    #creating GUI window
    root = Tk()
    root.title("Weather App")
    root.geometry("800x600")  
    root.configure(bg='#E6E6FA') 
    
    #Function to animate graph when a city button is clicked
    def animate_graph(place):
        animate_temperature_graph(weather_data, place)

    # Welcome message
    Label(root, text="Welcome to the Weather App!", font=("Papyrus", 18), bg='#E6E6FA').pack(pady=8)

    Label(root, text="Choose a City to see it's weather", font=("Papyrus", 15), bg='#E6E6FA').pack(pady=20)


    #weather icons 
    weather_icons = {
        'Sunny': '☀️',
        'Partly Cloudy': '⛅',
        'Cloudy': '☁️',
        'Rainy': '🌧️'
    }

    #creating buttons for each city with customized styling and weather icons
    for place in weather_data.keys():
        weather_icon = weather_icons[weather_data[place]['weather'][0]]
        Button(root, text=f"{weather_icon} {place}", command=lambda p=place: animate_graph(p),
               font=("Papyrus", 16), padx=20, pady=10, relief=RAISED, bg='#8A2BE2', fg='purple').pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
