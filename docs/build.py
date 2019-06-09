import os
import json

from pathlib import Path


# List of includes

include = {}
for file in os.listdir("./include"):
    information = os.path.splitext(file)
    if information[1] == ".html":
        include[information[0]] = Path(os.path.join("./include", file)).read_text()

# List of variables

variables = json.loads(Path(os.path.join("./", "variables.json")).read_text())

# Replace content

for file in os.listdir("./pages"):
    information = os.path.splitext(file)
    if information[1] == ".html":
        data = Path(os.path.join("./pages", file)).read_text()
        for key, value in include.items():
          data = data.replace("{{ " + key + " }}", value)
        for key, value in variables.items():
          data = data.replace("[[ " + key + " ]]", value)
        with open(os.path.join("./", file), "w") as new_file:
          new_file.write(data)
