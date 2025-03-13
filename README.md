# ArXiv Translator

![ArXiv Translator](https://via.placeholder.com/800x400?text=ArXiv+Translator)

## 概述

ArXiv Translator 是一个用于翻译ArXiv论文的Web应用程序。通过输入ArXiv ID和API密钥，用户可以选择不同的分割级别（如章节或子章节）来翻译LaTeX文档。该应用程序利用了现代Web技术和后端处理能力，为用户提供了一个便捷的翻译工具。

## 技术栈

- **前端技术**:
  - **HTML/CSS**: 用于构建用户界面。
  - **Tailwind CSS**: 用于快速构建响应式和美观的UI组件。
  - **JavaScript**: 用于处理动态内容和事件监听。

- **后端技术**:
  - **Flask**: 一个轻量级的Python Web框架，用于构建Web应用程序。
  - **Python**: 用于编写后端逻辑和处理翻译任务。

- **其他技术**:
  - **EventSource**: 用于实现实时进度更新。
  - **Queue**: 用于管理翻译过程中的进度信息。

## 功能特性

- **实时进度更新**: 用户可以实时查看翻译进度。
- **自定义分割级别**: 用户可以选择不同的分割级别来翻译LaTeX文档。
- **错误处理**: 提供友好的错误提示，帮助用户解决问题。

## 安装与运行

1. **克隆仓库**:
   ```bash
   git clone https://github.com/yourusername/ArxivTrans.git
   cd ArxivTrans