# 主题样式说明

## 样式特性

本项目使用自定义 CSS 实现了现代化的设计风格：

### 视觉效果

- **渐变背景** - 柔和的渐变背景，提升视觉层次
- **卡片式设计** - 内容区采用卡片样式，带阴影效果
- **毛玻璃效果** - 侧边栏和导航栏采用磨砂玻璃效果
- **动画过渡** - 平滑的悬停和页面加载动画

### 配色方案

- **主色调**: 蓝色 (#2563eb)
- **文本**: 深灰/浅灰，确保可读性
- **背景**: 浅灰渐变，护眼舒适
- **支持暗色模式**: 自动适配系统偏好

### 组件优化

- **标题** - 渐变色标题，左侧装饰线
- **链接** - 底部滑入动画
- **代码块** - 深色背景，语法高亮
- **表格** - 斑马纹，悬停高亮
- **按钮** - 阴影和悬停效果
- **搜索框** - 圆角设计，聚焦高亮

## 文件结构

```
daily-news/
├── theme/
│   └── css/
│       └── custom.css    # 自定义样式
├── src/theme/
│   └── css/
│       └── custom.css    # 备份（在 src 目录）
└── book.toml             # 配置文件（引用自定义 CSS）
```

## 自定义样式

### 修改配色

编辑 `theme/css/custom.css` 中的 CSS 变量：

```css
:root {
  --primary-color: #2563eb;      /* 主色 */
  --primary-hover: #1d4ed8;      /* 悬停色 */
  --bg-gradient-start: #f8fafc;  /* 背景渐变起始 */
  --bg-gradient-end: #e2e8f0;    /* 背景渐变结束 */
  /* ... 更多变量 */
}
```

### 修改字体

在 `custom.css` 中添加或修改字体规则：

```css
body {
  font-family: '你的字体', sans-serif;
}
```

### 添加新样式

在 `custom.css` 文件末尾添加自定义样式规则。

## 本地预览

### 安装 mdBook

```bash
cargo install mdbook
```

### 本地构建

```bash
cd ~/project/daily-news
mdbook build
```

### 本地服务

```bash
cd ~/project/daily-news
mdbook serve
```

然后访问 http://localhost:3000

## 部署更新

修改样式后：

```bash
cd ~/project/daily-news
git add -A
git commit -m "更新样式"
git push origin main
```

GitHub Actions 会自动部署新样式。

## 参考资源

- [mdBook 文档](https://rust-lang.github.io/mdBook/)
- [CSS 变量](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [CSS 渐变](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient)

---

*样式更新时间: 2026-01-31*
