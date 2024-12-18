import React from 'react';
import LocationSelector from './LocationSelector';

const LocationInfo = ({ user, selectedLocation, setSelectedLocation }) => {
  return (
    <div>
      <h5>City: {user?.user_location?.city}</h5>
      <h5>Region: {user?.user_location?.region}</h5>
      <h5>Country: {user?.user_location?.country}</h5>
      <h5>Current Latitude: {user?.user_location?.latitude}</h5>
      <h5>Current Longitude: {user?.user_location?.longitude}</h5>
      {/* <h5>ID: {user?.id}</h5>
      <h5>Last Login: {user?.last_login ? user.last_login : "Never"}</h5> */}
      <LocationSelector selectedLocation={selectedLocation} setSelectedLocation={setSelectedLocation} />
    </div>
  );
};

export default LocationInfo;