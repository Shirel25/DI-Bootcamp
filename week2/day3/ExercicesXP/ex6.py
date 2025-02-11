from datetime import datetime

now = datetime.now()
def time_lived(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

    time_diff = now - birth_date
    total_sec = time_diff.total_seconds()
    total_min = total_sec / 60

    print(f"You lived {total_min} minutes in your life.")


birth_date_str = input("Please enter your birth date (YYYY-MM-DD) :")
time_lived(birth_date_str)
