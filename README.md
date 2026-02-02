# 热门项目汇总 - GitHub Pages

> 自动收集 GitHub, Gitee, GitCode, AtomicGit 等平台的热门好玩项目，每日更新

## 📖 在线阅读

- **GitHub Pages**: https://reigadegr.github.io/daily-news/
- **GitHub 仓库**: https://github.com/reigadegr/daily-news

## ✨ 特性

- ⏰ **每日更新** - 自动收集最新热门项目
- 🌐 **多平台覆盖** - GitHub, Gitee, GitCode, AtomicGit
- 🔥 **智能筛选** - 按星标、活跃度等指标筛选优质项目
- 🗂️ **结构清晰** - 按平台、年份、月份、日期组织
- 🔍 **全文搜索** - 支持项目名称、描述、标签搜索
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
│   └── projects/          # 项目数据
│       ├── github/        # GitHub 热门项目
│       │   └── 2026/      # 按年份分类
│       │       └── 02/    # 按月份分类
│       │           └── 02.md  # 每日项目
│       ├── gitee/         # Gitee 热门项目
│       ├── gitcode/       # GitCode 热门项目
│       └── atomicgit/     # AtomicGit 热门项目
└── book.toml              # mdbook 配置
```

## 🔄 更新频率

- **频率**: 每日一次
- **时间**: 每天早上 09:00 (北京时间)
- **时区**: Asia/Shanghai

## 📊 项目来源

热门项目来源于以下主流代码托管平台：

- **GitHub** - 全球最大的开源社区
  - 每日/每周/每月 Trending
  - 按编程语言分类
  - AI 智能推荐

- **Gitee** - 中国最大的代码托管平台
  - GVP (Gitee Most Valuable Project)
  - 热门项目排行榜
  - 开源中国推荐

- **GitCode** - CSDN 代码托管平台
  - 热门项目推荐
  - 技术栈分类
  - 中文项目优先

- **AtomicGit** - 新兴代码托管平台
  - 创新项目展示
  - 技术前沿项目

## 🎯 项目分类

### 按编程语言
- Python
- JavaScript/TypeScript
- Java
- Go
- Rust
- C/C++
- 更多...

### 按应用领域
- 🤖 AI/机器学习
- 🌐 Web 开发
- 📱 移动应用
- 🔧 工具/库
- 🎮 游戏开发
- 🔐 安全/区块链
- 📊 数据科学
- 更多...

### 按热度指标
- ⭐ Stars 数量
- 🔄 Forks 数量
- 📈 增长趋势
- 🔥 活跃度

## 🛠️ 技术栈

- **mdBook** - 静态网站生成工具
- **GitHub Actions** - 自动构建和部署
- **GitHub Pages** - 静态网站托管
- **Python** - 项目爬虫脚本
- **requests** - HTTP 请求库

## 🚀 本地运行

### 前置要求

1. 安装 Rust 和 Cargo
2. 安装 mdBook:
   ```bash
   cargo install mdbook
   ```
3. 安装 Python 依赖:
   ```bash
   pip install requests
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

## 📝 手动运行项目收集

```bash
cd ~/project/daily-news
python3 ~/.openclaw/workspace/hot_projects_scraper.py
```

## 📊 数据格式

每个项目的数据包含：

```json
{
  "name": "项目名称",
  "author": "作者",
  "description": "项目描述",
  "url": "项目链接",
  "stars": 9999,
  "language": "Python",
  "tags": ["热门", "AI"],
  "forks": 1234
}
```

## 🔍 搜索技巧

- **按语言搜索**: `Python`, `JavaScript`, `Go`
- **按标签搜索**: `AI`, `Web`, `工具`
- **按作者搜索**: `facebook`, `google`, `microsoft`
- **组合搜索**: `Python AI`

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

如果你发现了有趣的项目，欢迎推荐！

## 📄 许可证

MIT License

## 🙏 致谢

感谢以下平台提供的 API 和数据：
- GitHub
- Gitee
- GitCode
- AtomicGit

---

*本项目使用 [OpenClaw](https://github.com/openclaw/openclaw) 自动化工具构建*
