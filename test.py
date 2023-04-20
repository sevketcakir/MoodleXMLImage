from xml.dom import minidom
from reader import *
from utility import *
import xml.etree.ElementTree as ET

class XMLSaver:
    def __init__(self) -> None:
        pass

    def save(self, quiz:Quiz, filename:str):
        root = ET.Element("quiz")
        for question in quiz.questions:
            qx = ET.SubElement(root, "question", {"type": "multichoice"})


        tree = ET.ElementTree(root)
        # ET.indent(tree, space="\t", level=0)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
        with open(filename, "wb") as f:
            #tree.write(f, xml_declaration=True, encoding="utf-8")
            f.write(xmlstr.encode("utf-8"))


if __name__ == "__main__":
    reader = AikenReader()
    quiz = reader.read_from_file("examples/chapter1.txt")
    XMLSaver().save(quiz, "text.xml")