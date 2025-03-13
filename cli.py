import os
import argparse

from arxiv_translate import arxiv_translate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download, parse, and translate an arXiv LaTeX document.")
    parser.add_argument("arxiv_id", type=str, help="The arXiv ID of the paper to download.")
    parser.add_argument("--api_key", type=str, help="The API key for the translation service.")
    parser.add_argument("--split_level", type=str, default='section', help="The level to split LaTeX documents (e.g., 'section', 'subsection').")  # 新增 split_level 参数
    args = parser.parse_args()

    arxiv_id = args.arxiv_id
    api_key = args.api_key or os.getenv("API_KEY")
    split_level = args.split_level  # 新增 split_level 参数

    if not api_key:
        print("API key is required. Please provide it via the --api_key argument or set the API_KEY environment variable.")
    else:
        result = arxiv_translate(arxiv_id, api_key, split_level)  # 修改这里，传递 split_level 参数
        print(result)