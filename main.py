import requests
#import os

#SIGN UP TWILO FOR GETTING API KEY AND ACC_SID AND TOKEN
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "[YOUR API KEY]"
account_sid = "[YOUR ACCOUNT SID]"
auth_token = "[YOUR AUTH TOKEN]"
#RECOVERY_CODE FOR TWILIO = BJE3F1BD3YLY678XYHQNHLG7

parameter = {
    "lat" : 23.719197, #latitude of your place
    "lon" :  90.396796, #longitude of your place
    "appid":API_KEY,
    "cnt":4
}
response = requests.get(OWM_Endpoint,params = parameter)
response.raise_for_status()
weather_data = response.json()
for i in range(0,4):
    if(weather_data["list"][i]["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(from_="whatsapp:[YOUR TWILIO NO",body="It's going to rain Today. Remember to bring an Umberlla",to="whatsapp:[YOUR VERIFIED TWILIO NO]")
    print(message.status)


# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
# API_KEY = os.environ.get("OWN_API_KEY")
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https' : os.environ['https_proxy']}
#     client = Client(account_sid,auth_token,http_client=proxy_client)