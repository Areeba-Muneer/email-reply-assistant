import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_reply(prompt, temperature=0.4):

    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key or api_key == "PASTE_YOUR_GEMINI_API_KEY_HERE":
        raise RuntimeError(
            "Gemini API key is missing. Add it to your .env file."
        )

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "temperature": temperature,
                "max_output_tokens": 500,
            },
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response. Please try again."
            )

        return response.text.strip()

    except Exception as e:
        raise RuntimeError(
            f"Gemini API error: {e}"
        ) from e