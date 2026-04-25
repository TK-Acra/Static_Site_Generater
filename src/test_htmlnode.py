import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

#HtmlNode Tests

class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag = "a", value = "click here", props = {"href": "https://google.com"})
        node2 = HTMLNode(tag = "a", value = "click here", props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"') 
        self.assertEqual(node2.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode(tag = "a", value = "click here", props={})
        node2 = HTMLNode(tag = "a", value = "click here", props=None)
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")     

    def test_not_implement_error(self):
        node = HTMLNode()
        with self.assertRaises((NotImplementedError)):
            node.to_html()
    
    
    #LeafNode Tests
     
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')


    #ParentNode Tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_tag(self):
        child_node = LeafNode("b", "hello")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_multiple_children(self):
        child_node1 = LeafNode("b", "hello")
        child_node2 = LeafNode("p", "hello")
        child_node3 = LeafNode("b", "bye")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3,])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>hello</b><p>hello</p><b>bye</b></div>"
        )
    
    def test_props(self):
        child_node = LeafNode("b", "hello" )
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><b>hello</b></div>'
        )