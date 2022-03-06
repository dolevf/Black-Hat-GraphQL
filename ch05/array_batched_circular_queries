# Array-based Query Batching with Circular Queries

import requests

appends = 5

query = {"query":"query { pastes { owner { pastes { owner { pastes { owner { name } } } } } } }"}
queries = []

for _ in range(appends):
  queries.append(query)

r = requests.post('http://localhost:5013/graphql', json=queries)

print(r.json())
