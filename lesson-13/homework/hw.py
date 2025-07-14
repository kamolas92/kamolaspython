#1
import datetime

birth_year = int(input("Tugiglan yilni kirit:"))
birth_month = int(input("Tugiglan oyni kirit:"))
birth_day = int(input("Tugiglan kunni kirit:"))
birth_date = datetime.date(birth_year,birth_month,birth_day)
today = datetime.date.today()
kunfarqi = today - birth_date
age = int(kunfarqi.days/365.25)
print(f'Sen {age} yoshdasan')


#2
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
birth_month = int(input("Tug‘ilgan oyingizni kiriting: "))
birth_day = int(input("Tug‘ilgan kuningizni kiriting: "))
today = datetime.date.today()
this_year_birthday = datetime.date(today.year, birth_month, birth_day)
if this_year_birthday < today:
    next_birthday = datetime.date(today.year + 1, birth_month, birth_day)
else:
    next_birthday = this_year_birthday
days_remaining = (next_birthday - today).days
print(f"\nBugungi sana: {today}")
print(f"Sizning keyingi tug‘ilgan kuningiz: {next_birthday}")
print(f"Tug‘ilgan kuningizgacha {days_remaining} kun qoldi!")

#3
year = int(input("Hozirgi yilni kiriting (masalan, 2025): "))
month = int(input("Hozirgi oyni kiriting (1-12): "))
day = int(input("Hozirgi kunni kiriting (1-31): "))
hour = int(input("Hozirgi soatni kiriting (0-23): "))
minute = int(input("Hozirgi daqiqani kiriting (0-59): "))
duration_hours = int(input("Uchrashuv davomiyligi (soat): "))
duration_minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

start_time = datetime.datetime(year, month, day, hour, minute)
duration = datetime.timedelta(hours=duration_hours, minutes=duration_minutes)
end_time = start_time + duration
print("\nUchrashuv boshlanish vaqti:", start_time.strftime("%Y-%m-%d %H:%M"))
print("Uchrashuv tugash vaqti:", end_time.strftime("%Y-%m-%d %H:%M"))


#4
import datetime
import pytz

# Step 1: Get user input for date and time
print("📅 Enter the date and time:")
year = int(input("Year (e.g. 2025): "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))
hour = int(input("Hour (0-23): "))
minute = int(input("Minute (0-59): "))

# Step 2: Get user input for timezones
print("\n🌐 Example timezones: Asia/Tashkent, Europe/London, US/Eastern, Asia/Tokyo")
current_tz_name = input("Enter your current timezone: ")
target_tz_name = input("Enter the timezone you want to convert to: ")

try:
    # Step 3: Create naive datetime and localize it
    naive_dt = datetime.datetime(year, month, day, hour, minute)
    current_tz = pytz.timezone(current_tz_name)
    target_tz = pytz.timezone(target_tz_name)

    localized_dt = current_tz.localize(naive_dt)
    converted_dt = localized_dt.astimezone(target_tz)

    # Step 4: Print results
    print("\n🕒 Original time:")
    print(f"{localized_dt.strftime('%Y-%m-%d %H:%M:%S')} ({current_tz_name})")

    print("\n➡️ Converted time:")
    print(f"{converted_dt.strftime('%Y-%m-%d %H:%M:%S')} ({target_tz_name})")

except pytz.UnknownTimeZoneError:
    print("❌ Invalid timezone. Please enter a valid timezone from the IANA list.")
except Exception as e:
    print(f"⚠️ Error: {e}")

#5
import datetime
import time

# Step 1: Get user input for target date and time
print("⏳ Countdown Timer Setup")
year = int(input("Enter the year (e.g. 2025): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))
second = int(input("Enter the second (0-59): "))

# Step 2: Create the future datetime object
target_time = datetime.datetime(year, month, day, hour, minute, second)

print(f"\n🕓 Countdown to: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Step 3: Start countdown loop
while True:
    now = datetime.datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("\n🚀 Countdown finished!")
        break

    # Clear previous line and print new countdown
    print(f"\r⏱️  Time remaining: {str(remaining).split('.')[0]}", end='')

    time.sleep(1)

#6
import re
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
email = input("📧 Enter an email address to validate: ")
if re.match(email_pattern, email):
    print("✅ Valid email address!")
else:
    print("❌ Invalid email address.")

#7
def format_phone_number(number):
    digits = ''.join(filter(str.isdigit, number))
    if len(digits) != 10:
        return "❌ Invalid number. Please enter exactly 10 digits."
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return f"✅ Formatted number: {formatted}"
user_input = input("📞 Enter a 10-digit phone number: ")
print(format_phone_number(user_input))

#8
import re

def check_password_strength(password):
    # Define strength conditions
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)

    # Evaluate overall strength
    if length_ok and has_upper and has_lower and has_digit:
        return "✅ Strong password!"
    else:
        print("❌ Weak password. Please make sure it has:")
        if not length_ok:
            print("  - At least 8 characters")
        if not has_upper:
            print("  - At least one uppercase letter")
        if not has_lower:
            print("  - At least one lowercase letter")
        if not has_digit:
            print("  - At least one digit")
        return ""

# Get password from user
user_password = input("🔐 Enter a password to check: ")
message = check_password_strength(user_password)
if message:
    print(message)

#9
def find_word_occurrences(text, target_word):
    # Normalize both text and word for case-insensitive matching
    words = text.split()
    target_word_lower = target_word.lower()

    # Store matched positions
    positions = []

    for index, word in enumerate(words):
        # Remove punctuation and compare
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word.lower() == target_word_lower:
            positions.append(index + 1)  # position in sentence (1-based index)

    return positions

# Sample text
sample_text = """
Python is a powerful programming language. The Python community is large, and Python is used in many fields such as data science, AI, web development, and automation.
"""

# Get user input
search_word = input("🔍 Enter the word to search for: ")

# Find positions
found_positions = find_word_occurrences(sample_text, search_word)

# Print results
if found_positions:
    print(f"\n✅ The word '{search_word}' was found {len(found_positions)} time(s).")
    print("📍 Word positions (by word number):", found_positions)
else:
    print(f"\n❌ The word '{search_word}' was not found in the text.")

#10
import re

def extract_dates(text):
    # Common date patterns (supports multiple formats)
    date_patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',    # e.g. 12/07/2025 or 12-07-25
        r'\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b',      # e.g. 2025-07-11 or 2025/7/11
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?\s+\d{1,2},?\s+\d{4}\b',  # e.g. July 11, 2025
    ]

    # Combine patterns
    combined_pattern = '|'.join(date_patterns)

    # Find all matches
    matches = re.findall(combined_pattern, text, re.IGNORECASE)
    return matches

# User input
user_text = input("📝 Enter text containing dates:\n")

# Extract and display
dates_found = extract_dates(user_text)

if dates_found:
    print("\n📅 Dates found in the text:")
    for date in dates_found:
        print(" -", date)
else:
    print("\n❌ No dates found in the text.")
