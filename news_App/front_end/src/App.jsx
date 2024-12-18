import { useEffect, useState } from "react";
import "./App.css";
import { Outlet, useLoaderData, useLocation, useNavigate } from "react-router-dom";
import NavBar from "./components/NavBar";

function App() {
  const [user, setUser] = useState(useLoaderData());
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
      <h3>Welcome {user?.email}</h3>
      <h5>City: {user?.user_location?.city}</h5>
      <h5>Region: {user?.user_location?.region}</h5>
      <h5>Country: {user?.user_location?.country}</h5>
      <h5>Current Latitude: {user?.user_location?.latitude}</h5>
      <h5>Current Longitude: {user?.user_location?.longitude}</h5>
      <h5>ID: {user?.id}</h5>
      <h5>Last Login: {user?.last_login ? user.last_login : "Never"}</h5>
    </>
  );
}

export default App;