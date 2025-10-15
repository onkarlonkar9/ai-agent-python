import os
import json
import requests

def lambda_handler(event, context):
    api_key = os.getenv("OPENROUTER_API_KEY")
    prompt = event.get("prompt", "Hello from Lambda!")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return {
        "statusCode": 200,
        "body": json.dumps({"response": result["choices"][0]["message"]["content"]})
    }
