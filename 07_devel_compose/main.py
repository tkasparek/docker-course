import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2


def get_connection_string():
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    db = os.environ.get("POSTGRES_DB", "postgres")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


connection_string = get_connection_string()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/add/{content}")
async def add(content: str):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()

    cur.execute(
        """
            INSERT INTO data (content) VALUES (%(content)s)
        """,
        {"content": content},
    )

    conn.commit()

    cur.close()
    conn.close()
    return {"message": "ok"}


@app.get("/list")
async def list():
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()

    cur.execute(
        """
            SELECT id, content FROM DATA
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"message": rows}
