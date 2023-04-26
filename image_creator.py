from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import re
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.styles.gh_dark import GhDarkStyle

class Settings:
    def __init__(self,
                 font_name="/home/cakir/.local/share/fonts/static/Inconsolata/Inconsolata-Medium.ttf",
                 font_size=20,
                 image_width=600,
                 text_width=60,
                 background_color='midnightblue',
                 color="white",
                 code_style="native",
                 line_numbers=True
                 ) -> None:
            self.font_name = font_name
            self.font_size = font_size
            self.line_height = font_size
            self.font = ImageFont.truetype(self.font_name, self.font_size)
            self.image_width = image_width
            self.text_width = text_width
            self.background_color = background_color
            self.color = color
            self.code_style = code_style
            self.line_numbers = line_numbers

class ImagePart():
    def __init__(self, content, settings=None) -> None:
        self.content = content
        if settings is None:
            self.settings = Settings()
        else:
            self.settings = settings
        self.image_height = None
        self.image = None
    def create_image(self, **kwargs):
        pass
    
    def get_image(self):
        return self.image

class TextPart(ImagePart):

    def __init__(self, content:str, settings=None) -> None:
        if settings is None:
            self.settings = Settings()
        else:
            self.settings = settings
        super().__init__(content, settings=settings)
        lines = []
        wrapper = textwrap.TextWrapper(width=self.settings.text_width)
        for splitted in self.content.split("\\n"):
            lines.extend(wrapper.wrap(splitted))
        self.text = '\n'.join(lines)
        self.image_height = self.settings.line_height * (len(lines) + 2)

    def create_image(self, **kwargs) -> Image:
        self.image = Image.new(mode="RGBA", size=(self.settings.image_width, self.image_height), color=self.settings.background_color)
        draw = ImageDraw.Draw(self.image)
        draw.text((self.settings.line_height//2, self.settings.line_height//2), self.text, fill=self.settings.color, font=self.settings.font)
        return self.image

class CodePart(ImagePart):
    def __init__(self, language, code, settings=None) -> None:
        if settings is None:
            self.settings = Settings()
        else:
            self.settings = settings
        super().__init__(f"`{language}`{code}`", settings=settings)
        self.language = language
        self.code = code.replace("\\n","\n").replace("\\t", "\t")
    def create_image(self, **kwargs):
        try:
            lexer = get_lexer_by_name(self.language)
            formatter = ImageFormatter(style=self.settings.code_style, line_numbers=self.settings.line_numbers)
            highlighted = highlight(self.code, lexer, formatter)
            self.image = Image.open(BytesIO(highlighted))
            return self.image
        except:
            return None
        
class ImageCreator():
    def __init__(self, settings=None) -> None:
        if settings is None:
            self.settings = Settings()
        else:
            self.settings = settings

    def parse_input_string(self, input_string):
        parts = []
        pos = 0
        while pos < len(input_string):
            match = re.search(r'`(?P<language>\w+)`(?P<code>[^`]+)`|(?P<text>[^`]+)', input_string[pos:])
            if match is not None:
                if match.group('code') is not None:
                    parts.append(CodePart(match.group('language'), match.group('code'), settings=self.settings))
                else:
                    parts.append(TextPart(match.group('text'), settings=self.settings))
                pos += len(match.group(0))
            else:
                break
        return parts


    def image(self, text:str):
        parts = self.parse_input_string(text)

        total_height = 0
        for part in parts:
            img = part.create_image()
            total_height += img.height

        img = Image.new(mode="RGBA", size=(self.settings.image_width, total_height))
        height = 0
        for part in parts:
            img.paste(part.get_image(), (0,height))
            height += part.get_image().height
      
        # img.show()
        return img


if __name__ == "__main__":
    text = "Aşağıdakilerden hangisi lambda hesabına(lambda calculus) hesaplama modeline dayanan bir dildir? \\nAşağıdaki dil çiftlerinden hangisi esinlenildiği dil bakımından YANLIŞ verilmiştir?\\nI. bir madde\\nII. ikinci madde\\nIII. 3. madde"
    code = "`python`def print():\\n\\tpass\\n`"
    code2 = "`scheme`(\\n\\tcar \\n\\t\\t(cdr L)\\n)`"
    code3 = "`python`def create_tests():\\n    test1 = list(range(10))\\n    if 5 in test1:\\n        print(\"Test failed!!!\")\\n`"
    text2 = text + code + text + code3 + code
    #print(text2)
    # import fontconfig
    # fonts = fontconfig.query(lang='en')
    # for i in range(1, len(fonts)):
    #     if fonts[i].fontformat == 'TrueType':
    #         absolute_path = fonts[i].file
    #         break
    ic = ImageCreator(settings=Settings(font_name="DejaVuSerif.ttf"))
    image = ic.image(text2)
    image.show()

