import RPi.GPIO as GPIO
import time

# GPIO Setup
ENA = 18  # PWM Pin
IN1 = 23
IN2 = 24

ENB = 13  # PWM Pin
IN3 = 5
IN4 = 6


GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Richtung festlegen
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)


# PWM initialisieren
pwm1 = GPIO.PWM(ENA, 1000)  # 1 kHz PWM-Frequenz
pwm2 = GPIO.PWM(ENB, 1000)  # Lüfter 1
pwm1.start(0)
pwm2.start(0)

try:
    while True:
        print("Startimpuls mit 100% PWM für 10 Sekunden")
        pwm1.ChangeDutyCycle(100)
        pwm2.ChangeDutyCycle(100)
        time.sleep(10)

        print("Reduziert auf 70% PWM für 30 Sekunden")
        pwm1.ChangeDutyCycle(70)
        pwm2.ChangeDutyCycle(70)
        time.sleep(30)



except KeyboardInterrupt:
    print("Beende...")
finally:
    pwm1.stop()
    pwm2.stop()

    GPIO.cleanup()