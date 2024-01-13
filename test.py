from supabase import create_client
from gotrue.errors import AuthApiError
from flask import Flask

SUPABASE_URL="https://ocalnnljxiorkuhmxihp.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jYWxubmxqeGlvcmt1aG14aWhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDQzMjcyMDksImV4cCI6MjAxOTkwMzIwOX0.HNoAukOyyqKRFx2AGBscRBe1uaqm2l2UkXQRMYM04GI"

#url = os.environ.get("SUPABASE_URL")
#key = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route


email = "vladvolkov06@yandex.ru"
password= "intersalad"
user = supabase.auth.sign_up({ "email": email, "password": password })

#session = None

try:
    #session = supabase.auth.sign_in_with_password({ "email": email, "password": password })
    #print(session)
    print('login')
except:
    print("login failed")




data = supabase.table("users").insert({"first_name":"vlad"}).execute()
#data = supabase.table("users").update({"name": "new_name"}).eq("id", 8).execute()
print()
print(data)
print()
print('123')