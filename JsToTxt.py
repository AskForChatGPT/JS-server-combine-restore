import os

def collect_files(directory):
    css_files = []
    html_files = []
    js_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
            elif file.endswith('.html'):
                html_files.append(os.path.join(root, file))
            elif file.endswith('.js'):
                js_files.append(os.path.join(root, file))
    
    return css_files, html_files, js_files

def write_to_txt(directory):
    dir_name = os.path.basename(os.path.abspath(directory))
    output_file = f"{dir_name}[ViewAll].txt"
    
    css_files, html_files, js_files = collect_files(directory)
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Write CSS files
        for file_path in css_files:
            rel_path = os.path.relpath(file_path, directory).replace(os.sep, '/')
            marker = f"<!--{rel_path}-->"
            out_file.write(f"{marker}\n")
            with open(file_path, 'r', encoding='utf-8') as f:
                out_file.write(f.read())
            out_file.write(f"\n{marker}\n")
        
        # Write HTML files
        for file_path in html_files:
            rel_path = os.path.relpath(file_path, directory).replace(os.sep, '/')
            marker = f"<!--{rel_path}-->"
            out_file.write(f"{marker}\n")
            with open(file_path, 'r', encoding='utf-8') as f:
                out_file.write(f.read())
            out_file.write(f"\n{marker}\n")
        
        # Write JS files
        for file_path in js_files:
            rel_path = os.path.relpath(file_path, directory).replace(os.sep, '/')
            marker = f"<!--{rel_path}-->"
            out_file.write(f"{marker}\n")
            with open(file_path, 'r', encoding='utf-8') as f:
                out_file.write(f.read())
            out_file.write(f"\n{marker}\n")

if __name__ == "__main__":
    current_dir = os.getcwd()
    write_to_txt(current_dir)