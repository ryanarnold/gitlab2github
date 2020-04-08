# Output created using:
# curl --header "Private-Token: KyQ3zGios3TX5sqBACQs" "https://gitlab.com/api/v4/projects/?owned=true&per_page=500" > projects.json

import json
import csv

with open('projects.json') as projects_file:
    projects =  json.load(projects_file)

with open('projects.csv', 'w', newline='') as projects_csv:
    writer = csv.writer(projects_csv, delimiter=',')
    for p in projects:
        writer.writerow([
            p['name'],
            p['description'],
            p['created_at'][:10],
            p['web_url'],
            p['http_url_to_repo']
        ])
