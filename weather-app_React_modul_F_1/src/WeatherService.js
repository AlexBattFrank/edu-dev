import axios from "axios";

const API_KEY = "8d38130928e33b7e0bac55fae8658a2b";
const BASE_URL = "https://api.openweathermap.org";

export const fetchCityCoordinates = async (city) => {
  const response = await axios.get(
    `${BASE_URL}/geo/1.0/direct?q=${city}&limit=1&appid=${API_KEY}&mode=cors`
  );
  return response.data[0];
};

export const fetchWeatherData = async (lat, lon, forecastType) => {
  const exclude = forecastType === "current" ? "minutely,hourly,daily,alerts" : "current,minutely,hourly,alerts";
  const response = await axios.get(
    `${BASE_URL}/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=${exclude}&appid=${API_KEY}&units=metric`
  );
  return response.data;
};

export const fetchCityName = async (lat, lon) => {
  const response = await axios.get(
    `${BASE_URL}/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`
  );
  return response.data.name;
};
