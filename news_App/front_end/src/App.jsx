import { useEffect, useState } from "react";
import "./App.css";
import { Outlet, useLoaderData, useLocation, useNavigate } from "react-router-dom";
import NavBar from "./components/NavBar";


function App() {

  const [user, setUser] = useState(useLoaderData());
  const navigate = useNavigate()
  const location = useLocation()


  useEffect(()=>{
    let nullUserUrls = ['/register/'];
    let isAllowed = nullUserUrls.includes(location.pathname)
    if(user && isAllowed){
      navigate("/")
    }
    else if (!user && !isAllowed){
      navigate("/register/")
    }
  }, [location.pathname, user])

  return (
    <>
      <Outlet context={{ user, setUser }} />
      <NavBar user={user} setUser={setUser} />
      <h3>Welcome {user?.email && user.email}</h3>
      <h5>Welcome {user?.user_location.latitude}</h5>
      <h5>Welcome {user?.user_location.longitude}</h5>
    </>
  );
}

export default App;