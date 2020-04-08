
import os
import xlrd

def retrieve_repo_new_name(repo_old_name):
    excel_file_path = 'projects.xlsx'

    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        old_name = sheet.cell_value(row, 0)
        new_name = sheet.cell_value(row, 1)

        if old_name == repo_old_name:
            workbook.release_resources()
            return new_name

def add_remote(repos_dir):
    for subdir, dirs, files in os.walk(repos_dir):
        for repo in dirs:
            repo_new_name = retrieve_repo_new_name(repo)
            repo_url = f'https://github.com/ryanarnold/{repo_new_name}.git'

            print('##########################################################')
            print(f'Adding remote for {repo_new_name}')
            print(f'URL: {repo_url}')

            os.chdir(f'{subdir}\{repo}')
            os.system(f'git remote add origin {repo_url}')
            os.system('git push -u origin master')
            os.chdir(f'..\..')
        break


if __name__ == '__main__':
    private_root_dir = r'C:\Users\ryana\Desktop\Projects\gitlab2github\private'
    public_root_dir = r'C:\Users\ryana\Desktop\Projects\gitlab2github\public'

    add_remote(private_root_dir)
    add_remote(public_root_dir)
