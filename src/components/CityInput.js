import React from 'react';
import Select from 'react-select';

const CityInput = ({ onCitySelect }) => {
  const cities = [
    { value: 'Dublin', label: 'Dublin' },
    { value: 'London', label: 'London' },
    { value: 'Paris', label: 'Paris' },
    { value: 'Berlin', label: 'Berlin' },
    { value: 'Moscow', label: 'Moscow' },
  ];

  return (
    <div className="city-input">
      <Select
        options={cities}
        placeholder="Select a city"
        onChange={(selected) => onCitySelect(selected.value)}
      />
    </div>
  );
};

export default CityInput;
