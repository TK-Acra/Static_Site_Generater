from textnode import TextNode, TextType
import os, shutil, sys
from copy_static import copy_from_static_recursive
from gencontent import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
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
    print("Deleting docs...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)   
    os.mkdir(dir_path_docs)  # add this line

    print("Copying static files to docs directory...")
    copy_from_static_recursive(dir_path_static, dir_path_docs)

    basepath = "/"

    if len(sys.argv) > 1 :
        basepath = sys.argv[1]

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)
main()
