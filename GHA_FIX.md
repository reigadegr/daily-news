# GitHub Actions 修复说明

## 问题

GitHub Actions 报错：
```
Error: Unable to resolve action `peaceiris/actions-mdbook@v3`, unable to find version `v3`
```

## 原因

`peaceiris/actions-mdbook` action 可能不存在或者版本号不正确。该 action 可能已经停止维护或者版本号发生了变化。

## 解决方案

不使用第三方 action，直接使用官方 Rust toolchain 安装 mdbook。

### 修改前
```yaml
- name: Setup mdBook
  uses: peaceiris/actions-mdbook@v3
  with:
    mdbook-version: 'latest'
```

### 修改后
```yaml
- name: Setup Rust
  uses: dtolnay/rust-toolchain@stable

- name: Install mdBook
  run: cargo install mdbook
```

## 优点

1. **更可靠** - 使用官方 Rust toolchain
2. **更简单** - 不依赖第三方 action
3. **更灵活** - 可以轻松指定 mdbook 版本

## 验证

修复后，访问 Actions 页面查看运行状态：
https://github.com/reigadegr/daily-news/actions

如果成功，你会看到绿色的 ✅ 标记。

## 其他可能的解决方案

如果想要使用预编译的二进制文件，可以使用：

```yaml
- name: Download mdBook
  run: |
    curl -sSL https://github.com/rust-lang/mdBook/releases/download/v0.4.40/mdbook-v0.4.40-x86_64-unknown-linux-gnu.tar.gz | tar -xz
    sudo mv mdbook /usr/local/bin/
```

不过使用 `cargo install` 更简单且官方支持。

---

**修复时间**: 2026-01-31 15:35
**状态**: ✅ 已修复并推送
