import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or "AIzaSyCz2_sNGSatPPH_USh9uJK5oSVWijDSs24"
genai.configure(api_key=api_key)

MODEL_NAME = "gemini-flash-latest"
SYSTEM_INSTRUCTION = "You are a helpful assistant."

print(f"Testing generation with model: {MODEL_NAME}")

try:
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=SYSTEM_INSTRUCTION
    )
    response = model.generate_content("Hello, can you hear me?")
    print("Response received:")
    print(response.text)
except Exception as e:
    print(f"Error during generation: {e}")
