
from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
from pathlib import Path
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No header available...")
        
def generate_pages_recursive(dir_path_content, template_path, dest_path_content):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        new_dest_path = os.path.join( dest_path_content, entry)
        if os.path.isfile(full_path) and full_path.endswith(".md"):
            html_dest_path = Path(new_dest_path).with_suffix(".html")
            print(f"about to generate: {full_path}")
            generate_page(full_path, template_path, html_dest_path)
        elif os.path.isdir(full_path):
                print(f"recursing into: {full_path}")
                generate_pages_recursive(full_path, template_path, new_dest_path)
            
def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as c:
        from_path_contents = c.read()
    with open(template_path) as c:
        template_path_contents = c.read()
    
    html_string = markdown_to_html_node(from_path_contents).to_html()
    print(f"extracting title from {from_path}")
    extracted_from_path_content = extract_title(from_path_contents)
    new_template_contents = template_path_contents.replace("{{ Title }}", extracted_from_path_content)
    new_from_path_contents = new_template_contents.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_from_path_contents)
