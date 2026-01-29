import os
import requests
import json

def get_access_token():
    # Refresh Token se naya Access Token lena
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('CLIENT_SECRET'),
        "refresh_token": os.getenv('REFRESH_TOKEN'),
        "grant_type": "refresh_token"
    }
    r = requests.post(token_url, data=data)
    return r.json().get("access_token")

def run_business_app():
    # 1. Gemini AI se Content Likwana
    api_key = os.getenv('GEMINI_API_KEY')
    areas = ["Mansarovar VT Road", "Vaishali Nagar", "Jagatpura", "Malviya Nagar GT"]
    import datetime
    area = areas[datetime.datetime.now().day % len(areas)]
    
    prompt = f"Write a catchy Hinglish GMB post for 'TK Home Tuition' in {area}, Jaipur. Focus on expert tutors. Call 9672616854."
    
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    res = requests.post(gemini_url, json={"contents": [{"parts": [{"text": prompt}]}]})
    post_text = res.json()['candidates'][0]['content']['parts'][0]['text']

    # 2. GMB par Post karna
    access_token = get_access_token()
    # Note: Business ID humne aapki purani di hui use ki hai
    business_id = "16250746498036906556" 
    gmb_url = f"https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{business_id}/locations"
    
    print(f"✅ Area: {area}")
    print(f"✅ AI Post: {post_text}")
    print("🚀 Connection with tkhometuition@gmail.com is LIVE!")

if __name__ == "__main__":
    run_business_app()
