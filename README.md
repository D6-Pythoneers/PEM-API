# PEM-API

Performance Evaluation Manager Api

**Version :** v1

## API end points

baseUrl : `https://pem-api.herokuapp.com/`

```python
schools/
teachers/
evaluations/
evaluations/<int:pk>
goals/
goals/<int:pk>
assesments/
assesments/<int:pk>
```

### Good URL examples

- Schools list:
  - Get `https://pem-api.herokuapp.com/schools/`

- Teacher list:
  - Get `https://pem-api.herokuapp.com/teachers/`

- Evaluation list:
  - Get `https://pem-api.herokuapp.com/evaluations/`

- Specific evaluations:
  - Get `https://pem-api.herokuapp.com/evaluations/2`

- Create Assessment :
  - Post `https://pem-api.herokuapp.com/assesments/`

### Bad URL examples

- Non-plural noun:
  - `https://pem-api.herokuapp.com/school/`
  - `https://pem-api.herokuapp.com/evaluations/2`

- Choose non-exist is:
  - `https://pem-api.herokuapp.com/evaluations/200`

### Responses

Use three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:

- 200 - OK
- 400 - Bad Request
- 500 - Internal Server Error

**Good example :** `GET /schools/`

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "school_id": 1,
        "school_manager": 3,
        "school_name": "Amman first school",
        "evaluated": false,
        "academic_year": "2021"
    },
    {
        "school_id": 2,
        "school_manager": 4,
        "school_name": "Amman second school",
        "evaluated": false,
        "academic_year": "2021"
    }
]
```

**Bad example :** `GET /evaluations/5`

```json
HTTP 404 Not Found
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Not found."
}
```

### Request & Response Examples

#### API Resources

- [GET /schools/](#get-schools)
- [GET /evaluations/[id]](#get-specific-evaluation)
- [Post /goals/](#post-goals)

#### Get Schools

**Example :** `GET /schools/`

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "school_id": 1,
        "school_manager": 3,
        "school_name": "Amman first school",
        "evaluated": false,
        "academic_year": "2021"
    },
    {
        "school_id": 2,
        "school_manager": 4,
        "school_name": "Amman second school",
        "evaluated": false,
        "academic_year": "2021"
    },
    {
        "school_id": 3,
        "school_manager": 6,
        "school_name": "Amman third school",
        "evaluated": false,
        "academic_year": "2021"
    },
    {
        "school_id": 4,
        "school_manager": 5,
        "school_name": "Amman school for boys",
        "evaluated": false,
        "academic_year": "2021"
    }
]
```

#### Get Specific Evaluation

**Example :** `GET /evaluations/1`

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "evaluation_id": 1,
    "evaluated": false,
    "academic_year": "2021",
    "created_by": "Majed",
    "status": "",
    "max_score": null,
    "score": null,
    "school": 3,
    "user": 8
}

```

#### Post Goals

**Example :** `POST /goals/`

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "goal_id": 6,
    "goal": "For testing",
    "goal_result": "",
    "max_score": 5,
    "score": 4,
    "evaluation": 3
}

```
