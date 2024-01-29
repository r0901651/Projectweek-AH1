from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class IDPayload(BaseModel):
    id: int

def start_main_script():
    try:
        subprocess.run(["python", "main.py"])  # Adjust this command based on your setup
    except Exception as e:
        print(f"Error starting main script: {str(e)}")

@app.post("/setid")
async def set_id(payload: IDPayload):
    try:
        script_id = payload.id
        print("Received ID:", script_id)

        # Write the result to a file
        result = f"Result for ID {script_id}"  # This could be any value you want to return
        with open("result.txt", "w") as file:
            file.write(result)

        print("Script Result:", result)

        # Start the main script
        start_main_script()

        return {"detail": f"ID {script_id} set successfully", "result": result}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing request")