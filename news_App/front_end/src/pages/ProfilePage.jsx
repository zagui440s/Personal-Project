import React, { useState, useEffect } from 'react';
import { useOutletContext, useNavigate } from 'react-router-dom';
import LocationSelector from '../components/LocationSelector';
import LocationInfo from '../components/LocationInfo'; // Import LocationInfo
import axios from 'axios';
import '../App.css'; // Import the CSS file

const ProfilePage = () => {
  const { user, setUser, selectedLocation, setSelectedLocation } = useOutletContext();
  const navigate = useNavigate();
  const [bio, setBio] = useState(user?.bio || '');
  const [useDefaultLocation, setUseDefaultLocation] = useState(false); // State to toggle location choice
  const [city, setCity] = useState(user?.user_location?.city || '');
  const [region, setRegion] = useState(user?.user_location?.region || '');
  const [country, setCountry] = useState(user?.user_location?.country || '');
  const [latitude, setLatitude] = useState(user?.user_location?.latitude || '');
  const [longitude, setLongitude] = useState(user?.user_location?.longitude || '');

  useEffect(() => {
    if (useDefaultLocation) {
      // Fetch location data based on IP address
      const fetchLocation = async () => {
        try {
          const response = await axios.get('http://ip-api.com/json');
          if (response.status === 200) {
            const data = response.data;
            setCity(data.city);
            setRegion(data.regionName);
            setCountry(data.country);
            setLatitude(data.lat);
            setLongitude(data.lon);
          }
        } catch (error) {
          console.error('Error fetching location data:', error);
        }
      };
      fetchLocation();
    } else {
      // Clear the input fields when not using the default location
      setCity('');
      setRegion('');
      setCountry('');
      setLatitude('');
      setLongitude('');
    }
  }, [useDefaultLocation]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token'); // Retrieve the token from local storage
    try {
      const response = await axios.put('http://127.0.0.1:8000/api/v1/users/profile/', {
        bio,
        user_location: useDefaultLocation ? {
          city,
          region,
          country,
          latitude,
          longitude,
        } : {
          city,
          region,
          country,
          latitude,
          longitude,
        },
      }, {
        headers: {
          'Authorization': `Token ${token}`
        }
      });
      setUser(response.data);
      alert('Profile updated successfully');
    } catch (error) {
      console.error('Error updating profile:', error);
      alert('Failed to update profile');
    }
  };

  const handleDelete = async () => {
    const token = localStorage.getItem('token'); // Retrieve the token from local storage
    try {
      await axios.delete('http://127.0.0.1:8000/api/v1/users/profile/', {
        headers: {
          'Authorization': `Token ${token}` // Include the token in the headers
        }
      });
      setUser(null);
      alert('Profile deleted successfully');
      navigate('/register'); // Redirect to the registration page or any other page
    } catch (error) {
      console.error('Error deleting profile:', error);
      alert('Failed to delete profile');
    }
  };

  return (
    <div className="center-container">
      <div className="profile-box">
        <h2>Profile Page</h2>
        <p>{user?.email}</p>
        <p>Location: {city}, {region}, {country}</p>
        <p>Coordinates: {latitude}, {longitude}</p>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Bio:</label>
            <textarea value={bio} onChange={(e) => setBio(e.target.value)} />
          </div>
          <div>
            <label>
              <input
                type="checkbox"
                checked={useDefaultLocation}
                onChange={(e) => setUseDefaultLocation(e.target.checked)}
              />
              Use default location
            </label>
          </div>
          {useDefaultLocation ? (
            <LocationInfo user={{ user_location: { city, region, country, latitude, longitude } }} selectedLocation={selectedLocation} setSelectedLocation={setSelectedLocation} />
          ) : (
            <>
              <div>
                <label>City:</label>
                <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
              </div>
              <div>
                <label>Region:</label>
                <input type="text" value={region} onChange={(e) => setRegion(e.target.value)} />
              </div>
              <div>
                <label>Country:</label>
                <input type="text" value={country} onChange={(e) => setCountry(e.target.value)} />
              </div>
              <div>
                <label>Latitude:</label>
                <input type="text" value={latitude} onChange={(e) => setLatitude(e.target.value)} />
              </div>
              <div>
                <label>Longitude:</label>
                <input type="text" value={longitude} onChange={(e) => setLongitude(e.target.value)} />
              </div>
              <LocationSelector selectedLocation={selectedLocation} setSelectedLocation={setSelectedLocation} />
            </>
          )}
          <button type="submit">Update Profile</button>
        </form>
        <button onClick={handleDelete} className="delete">Delete Profile</button>
      </div>
    </div>
  );
};

export default ProfilePage;