# Weather Forecast Dashboard

A simple weather forecast dashboard built using Flask and OpenWeatherMap API. This application allows users to enter a city name and view the current weather, including temperature, humidity, wind speed, and more.

## Features

- Get current weather for any city
- Displays temperature, humidity, wind speed, and weather description
- Map integration to show the location of the city on a map
- Converts time to local time for India (IST) or shows time based on the city timezone

## Requirements

- Python 3.x
- Flask
- requests
- pytz
- Leaflet (for map integration)

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/S-Rohith-Reddy/weather-dashboard.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-dashboard
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Get an API key from [OpenWeatherMap](https://openweathermap.org/). Replace `YOUR_API_KEY` in `weather_app.py` with your actual API key.

5. Run the Flask application:

    ```bash
    python weather_app.py
    ```

6. Open your browser and visit `http://127.0.0.1:5000/` to view the app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[S.Rohith Reddy](https://github.com/S-Rohith-Reddy)
