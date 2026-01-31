# 每日新闻汇总 - GitHub Pages

> 自动获取中国大陆各大新闻网站最新新闻，每小时更新一次

## 📖 在线阅读

- **GitHub Pages**: https://reigadegr.github.io/daily-news/
- **GitHub 仓库**: https://github.com/reigadegr/daily-news

## ✨ 特性

- ⏰ **每小时更新** - 自动获取最新新闻
- 🗂️ **结构清晰** - 按年份、月份、日期组织
- 🔍 **全文搜索** - 支持中文搜索
- 📱 **响应式设计** - 完美适配各种设备
- 🚀 **自动部署** - 使用 GitHub Actions 自动构建部署

## 📁 目录结构

```
daily-news/
├── .github/workflows/    # GitHub Actions 工作流
├── src/                   # mdbook 源文件
│   ├── SUMMARY.md         # 目录索引
│   ├── README.md          # 首页
│   ├── ABOUT.md           # 使用说明
│   └── 2026/              # 按年份分类
│       └── 01/            # 按月份分类
│           └── 31.md      # 每日新闻
└── book.toml              # mdbook 配置
```

## 🔄 更新频率

- **频率**: 每小时一次
- **时间**: 每小时的整点 (如 09:00, 10:00, 11:00...)
- **时区**: 北京时间 (Asia/Shanghai)

## 📰 新闻来源

新闻来源于以下中国大陆主流新闻网站：

- 澎湃新闻 (https://www.thepaper.cn)
- 央视新闻 (https://news.cctv.com)
- 人民网 (http://www.people.com.cn)
- 新华网 (https://www.xinhuanet.com)
- 环球网 (https://www.huanqiu.com)
- 网易新闻 (https://news.163.com)
- 等等

## 🛠️ 技术栈

- **mdBook** - 静态网站生成工具
- **GitHub Actions** - 自动构建和部署
- **GitHub Pages** - 静态网站托管
- **Python** - 新闻爬虫脚本

## 🚀 本地运行

### 前置要求

1. 安装 Rust 和 Cargo
2. 安装 mdBook:
   ```bash
   cargo install mdbook
   ```

### 构建网站

```bash
cd ~/project/daily-news
mdbook build
```

### 本地预览

```bash
cd ~/project/daily-news
mdbook serve
```

然后访问 http://localhost:3000

## 📝 手动运行新闻爬虫

```bash
cd ~/project/daily-news
python3 ~/.openclaw/workspace/hourly_news_scraper.py
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

*本项目使用 [OpenClaw](https://github.com/openclaw/openclaw) 自动化工具构建*
