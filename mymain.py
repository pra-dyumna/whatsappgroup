from fastapi import FastAPI, Request, HTTPException
import requests

app = FastAPI()

# Configuration
WASSENGER_API_KEY = '6a4e3923600906e7d721b0ef7ae085294a9bf14ede5cc1571c422c4740a768b262cf07074469d69a'
WHATSAPP_GROUP_ID = '120363400582679816@g.us'

@app.get("/")
def home():
    return {"message": "✅ WhatsApp Sender API is running!"}

@app.post("/create-and-send")
async def create_and_send(request: Request):
    data = await request.json()
    document_url = data.get("document_url")
    message_text = data.get("message")

    if not document_url or not message_text:
        raise HTTPException(status_code=400, detail="document_url and message are required")

    final_message = f"{message_text}\n\n{document_url}"

    response = requests.post(
        f"https://api.wassenger.com/v1/messages?token={WASSENGER_API_KEY}",
        json={"group": WHATSAPP_GROUP_ID, "message": final_message},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {response.text}")

    return {
        "message_sent": True,
        "wassenger_response": response.json()
    }
