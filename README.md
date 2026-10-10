# Gemini AI Vision → ESP32 Serial Controller

An AI-powered vision and automation project that combines **Python, Google Gemini, and ESP32** to interpret images and trigger hardware actions through serial communication.

The system sends an image and a prompt to Gemini, retrieves the AI-generated description or response, and forwards the result to an ESP32 over a serial connection. This creates a foundation for intelligent hardware automation, from simple LED control to more advanced vision-based security systems.

## 🚀 Features

* **AI Image Analysis:** Sends images to Gemini alongside a custom prompt to interpret visual content.
* **Serial Communication:** Transmits Gemini's response to an ESP32 using Python's serial communication capabilities.
* **Hardware Automation:** Provides a foundation for controlling LEDs and other hardware based on AI-generated responses.
* **HTTP 503 Error Handling:** Detects Gemini API `503 UNAVAILABLE` errors and automatically retries the request.
* **Progressive Retry Delay:** Increases the delay after consecutive 503 errors using an exponential backoff strategy.
* **Non-blocking Delay Logic:** Uses elapsed-time checks with `time.monotonic()` to manage retry timing without relying on `time.sleep()` during the waiting period.
* **Extensible Architecture:** Designed for future applications such as object recognition, people detection, and intelligent security monitoring.

## ⚙️ How It Works

1. **Load an image:** Python loads an image from a specified file path.
2. **Build a prompt:** A custom prompt instructs Gemini how to interpret the image and format its response.
3. **Analyze with Gemini:** The image and prompt are submitted to the Gemini API.
4. **Handle errors:** If the API returns a `503` error, the program schedules a retry with an increased delay.
5. **Transmit the response:** Once a valid response is received, Python sends it to the ESP32 over serial.
6. **Perform hardware actions:** The ESP32 can interpret the received command and execute the corresponding operation.

## 🧠 Retry Mechanism

Temporary service unavailability can interrupt AI-powered automation. To improve reliability, the program detects HTTP 503 errors and progressively increases the retry delay.

The delay follows:

`delayTime = 5 * (2 ** numTry)`

The program uses `time.monotonic()` to track elapsed time and determine when the next attempt is due.

This avoids using a blocking `time.sleep()` call during the retry-waiting period, allowing the program to perform other tasks while waiting.

**Note:** The retry loop shown in the current implementation handles HTTP 503 errors specifically. Other API errors are reported and terminate the retry loop.

## 🛠️ Technologies Used

* **Python** — Application logic and image processing workflow.
* **Google Gemini API** — AI-powered image interpretation.
* **PySerial** — Serial communication between Python and ESP32.
* **ESP32** — Hardware control and automation.
* **`time.monotonic()`** — Elapsed-time tracking for retry scheduling.

## 🔮 Future Applications

* AI-assisted theft detection.
* Object and people recognition.
* Smart surveillance and security systems.
* Context-aware home automation.
* Intelligent hardware control based on visual input.

## 🔧 Setup

1. Install the required Python packages:

   ```bash
   pip install google-genai pyserial
   ```

2. Configure your Gemini API key.

3. Set the image path and customize the prompt.

4. Configure the correct serial port and baud rate for your ESP32.

5. Upload the corresponding firmware to the ESP32.

6. Run the Python application.

Ensure that the Python program and ESP32 firmware agree on the serial message format and that the ESP32 interprets incoming commands safely.
