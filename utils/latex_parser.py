import re
from pathlib import Path
from typing import List, Dict

class LatexParser:
    def __init__(self, tex_dir: Path):
        self.tex_dir = tex_dir
        self.xecjk_added = False
        
    def process_document(self, tex_file: Path, split_level: str = 'section') -> List[str]:
        """
        根据章节级别分割文档内容
        
        :param split_level: section 或 subsection 作为分块依据
        """
        with open(tex_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 找到 \documentclass 所在的行，并在其下一行插入 \usepackage{xeCJK}
        document_class_line = next((i for i, line in enumerate(lines) if r'\documentclass' in line), None)
        if document_class_line is not None and not self.xecjk_added:
            lines.insert(document_class_line + 1, r'\usepackage{xeCJK}\n')
            self.xecjk_added = True
        
        # 删除以 % 开头的注释行
        content = ''.join(lines)
        content = re.sub(r'^\s*%.*$', '', content, flags=re.MULTILINE)
        
        pattern = re.compile(rf"\\{split_level}\*?{{.*?}}", re.DOTALL)
        split_parts = pattern.split(content)
        section_commands = pattern.findall(content)
        result = []
        pre_section = split_parts[0]
        result.append(pre_section)
        for i in range(1, len(split_parts)):
            section_block = section_commands[i-1] + '\n' + split_parts[i]
            result.append(section_block)
        return result

    def process_all_tex(self, split_level: str = 'section') -> Dict[str, List[str]]:
        """
        处理项目中的所有.tex文件，并返回一个字典，键为文件的相对路径，值为分割后的LaTeX源码列表
        """
        tex_files = list(self.tex_dir.rglob("*.tex"))  # 修改这里，使用 rglob 递归查找
        result_dict = {}
        for tex_file in tex_files:
            result_dict[tex_file.relative_to(self.tex_dir)] = self.process_document(tex_file, split_level)  # 修改这里，使用文件的相对路径作为键
        return result_dict

if __name__ == "__main__":
    parser = LatexParser(Path("output/raw_files/0704.0001"))
    parsed_content_dict = parser.process_all_tex()
    print(f"解析到{len(parsed_content_dict)}个文件")
    for file_name, content_blocks in parsed_content_dict.items():
        print(f"文件 {file_name} 解析到 {len(content_blocks)} 个内容块")