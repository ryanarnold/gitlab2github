
import requests
import xlrd

# Constants

headers = {
    'Accept': 'application/vnd.github.nebula-preview+json',
    'Authorization': 'token a9095934a3820fe5986dd521eeffb499631352c5 '
}

url = 'https://api.github.com/user/repos'

visibility_table = {
    'GITHUB PRIVATE': True,
    'GITHUB PUBLIC': False
}


if __name__ == '__main__':
    excel_file_path = 'projects.xlsx'

    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        todo = sheet.cell_value(row, 2)
        private = False

        if todo == 'LOCAL ONLY':
            continue

        params = {
            'name': sheet.cell_value(row, 1),
            'description': sheet.cell_value(row, 3),
            'private': visibility_table[todo]
        }

        print(f"Creating repository for {params['name']}")
        response = requests.post(url, headers=headers, json=params)
        print(response)
