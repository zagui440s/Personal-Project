import { Link } from "react-router-dom";
import { signOut } from "../utilities";

const NavBar = ({ user, setUser }) => {
  const logOut = async () => {
    setUser(await signOut(user));
  };

  console.log("User state:", user); // Debugging output
  
  return (
    <ul style={{ display: "flex", justifyContent: "space-around" }}>
      {user ? (
        <>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/profile">Profile</Link> {/* Add Profile link */}
          </li>
          <li>
              <Link to="/articles/">Articles</Link> {/* Add Articles link */}
            </li>
            <li><Link to="/favorite-articles">Favorite Articles</Link></li> 
          <li>
            <button onClick={logOut}>Sign Out</button>
          </li>
        </>
      ) : (
        <>
          <li>
            <Link to="/register/">Register</Link>
          </li>
          <li>
            <Link to="/login/">Log In</Link>
          </li>
        </>
      )}
    </ul>
  );
};

export default NavBar;