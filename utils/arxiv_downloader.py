import os
import requests
import tarfile
from pathlib import Path

class ArXivDownloader:
    def __init__(self, output_dir="output/raw_files"):
        self.base_url = "https://arxiv.org/src/"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def download(self, arxiv_id):
        """下载arXiv论文源码包"""
        url = f"{self.base_url}{arxiv_id}"
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            tar_path = self.output_dir / f"{arxiv_id}.tar.gz"
            with open(tar_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return tar_path
        except requests.exceptions.RequestException as e:
            print(f"下载失败: {e}")
            return None

    def extract(self, tar_path, extract_dir=None):
        """解压tar.gz文件"""
        if extract_dir is None:
            extract_dir = self.output_dir / Path(tar_path).stem
        
        extract_dir = Path(extract_dir)
        extract_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=extract_dir)
            return extract_dir
        except (tarfile.TarError, IOError) as e:
            print(f"解压失败: {e}")
            return None

    def cleanup(self, path):
        """清理临时文件"""
        try:
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                import shutil
                shutil.rmtree(path)
        except Exception as e:
            print(f"清理失败: {e}")

if __name__ == "__main__":
    downloader = ArXivDownloader()
    test_id = "0704.0001"  # arXiv测试用ID
    tar_file = downloader.download(test_id)
    if tar_file:
        extract_path = downloader.extract(tar_file)
        print(f"文件已解压到: {extract_path}")
