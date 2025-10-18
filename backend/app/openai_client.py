import os
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

async def ask_ai(prompt: str) -> str:
    # Simple wrapper for synchronous completion to keep MVP small
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant that asks clarifying questions when needed."},
                      {"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return resp.choices[0].message.content
    except Exception as e:
        # In case no API key provided or error, fallback
        return "No AI response available."
