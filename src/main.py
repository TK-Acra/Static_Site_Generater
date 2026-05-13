from textnode import TextNode, TextType
import os, shutil
from copy_static import copy_from_static_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

# def main():
#     if os.path.exists("public"):
#         shutil.rmtree("public")
#     os.mkdir("public")
#     copy_from_static_recursive("static", "public")
#     # generate_page("content/index.md", "template.html", "public/index.html")
#     generate_pages_recursive("content", "template.html", "public")


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)      
    os.mkdir(dir_path_public)  # add this line

    print("Copying static files to public directory...")
    copy_from_static_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
main()
