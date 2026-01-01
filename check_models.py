import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or "AIzaSyCz2_sNGSatPPH_USh9uJK5oSVWijDSs24"
genai.configure(api_key=api_key)

print("Listing models...")
try:
    with open("models_list_utf8.txt", "w", encoding="utf-8") as f:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
                f.write(m.name + "\n")
except Exception as e:
    print(f"Error: {e}")
