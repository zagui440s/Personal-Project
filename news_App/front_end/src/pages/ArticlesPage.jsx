import React, { useEffect, useState } from "react";
import axios from "axios";

const ArticlesPage = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/articles/fetch-articles/");
        setArticles(response.data); // No need to slice, backend already returns 3 articles
        setLoading(false);
      } catch (err) {
        console.error("Error fetching articles:", err);
        setError("Could not fetch articles.");
        setLoading(false);
      }
    };

    fetchArticles();
  }, []);

  const handleFavorite = async (article) => {
    try {
      const token = localStorage.getItem('token'); // Retrieve the token from local storage
      const articleData = {
        title: article.title,
        description: article.description,
        url: article.url,
        // Add any other fields that the backend expects
      };
      await axios.post("http://127.0.0.1:8000/api/v1/articles/saved-articles/", articleData, {
        headers: {
          Authorization: `Token ${token}` // Send the token in the Authorization header
        }
      });
      alert("Article saved to favorites!");
    } catch (err) {
      console.error("Error saving article:", err);
      setError("Could not save article.");
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
      <h2>Business Articles</h2>
      <ul>
        {articles.map((article, index) => (
          <li key={index}>
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">
              Read more
            </a>
            <button onClick={() => handleFavorite(article)}>Favorite</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ArticlesPage;