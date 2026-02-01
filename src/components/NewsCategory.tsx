import type { NewsCategory } from '../types/news';
import NewsCard from './NewsCard';
import './NewsCategory.css';

interface NewsCategoryProps {
  category: NewsCategory;
}

export default function NewsCategory({ category }: NewsCategoryProps) {
  return (
    <div className="news-category">
      <h2 className="category-title">{category.name}</h2>
      <div className="news-grid">
        {category.news.map((news, index) => (
          <NewsCard key={`${news.url}-${index}`} news={news} />
        ))}
      </div>
      {category.news.length === 0 && (
        <div className="empty-message">
          暂无{category.name}新闻
        </div>
      )}
    </div>
  );
}