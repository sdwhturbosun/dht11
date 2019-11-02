import time
import dht11
d=dht11.DHT(17)
while True:
    chk = d.readDHT11()
    if (chk is 0):
        print("湿度: %.2f, \t 温度: %.2f "%(d.humidity,d.temperature))
    time.sleep(2)	