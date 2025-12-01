import xml.etree.cElementTree as ET #Does most of the work for us
data = '''<person>
    <name>Arjun</name>
    <phone type= "intl">
        +1 123 456 7890
    </phone>
    <email hide= "yes"
</person>'''

tree = ET.fromstring(data)
print('Name:' ,tree.find('name').text)
print('Attr:' ,tree.find('email').get('hide')) #tree.find finds specific elements/tags within XML
