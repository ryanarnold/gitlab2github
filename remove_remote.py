import os

def remove_remote(repos_dir):
    for subdir, dirs, files in os.walk(repos_dir):
        for repo in dirs:
            print(f'Removing remote for {repo}')
            os.chdir(f'{subdir}\{repo}')
            os.system(f'git remote remove origin')
        break


if __name__ == '__main__':
    local_root_dir = r'C:\Users\ryana\Desktop\Projects\gitlab2github\local'
    private_root_dir = r'C:\Users\ryana\Desktop\Projects\gitlab2github\private'
    public_root_dir = r'C:\Users\ryana\Desktop\Projects\gitlab2github\public'

    remove_remote(local_root_dir)
    remove_remote(private_root_dir)
    remove_remote(public_root_dir)
