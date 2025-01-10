from abc import ABC, abstractmethod

# Produkt
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


# Konkretne produkty
class WebButton(Button):
    def render(self):
        return "<button>Web Button</button>"


class DesktopButton(Button):
    def render(self):
        return "[Desktop Button]"


# Fabryka abstrakcyjna
class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


# Konkretne fabryki
class WebButtonFactory(ButtonFactory):
    def create_button(self):
        return WebButton()


class DesktopButtonFactory(ButtonFactory):
    def create_button(self):
        return DesktopButton()


# Klient
def render_button(factory: ButtonFactory):
    button = factory.create_button()
    print(button.render())


# Testowanie
web_factory = WebButtonFactory()
desktop_factory = DesktopButtonFactory()

print("Web Button:")
render_button(web_factory)
