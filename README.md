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
