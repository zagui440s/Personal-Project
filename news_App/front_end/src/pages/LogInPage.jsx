import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { userRegistration } from "../utilities";

const LogInPage = () => {
  const navigate = useNavigate(); // Initialize navigate function
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(""); // State to hold error message

  const handleSubmit = async (e) => {
    e.preventDefault();
    let formData = {
      email: email,
      password: password,
      registration: false, // Ensure login endpoint is used
    };
    
    // Attempt to log in
    const user = await userRegistration(formData);
    
    if (user) {
      // If successful, redirect to home page or dashboard
      navigate("/");
    } else {
      // If login fails, set the error message
      setError("Invalid email or password. Please try again.");
    }
  };

  return (
    <>
      <h1>Log In</h1>
      {error && <p style={{ color: "red" }}>{error}</p>} {/* Display error message */}
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            type="email"
            placeholder="Enter email"
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            placeholder="Password"
          />
        </Form.Group>
        
        <Button variant="primary" type="submit">
          Log In
        </Button>
      </Form>
    </>
  );
};

export default LogInPage;
