import json
import sys

from subprocess import check_output

import tools

program_out = check_output(["soundmeter","--collect","--seconds",sys.argv[1]])
clean_program_data = tools.clean_text(program_out)

with open('output/output.json', 'w') as outfile:
    json.dump(clean_program_data, outfile)
