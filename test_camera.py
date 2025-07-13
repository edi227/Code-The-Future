from picamera2 import Picamera2  
import time  

picam2 = Picamera2()  
picam2.start()  
time.sleep(2)  # Așteaptă ca camera să se încălzească  

# Captură o imagine  
picam2.capture_file("test_image.jpg")  
picam2.stop()  
print("Imagine salvată ca test_image.jpg!")  