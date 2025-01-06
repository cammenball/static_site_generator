from textnode import TextType, TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and 
            self.value == other.value and 
            self.children == other.children and 
            self.props == other.props
    )


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        x = None
        if self.props == None:
            return None
        for key, value in self.props.items():
            if x == None:
                x = f' {key}="{value}"'
            else:
                x = x + f' {key}="{value}"'
        return x
    def __repr__(self):
        return f"{self.tag}|{self.value}|{self.children}|{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            x = ""
            for key, value in self.props.items():
                x = x + f' {key}="{value}"'
            return f'<{self.tag}{x}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        HTMLNode.__init__(self,tag,props)
        self.children = children
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("no value")
        string = f'<{self.tag}>'
        for i in self.children:
            string = string + i.to_html()
        string = f"{string}</{self.tag}>"
        return string

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text,None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text,None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i",text_node.text,None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text,None)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text,{"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img","",{"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("no valid TextType")
    