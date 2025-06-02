import xml.etree.ElementTree as ET
import os

def invert_file(svg_file, output_file):

    ET.register_namespace("","http://www.w3.org/2000/svg")

    tree = ET.parse(svg_file)
    root = tree.getroot()

    def invert_color(color):
        if color.lower() in ['black', '#000', '#000000']:
            return 'white'
        elif color.lower() in ['white', '#fff', '#ffffff']:
            return 'black'
        elif color.lower().startswith('#') and len(color) == 7:
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            if r == 0 and g == 0 and b == 0:
                return '#ffffff'
        elif color.lower().startswith('#') and len(color) == 7:
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            if r == 0xff and g == 0xff and b == 0xff:
                return '#000000'
        return color

    for elem in root.iter():
        if 'fill' in elem.attrib:
            elem.attrib['fill'] = invert_color(elem.attrib['fill'])

        if 'stroke' in elem.attrib:
            elem.attrib['stroke'] = invert_color(elem.attrib['stroke'])

        if 'stop-color' in elem.attrib:
            elem.attrib['stop-color'] = invert_color(elem.attrib['stop-color'])

    tree.write(output_file, encoding='utf-8') #xml_declaration=True

script_dir = os.path.dirname(os.path.abspath(__file__))

light_dir = os.path.join(script_dir, 'Onigiri', 'icons', 'light')
dark_dir = os.path.join(script_dir, 'Onigiri', 'icons', 'dark')

print("Converting "+light_dir+"\n")
for root, dirs, files in os.walk(light_dir):
    for file in files:
        if file.endswith(".svg"):
            print("Converting "+file)
            invert_file(os.path.join(light_dir, file), os.path.join(dark_dir, file))