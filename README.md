# semaforo-IOT
🚦 Projeto Semáforo com ESP32 (IoT)
📌 Descrição
Este projeto simula o funcionamento de um semáforo utilizando o microcontrolador ESP32, três LEDs (vermelho, amarelo e verde), resistores e uma protoboard. Toda a simulação foi realizada através da plataforma Wokwi, utilizando MicroPython para controle dos pinos digitais do ESP32.

🧰 Tecnologias Utilizadas
ESP32
Protoboard
Simulador Wokwi
MicroPython
📷 Esquema de Montagem
Montagem Geral:
![alt text](image-1.png)Montagem do circuito
Conexão com o ESP32:
![alt text](image.png)

As imagens acima representam a montagem simulada no Wokwi.

🔌 Conexões dos Componentes
LED	Pino no ESP32
Verde	GPIO 5
Amarelo	GPIO 4
Vermelho	GPIO 16
💻 Código Fonte (MicroPython)
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
📚 Informações Acadêmicas
Disciplina: Internet das Coisas (IoT)
Professor(a): Yuri
Instituição: SENAI Jandira - Curso Técnico em Desenvolvimento de Sistemas
Ano/Semestre: 2025 - 4º Semestre

Autor
Gustavo Deodato