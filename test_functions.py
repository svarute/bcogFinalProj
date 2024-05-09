import pytest
from project import read_weather_data, draw_temperature_graph

# Test read_weather_data function
def test_read_weather_data():
    # Define a sample CSV data as a string
    sample_csv_data = """Place,Temperature (9am),Temperature (12pm),Temperature (3pm),Temperature (6pm),Weather
                        New York,15,20,18,22,Sunny
                        New York,16,22,20,24,Partly Cloudy
                        New York,18,23,22,25,Rainy"""

    # Create a temporary CSV file using the sample data
    with open('temp_weather_data.csv', 'w') as file:
        file.write(sample_csv_data)

    # Test reading the data from the temporary CSV file
    weather_data = read_weather_data('temp_weather_data.csv')

    # Remove whitespace
    stripped_keys = [key.strip() for key in weather_data.keys()]
    
    # Assert we see what is expected
    assert len(weather_data) == 1
    assert stripped_keys == ['New York']

# Test draw_temperature_graph function
def test_draw_temperature_graph():
    # Define a sample weather data dictionary
    sample_weather_data = {'New York': {'temperatures': [(15, 20, 18, 22), (16, 22, 20, 24), (18, 23, 22, 25)],
                                        'weather': ['Sunny', 'Partly Cloudy', 'Rainy']}}

    # Test the function with the sample weather data and temp threshold
    draw_temperature_graph(sample_weather_data, 'New York', 25)  # setting a temperature threshold of 25°F


# Test draw_temperature_graph function when place/city is not present in the data
def test_draw_temperature_graph_missing_place():
    # Define a sample weather data dictionary with missing place
    sample_weather_data = {'New York': {'temperatures': [(15, 20, 18, 22), (16, 22, 20, 24), (18, 23, 22, 25)],
                                        'weather': ['Sunny', 'Partly Cloudy', 'Rainy']}}

    # Test the function with a place that is not present in the weather data
    with pytest.raises(KeyError):
        draw_temperature_graph(sample_weather_data, 'Los Angeles', 25)  # place is non-existing so should fail

# Run the tests
if __name__ == "__main__":
    pytest.main()
