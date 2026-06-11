"""
INPUT:
AI Prompt

OUTPUT:
Gemini Response

USED BY:
ai_service.py
"""

import google.generativeai as genai

from config.settings import GEMINI_API_KEY


genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt):

    print(f"Prompt sent to Gemini: {prompt}")

    try:
        response = model.generate_content(
            prompt
        )

        print(f"Response from Gemini: {response.text}")

        return response.text

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return f"AI Service Unavailable: {str(e)}"


# """
# INPUT:
# AI Prompt

# OUTPUT:
# LLM Response

# USED BY:
# ai_service.py
# """

# from openai import OpenAI

# from config.settings import (
#     OPENROUTER_API_KEY,
#     AI_MODEL,
# )

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENROUTER_API_KEY,
# )


# def ask_gemini(prompt):
#     """
#     Keeping function name unchanged
#     so ai_service.py does not need
#     any modifications.
#     """

#     try:
#         response = (
#             client.chat.completions.create(
#                 model=AI_MODEL,
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": prompt,
#                     }
#                 ],
#                 temperature=0.7,
#                 max_tokens=1000,
#             )
#         )

#         return (
#             response
#             .choices[0]
#             .message.content
#         )

#     except Exception as e:
#         print(
#             f"OpenRouter Error: {str(e)}"
#         )

#         return (
#             "AI service is temporarily "
#             "unavailable. Please try "
#             "again later."
#         )