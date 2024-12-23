import React, { useEffect, useState } from "react";
import axios from "axios";
import "../App.css"; // Import the CSS file

const ArticlesPage = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [missingArticle, setMissingArticle] = useState(null);
  const [favoritedArticles, setFavoritedArticles] = useState(new Set()); // State to track favorited articles

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/articles/fetch-articles/");
        setArticles(response.data); // No need to slice, backend already returns 10 articles
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
      if (!article.title || !article.description || !article.url) {
        throw new Error("Missing required article fields");
      }
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
      setFavoritedArticles(new Set(favoritedArticles).add(article.url)); // Mark article as favorited
      alert("Article saved to favorites!");
    } catch (err) {
      console.error("Error saving article:", err);
      if (err.message === "Missing required article fields") {
        setMissingArticle(article);
      } else {
        setError("Could not save article.");
      }
    }
  };

  const handleDelete = async (article) => {
    try {
      const token = localStorage.getItem('token'); // Retrieve the token from local storage
      await axios.delete(`http://127.0.0.1:8000/api/v1/articles/saved-articles/${article.id}/`, {
        headers: {
          Authorization: `Token ${token}` // Send the token in the Authorization header
        }
      });
      setArticles(articles.filter(a => a.id !== article.id));
      setMissingArticle(null);
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
      <h2>Business Articles</h2>
      <ul>
        {articles.map((article, index) => (
          <li key={index} className="article-container">
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            {missingArticle && missingArticle.url === article.url ? (
              <div>
                <p style={{ color: "red" }}>Article doesn't exist.</p>
                <button onClick={() => handleDelete(article)}>Delete</button>
              </div>
            ) : (
              <>
                <button
                  className="read-more-button"
                  onClick={() => window.open(article.url, "_blank", "noopener noreferrer")}
                >
                  Read more
                </button>
                <button
                  className={`favorite-button ${favoritedArticles.has(article.url) ? 'favorited' : ''}`}
                  onClick={() => handleFavorite(article)}
                  disabled={favoritedArticles.has(article.url)}
                >
                  {favoritedArticles.has(article.url) ? 'Favorited' : 'Favorite'}
                </button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ArticlesPage;