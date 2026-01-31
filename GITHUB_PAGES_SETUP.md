# GitHub Pages 启用指南

## 步骤 1: 启用 GitHub Pages

1. 访问你的仓库设置页面:
   https://github.com/reigadegr/daily-news/settings/pages

2. 在 "Build and deployment" 部分:
   - **Source**: 选择 "GitHub Actions"
   - 点击 "Save"

3. GitHub Actions 会自动检测到 `.github/workflows/deploy.yml` 文件
4. 等待几分钟，GitHub Actions 会自动构建并部署网站

## 步骤 2: 查看部署状态

1. 访问 Actions 页面:
   https://github.com/reigadegr/daily-news/actions

2. 等待 workflow 完成运行（通常需要 1-3 分钟）
3. 如果成功，你会看到绿色的 ✅ 标记

## 步骤 3: 访问你的网站

部署成功后，访问:
https://reigadegr.github.io/daily-news/

## 常见问题

### Q: 部署失败怎么办？
A: 检查 Actions 页面的错误日志，通常问题是:
- 仓库权限未正确设置
- workflow 文件语法错误
- mdbook 构建失败

### Q: 更新后多久能看到新内容？
A: 通常 1-3 分钟。每次推送代码到 main 分支都会触发自动部署。

### Q: 自定义域名如何设置？
A:
1. 在仓库设置中添加自定义域名
2. 配置 DNS 记录 (CNAME)
3. GitHub Pages 会自动配置 SSL 证书

## 下次更新

下一次新闻更新时间: {{下次整点时间}}

---

*如果需要帮助，请在 GitHub 提交 Issue*
