import type { NewsData, NewsItem } from '../types/news';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:3000';
const GITHUB_RAW_BASE = 'https://raw.githubusercontent.com/reigadegr/daily-news/main/src';

class NewsService {
  async getDailyNews(year: number, month: number, day: number): Promise<NewsData> {
    const dateStr = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    
    try {
      // 首先尝试从 API 获取
      const response = await fetch(`${API_BASE_URL}/api/news/${dateStr}`);
      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.warn('API request failed, falling back to GitHub:', error);
    }
    
    // 如果 API 失败，从 GitHub 获取
    return this.getNewsFromGitHub(year, month, day);
  }

  async getNewsFromGitHub(year: number, month: number, day: number): Promise<NewsData> {
    const dateStr = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    const url = `${GITHUB_RAW_BASE}/${year}/${String(month).padStart(2, '0')}/${String(day).padStart(2, '0')}.md`;
    
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Failed to fetch news from GitHub: ${response.statusText}`);
      }
      
      const content = await response.text();
      return this.parseMarkdownContent(content, dateStr);
    } catch (error) {
      console.error('Failed to fetch news from GitHub:', error);
      // 返回空数据结构
      return {
        date: dateStr,
        categories: [
          { id: 'politics', name: '时政新闻', news: [] },
          { id: 'economy', name: '经济新闻', news: [] },
          { id: 'international', name: '国际新闻', news: [] },
          { id: 'tech', name: '科技新闻', news: [] },
          { id: 'society', name: '社会新闻', news: [] },
        ]
      };
    }
  }

  private parseMarkdownContent(markdown: string, dateStr: string): NewsData {
    const categories = [
      { id: 'politics', name: '时政新闻', news: this.extractNewsItems(markdown, '时政新闻') },
      { id: 'economy', name: '经济新闻', news: this.extractNewsItems(markdown, '经济新闻') },
      { id: 'international', name: '国际新闻', news: this.extractNewsItems(markdown, '国际新闻') },
      { id: 'tech', name: '科技新闻', news: this.extractNewsItems(markdown, '科技新闻') },
      { id: 'society', name: '社会新闻', news: this.extractNewsItems(markdown, '社会新闻') },
    ];

    return {
      date: dateStr,
      categories,
    };
  }

  private extractNewsItems(markdown: string, categoryName: string): NewsItem[] {
    const items: NewsItem[] = [];
    
    // 查找分类部分
    const categoryPattern = new RegExp(`##\\s*${categoryName}[\\s\\S]*?(?=##|$)`, 'i');
    const categoryMatch = markdown.match(categoryPattern);
    
    if (!categoryMatch) return items;
    
    const categoryContent = categoryMatch[0];
    
    // 提取新闻项（简化版，实际需要更复杂的解析）
    const titlePattern = /###\s+([^\n]+)/g;
    let titleMatch;
    
    while ((titleMatch = titlePattern.exec(categoryContent)) !== null) {
      const title = titleMatch[1].trim();
      
      // 查找来源
      const sourceMatch = categoryContent.substring(titleMatch.index).match(/\*\*来源：\*\*\s*([^\n]+)/);
      const source = sourceMatch ? sourceMatch[1].trim() : '未知来源';
      
      // 查找链接
      const linkMatch = categoryContent.substring(titleMatch.index).match(/\[阅读全文\]\(([^)]+)\)/);
      const url = linkMatch ? linkMatch[1] : '';
      
      // 查找图片
      const imageMatch = categoryContent.substring(titleMatch.index).match(/!\[新闻图片\]\(([^)]+)\)/);
      const image = imageMatch ? imageMatch[1] : '';
      
      items.push({
        title,
        url,
        image,
        source,
        category: categoryName,
      });
    }
    
    return items;
  }

  async getAvailableDates(): Promise<string[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/dates`);
      if (response.ok) {
        return await response.json();
      }
    } catch (error) {
      console.warn('Failed to fetch available dates:', error);
    }
    
    // 返回最近的日期
    const dates: string[] = [];
    const today = new Date();
    for (let i = 0; i < 7; i++) {
      const date = new Date(today);
      date.setDate(date.getDate() - i);
      dates.push(date.toISOString().split('T')[0]);
    }
    return dates;
  }
}

export default new NewsService();