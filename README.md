# Daily News React - 每日新闻汇总前端应用

一个现代化的 React + TypeScript + Vite 新闻展示应用，作为 daily-news 项目的 React 前端版本。

[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-7.2-646CFF?logo=vite)](https://vitejs.dev/)

[在线演示](https://reigadegr.github.io/daily-news/) | [后端仓库](https://github.com/reigadegr/daily-news) | [问题反馈](https://github.com/reigadegr/daily-news/issues)

## 📖 项目简介

Daily News React 是每日新闻汇总系统的前端应用，提供现代化的新闻浏览体验。支持按日期查看历史新闻，分类浏览（时政、经济、国际、科技、社会），以及响应式设计适配移动端。

## ✨ 功能特性

- 📅 **日期选择**: 选择任意日期查看历史新闻
- 🏷️ **新闻分类**: 支持时政、经济、国际、科技、社会五大分类
- 🎨 **现代UI**: 卡片式设计，优美的视觉效果
- 📱 **响应式**: 完美适配桌面和移动设备
- ⚡ **快速加载**: Vite 构建优化，秒级加载
- 🔍 **搜索功能**: 支持新闻标题搜索
- 🌙 **深色模式**: 支持深色/浅色主题切换

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

应用将在 http://localhost:5173 启动

### 构建生产版本

```bash
npm run build
```

构建产物将在 `dist` 目录中

### 预览生产版本

```bash
npm run preview
```

## 📁 项目结构

```
daily-news-react/
├── public/                  # 静态资源
├── src/
│   ├── components/          # React 组件
│   │   ├── NewsCard.tsx    # 新闻卡片组件
│   │   ├── NewsCard.css
│   │   ├── NewsCategory.tsx # 新闻分类容器
│   │   └── NewsCategory.css
│   ├── services/            # API 服务
│   │   └── newsService.ts  # 新闻数据服务
│   ├── types/               # TypeScript 类型
│   │   └── news.ts         # 数据模型
│   ├── App.tsx             # 主应用组件
│   ├── App.css
│   └── main.tsx            # 应用入口
├── index.html              # HTML 模板
├── package.json            # 项目配置
├── tsconfig.json            # TypeScript 配置
├── vite.config.ts          # Vite 配置
└── README.md               # 本文件
```

## 🔧 技术栈

- **框架**: React 19
- **语言**: TypeScript 5.9
- **构建工具**: Vite 7.2
- **样式**: CSS Modules
- **API**: 原生 Fetch API

## 🌐 部署

### GitHub Pages

本项目已配置为自动部署到 GitHub Pages。

1. 推送代码到 `react` 分支
2. GitHub Actions 会自动构建并部署

访问地址: https://reigadegr.github.io/daily-news/

### 手动部署

```bash
# 构建项目
npm run build

# 部署 dist 目录到你的服务器
```

## 📊 数据源

该应用从以下来源获取新闻数据：

1. **GitHub Raw** (主要数据源)
   - 直接从 `reigadegr/daily-news` 仓库读取 markdown 文件
   - 实时获取最新新闻内容

2. **后端 API** (可选)
   - 如果配置了 `VITE_API_BASE_URL`
   - 提供更好的性能和缓存

## 🎯 开发计划

- [x] 基础新闻展示功能
- [x] 响应式设计
- [x] 日期选择器
- [x] 新闻分类展示
- [ ] 搜索功能
- [ ] 新闻收藏功能
- [ ] 深色模式
- [ ] PWA 离线支持
- [ ] 社交分享
- [ ] 个性化推荐

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🔗 相关链接

- [后端项目](https://github.com/reigadegr/daily-news) - Python 新闻爬虫
- [mdbook 分支](https://github.com/reigadegr/daily-news) - mdbook 静态站点版本
- [在线演示](https://reigadegr.github.io/daily-news/) - GitHub Pages 部署

## 💬 联系方式

- GitHub: [@reigadegr](https://github.com/reigadegr)
- 问题反馈: [Issues](https://github.com/reigadegr/daily-news/issues)

---

**注意**: 这是 daily-news 项目的 React 前端分支。如需查看 mdbook 版本，请切换到 `main` 分支。