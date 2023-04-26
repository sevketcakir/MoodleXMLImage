from xml.dom import minidom
from reader import *
from utility import *
import xml.etree.ElementTree as ET
import base64
from PIL import Image
from io import BytesIO
from image_creator import *

############# stackoverflow #####################
ET._original_serialize_xml = ET._serialize_xml

def serialize_xml_with_CDATA(write, elem, qnames, namespaces, short_empty_elements, **kwargs):
    if elem.tag == 'CDATA':
        write("<![CDATA[{}]]>".format(elem.text))
        return
    return ET._original_serialize_xml(write, elem, qnames, namespaces, short_empty_elements, **kwargs)


ET._serialize_xml = ET._serialize['xml'] = serialize_xml_with_CDATA


def CDATA(text):
   element =  ET.Element("CDATA")
   element.text = text
   return element
############# stackoverflow #####################

class XMLSaver:
    def __init__(self, settings=None) -> None:
        if settings is None:
            settings=Settings()
        self.settings = settings

    def save(self, quiz:Quiz, filename:str):
        root = ET.Element("quiz")
        for question in quiz.questions:
            qx = ET.SubElement(root, "question", {"type": "multichoice"})

            qname = ET.SubElement(qx, "name")
            qname = ET.SubElement(qname, "text")
            qname.text = question.text[:100]
            qshuffle = ET.SubElement(qx, "shuffleanswers")
            qshuffle.text = "true"
            qcontent = ET.SubElement(qx, "questiontext")
            qfile = ET.SubElement(qcontent, "file", {"name": "image.png", "path":"/", "encoding":"base64"})
            qcontent = ET.SubElement(qcontent, "text")
            #qcontent.text = '<![CDATA[<img src="@@PLUGINFILE@@/image.png"/>]]'
            qcontent.append(CDATA('<img src="@@PLUGINFILE@@/image.png"/>'))
            ic = ImageCreator(settings=self.settings)
            image = ic.image(question.text)
            qfile.text = self.convert_image_to_base64(image)

            #qcontent.text = question.text
            for choice in question.choices:
                cx = ET.SubElement(qx, "answer", {"fraction": "100" if choice.correct else "0"})
                ctext = ET.SubElement(cx, "text")
                ctext.append(CDATA('<img src="@@PLUGINFILE@@/image.png"/>'))
                cfile = ET.SubElement(cx, "file", {"name": "image.png", "path":"/", "encoding":"base64"})
                cimage = ic.image(choice.text)
                cfile.text = self.convert_image_to_base64(cimage)
                #cx.text = choice.text

        # tree = ET.ElementTree(root)
        # ET.indent(tree, space="\t", level=0)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
        with open(filename, "wb") as f:
            #tree.write(f, xml_declaration=True, encoding="utf-8")
            f.write(xmlstr.encode("utf-8"))

    def convert_image_to_base64(self, image:Image):
        im_file = BytesIO()
        image.save(im_file, format='PNG')
        im_bytes = im_file.getvalue()
        return base64.b64encode(im_bytes).decode("utf-8")


if __name__ == "__main__":
    reader = AikenReader()
    quiz = reader.read_from_file("examples/chapter1.txt")
    XMLSaver().save(quiz, "text.xml")