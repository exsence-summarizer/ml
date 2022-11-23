import uvicorn
from fastapi import FastAPI
from type_1 import summarize_text
# load api
app = FastAPI()


# sample home page
@app.get('/')
def index():
    return {'message': 'Hello, World'}


# Summarize the text
@app.get("/summarize")
async def summarize(text: str):
    output = summarize_text(text)
    # output = "This is a sample summary " + text
    return output



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload
