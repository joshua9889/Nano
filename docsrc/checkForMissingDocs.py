"""
This script scans the docs folder and alerts you of any
missing markdown files that should be added to mkdocs.yml
"""

import os

doc = None
with open('./mkdocs.yml') as f:
	doc = f.read()

listOfFiles = os.listdir("./docs");
	
for file in listOfFiles:
	if os.path.isfile("./docs/" + file) and file not in doc:
		print file