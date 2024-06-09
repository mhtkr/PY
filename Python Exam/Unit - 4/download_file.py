import requests

url = "https://djyoungster.us/music/320/Single-Tracks/April(2024)/Channa%20Jayi%20Na%20Kuldeep%20Manak.mp3"

response = requests.get(url)

print(response)

file_name = url.split('/')[-1]
with open(file_name, 'wb') as f:
    f.write(response.content)