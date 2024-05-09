#Suhani Varute

from tkinter import *
import csv
import matplotlib.pyplot as plt

# Read csv data
def read_weather_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            place = row['Place']
            temp_9am_fahrenheit = int(row['Temperature (9am)'])
            temp_12pm_fahrenheit = int(row['Temperature (12pm)'])
            temp_3pm_fahrenheit = int(row['Temperature (3pm)'])
            temp_6pm_fahrenheit = int(row['Temperature (6pm)'])

            weather = row['Weather']
            if place not in data:
                data[place] = {'temperatures': [], 'weather': []}

            # Appending temperatures for each day separately
            data[place]['temperatures'].append((temp_9am_fahrenheit, temp_12pm_fahrenheit, temp_3pm_fahrenheit, temp_6pm_fahrenheit))
            data[place]['weather'].append(weather)
    return data

# Draw temperature graph for a specific place
def draw_temperature_graph(data, place, temperature_threshold):

    if place not in data:
        print("Sorry, weather information for {} is not available.".format(place))
        raise KeyError("Weather information for {} is not available.".format(place))
        return
    
    temperatures = data[place]['temperatures']
    weather_days = len(temperatures)
    times_of_day = ['9am', '12pm', '3pm', '6pm']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#E6E6FA')  

    line_colors = ['#8A2BE2', '#32CD32', '#4169E1', '#FFA500']  
    line_styles = ['-', '--', ':', '-']  
    markers = ['o', 's', '^', 'D']  
    
    # Plot each day temperatures
    for day in range(weather_days):
        x_data = list(range(len(times_of_day)))
        y_data = [temperatures[day][i] for i in range(len(times_of_day))]

        line, = ax.plot(x_data, y_data, lw=2, linestyle=line_styles[day], color=line_colors[day], marker=markers[day], markersize=8, label=f"Day {day+1}")
        ax.annotate(f"{place}: Day {day+1}", xy=(x_data[0], y_data[0]), xytext=(x_data[0] + 0.2, y_data[0] + 2),
                     arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
        line.set_picker(5)  # Set picker for each line

    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Temperature (°F)')
    ax.set_title('Temperature Trend Over 3 Days for {}'.format(place))
    ax.set_xlim(0, len(times_of_day)-1)
    ax.set_ylim(0, 100)
    ax.set_xticks(range(len(times_of_day)))
    ax.set_xticklabels(times_of_day)
    ax.axhline(y=temperature_threshold, color='r', linestyle='--', label=f'Temperature Threshold: {temperature_threshold}°F')
    ax.legend()
    
    ax.text(0.1, temperature_threshold + 2, 'Anything above this is too hot for you', fontsize=10, color='red')

    def on_pick(event):
        if isinstance(event.artist, plt.Line2D):
            x_index = int(event.mouseevent.xdata)
            y_value = event.artist.get_ydata()[x_index]
            plt.gca().set_title(f"Temperature at {times_of_day[x_index]}: {y_value}°F")

    fig.canvas.mpl_connect('pick_event', on_pick)
    
    plt.show()


# Welcome message and input for city selecting
def main():
    file_path = 'weather_data.csv'
    weather_data = read_weather_data(file_path)
    
    root = Tk()
    root.title("Weather App")
    root.geometry("800x600")  
    root.configure(bg='#E6E6FA') 
    
    Label(root, text="Welcome to the Weather App!", font=("Papyrus", 18), bg='#E6E6FA').pack(pady=8)
    Label(root, text="Choose a City to see its weather", font=("Papyrus", 15), bg='#E6E6FA').pack(pady=20)

    # temperature threshold slider
    temperature_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Temperature Threshold (°F)", length=300)
    temperature_slider.pack(pady=10)
    temperature_slider.set(50)

    Label(root, text="Adjust the threshold to the temperature you are comfortable with", font=("Papyrus", 12), bg='#E6E6FA').pack()

    # symbols corresponding to different weather conditions
    weather_symbols = {
        'Sunny': '☀️',
        'Cloudy': '☁️',
        'Rainy': '🌧️',
        'Stormy': '⛈️',
        'Snowy': '❄️'
    }

    for place, weather_info in weather_data.items():
        # Get the weather for the first day
        current_weather = weather_info['weather'][0]
        # Select appropriate symbol for the current weather
        weather_symbol = weather_symbols.get(current_weather, '❓')

        # Add buttons with weather symbols for each city
        Button(root, text=f"{place} {weather_symbol}", 
               command=lambda p=place: draw_temperature_graph(weather_data, p, temperature_slider.get()),
               font=("Papyrus", 16), padx=20, pady=10, relief=RAISED, 
               bg='#8A2BE2', fg='purple').pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
