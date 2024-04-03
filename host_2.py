ticket = "NC-9-ab380830e08640d6a468-nbi"

import http.client

conn = http.client.HTTPConnection("localhost:58000")

headers = { 'X-Auth-Token': ticket }

conn.request("GET", "/api/v1/host", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))