import React from 'react';

const LocationSelector = ({ selectedLocation, setSelectedLocation }) => {
  const countries = [
    { code: 'US', name: 'United States' },
    { code: 'CA', name: 'Canada' },
    { code: 'GB', name: 'United Kingdom' },
    { code: 'AU', name: 'Australia' },
  ];

  const handleChange = (event) => {
    setSelectedLocation(event.target.value);
  };

  return (
    <div>
      <label htmlFor="location">Choose a location:</label>
      <select id="location" value={selectedLocation} onChange={handleChange}>
        {countries.map((country) => (
          <option key={country.code} value={country.code}>
            {country.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default LocationSelector;