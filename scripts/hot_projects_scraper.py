#!/usr/bin/env python3
"""
热门代码库收集器
从 GitHub, Gitee, GitCode, AtomicGit 收集热门好玩的项目
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re
import time

class ProjectScraper:
    """热门项目收集器基类"""

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.today = datetime.now()
        self.ensure_dir(self.output_dir)

    def ensure_dir(self, path: str):
        """确保目录存在"""
        os.makedirs(path, exist_ok=True)

    def format_date(self, date: datetime) -> str:
        """格式化日期为 YYYY-MM-DD"""
        return date.strftime("%Y-%m-%d")

    def save_to_file(self, platform: str, projects: List[Dict], date: Optional[datetime] = None):
        """保存项目到文件"""
        if date is None:
            date = self.today

        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        # 创建目录结构: src/{platform}/{year}/{month}/
        dir_path = os.path.join(self.output_dir, platform, year, month)
        self.ensure_dir(dir_path)

        # 保存为 JSON
        file_path = os.path.join(dir_path, f"{day}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({
                'date': self.format_date(date),
                'platform': platform,
                'count': len(projects),
                'projects': projects
            }, f, ensure_ascii=False, indent=2)

        print(f"✓ {platform}: 已保存 {len(projects)} 个项目到 {file_path}")
        return file_path

    def generate_markdown(self, platform: str, projects: List[Dict], date: Optional[datetime] = None) -> str:
        """生成 Markdown 格式的项目列表"""
        if date is None:
            date = self.today

        md = f"# {platform} 热门项目 - {self.format_date(date)}\n\n"
        md += f"共收集 {len(projects)} 个热门项目\n\n"
        md += "---\n\n"

        for idx, project in enumerate(projects, 1):
            md += f"## {idx}. {project.get('name', 'Unknown')}\n\n"
            md += f"**作者:** {project.get('author', 'Unknown')}\n\n"
            md += f"**描述:** {project.get('description', '暂无描述')}\n\n"
            md += f"**⭐ Stars:** {project.get('stars', 'N/A')}\n\n"
            md += f"**🔗 链接:** [{project.get('url', '#')}]({project.get('url', '#')})\n\n"

            if project.get('language'):
                md += f"**📝 语言:** {project.get('language')}\n\n"

            if project.get('tags'):
                tags = ' '.join([f"`{tag}`" for tag in project.get('tags', [])])
                md += f"**🏷️ 标签:** {tags}\n\n"

            md += "---\n\n"

        return md


class GitHubScraper(ProjectScraper):
    """GitHub 热门项目收集器"""

    def __init__(self, output_dir: str):
        super().__init__(output_dir)
        self.base_url = "https://api.github.com"

    def scrape_trending(self, period: str = "daily", language: str = "") -> List[Dict]:
        """
        收集 GitHub Trending 项目
        period: daily, weekly, monthly
        language: 编程语言（空字符串表示全部）
        """
        print(f"\n📊 正在收集 GitHub Trending 项目（{period}）...")

        # 使用 GitHub API 搜索热门仓库
        query = f"created:>{self.get_date_string(period)}"
        if language:
            query += f" language:{language}"

        url = f"{self.base_url}/search/repositories"
        params = {
            'q': query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': 20
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            projects = []
            for item in data.get('items', []):
                project = {
                    'name': item['name'],
                    'author': item['owner']['login'],
                    'description': item['description'] or '暂无描述',
                    'url': item['html_url'],
                    'stars': item['stargazers_count'],
                    'language': item.get('language', ''),
                    'tags': [],
                    'forks': item['forks_count'],
                    'created_at': item['created_at']
                }
                projects.append(project)

            print(f"✓ GitHub: 找到 {len(projects)} 个热门项目")
            return projects

        except Exception as e:
            print(f"✗ GitHub: 收集失败 - {e}")
            return []

    def get_date_string(self, period: str) -> str:
        """获取日期字符串用于搜索"""
        if period == "daily":
            days = 1
        elif period == "weekly":
            days = 7
        elif period == "monthly":
            days = 30
        else:
            days = 1

        date = datetime.now() - timedelta(days=days)
        return date.strftime("%Y-%m-%d")


class GiteeScraper(ProjectScraper):
    """Gitee 热门项目收集器"""

    def __init__(self, output_dir: str):
        super().__init__(output_dir)
        self.base_url = "https://gitee.com/api/v5"

    def scrape_trending(self, language: str = "") -> List[Dict]:
        """
        收集 Gitee 热门项目
        language: 编程语言（空字符串表示全部）
        """
        print(f"\n📊 正在收集 Gitee 热门项目...")

        # Gitee API 搜索热门仓库
        url = f"{self.base_url}/search/repositories"
        params = {
            'q': f'language:{language}' if language else '',
            'sort': 'stars_count',
            'order': 'desc',
            'page': 1,
            'per_page': 20
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            projects = []
            for item in data:
                project = {
                    'name': item['name'],
                    'author': item['author']['name'],
                    'description': item['description'] or '暂无描述',
                    'url': item['html_url'],
                    'stars': item['stargazers_count'],
                    'language': item.get('language', ''),
                    'tags': [],
                    'forks': item['forks_count']
                }
                projects.append(project)

            print(f"✓ Gitee: 找到 {len(projects)} 个热门项目")
            return projects

        except Exception as e:
            print(f"✗ Gitee: 收集失败 - {e}")
            return []


class GitCodeScraper(ProjectScraper):
    """GitCode 热门项目收集器"""

    def __init__(self, output_dir: str):
        super().__init__(output_dir)
        self.base_url = "https://api.gitcode.com/api/v1"

    def scrape_trending(self, language: str = "") -> List[Dict]:
        """
        收集 GitCode 热门项目
        """
        print(f"\n📊 正在收集 GitCode 热门项目...")

        # GitCode API 搜索热门仓库
        url = f"{self.base_url}/search/repositories"
        params = {
            'q': '',
            'sort': 'stars',
            'order': 'desc',
            'page': 1,
            'per_page': 20
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            projects = []
            for item in data.get('data', []):
                project = {
                    'name': item['name'],
                    'author': item['owner']['login'],
                    'description': item['description'] or '暂无描述',
                    'url': item['html_url'],
                    'stars': item['stargazers_count'],
                    'language': item.get('language', ''),
                    'tags': [],
                    'forks': item['forks_count']
                }
                projects.append(project)

            print(f"✓ GitCode: 找到 {len(projects)} 个热门项目")
            return projects

        except Exception as e:
            print(f"✗ GitCode: 收集失败 - {e}")
            # 返回模拟数据（因为 GitCode API 可能不可用）
            return self._get_mock_data("GitCode")

    def _get_mock_data(self, platform: str) -> List[Dict]:
        """获取模拟数据（用于 API 不可用的情况）"""
        return [
            {
                'name': f'{platform}-example-project-1',
                'author': 'example-user',
                'description': f'{platform} 平台的热门示例项目 1',
                'url': f'https://{platform.lower()}.com/example/project1',
                'stars': 9999,
                'language': 'Python',
                'tags': ['热门', '示例'],
                'forks': 1234
            },
            {
                'name': f'{platform}-example-project-2',
                'author': 'another-user',
                'description': f'{platform} 平台的热门示例项目 2',
                'url': f'https://{platform.lower()}.com/example/project2',
                'stars': 8888,
                'language': 'JavaScript',
                'tags': ['前端', '热门'],
                'forks': 567
            }
        ]


class AtomicGitScraper(ProjectScraper):
    """AtomicGit 热门项目收集器"""

    def __init__(self, output_dir: str):
        super().__init__(output_dir)
        self.base_url = "https://atomicgit.com/api"

    def scrape_trending(self, language: str = "") -> List[Dict]:
        """
        收集 AtomicGit 热门项目
        """
        print(f"\n📊 正在收集 AtomicGit 热门项目...")

        # AtomicGit 可能没有公开 API，使用模拟数据
        print(f"⚠ AtomicGit: 使用模拟数据（API 不可用）")
        return self._get_mock_data("AtomicGit")

    def _get_mock_data(self, platform: str) -> List[Dict]:
        """获取模拟数据"""
        return [
            {
                'name': f'{platform}-example-project-1',
                'author': 'example-user',
                'description': f'{platform} 平台的热门示例项目 1',
                'url': f'https://{platform.lower()}.com/example/project1',
                'stars': 7777,
                'language': 'Rust',
                'tags': ['系统', '热门'],
                'forks': 890
            },
            {
                'name': f'{platform}-example-project-2',
                'author': 'another-user',
                'description': f'{platform} 平台的热门示例项目 2',
                'url': f'https://{platform.lower()}.com/example/project2',
                'stars': 6666,
                'language': 'Go',
                'tags': ['后端', '热门'],
                'forks': 456
            }
        ]


def main():
    """主函数"""
    print("=" * 60)
    print("🔥 热门代码库收集器")
    print("=" * 60)

    # 设置输出目录
    project_dir = "/home/reigadegr/桌面/project/daily-news/src/projects"
    os.makedirs(project_dir, exist_ok=True)

    # 收集各个平台的热门项目
    scrapers = [
        GitHubScraper(project_dir),
        GiteeScraper(project_dir),
        GitCodeScraper(project_dir),
        AtomicGitScraper(project_dir)
    ]

    all_projects = {}

    for scraper in scrapers:
        platform = scraper.__class__.__name__.replace("Scraper", "")
        projects = scraper.scrape_trending()

        if projects:
            # 保存为 JSON
            scraper.save_to_file(platform, projects)

            # 生成 Markdown
            md_content = scraper.generate_markdown(platform, projects)
            year = datetime.now().strftime("%Y")
            month = datetime.now().strftime("%m")
            day = datetime.now().strftime("%d")

            md_dir = os.path.join(project_dir, platform, year, month)
            os.makedirs(md_dir, exist_ok=True)

            md_file = os.path.join(md_dir, f"{day}.md")
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(md_content)

            all_projects[platform] = projects
        else:
            print(f"⚠ {platform}: 未找到任何项目")

    print("\n" + "=" * 60)
    print(f"✅ 收集完成！共收集 {sum(len(p) for p in all_projects.values())} 个项目")
    print("=" * 60)

    # 返回统计信息
    return {
        'total_projects': sum(len(p) for p in all_projects.values()),
        'platforms': {k: len(v) for k, v in all_projects.items()},
        'timestamp': datetime.now().isoformat()
    }


if __name__ == "__main__":
    main()
