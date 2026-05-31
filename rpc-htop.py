import time
import psutil
from pypresence import Presence

client_id = "1510348392960888852"

try:
    RPC = Presence(client_id)
    RPC.connect()
    print("Discord RPC baglantisi basarili.")
except Exception as e:
    print(f"Baglanti hatasi: {e}")
    exit(1)

def make_ansi_bar(percent):
    size = 7  
    filled_size = int(round((percent / 100) * size))
    empty_size = size - filled_size
    return "█" * filled_size + "░" * empty_size

boot_time = psutil.boot_time()

while True:
    try:
        cpu_usage = round(psutil.cpu_percent(interval=None), 1)
        ram = psutil.virtual_memory()
        ram_usage = round(ram.percent, 1)

        try:
            battery = psutil.sensors_battery()
            percent = round(battery.percent, 1)
            power_plugged = battery.power_plugged
            bat_icon = "🔌" if power_plugged else "🔋"
            bat_str = f" | {bat_icon}{percent}%"
        except:
            bat_str = ""

        first_line = f"CPU: {make_ansi_bar(cpu_usage)} {cpu_usage}%"
        second_line = f"RAM: {make_ansi_bar(ram_usage)} {ram_usage}%{bat_str}"

        RPC.update(
            details=first_line,   
            state=second_line,    
            start=int(boot_time)
        )
        
    except Exception as e:
        print(f"Hata: {e}")
        
    time.sleep(15)
