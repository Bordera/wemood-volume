import json
import sys

from subprocess import check_output
from datetime import datetime as dt
from pymongo import MongoClient

import tools

client = MongoClient()
db = client.wemood

program_out = check_output(["soundmeter","--collect","--seconds",sys.argv[1]])
clean_program_data = tools.clean_text(program_out)

clean_program_data["date"] = unicode(dt.now())
clean_program_data["sensor"] = "volume"

db.sensors.insert_one(clean_program_data)

with open('output/output.json', 'w') as outfile:
    json.dump(clean_program_data, outfile)
