import asyncio
from openai import AsyncOpenAI

async def call_openai():
    client = AsyncOpenAI()
    response = client.chat.completions.create(
        model = "",
        messages=[]
    )
    return response.choices[0].messages.content

async def main():
    prompts = ['', '']
    await asyncio.gather(*[call_openai(prompt) for prompt in prompts])
    
asyncio.run(main())