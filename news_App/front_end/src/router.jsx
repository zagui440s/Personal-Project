import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import RegistrationPage from "./pages/RegistrationPage";
import LogInPage from "./pages/LogInPage";
import ProfilePage from "./pages/ProfilePage"; // Import ProfilePage
import ArticlesPage from "./pages/ArticlesPage"; // Import ArticlesPage
import { getInfo } from "./utilities";
import SavedArticlesPage from "./pages/SavedArticlesPage";

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
      {
        path: "/articles/",
        element: <ArticlesPage />, // Add ArticlesPage route
      },
      {
        path: "/favorite-articles/",
        element: <SavedArticlesPage />, // Add ArticlesPage route
      },
    ],
  },
]);

export default router;