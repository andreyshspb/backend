# Database Running

```
docker-compose build
docker-compose up
```

# Application Running

```
fastapi run
```

# Test Running

```
python -m pytest
```

# GraphQL Running

Run application 
```
fastapi run
```

Go to:
```
http://127.0.0.1:8000/notes
```

Put next query and run:
```
{
  getNotes(offset: 0, count: 2) {
    topic,
    content,
    author {
      name,
      surname
    }
  }
}
```

# Rabbit testing

Run general application
```
fastapi run
```

Run statistics application
```
cd app/statistics_service
uvicorn main:app --reload --port 8080
```

Make post creation request
```
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"author_id": 1, "topic": "fuck", "content": "fuck"}' \
     http://127.0.0.1:8000/create/note
```

Make get statistics request. It returns some topic
```
curl --request GET http://127.0.0.1:8080/get/statistics/
```
