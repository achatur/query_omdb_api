# query_omdb_api

## Prerequisite 
Must have API key from http://www.omdbapi.com
Edit docker/images/query_omdb_api/query_omdb_api.py
change:
line 24: return 'new_key`

docker build --tag query_omdb_api docker/images/query_omdb_api/

docker run --rm -it query_omdb_api
