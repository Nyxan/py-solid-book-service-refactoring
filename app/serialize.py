import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = content
        return ElementTree.tostring(root, encoding="unicode")
