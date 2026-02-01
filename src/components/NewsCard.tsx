import type { NewsItem } from '../types/news';
import './NewsCard.css';

interface NewsCardProps {
  news: NewsItem;
}

export default function NewsCard({ news }: NewsCardProps) {
  return (
    <div className="news-card">
      {news.image && (
        <div className="news-card-image">
          <img src={news.image} alt={news.title} loading="lazy" />
        </div>
      )}
      <div className="news-card-content">
        <h3 className="news-card-title">
          {news.url ? (
            <a href={news.url} target="_blank" rel="noopener noreferrer">
              {news.title}
            </a>
          ) : (
            news.title
          )}
        </h3>
        <div className="news-card-meta">
          {news.source && <span className="news-source">{news.source}</span>}
          {news.published_at && (
            <span className="news-time">{news.published_at}</span>
          )}
        </div>
        {news.summary && (
          <p className="news-card-summary">{news.summary}</p>
        )}
      </div>
    </div>
  );
}