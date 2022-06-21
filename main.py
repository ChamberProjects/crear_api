from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def home():
    return  [
                {   
                    "id":"1",
                    "Nombre":"Jorge",
                    "Edad":"18",
                    "Ciudad":"Santiago"
                },
             
                {
                    "id":"2",
                    "Nombre":"Jose",
                    "Edad":"21",
                    "Ciudad":"Santiago" 
                },
            
                {
                    "id":"3",
                    "Nombre":"Andres",
                    "Edad":"23",
                    "Ciudad":"Santiago"
                }
            
            ]



