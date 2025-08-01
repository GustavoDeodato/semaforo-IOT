from machine import Pin 
from utime import sleep 

print("Hello, ESP32!")

verde = Pin(5, Pin.OUT)
amarelo = Pin(4, Pin.OUT)
vermelho = Pin(16, Pin.OUT)
while True: 
    verde.on()
    print("verde on!")
    sleep(20)
    verde.off()
    print("verde off!")
    sleep(0.5)

    amarelo.on()
    print("amarelo on!")
    sleep(10)
    amarelo.off()
    print("amarelo off!")
    sleep(0.5)

    vermelho.on()
    print("vermelho on!")
    sleep(7)
    vermelho.off()
    print("vermelho off!")
    sleep(0.5)