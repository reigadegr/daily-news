# 使用说明

## 如何浏览项目

1. 在左侧目录栏中选择平台（GitHub, Gitee, GitCode, AtomicGit）
2. 展开对应的年份
3. 展开对应的月份
4. 点击日期查看当天的热门项目

## 搜索项目

使用页面顶部的搜索框（🔍 图标）可以搜索项目：
- 按项目名称搜索
- 按编程语言搜索（如：Python, JavaScript）
- 按标签搜索（如：AI, Web）
- 按作者搜索（如：facebook, google）

## 目录结构说明

项目按以下层级组织：

```
src/
├── SUMMARY.md           # 总索引
├── README.md            # 首页
├── ABOUT.md             # 本页面
└── projects/            # 项目数据
    ├── github/          # GitHub 项目
    │   └── 2026/        # 按年份分类
    │       ├── SUMMARY.md
    │       └── 02/      # 按月份分类
    │           ├── SUMMARY.md
    │           └── 02.md # 具体日期的项目
    ├── gitee/           # Gitee 项目
    ├── gitcode/         # GitCode 项目
    └── atomicgit/       # AtomicGit 项目
```

## 项目信息

每个项目包含以下信息：

- **项目名称** - 项目在平台上的名称
- **作者** - 项目作者/组织
- **描述** - 项目简介
- **⭐ Stars** - 星标数量（热度指标）
- **🔄 Forks** - 复制数量（活跃度指标）
- **📝 语言** - 主要编程语言
- **🏷️ 标签** - 项目标签（如：热门, AI, Web）
- **🔗 链接** - 项目链接

## 项目筛选

### 按平台
- GitHub - 全球最大开源社区
- Gitee - 中国最大代码托管平台
- GitCode - CSDN 代码托管平台
- AtomicGit - 新兴代码托管平台

### 按热度
- ⭐ 高星标项目（推荐）
- 📈 快速增长项目
- 🔥 最新热门项目

### 按领域
- 🤖 AI/机器学习
- 🌐 Web 开发
- 📱 移动应用
- 🔧 工具/库
- 🎮 游戏开发
- 🔐 安全/区块链
- 📊 数据科学

## 常见问题

**Q: 项目多久更新一次？**
A: 每天上午 09:00（北京时间）自动更新。

**Q: 项目数据来源是什么？**
A: 来源于 GitHub, Gitee, GitCode, AtomicGit 等主流代码托管平台。

**Q: 如何分享一个项目？**
A: 点击项目标题，复制浏览器地址栏的 URL 即可分享。

**Q: 可以下载项目列表吗？**
A: 可以，点击右侧的 ⬇️ 图标下载 PDF 格式。

**Q: 如何提交项目推荐？**
A: 欢迎通过 GitHub Issues 提交你发现的好项目！

**Q: 项目数据是实时的吗？**
A: 不是，我们每天采集一次，数据会有一定延迟。

## 技术说明

本项目使用以下技术构建：

- **mdBook** - 静态网站生成工具
- **OpenClaw** - 自动化项目采集工具
- **Python** - 项目爬虫脚本
- **requests** - HTTP 请求库
- **GitHub Actions** - 自动构建和部署

## 数据格式

项目数据以 JSON 格式存储，每个文件包含一天的项目数据：

```json
{
  "date": "2026-02-02",
  "platform": "GitHub",
  "count": 20,
  "projects": [
    {
      "name": "example-project",
      "author": "author-name",
      "description": "项目描述",
      "url": "https://github.com/author/project",
      "stars": 9999,
      "language": "Python",
      "tags": ["AI", "热门"],
      "forks": 1234
    }
  ]
}
```

## 联系方式

如有问题或建议，请通过以下方式联系：

- GitHub Issues: [提交问题](https://github.com/reigadegr/daily-news/issues)
- GitHub Discussions: [参与讨论](https://github.com/reigadegr/daily-news/discussions)

## 贡献指南

欢迎贡献！

1. 发现有趣的优质项目，可以通过 Issue 推荐
2. 改进项目爬虫，提升数据质量
3. 优化网站展示，提升用户体验
4. 翻译文档，帮助更多开发者

---

*最后更新：2026年2月2日*
