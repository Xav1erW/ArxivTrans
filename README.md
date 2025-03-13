# ArXiv Translator

![ArXiv Translator](https://placehold.co/600x200/bisque/midnightblue?text=ArXiv\nTranslator&font=lora)

## 概述

ArXiv Translator 是一个用于翻译ArXiv论文的Web应用程序。通过输入ArXiv ID和API密钥，用户可以选择不同的分割级别（如章节或子章节）来翻译LaTeX文档。


## 功能特性

- **实时进度更新**: 用户可以实时查看翻译进度。
- **自定义分割级别**: 用户可以选择不同的分割级别来翻译LaTeX文档。
- **错误处理**: 提供友好的错误提示，帮助用户解决问题。

## 安装与运行

1. **克隆仓库**:
   ```bash
   git clone https://github.com/yourusername/ArxivTrans.git
   cd ArxivTrans
   ```
2. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

## 使用示例

### 命令行工具

1. **下载、解析并翻译ArXiv论文**:
   ```bash
   python cli.py <arxiv_id> --api_key <your_api_key> --split_level <section|subsection>
   ```
   例如:
   ```bash
   python cli.py 2301.00001 --api_key your_api_key_here --split_level section
   ```

### Web应用程序

1. **启动Web服务器**:
   ```bash
   python webui.py
   ```

2. **访问Web界面**:
   打开浏览器并访问 `http://127.0.0.1:5000/`。

3. **输入ArXiv ID和API密钥**:
   - 在“ArXiv ID”字段中输入论文的ArXiv ID。
   - 在“API Key”字段中输入翻译服务的API密钥。
   - 选择分割级别（如“section”或“subsection”）。
   - 点击“Translate”按钮开始翻译。

> [!IMPORTANT] 注意
>
> 本应用只提供对LaTeX源码的翻译，翻译后需要自行编译