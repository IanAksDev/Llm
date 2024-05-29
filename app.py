import requests

url = 'http://localhost:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt":"¿Por qué el cielo es azul?",
  "stream": False
}
x = requests.post(url, json = myobj)

print(x.text)