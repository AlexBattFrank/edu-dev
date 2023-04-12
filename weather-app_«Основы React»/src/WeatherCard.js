import React from "react";

const WeatherCard = ({ data, forecastType }) => {
  const formatDate = (timestamp) => {
    const date = new Date(timestamp * 1000);
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
  };

  const renderWeatherData = () => {
    if (forecastType === "now") {
      return (
        <div>
          <p>Temperature: {data.main.temp}°C</p>
          <p>Humidity: {data.main.humidity}%</p>
          <p>Wind: {data.wind.speed} m/s {data.wind.deg}°</p>
          <p>Pressure: {data.main.pressure} gPa</p>
        </div>
      );
    } else {
      return data.list.map((item) => (
        <div key={item.dt}>
          <h4>{formatDate(item.dt)}</h4>
          <p>Temperature: {item.main.temp}°C</p>
          <p>Humidity: {item.main.humidity}%</p>
          <p>Wind: {item.wind.speed} m/s {item.wind.deg}°</p>
          <p>Pressure: {item.main.pressure} gPa</p>
        </div>
      ));
    }
  };

  return (
    <div>
      <h3>{data.city?.name || data.name}</h3>
      {renderWeatherData()}
    </div>
  );
};

export default WeatherCard;
