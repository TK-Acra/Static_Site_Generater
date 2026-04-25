from textnode import TextNode, TextType

def main():
	print_text = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")
	print (print_text)


main()


