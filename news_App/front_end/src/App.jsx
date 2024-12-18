import { useEffect, useState } from "react";
import { Outlet, useLoaderData, useLocation, useNavigate } from "react-router-dom";
import NavBar from "./components/NavBar";
import LocationInfo from "./components/LocationInfo"; // Import LocationInfo
import "./App.css"; // Import the CSS file

function App() {
  const [user, setUser] = useState(useLoaderData());
  const [selectedLocation, setSelectedLocation] = useState(user?.user_location?.country || 'US');
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let nullUserUrls = ['/register/'];
    let isAllowed = nullUserUrls.includes(location.pathname);
    if (user && isAllowed) {
      navigate("/");
    } else if (!user && !isAllowed) {
      navigate("/register/");
    }
  }, [location.pathname, user, navigate]);

  return (
    <>
      <Outlet context={{ user, setUser }} />
      <NavBar user={user} setUser={setUser} />
      <div className="container left-align">
        <h3>Welcome {user?.email}</h3>
        <LocationInfo user={user} selectedLocation={selectedLocation} setSelectedLocation={setSelectedLocation} />
      </div>
    </>
  );
}

export default App;