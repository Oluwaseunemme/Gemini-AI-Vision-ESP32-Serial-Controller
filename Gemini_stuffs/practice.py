import os
from google import genai
from google.genai import types, errors
import time
import serial

ser = serial.Serial("COM10", 115200, timeout=1)
def sendSerial(txtString):

    ser.write(f"{txtString}\n".encode("utf-8"))
    ser.close()
client = genai.Client(
    api_key=""
)

model = "gemini-3.8-flash"

image_path = "OffPng.png"
prompt = "if(image says ON) return ON, else return OFF"

with open(image_path, "rb") as f:
    image_bytes = f.read()

image = types.Part.from_bytes(
    data=image_bytes,
    mime_type="image/png"
)

numTry=0
delayTime=0
startTime= int(time.monotonic())
while numTry<3:
    print(f"Elapsed time {int(time.monotonic())-startTime}")
    if(int(time.monotonic())-startTime >= delayTime):
        try:
            response = client.models.generate_content(
                model=model,
                contents=[
                    image,
                    prompt,
                    ]
            )
            if not response.text:
                raise ValueError("The model returned an empty response (possibly blocked by safety filters).")

            print(response.text)
            sendSerial(response.text)
            break

        except errors.APIError as e:
            # Catch-all for formatting or custom runtime errors
            if e.code ==503:
                delayTime= 5*(2**numTry)#each 503 return leads to incremented delay time before retrying
                startTime= int(time.monotonic())
                numTry=numTry+1
                print(f"Error 503 encountered, Retrying for the {numTry+1} time with {delayTime}sec delay")
            else:
                print(f"Gemini API error {e.code}: {e.message}")
                break