import { useState, useEffect } from 'react';
import './App.css';
import NewsCategory from './components/NewsCategory';
import newsService from './services/newsService';
import type { NewsData } from './types/news';

function App() {
  const [newsData, setNewsData] = useState<NewsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedDate, setSelectedDate] = useState<string>(() => {
    const today = new Date();
    return today.toISOString().split('T')[0];
  });

  useEffect(() => {
    loadNews(selectedDate);
  }, [selectedDate]);

  const loadNews = async (date: string) => {
    setLoading(true);
    setError(null);
    
    try {
      const [year, month, day] = date.split('-').map(Number);
      const data = await newsService.getDailyNews(year, month, day);
      setNewsData(data);
    } catch (err) {
      setError('加载新闻失败，请稍后重试');
      console.error('Failed to load news:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedDate(event.target.value);
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="container">
          <h1 className="app-title">📰 每日新闻汇总</h1>
          <div className="date-selector">
            <label htmlFor="date-input">选择日期：</label>
            <input
              id="date-input"
              type="date"
              value={selectedDate}
              onChange={handleDateChange}
              max={new Date().toISOString().split('T')[0]}
              className="date-input"
            />
          </div>
        </div>
      </header>

      <main className="app-main">
        <div className="container">
          {loading && (
            <div className="loading">
              <div className="spinner"></div>
              <p>加载中...</p>
            </div>
          )}

          {error && (
            <div className="error">
              <p>⚠️ {error}</p>
              <button onClick={() => loadNews(selectedDate)} className="retry-button">
                重试
              </button>
            </div>
          )}

          {newsData && !loading && !error && (
            <>
              <div className="news-date-info">
                <h2>{newsData.date} 新闻</h2>
                <p className="total-news">
                  共 {newsData.categories.reduce((total, cat) => total + cat.news.length, 0)} 条新闻
                </p>
              </div>

              {newsData.categories.map((category) => (
                <NewsCategory key={category.id} category={category} />
              ))}
            </>
          )}
        </div>
      </main>

      <footer className="app-footer">
        <div className="container">
          <p>数据来源：澎湃新闻、网易新闻、央视新闻、新华网等</p>
          <p>© 2026 每日新闻汇总 | 基于 React + TypeScript + Vite 构建</p>
        </div>
      </footer>
    </div>
  );
}

export default App;