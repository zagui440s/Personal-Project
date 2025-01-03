import React, { useEffect, useState } from "react";
import axios from "axios";
import "../App.css"; // Import the CSS file

const SavedArticlesPage = () => {
  const [savedArticles, setSavedArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSavedArticles = async () => {
      try {
        const token = localStorage.getItem('token'); // Retrieve the token from local storage
        const response = await axios.get("http://127.0.0.1:8000/api/v1/articles/saved-articles/", {
          headers: {
            Authorization: `Token ${token}` // Send the token in the Authorization header
          }
        });
        setSavedArticles(response.data);
        setLoading(false);
      } catch (err) {
        console.error("Error fetching saved articles:", err);
        setError("Could not fetch saved articles.");
        setLoading(false);
      }
    };

    fetchSavedArticles();
  }, []);

  const handleDelete = async (id) => {
    try {
      const token = localStorage.getItem('token'); // Retrieve the token from local storage
      await axios.delete(`http://127.0.0.1:8000/api/v1/articles/saved-articles/${id}/`, {
        headers: {
          Authorization: `Token ${token}` // Send the token in the Authorization header
        }
      });
      setSavedArticles(savedArticles.filter(article => article.id !== id));
    } catch (err) {
      console.error("Error deleting article:", err);
      setError("Could not delete article.");
    }
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
    <div>
      <h2>Saved Articles</h2>
      <ul>
        {savedArticles.map((article, index) => (
          <li key={index} className="article-container">
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            <button
              className="read-more-button"
              onClick={() => window.open(article.url, "_blank", "noopener noreferrer")}
            >
              Read more
            </button>
            <button
              className="remove-article-button"
              onClick={() => handleDelete(article.id)}
            >
              Remove Article
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SavedArticlesPage;