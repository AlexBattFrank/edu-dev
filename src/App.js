import React, { useState } from 'react';
import './App.css';
import axios from 'axios';
import CityInput from './components/CityInput';
import TimeInterval from './components/TimeInterval';
import WeatherInfo from './components/WeatherInfo';

const API_KEY = '8d38130928e33b7e0bac55fae8658a2b';

function App() {
  const [city, setCity] = useState('');
  const [interval, setInterval] = useState('');
  const [weatherData, setWeatherData] = useState(null);
  const [format, setFormat] = useState('text');

  const fetchWeatherData = async () => {
    const apiEndpoint = interval === 'current'
      ? `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`
      : `https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&appid=${API_KEY}`;

    try {
      const response = await axios.get(apiEndpoint);

      if (interval === 'current') {
        setWeatherData(response.data.main);
      } else {
        // Обработка прогноза на 5 дней
      }
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  const handleCitySelect = (selectedCity) => {
    setCity(selectedCity);
  };

  const handleIntervalSelect = (selectedInterval) => {
    setInterval(selectedInterval);
    fetchWeatherData().then(r => {});
  };

  return (
    <div className="App">
      <h1>Get Weather Forecast for Selected City</h1>
      <CityInput onCitySelect={handleCitySelect} />
      <TimeInterval onIntervalSelect={handleIntervalSelect} />
      <WeatherInfo weatherData={weatherData} format={format} />
    </div>
  );
}

export default App;
