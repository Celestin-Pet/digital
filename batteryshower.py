import psutil
battery = psutil.sensors_battery()

plugged = battery.power_plugged

show_percent = str(battery.percent)

is_plugged = "Plugged Inn" if plugged else "Not Plugged In"

print(show_percent + "% | " +is_plugged)