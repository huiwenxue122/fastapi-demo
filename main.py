from fastapi import FastAPI
from pydantic import BaseModel

# 创建 FastAPI 应用
app = FastAPI(
    title="FastAPI Sentiment Demo",
    description="A minimal FastAPI app for text sentiment classification.",
    version="1.0.0"
)

# 定义输入数据格式
class InputText(BaseModel):
    text: str

# 健康检查接口（用于测试服务器是否正常运行）
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 情感分析预测接口
@app.post("/predict")
async def predict(payload: InputText):
    text = payload.text.lower()

    if "good" in text:
        sentiment = "positive"
    elif "bad" in text:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"sentiment": sentiment}
