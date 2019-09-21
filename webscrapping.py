import requests
import json
import time


r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()
# print(packages_json)


results = []

for i in packages_json:
    package_name = i['name']
    package_decr = i['desc']
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

    r = requests.get(package_url)
    package_json = r.json()


    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]
    
    data = {
        'name': package_name,
        'desc': package_decr,
        'analytics': {
            '30d':installs_30,
            '90d':installs_90,
            '365d':installs_365,
        }
    }
    
    results.append(data)
    time.sleep(r.elapsed.total_seconds())
    
    break
    
    print(package_name, package_decr, installs_30, installs_90, installs_365)

    
print(results)


with open('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)