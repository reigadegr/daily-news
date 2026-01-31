# mdbook URL 访问指南

## 问题说明

你之前访问的 URL `http://localhost:8475/2026/01/SUMMARY.html` 是错误的。

## 原因

`SUMMARY.md` 是 mdbook 的目录索引文件，用于定义书的结构，**不是一个可以直接访问的页面**。mdbook 不会为 `SUMMARY.md` 生成 HTML 文件。

## 正确的访问方式

### 首页
```
http://localhost:3000/
```

### 2026年概览
```
http://localhost:3000/2026/index.html
```

### 2026年1月概览
```
http://localhost:3000/2026/01/index.html
```

### 1月31日的新闻
```
http://localhost:3000/2026/01/31.html
```

### 关于页面
```
http://localhost:3000/ABOUT.html
```

## URL 规则

在 mdbook 中：

1. **所有页面都是 `.html` 结尾**
2. **`SUMMARY.md` 不会生成 HTML 文件** - 它只是目录索引
3. **`index.md` 生成 `index.html`** - 作为章节的概览页面
4. **其他 `.md` 文件生成对应的 `.html` 文件**

## 文件对应关系

```
源文件                          → 生成的 URL
─────────────────────────────────────────────────────────
src/README.md                   → http://localhost:3000/
src/SUMMARY.md                  → 不生成 URL（目录索引）
src/ABOUT.md                    → http://localhost:3000/ABOUT.html
src/2026/index.md              → http://localhost:3000/2026/index.html
src/2026/01/index.md           → http://localhost:3000/2026/01/index.html
src/2026/01/31.md              → http://localhost:3000/2026/01/31.html
```

## 导航方式

### 方式 1: 使用左侧导航栏
mdbook 的左侧有完整的目录树，点击即可导航。

### 方式 2: 使用顶部导航栏
- **首页**: 点击左上角 "每日新闻汇总"
- **目录**: 点击左侧边栏的章节
- **搜索**: 点击放大镜图标 🔍 进行全文搜索

### 方式 3: 使用页面内的链接
每个页面底部都有返回链接，例如：
```
[返回 2026年索引](../2026.html) | [返回首页](../index.html)
```

## 常见错误

### ❌ 错误的 URL
```
http://localhost:3000/SUMMARY.html        ← SUMMARY 不是页面
http://localhost:3000/2026/SUMMARY.html   ← SUMMARY 不是页面
http://localhost:3000/2026/01/SUMMARY.md  ← .md 不是 URL
```

### ✅ 正确的 URL
```
http://localhost:3000/                     ← 首页
http://localhost:3000/2026/index.html     ← 2026年概览
http://localhost:3000/2026/01/index.html  ← 1月概览
```

## 修复内容

为了更好的用户体验，我添加了以下 `index.md` 文件：

1. **`src/2026/index.md`** - 2026年概览页面
2. **`src/2026/01/index.md`** - 2026年1月概览页面

这些页面提供了月份/日期的索引，方便浏览。

## 本地启动命令

```bash
cd ~/project/daily-news
mdbook serve
```

然后访问: http://localhost:3000/

**注意**: 默认端口是 3000，如果你看到的是 8475，可能是你之前用了不同的端口或者有其他服务在运行。

---

**修复时间**: 2026-01-31 15:45
**状态**: ✅ 已修复
