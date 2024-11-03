import datetime
import serpapi
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('key')
client=serpapi.Client(api_key=api_key)

print("Hello! How can i help you")



while True:
    
    message=input(">>>")
    if "hello" in message.lower():
         print("Hello! How can i help you ?")
    elif "how are you" in message.lower():
        print("I am just a chatbot ,but I am here to help you")
    elif any(word in message.lower() for word in ["thanks,thank you"]):
        print("You are welcome! Feel free to ask if you need any more help.")
    elif message.lower() in ["goodbye","bye"]:
        print("Goodbye! Have a great day!") 
        break
    elif "time" in message.lower():
        x = datetime.datetime.now()
        print('The time is '+x.strftime("%X"))            
    elif "search" in message.lower():
            result=client.search(
                q=message,
                engine="google",
                
            )
            print("Here is what i found ")
            for item in result['organic_results']:
                print(item['title'])
                print(item['link'])
                print(item['snippet'])
                print("------------------")    
    elif"exit"in message.lower():
        break
    else:
        print("Sorry , i only respond to simple commands")
        