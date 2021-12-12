from metrics_client.client import Client

client = Client("127.0.0.1", 1337, timeout=15)
print(client.get("*"))
