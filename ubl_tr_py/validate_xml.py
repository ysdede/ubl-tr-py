# Get xml filename from command line and assert validate with xsd file using lxml

import sys
import os
import lxml.etree as etree

cwd = os.getcwd()
file_path = os.path.join(cwd, "UBLTR_1.2.1_Paketi", "xsdrt", "maindoc", "UBL-Invoice-2.1.xsd")

print(file_path)


# Parse the XSD schema
schema_doc = etree.parse(file_path)
schema = etree.XMLSchema(schema_doc)

# Parse the XML file
doc = etree.parse(sys.argv[1])

# Validate the XML file against the XSD schema
schema.assertValid(doc)
