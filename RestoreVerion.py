import os
import re
import argparse
from pathlib import Path

def process_template_file(template_path):
    # 读取模板文件
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 <!--path/filename.ext-->内容<!--path/filename.ext--> 格式
    pattern = r'<!--([a-zA-Z0-9_/.-]+)-->(.*?)<!--\1-->'
    file_blocks = re.findall(pattern, content, re.DOTALL)
    
    for file_path, file_content in file_blocks:
        # 清理内容（去除前后空白）
        file_content = file_content.strip()
        
        # 检查是否是有效的文件路径（包含扩展名）
        if not re.search(r'\.\w+$', file_path):
            print(f"跳过非文件路径的标记: {file_path}")
            continue
            
        # 创建目录（如果需要）
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"已成功写入文件: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='根据模板文件更新对应文件')
    parser.add_argument('template_file', help='模板文件路径')
    args = parser.parse_args()
    
    if not os.path.exists(args.template_file):
        print(f"错误: 文件 {args.template_file} 不存在")
        exit(1)
    
    print(f"正在处理文件: {args.template_file}")
    process_template_file(args.template_file)