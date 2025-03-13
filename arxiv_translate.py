import os
import argparse
import shutil
from utils import ArXivDownloader, LatexParser, TranslationEngine

def arxiv_translate(arxiv_id: str, api_key: str, split_level: str = 'section', progress_callback=None):
    try:
        # 下载并解压arXiv论文源码包
        downloader = ArXivDownloader()
        if progress_callback:
            progress_callback("开始下载arXiv论文...")
        tar_file = downloader.download(arxiv_id)
        if not tar_file:
            if progress_callback:
                progress_callback("下载失败")
            return "下载失败"
        if progress_callback:
            progress_callback(f"文件已下载到: {tar_file}")
        extract_path = downloader.extract(tar_file)
        if not extract_path:
            if progress_callback:
                progress_callback("解压失败")
            return "解压失败"
        
        # 复制原始工程目录
        copy_path = extract_path.parent / f"{extract_path.name}_translated"
        shutil.copytree(extract_path, copy_path, dirs_exist_ok=True)
        
        # 解析LaTeX文档
        parser = LatexParser(copy_path)  # 修改这里，使用复制后的工程目录
        parsed_content_dict = parser.process_all_tex(split_level=split_level)  # 修改这里，传递 split_level 参数
        if progress_callback:
            progress_callback(f"解析到{len(parsed_content_dict)}个文件")
        
        # 翻译LaTeX文档
        translator = TranslationEngine(api_key)
        for i, (tex_file, content_blocks) in enumerate(parsed_content_dict.items()):
            translated_blocks = []
            for block in content_blocks:
                translated_block = translator.translate_segment(block)
                translated_blocks.append(translated_block)
            
            # 输出翻译后的文件
            translated_file_path = copy_path / tex_file  # 修改这里，确保文件路径正确
            with open(translated_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(translated_blocks))
            
            if progress_callback:
                progress_callback(f"文件 {tex_file} 已翻译并保存到 {translated_file_path} ({i+1}/{len(parsed_content_dict)})")
        
        return "翻译完成"
    except Exception as e:
        return f"发生错误: {str(e)}"