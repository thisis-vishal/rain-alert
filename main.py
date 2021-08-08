import requests
from twilio.rest import Client




api_key="my key from one weather"
OWM_endpoint="https://api.openweathermap.org/data/2.5/onecall"
MY_LAT=27.8974
MY_LONG=78.0880
parameters={"lat":MY_LAT,
            "lon":MY_LONG,
            "appid":api_key,
            "exclude":"current,minutely,daily,alerts",
            }
response=requests.get(OWM_endpoint,params=parameters)
response.raise_for_status()
data=response.json()
slice_data=data["hourly"][:12]
for hour_data in slice_data:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code<700:
        will_rain=True
if will_rain:
    print("Bring an Umbrella")
    account_sid =os.environ['TWILIO_ACCOUNT_SID']
    auth_token =os.environ['auth token']
    client = Client(account_sid, auth_token)
    message=client.messages.create(
                              body='Its going to be rain bring umbrella',
                              from_='+my twilio number',
                              to='my number'
                          )
    print(message.status)                      
 #code defers for running on cloud 
#make environment variable:export API_KEY=PASTE KEY TO, TO CALL ENVA CODE IS SAME LIKE FOR SID to see actual value type env in terminal
