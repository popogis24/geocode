import requests


r = requests.get('https://geocode.search.hereapi.com/v1/geocode?q=Invalidenstr+117+Berlin&apiKey=-dfJYn8-HT_zeiS6OApYAqXLG1zmq6oUFolqf3XJg0k')

print(r.json())
