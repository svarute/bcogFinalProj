import pytest
from project import read_weather_data, animate_temperature_graph

#Test read_weather_data function
def test_read_weather_data():
    # Define a sample CSV data as a string
    sample_csv_data = """Place,Temperature (9am),Temperature (12pm),Temperature (3pm),Weather
                        New York,15,20,18,Sunny
                        New York,16,22,20,Partly Cloudy
                        New York,18,23,22,Rainy"""

    #Create a temporary CSV file using the sample data
    with open('temp_weather_data.csv', 'w') as file:
        file.write(sample_csv_data)

    #Test reading the data from the temporary CSV file
    weather_data = read_weather_data('temp_weather_data.csv')

    #Remove whitespace
    stripped_keys = [key.strip() for key in weather_data.keys()]
    #Assert we see what is expected
    assert len(weather_data) == 1
    assert stripped_keys == ['New York']

#Test read_weather_data function with multiple places
def test_read_weather_data_multiple_places():
    # Define a sample CSV data with multiple places
    sample_csv_data = """Place,Temperature (9am),Temperature (12pm),Temperature (3pm),Weather
                        New York,15,20,18,Sunny
                        Chicago,13,18,17,Partly Cloudy
                        Paris,21,26,24,Partly Cloudy"""

    #Create a temporary CSV file using the sample data
    with open('temp_weather_data_multiple.csv', 'w') as file:
        file.write(sample_csv_data)

    #test reading the data from file
    weather_data = read_weather_data('temp_weather_data_multiple.csv')

    #remove the whitespace
    stripped_keys = [key.strip() for key in weather_data.keys()]

    #see if it is as expected
    assert len(weather_data) == 3
    assert stripped_keys == ['New York', 'Chicago', 'Paris']

#Test animate_temperature_graph function
def test_animate_temperature_graph():
    # Define a sample weather data dictionary
    sample_weather_data = {'New York': {'temperatures': [(15, 20, 18), (16, 22, 20), (18, 23, 22)],
                                        'weather': ['Sunny', 'Partly Cloudy', 'Rainy']}}
    
    #Test the function with the sample weather data
    #testing the animation process
    animate_temperature_graph(sample_weather_data, 'New York')
    # this is a visual test -- so look at it


# Run the tests
if __name__ == "__main__":
    pytest.main()
