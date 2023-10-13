from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

from utils import documents_to_index

from indexer import QueryIndex

queryindex = QueryIndex()

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("query.log", mode="a")
fh.setLevel(logging.INFO)
logger.addHandler(fh)

###### Pydantic base classes for FastAPI ######


class Message(BaseModel):
    content: str


class Response(BaseModel):
    content: str
    sources: list


####################################################


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/converse/")
def get_response(
    message: Message,
) -> Response:
    response = queryindex.query(message.content)
    response_obj = {
        "content": response.text,
        "sources": response.source_nodes,
    }
    return Response(**response_obj)


if __name__ == "__main__":
    # memory_refresher()
    # import uvicorn

    # uvicorn.run(app, port=8001)

    # for doc_location, start_skip, end_skip in documents_to_index:
    #     BuildRagIndex(doc_location, start_skip, end_skip)
    while True:
        query = input("Enter query: ")
        message = Message(content=query)
        print(get_response(message))
