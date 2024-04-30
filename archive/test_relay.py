import RPi.GPIO as GPIO
import time

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin controlled the relay module
RELAY_PIN = 13

# Set the relay pin as an output pin
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW) # Turn the relay OFF (LOW) Initially

try:
    # Run the loop function indefinitely
    while True:
        # Turn the relay ON (HIGH) 
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(4)  # Wait for seconds

        # Turn the relay OFF (LOW) 
        GPIO.output(RELAY_PIN, GPIO.LOW)
        time.sleep(4)  # Wait for seconds

except KeyboardInterrupt:
    # If the user presses Ctrl+C, clean up the GPIO configuration
    GPIO.cleanup()