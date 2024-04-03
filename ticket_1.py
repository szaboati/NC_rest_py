import http.client

conn = http.client.HTTPConnection("localhost:58000")

payload = "{\n    \"username\": \"Oadmin\",\n    \"password\": \"q1w2e3\"\n}\n"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/api/v1/ticket", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))