class Node:
    """Bazowa klasa reprezentująca węzeł."""
    def render(self, indent=0):
        raise NotImplementedError("Subclasses must implement render()")


class TextNode(Node):
    """Liść: Węzeł tekstowy."""
    def __init__(self, text):
        self.text = text

    def render(self, indent=0):
        return ' ' * indent + self.text


class ElementNode(Node):
    """Kompozyt: Węzeł elementu."""
    def __init__(self, tag):
        self.tag = tag
        self.attributes = {}
        self.children = []

    def set_attribute(self, name, value):
        """Ustaw atrybut elementu."""
        self.attributes[name] = value
        return self  # Fluent Interface

    def add_child(self, child):
        """Dodaj dziecko do elementu."""
        self.children.append(child)
        return self  # Fluent Interface

    def render(self, indent=0):
        attrs = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        result = ' ' * indent + f"<{self.tag}{attrs}>\n"
        for child in self.children:
            result += child.render(indent + 2) + "\n"
        result += ' ' * indent + f"</{self.tag}>"
        return result


class DOMDocument:
    """Klasa zarządzająca dokumentem."""
    def __init__(self):
        self.root = None

    def create_element(self, tag):
        return ElementNode(tag)

    def create_text_node(self, text):
        return TextNode(text)

    def set_root(self, root):
        self.root = root
        return self  # Fluent Interface

    def render(self):
        if not self.root:
            return ""
        return self.root.render()

doc = DOMDocument()

root = doc.create_element("html")
body = doc.create_element("body").set_attribute("class", "main-body")
p = doc.create_element("p").set_attribute("id", "intro")
text = doc.create_text_node("Hello, World!")

p.add_child(text)
body.add_child(p)
root.add_child(body)

doc.set_root(root)

print(doc.render())