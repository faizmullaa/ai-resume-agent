import os, openai
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
openai.api_key=OPENAI_API_KEY

PROMPT_TEMPLATE = '''
Improve this resume text for ATS optimization and professional tone:
{text}
'''

def enhance_resume_text(text: str) -> str:
    if not OPENAI_API_KEY:
        return text
    r=openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role":"user","content":PROMPT_TEMPLATE.format(text=text)}],
        max_tokens=1200,
        temperature=0.2
    )
    return r['choices'][0]['message']['content']
