# curl --header "Private-Token: KyQ3zGios3TX5sqBACQs" "https://gitlab.com/api/v4/projects/?owned=true&per_page=500" > projects.json

import requests
import xlrd
import os
import json

# Constants
subdir = {
    'LOCAL ONLY': 'local',
    'GITHUB PRIVATE': 'private',
    'GITHUB PUBLIC': 'public',
}
headers = {'Private-Token': 'KyQ3zGios3TX5sqBACQs'}
delete_url = 'https://gitlab.com/api/v4/projects/ryanarnold%2f'

if __name__ == '__main__':
    excel_file_path = 'projects.xlsx'

    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        name = sheet.cell_value(row, 0)
        project_path = sheet.cell_value(row, 4).split('/')[-1]

        url = delete_url + project_path

        print(f'Deleting {url}')
        response = requests.delete(url, headers=headers)
        print(json.loads(response.text)['message'])
