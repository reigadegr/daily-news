// 新闻数据类型定义

export interface NewsItem {
  title: string;
  url: string;
  image?: string;
  source?: string;
  category?: string;
  summary?: string;
  published_at?: string;
}

export interface NewsCategory {
  id: string;
  name: string;
  news: NewsItem[];
}

export interface NewsData {
  date: string;
  categories: NewsCategory[];
}

export interface DailyNewsResponse {
  date: string;
  content: string;
  categories: {
    时政: NewsItem[];
    经济: NewsItem[];
    国际: NewsItem[];
    科技: NewsItem[];
    社会: NewsItem[];
  };
}