import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import RegistrationPage from "./pages/RegistrationPage";
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
    ],
  },
]);

export default router;