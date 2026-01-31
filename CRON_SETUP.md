# 自动化更新配置

## Cron 任务

系统 crontab 已配置每小时自动执行新闻爬虫脚本：

```cron
0 * * * * python3 ~/.openclaw/workspace/hourly_news_scraper.py >> ~/.openclaw/workspace/hourly_news.log 2>&1
```

## 工作流程

1. **每小时整点**（00分）自动触发脚本
2. 脚本执行以下任务：
   - 拉取最新代码
   - 获取最新新闻
   - 更新 mdBook 源文件
   - 推送到 GitHub 仓库
   - 触发 GitHub Actions 部署到 Pages

3. GitHub Actions 自动构建并部署（约 1-2 分钟）

## 日志文件

脚本执行日志保存在：`~/.openclaw/workspace/hourly_news.log`

查看日志：
```bash
tail -f ~/.openclaw/workspace/hourly_news.log
```

## 手动管理

### 查看当前 crontab
```bash
crontab -l
```

### 编辑 crontab
```bash
crontab -e
```

### 删除任务
```bash
crontab -r  # 删除所有任务
```

## 测试

手动运行脚本测试：
```bash
cd ~/project/daily-news
python3 ~/.openclaw/workspace/hourly_news_scraper.py
```

## 监控

### 查看最近的 GitHub Actions 运行
```bash
cd ~/project/daily-news
gh run list --limit 5
```

### 查看部署状态
```bash
cd ~/project/daily-news
gh run view <run-id>
```

## 下次更新时间

当前时间后的下一个整点（如 17:00, 18:00, 19:00...）

---

*配置时间: 2026-01-31*
