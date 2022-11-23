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
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
            "Access-Control-Allow-Methods": "POST, OPTIONS"
        },
        "body": output
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload
