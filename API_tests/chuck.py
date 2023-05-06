import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(result.text)
assert 200 == result.status_code
print("Успешно!!! Мы получили новую шутку")
result.encoding = 'utf-8'
print('Статус код ' + str(result.status_code))
