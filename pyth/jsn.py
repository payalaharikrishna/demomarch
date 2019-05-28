employee = eval(input('enter employee data in {}'))
import json
str=json.dumps(employee)

with open('jsondata.txt' ,'w') as f:
    f.write(str(employee))
