"""Optional command-line version. For the visual interface run: streamlit run app.py"""
from prompts import PURPOSES, TONES, build_prompt
from llm_client import generate_reply
from validator import validate_reply

def main():
    email=input("Paste email: ").strip()
    for i,x in enumerate(PURPOSES,1): print(i,x)
    purpose=PURPOSES[int(input("Purpose number: "))-1]
    for i,x in enumerate(TONES,1): print(i,x)
    tone=TONES[int(input("Tone number: "))-1]
    custom=input("Custom goal if needed: ")
    reply=generate_reply(build_prompt(email,purpose,tone,custom))
    validate_reply(reply)
    print("\n"+reply)
if __name__=="__main__": main()
