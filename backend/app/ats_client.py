import os
ATS_API_KEY=os.getenv("ATS_API_KEY")

def get_ats_score(text: str):
    if ATS_API_KEY:
        return {"score":75,"details":{"keywords":8}}
    kws=['experience','skills','projects','education']
    found=sum(k in text.lower() for k in kws)
    base=min(40+found*12,95)
    return {"score":base,"details":{"found":found}}
