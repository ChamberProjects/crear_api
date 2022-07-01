from fastapi import FastAPI, Request, HTTPException

app = FastAPI(root_path="/persons")

@app.get('/persons')
async def home(request: Request):
  
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
                    "Edad":"19",
                    "Ciudad":"Concepcion" 
                },
            
                {
                    "id":"3",
                    "Nombre":"Andres",
                    "Edad":"20",
                    "Ciudad":"Puerto Natales"
                },
                
                  {
                    "id":"4",
                    "Nombre":"Juan",
                    "Edad":"21",
                    "Ciudad":"Valdivia", 
                    "root_path" : request.scope.get("root_path")
                    
                }
                   
            ]
     
    

