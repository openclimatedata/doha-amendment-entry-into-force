
import os
import re
import sys
import xml.etree.ElementTree as ET

import countrynames
import pandas as pd
import requests


print("Doha Amendment to the Kyoto Protocoll")
path = os.path.dirname(os.path.realpath(__file__))
treaty_url = "https://treaties.un.org/doc/Publication/MTDSG/Volume%20II/Chapter%20XXVII/XXVII-7-c.en.xml"
outfile = os.path.join(path, "../data/doha-amendment.csv")
print("Fetching ", treaty_url)
r = requests.get(treaty_url)

if "urgent maintenance and is currently unavailable" in r.text:
    print("\nNo data found.")
    print("\nMaybe https://treaties.un.org/Pages/ViewDetails.aspx?"
          "src=TREATY&mtdsg_no=XXVII-7-c&chapter=27&clang=_en is down?")
    sys.exit()


xml = r.text
tree = ET.fromstring(xml)
rows = tree.find("Treaty/Participants/Table/TGroup/Tbody/Rows")

entries = []
for row in rows:
    # Remove footnotes from country names.
    name = re.sub('<superscript>.</superscript>', '', row[0].text)
    # Parse dates, remove " A" from end of string.
    date = pd.to_datetime(row[1].text.replace("\t", "")[:-2])
    entries.append((name, date,))

df = pd.DataFrame.from_records(entries, columns=('Name', 'Acceptance'))
df.index = df.Name.apply(countrynames.to_code_3)
df.index.name = "Code"

df.to_csv(outfile)

print("Count: {}".format(df.Name.count()))
print("Last five entries:")
print(df.sort_values("Acceptance").tail(5))
