# Demo: FastAPI whoami

**Framework:** FastAPI (Python). **Moving parts locally:** none. The handlers are plain synchronous functions, so there is no async to manage.

It exists to be deployed to several accounts so you can curl it across the Transit Gateway: reachable where routes exist, timing out where you blackholed them.

## Run it

```bash
cd app
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

```bash
pytest                              # 2 tests
uvicorn main:app --reload           # http://localhost:8000
```

## Try it

```bash
curl localhost:8000/whoami          # {"host":"<machine>","account":"unknown"}
ACCOUNT_NAME=prod uvicorn main:app  # account now says "prod"
```

FastAPI also serves interactive docs at http://localhost:8000/docs.

## Docker

```bash
docker build -t whoami . && docker run -p 8000:8000 -e ACCOUNT_NAME=dev whoami
```

## What to learn

`uvicorn` is the server, `main:app` means "the `app` object in `main.py`". Type hints become the API schema.
