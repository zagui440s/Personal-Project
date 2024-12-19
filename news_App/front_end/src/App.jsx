import { useEffect, useState } from "react";
import { Outlet, useLoaderData, useLocation, useNavigate } from "react-router-dom";
import NavBar from "./components/NavBar";
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
      <NavBar user={user} setUser={setUser} />
      <div className="container left-align">
        <h3>Welcome {user?.email}</h3>
        <Outlet context={{ user, setUser, selectedLocation, setSelectedLocation }} />
      </div>
    </>
  );
}

export default App;