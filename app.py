import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from type_1 import summarize_text
# load api
app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# sample home page
@app.get('/')
def index():
    return {'message': 'Hello, World'}


# Summarize the text
# @app.get("/summarize")
# async def summarize(text: str, n:int):
#     #n is the number of lines to be returned
#     output = summarize_text(text, n)
#     return output


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload
