import requests
import json


endpoint = "http://localhost:4200/graphql"

query = """query {
  users {
	  name
	  email
	  posts  {	
          title
    }
  }
}"""

r = requests.post(endpoint, json={"query": query})
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))
else:
    raise Exception(f"Query failed to run with a {r.text}.")
