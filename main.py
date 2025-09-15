import base64
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
@app.post("/")
async def pubsub_push(request: Request):
    
    envelope = await request.json()

    if not envelope or "message" not in envelope:
        return JSONResponse(status_code=400, content={"error": "Bad Request"})

    pubsub_message = envelope["message"]

    data = ""
    if "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8")

    print(f"Received Pub/Sub message: {data}")  
    
    return JSONResponse(status_code=200, content=data)
