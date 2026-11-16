from djitellopy import Tello
import time

tello = Tello()
tello.connect()

bat = tello.get_battery()
print(f" Nivel de bateria: {bat}%")

tello.takeoff()
time.sleep(2)
tello.flip('f')
# Subir
tello.move_up(100)
time.sleep(1)


time.sleep(1)
# Bajar
tello.move_down(100)
time.sleep(1)
# Aterrizar
tello.land()
# Finalizar
tello.end()




