import React from "react";

const WeatherInfo = ({ weatherData }) => {
  const { cityName, temperature, humidity, windSpeed, windDirection, pressure } = weatherData;

  return (
    <div className="weather-info">
        <p>
          {`City: ${cityName}\n`}
          {`Temperature: ${temperature}°C\n`}
          {`Humidity: ${humidity}%\n`}
          {`Wind: ${windSpeed} m/s, ${windDirection}\n`}
          {`Pressure: ${pressure} gPa`}
        </p>
    </div>
  );
};

export default WeatherInfo;
