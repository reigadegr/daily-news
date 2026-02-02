# 部署指南

## 自动部署（推荐）

### GitHub Actions 自动部署

项目已配置 GitHub Actions，会在以下时机自动部署：

1. **推送到 main 分支** - 自动触发部署
2. **定时任务** - 每天北京时间 09:00（UTC 01:00）自动运行
3. **手动触发** - 在 GitHub 仓库页面手动触发

#### 工作流程

```
触发 → 收集项目 → 构建 mdBook → 部署到 GitHub Pages
```

## 手动部署

### 方式一：使用一键脚本（推荐）

```bash
cd /home/reigadegr/.openclaw/workspace
./update_and_push.sh
```

这个脚本会自动完成以下操作：
1. 收集各平台热门项目
2. 构建网站
3. 提交变更
4. 推送到 GitHub
5. 触发 GitHub Actions 自动部署

### 方式二：手动执行

#### 1. 收集项目

```bash
cd /home/reigadegr/桌面/project/daily-news
python3 ~/.openclaw/workspace/hot_projects_scraper.py
```

#### 2. 构建网站

```bash
mdbook build
```

#### 3. 提交并推送

```bash
git add -A
git commit -m "📊 Update hot projects"
git push origin main
```

## GitHub Actions 工作流说明

### 工作流文件

`.github/workflows/deploy.yml`

### 三个 Jobs

1. **scrape** - 收集热门项目数据
   - 设置 Python 环境
   - 安装依赖
   - 运行收集脚本
   - 提交变更

2. **build** - 构建 mdBook 网站
   - 设置 Rust 环境
   - 安装 mdBook
   - 构建网站
   - 上传构建产物

3. **deploy** - 部署到 GitHub Pages
   - 部署到 GitHub Pages
   - 生成部署 URL

### 定时任务

每天北京时间 09:00 自动运行收集并部署：

```yaml
schedule:
  - cron: '0 1 * * *'  # UTC 01:00 = 北京时间 09:00
```

## 查看部署状态

### 在 GitHub 上查看

1. 进入仓库: https://github.com/reigadegr/daily-news
2. 点击 "Actions" 标签
3. 查看工作流运行状态

### 部署 URL

- **GitHub Pages**: https://reigadegr.github.io/daily-news/
- **工作流日志**: https://github.com/reigadegr/daily-news/actions

## 故障排查

### 1. GitHub Actions 失败

**可能原因：**
- API 限流（GitHub, Gitee 等）
- 网络问题
- 脚本错误

**解决方案：**
- 查看 Actions 日志
- 重新运行失败的 workflow
- 检查 API 配置

### 2. 本地推送失败

**可能原因：**
- Git 配置错误
- 网络连接问题
- 权限问题

**解决方案：**
```bash
# 检查 Git 配置
git config --list

# 检查远程仓库
git remote -v

# 检查连接
git ls-remote origin
```

### 3. 网站未更新

**可能原因：**
- GitHub Pages 缓存
- 部署未完成

**解决方案：**
- 等待 1-2 分钟（GitHub Pages 部署需要时间）
- 强制刷新浏览器
- 检查 GitHub Actions 状态

## 高级配置

### 修改收集频率

编辑 `.github/workflows/deploy.yml`，修改 cron 表达式：

```yaml
schedule:
  - cron: '0 1 * * *'  # 每天 09:00
  # - cron: '0 1,13 * * *'  # 每天 09:00 和 21:00
  # - cron: '0 */6 * * *'  # 每 6 小时
```

### 修改收集语言

编辑 `scripts/hot_projects_scraper.py`，修改语言参数：

```python
# 收集特定语言的项目
projects = scraper.scrape_trending(language="Python")
```

### 添加新的平台

在 `scripts/hot_projects_scraper.py` 中添加新的 Scraper 类：

```python
class NewPlatformScraper(ProjectScraper):
    def scrape_trending(self, language: str = "") -> List[Dict]:
        # 实现你的收集逻辑
        pass
```

## 监控和维护

### 定期检查

建议每周检查一次：
1. GitHub Actions 运行状态
2. 网站是否正常更新
3. 数据质量

### 数据备份

所有数据都保存在 GitHub 仓库中，自动备份：
- 源码在 `src/` 目录
- 构建产物在 `book/` 目录
- 脚本在 `scripts/` 目录

### 性能优化

如果收集时间过长：
- 减少每个平台收集的项目数量
- 添加缓存机制
- 使用异步请求

## 相关文档

- [mdBook 官方文档](https://rust-lang.github.io/mdBook/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

*最后更新：2026年2月2日*
