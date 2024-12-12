import { useEffect, useState } from "react";
import "./App.css";
import { Outlet, useLoaderData, useLocation, useNavigate } from "react-router-dom";
import NavBar from "./components/NavBar";


function App() {
  // const testConnection = async() => {
  //   let response = await axios.get("http://127.0.0.1:8000/")
  //   if (!response.data.connected){
  //     console.log("not communicating with server")
  //   }
  //   else{
  //     console.log("communication established with server")
  //   }
  // }

  // useEffect(()=>{
  //   testConnection()
  // }, [])

  // useEffect(() => {
  //   const grabUser = async () => {
  //     setUser(await getInfo());
  //   };
  //   grabUser();
  // }, []);

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
      <h1>Welcome {user && user}</h1>
      <NavBar user={user} setUser={setUser} />
      <Outlet context={{ user, setUser }} />
    </>
  );
}

export default App;