from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import os, asyncio, httpx

app = FastAPI(title="Notification & Payment Gateway Integration Service", version="1.0.0")

class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str = "INR"

class NotificationRequest(BaseModel):
    recipient: str
    message: str
    channel: str  # sms | email

@app.get("/health")
async def health():
    return {"status": "ok"}

async def post_with_retry(url: str, payload: dict, attempts: int = 3):
    last_error = None
    for attempt in range(attempts):
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
        except Exception as exc:
            last_error = str(exc)
            if attempt < attempts - 1:
                await asyncio.sleep(2 ** attempt)
    raise HTTPException(status_code=502, detail=f"Upstream failed: {last_error}")

@app.post("/api/payments")
async def create_payment(req: PaymentRequest):
    url = os.getenv("PAYMENT_API_URL")
    if not url:
        return {"status": "accepted", "order_id": req.order_id, "provider": "mock"}
    return await post_with_retry(url, req.model_dump())

@app.post("/api/notifications")
async def notify(req: NotificationRequest):
    env_key = f"{req.channel.upper()}_API_URL"
    url = os.getenv(env_key)
    if not url:
        return {"status": "queued", "channel": req.channel, "recipient": req.recipient}
    return await post_with_retry(url, req.model_dump())

@app.post("/api/webhooks/payment")
async def payment_webhook(payload: dict):
    return {"received": True, "event": payload.get("event", "unknown")}

@app.post("/api/webhooks/notification")
async def notification_webhook(payload: dict):
    return {"received": True, "event": payload.get("event", "unknown")}
