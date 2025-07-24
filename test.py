import ephem
import datetime

# Step 1: Get user location
city = input("Enter your city (e.g., Delhi): ")
latitude = input("Enter your latitude (e.g., 28.6139): ")
longitude = input("Enter your longitude (e.g., 77.2090): ")

# Step 2: Set observer location
observer = ephem.Observer()
observer.lat = latitude
observer.lon = longitude

# Step 3: Ask the user for a date range
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
delta = datetime.timedelta(days=1)

# Step 4: Loop through each day and print moon phase
print("\nMoon Phases:")
while start_date <= end_date:
    observer.date = start_date
    moon = ephem.Moon(observer)
    phase = moon.phase

    # Determine phase name roughly
    if phase < 1:
        phase_name = "New Moon"
    elif 1 <= phase < 49:
        phase_name = "Waxing Moon"
    elif 49 <= phase < 51:
        phase_name = "Full Moon"
    else:
        phase_name = "Waning Moon"

    print(f"{start_date.strftime('%Y-%m-%d')} – {phase_name} ({phase:.1f}% illuminated)")
    start_date += delta
