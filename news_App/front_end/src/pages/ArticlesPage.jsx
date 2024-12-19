import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ArticlesPage = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchArticles = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('No token found');
        return;
      }
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/articles/articles/', {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        console.log('Response data:', response.data); // Log the response data
        setArticles(response.data);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, []);

  return (
    <div>
      <h2>Articles</h2>
      <ul>
        {articles.map(article => (
          <li key={article.id}>
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">Read more</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ArticlesPage;