# 🚀 AutoTest Platform

基于 **Playwright + Pytest** 的 Web UI 自动化测试框架。

## ✨ 功能特性

- 🎭 **Playwright 引擎**：智能等待、跨浏览器、自动截图
- 🧪 **Pytest 框架**：fixture 管理、参数化、标记分类
- 📄 **Page Object 模式**：页面元素与业务逻辑解耦
- 📊 **Allure 报告**：可视化报告，失败自动附截图
- 🔁 **可扩展结构**：新增用例只需在 `tests/` 加文件

## 🏗️ 项目结构

```
autotest-platform/
├── conftest.py              # 全局 fixture（browser / page + 失败截图）
├── pytest.ini               # pytest 配置
├── pages/                   # Page Object 层
│   └── login_page.py
└── tests/                   # 测试用例
    └── test_login.py
```

## 🚀 快速开始

```bash
# 1. 克隆
git clone https://github.com/你的用户名/autotest-platform.git
cd autotest-platform

# 2. 安装依赖
pip install pytest pytest-playwright allure-pytest
playwright install chromium

# 3. 运行测试
pytest

# 4. 查看报告
pytest --alluredir=./allure-results
allure serve ./allure-results
```

## 🧪 当前覆盖用例

| 模块 | 用例 | 类型 |
|------|------|------|
| 登录 | 正确账号密码登录成功 | 正向 |
| 登录 | 密码错误提示报错 | 异常 |
| 登录 | 用户名为空提示报错 | 异常 |
| 登录 | 锁定用户无法登录 | 异常 |

测试站点：https://www.saucedemo.com

## 📈 Roadmap

- [x] Pytest + Playwright 框架搭建
- [x] Page Object 模式
- [x] Allure 报告 + 失败截图
- [ ] 数据驱动（参数化 + YAML）
- [ ] 接口自动化（httpx）
- [ ] 异步执行
- [ ] Docker 部署
- [ ] GitHub Actions CI

## 📄 License

MIT