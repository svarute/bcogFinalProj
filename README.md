# bcogFinalProj

Welcome to the Weather App Project. The goal of this project is to create a Python application that shows the user the weather information for a certain city when it has been retrieved from a csv file. 

Features:
- Provides weather conditions for the selected city (Sunny, Cloudy, Rainy, Snowy)
- Shows the weather for the past three days in visual form
- Displays the weather at specific times
- Users can select any city they would like to see
- Users can also set a threshold for their temperature comfort level

Users will interact with this application by being prompted to choose the name of the city they would like to know more about. The input data is processed as a string representing the name of the city. The app validates the input to ensure it matches one of the available cities that is in the weather data CSV file.

Dependencies:
- matplotlib is used for plotting temperature graphs
- tkinter is used for creating the graphical user interface that users can interact with (when they choose the city)
- pytest - I used this to run the test cases I made to make sure the app was functioning as expected

Usage:
1. download csv file
2. run project.py file
3. choose the city you want to see the weather for
4. then the app will display the requested information

File Structure:
- README.md: this file helps to provide an overview of the project for the users. It has the functionality, purpose, and file structure
- project.py: Contains the main logic of the weather app.
- test_functions.py: Contains all the test cases to ensure the app functions as is expected.
- weather_data.csv: Contains the data being used to show the weather data
