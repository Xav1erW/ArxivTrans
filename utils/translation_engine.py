import os
import time
from typing import List, Dict
from openai import OpenAI

class TranslationEngine:
    def __init__(self, api_key: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        
    def translate_segment(self, text: str) -> str:
        """使用API进行翻译（示例使用OpenAI API）"""
        response = self.client.chat.completions.create(
            model="qwen-plus", 
            messages=[
                {"role": "system", "content": "你是一个翻译助手，能够将英文文本翻译成中文，同时保留LaTeX格式和数学公式，仅翻译latex会显示出来的自然语言部分，而不编译命令部分。如果没有需要翻译的部分，按照原样输出。不需要除翻译内容外的任何内容，包括```等符号包裹代码"},
                {"role": "user", "content": text}
            ]
        )
        if response.choices[0].message.content:
            return response.choices[0].message.content.strip()
        else:
            return text
            
    def translate_document(self, content_segments: List[Dict]) -> List[Dict]:
        """批量翻译文本段"""
        translated = []
        for segment in content_segments:
            if segment["type"] == "text":
                translated_segment = {
                    "type": "text",
                    "content": self.translate_segment(segment["content"])
                }
                translated.append(translated_segment)
                time.sleep(0.1)  # 避免API频率限制
            else:
                translated.append(segment)
        return translated

if __name__ == "__main__":
    # 测试用例
    test_segments = [
        {"type": "text", "content": "This is a test sentence."},
        {"type": "latex", "content": "\\section{Introduction}\n Our model is most nb"}
    ]
    translator = TranslationEngine("YOUR_API_KEY")
    translated = translator.translate_document(test_segments)
    print(translated[0]["content"])  # 应显示中文翻译
