import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import RegistrationPage from "./pages/RegistrationPage";
import LogInPage from "./pages/LogInPage";
import ProfilePage from "./pages/ProfilePage"; // Import ProfilePage
import { getInfo } from "./utilities";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    loader: getInfo,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "/register/",
        element: <RegistrationPage />,
      },
      {
        path: "/login/",
        element: <LogInPage />,
      },
      {
        path: "/profile/",
        element: <ProfilePage />, // Add ProfilePage route
      },
    ],
  },
]);

export default router;