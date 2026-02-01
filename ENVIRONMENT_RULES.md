# GitHub Pages 环境保护规则配置

## 当前允许的部署分支

环境保护规则 `github-pages` 现在允许以下分支部署：

1. **main** - mdbook 静态站点
2. **react** - React 前端应用

## 配置历史

- 初始配置：只允许 main 分支
- 问题：react 分支被环境保护规则阻止
- 解决：添加 react 分支到允许列表

## 部署流程

### main 分支
- 触发：推送到 main 分支
- 工作流：`Deploy mdBook to GitHub Pages`
- 产物：mdbook 构建的静态站点

### react 分支
- 触发：推送到 react 分支
- 工作流：`Deploy React to GitHub Pages`
- 产物：React + Vite 构建的单页应用

## 访问地址

两个分支都部署到同一个 GitHub Pages 地址：
- https://reigadegr.github.io/daily-news/

## 环境保护

环境保护规则确保：
- 只有指定的分支可以部署
- 部署前需要环境变量和权限验证
- 防止意外或未授权的部署

---

*配置更新时间: 2025-06-20*