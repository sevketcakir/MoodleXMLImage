# MoodleXMLImage
MoodleXMLImage is an application that can read a quiz in Aiken format and export it into Moodle XML format with embedded images. The purpose of the application is to prevent copying exam questions and pasting them into chatbots like ChatGPT. Although images can be pasted in ChatGPT plus at the moment, it is a proprietary and limited service which is not everyone can get access.

## Installation
There is a compiled executable version for any major operating systems in [Releases](https://github.com/sevketcakir/MoodleXMLImage/releases) section.

If you want to run it from the sources you need to have Python installed and install required Python packages and run like below in the terminal window:
```bash
# Download files via git or you can download them from the website
git clone https://github.com/sevketcakir/MoodleXMLImage.git
# Enter the application directory
cd MoodleXMLImage
# Install required Python packages
pip install -r requirements.txt
# Run the application
python3 main.py
```

## Usage
The application can only read text files with Aiken format at the moment. Aiken format is a quiz format that has a one line question, choices with respective names such as (A, B, C, etc.) and the correct answer line like below:
```
The question must be in a single line. If you want to add multiple lines, you should add \n between lines. You can enter choices from A to Z(generally it is up to E). This is a long question, it might seem to have multiple lines, but it is in a single line. Let's assume the correct answer is C.
A. an answer
B. wrong answer
C. right one
D. not so right
E. final choice
ANSWER: C
```

You can have code blocks in the questions and answers. They are highlighted using the pygments package. An example with code blocks inside is given below(All in one line, change newlines with \n and tabs with \t):
```
This question is about multi line code blocks. What is the output of the Python code below?`python`def secret(n):\n    if n < 2:\n        return 1\n    return secret(n-1) + secret(n-2)\n\nsecret(7)\n`
A. 21
B. 8
C. 5
D. 34
E. 13
ANSWER: A
```

Steps in a common workflow:
1. Prepare the quiz as text file(s) in Aiken format
2. Open the text file in the application
3. Check export settings
4. Export the file into XML format
5. Import the XML from Moodle as "Moodle XML Format"

![Usage Example](images/usage.gif)


## LICENSE
The software is licensed under GPL(General Public License). Please use it at your own risk.
There are fonts in the application that has Open Font License such as [Inconsolata](https://github.com/sevketcakir/MoodleXMLImage/blob/main/fonts/Inconsolata/OFL.txt).