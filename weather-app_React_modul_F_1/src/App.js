import React, { useState } from "react";
import { fetchCityCoordinates, fetchWeatherData, fetchCityName } from './WeatherService';
import "./App.css";

function WeatherInfo({ data, weatherType }) {
  if (!data) {
    return null;
  }
  const current = data.current;
  const daily = data.daily;
  const cityName = data.timezone;


  if (weatherType === "current") {
    if (!current) {
      return null;
    }
    const { temp, humidity, weather } = current;
    const { description, icon } = weather[0];

    return (
      <div className="weather-info">
        <h2 className="weather-info-title">
          The Weather in {cityName} Now
        </h2>
        <h3>Temperature: {temp}°C</h3>
        <h3>Humidity: {humidity}%</h3>
        <h3>Description: {description}</h3>
        <img
          src={`https://openweathermap.org/img/wn/${icon}.png`}
          alt={description}
        />
      </div>
    );
  } else {
    if (!daily) {
      return null;
    }
    return (
      <div className="weather-info">
        <h2 className="weather-info-title">
          Next 5 days forecast for {cityName}
        </h2>
        {daily.slice(0, 5).map((day, index) => (
          <div key={index} className="weather-day">
            <h3>Day {index + 1}</h3>
            <h4>Temperature: {day.temp.day}°C</h4>
            <h4>Humidity: {day.humidity}%</h4>
            <h4>Description: {day.weather[0].description}</h4>
            <img
              src={`https://openweathermap.org/img/wn/${day.weather[0].icon}.png`}
              alt={day.weather[0].description}
            />
          </div>
        ))}
      </div>
    );
  }
}

function App() {
  const [city, setCity] = useState("");
  const [weatherType, setWeatherType] = useState("current");
  const [useGeolocation, setUseGeolocation] = useState(false);
  const [weatherData, setWeatherData] = useState(null);

  const getWeather = async () => {
    try {
      let lat, lon;

      if (useGeolocation) {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(async (position) => {
            lat = position.coords.latitude;
            lon = position.coords.longitude;

            const data = await fetchWeatherData(lat, lon, weatherType);
            const cityName = await fetchCityName(lat, lon);
            setWeatherData({ ...data, city: { name: cityName } });
          });
        } else {
          throw new Error("Geolocation is not supported by this browser.");
        }
      } else {
        const coordinates = await fetchCityCoordinates(city);
        lat = coordinates.lat;
        lon = coordinates.lon;

        const data = await fetchWeatherData(lat, lon, weatherType);
        const cityName = await fetchCityName(lat, lon);
        setWeatherData({ ...data, city: { name: cityName } });
      }
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div className="App">
      <header>Actual Weather Report</header>

      <div className="container">
        <input
          className="city-name"
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />

        <select
          className="now-next select"
          value={weatherType}
          onChange={(e) => setWeatherType(e.target.value)}
        >
          <option value="current">Now</option>
          <option value="forecast">Next 5 days</option>
        </select>

        <button className="get-weather-button" onClick={getWeather}>
          Get Weather
        </button>

        <label className="use-geolocation">
          <input
            type="checkbox"
            checked={useGeolocation}
            onChange={(e) => setUseGeolocation(e.target.checked)}
          />
          Use Geolocation
        </label>
      </div>

      <WeatherInfo data={weatherData} weatherType={weatherType} />

      <footer>(c) A. B.</footer>
    </div>
  );
}

export default App;

