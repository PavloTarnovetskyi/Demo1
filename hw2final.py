'''
Task: There are a set of JSON-files that contains answers from the CI server.
 An example of such is attached hw2_example.json. 
 Create a program that returns JSON-file which contains 'id', 'number', 'committer_name' and 'committer_email' from last of failed builds
 (in other words - with the highest value of 'number' and non-zero 'result').
Program name: hw2.py
Input parameters: path_to_files, path_to_result
Example: python hw2.py /home/usr/data_json /home/usr/result.json
Result of example run: it reads all files on the path /home/usr/data_json and writes on the file /home/usr/result.json the necessary information like this:
{"id": 22, "number": "34", "committer_name": "Some Commiter", "committer_email": "some.commiter@gmail.com"}
'''

import os, sys, json

path_to_files = sys.argv[1]
json_file_name = sys.argv[2]

result = {
    'id': 0, 'number': '0', 'committer_name': '', 'committer_email': ''
}

file_list = os.listdir(path_to_files)

for current_file in file_list:
    current_file_descriptor = open(path_to_files + '/' + current_file )
    json_data = json.load(current_file_descriptor)
    if json_data['result'] != 0:
        if int(json_data['number']) > int(result['number']):
            result['id'] = json_data['id']
            result['number'] = json_data['number']
            result['committer_name'] = json_data['committer_name']
            result['committer_email'] = json_data['committer_email']
    current_file_descriptor.close()

json_file_descriptor = open(json_file_name, 'w+')
json_file_descriptor.write(json.JSONEncoder().encode(result))
json_file_descriptor.close()




