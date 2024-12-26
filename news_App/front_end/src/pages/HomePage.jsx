import React, { useEffect, useState } from "react";
import axios from "axios";

const HomePage = () => {
  const [location, setLocation] = useState(null); // State to store location
  const [loading, setLoading] = useState(true);  // State to manage loading status
  const [error, setError] = useState("");        // State to manage errors

  useEffect(() => {
    const fetchLocation = async () => {
      try {
        // Get the token from localStorage
        const token = localStorage.getItem("token");

        // If no token is present, the user isn't logged in
        if (!token) {
          setError("You must be logged in to view location data.");
          setLoading(false);
          return;
        }

        // Make the API call with the token in the Authorization header
        const response = await axios.get("http://127.0.0.1:8000/api/v1/users/info/", {
          headers: {
            Authorization: `Token ${token}`, // Pass token here
          },
        });

        setLocation(response.data); // Save location data
        setLoading(false);
      } catch (err) {
        console.error("Error fetching location:", err);
        setError("Could not fetch location data.");
        setLoading(false);
      }
    };

    fetchLocation();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
    <div>
      <h1>Home Page, Welcome to the Daily Business</h1>
      <h3>The one stop shop for all business news related to your country</h3>
    </div>
  );
};

export default HomePage;
