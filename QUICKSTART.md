# 快速开始指南

## 5 分钟快速部署

### 步骤 1: 首次收集项目

```bash
# 使用一键脚本（推荐）
cd /home/reigadegr/.openclaw/workspace
./update_and_push.sh
```

### 步骤 2: 等待部署

GitHub Actions 会自动部署，通常需要 1-3 分钟。

访问: https://reigadegr.github.io/daily-news/

### 步骤 3: 查看结果

在网站上查看：
- GitHub 热门项目
- Gitee 热门项目
- GitCode 热门项目
- AtomicGit 热门项目

## 常用命令

### 本地测试

```bash
# 仅收集项目（不推送）
python3 ~/.openclaw/workspace/hot_projects_scraper.py

# 仅构建网站
cd /home/reigadegr/桌面/project/daily-news
mdbook build

# 本地预览网站
mdbook serve
# 然后访问 http://localhost:3000
```

### 推送和部署

```bash
# 一键推送并部署
./update_and_push.sh

# 手动推送
git push origin main
```

### 查看状态

```bash
# 查看 Git 状态
cd /home/reigadegr/桌面/project/daily-news
git status

# 查看最近变更
git log --oneline -5

# 查看部署状态
# 在浏览器打开: https://github.com/reigadegr/daily-news/actions
```

## 定时任务

### Cron 设置（可选）

如果想在本地设置定时任务：

```bash
# 编辑 crontab
crontab -e

# 添加以下行（每天 09:00 运行）
0 9 * * * /home/reigadegr/.openclaw/workspace/update_and_push.sh >> /tmp/daily-news.log 2>&1
```

注意：GitHub Actions 已经配置了自动部署，通常不需要本地 cron。

## 数据文件位置

```
项目根目录/
├── scripts/
│   └── hot_projects_scraper.py      # 收集脚本
├── src/projects/
│   ├── GitHub/2026/02/               # GitHub 项目数据
│   │   ├── 02.json                   # JSON 数据
│   │   └── 02.md                     # Markdown 显示
│   ├── Gitee/2026/02/                # Gitee 项目数据
│   ├── GitCode/2026/02/              # GitCode 项目数据
│   └── AtomicGit/2026/02/            # AtomicGit 项目数据
└── book/                             # 构建输出目录
```

## 故障排查快速检查

### 网站没有更新？

1. 检查 GitHub Actions 是否运行成功
2. 强制刷新浏览器
3. 清除浏览器缓存

### 收集失败？

1. 检查网络连接
2. 查看错误日志
3. 某些平台 API 可能暂时不可用（会使用模拟数据）

### 推送失败？

1. 检查 Git 配置
2. 确认仓库地址正确
3. 检查权限设置

## 获取帮助

- 📖 完整文档: [README.md](./README.md)
- 🚀 部署指南: [DEPLOY.md](./DEPLOY.md)
- 💬 提交问题: [GitHub Issues](https://github.com/reigadegr/daily-news/issues)

---

*祝你使用愉快！*
