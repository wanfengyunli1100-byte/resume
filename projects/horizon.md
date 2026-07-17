# Horizon ? AI 可读写桌面项目进度面板

## 一句话定位
> **Horizon** — 一个 AI 可读写的桌面项目进度面板。核心理念是“数据是核心，界面是视图，AI 是一等公民”。

## 技术栈

| 层 | 技术 |
|---|------|
| 前端 | React 19 + TypeScript 5.8 + Tailwind CSS v4 + shadcn/ui |
| 桌面容器 | Tauri 2 (Rust)，含系统托盘、开机自启、自动更新 |
| 数据 | 本地 JSON（原子写入 + 3 版本备份 + 文件监听自动刷新） |
| AI 接口 | MCP 协议（Python 服务器，零外部依赖，6 个工具） |
| 构建 | Vite 7 + NSIS 安装包 + GitHub Actions CI/CD |
| 图标 | 自定义 16 尺寸应用图标 |

## 关键数据
- 8 个 React 组件：项目卡片网格、创建/编辑弹窗、详情页（时间线+待办）、设置面板、确认对话框
- ~400 行 Rust 后端：数据 CRUD、文件监听（notify crate）、系统托盘、单实例锁
- ~300 行 Python MCP 服务器：6 个标准化工具（list/get/create/update/delete/read），零外部依赖
- 11 个里程碑：从骨架搭建到构建分发，全链路交付

## 核心设计
AI 和人类共用同一个 `horizon.json` 数据文件。AI 通过 MCP 协议或直接文件读写操作数据，Horizon 通过文件监听自动刷新界面。数据文件即“唯一真相源”，界面只是视图。

## 英文版
> **Horizon** — An AI-readable desktop project progress panel. Core principle: \"Data is the source of truth, UI is a view, AI is a first-class citizen.\"
>
> **Tech Stack**: React 19 + TypeScript + Tailwind CSS v4 + shadcn/ui + Tauri 2 (Rust) + Python MCP Server
>
> **Key Features**:
> - Desktop app with system tray, auto-start, auto-update, custom icons
> - CRUD project management with timeline history and task checklist
> - JSON data file with atomic writes, 3-version backup, file-watch auto-reload
> - MCP (Model Context Protocol) server: 6 tools, zero external dependencies
> - GitHub Actions CI/CD with NSIS installer generation
>
> **Architecture**: Data-first design where AI and human share a single JSON file as the single source of truth.
