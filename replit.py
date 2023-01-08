import threading
import requests

c = 0
semaphore = threading.Semaphore(10)

def check_username(username):
  semaphore.acquire()
  try:
    url = 'https://replit.com/@' + username
    x = requests.get(url)
    if x.status_code == 200:
      pass
    if x.status_code == 404:
      print(username, 'Is Available')
      found.append(username)
  finally:
    semaphore.release()

with open("users.txt", "r") as f:
  lines = f.readlines()
  found = []

threads = []
for word in lines:
  if c != len(lines):
    word = word[:-1]
  t = threading.Thread(target=check_username, args=(word,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

with open("hits.txt", "w") as f:
  for i in found:
    if i == None:
      break
    f.write(i + str("\n"))
