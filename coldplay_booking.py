from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def check_booking_time():
    # Define the time when booking will open (22nd September 12:00 PM)
    booking_open_time = datetime(2024, 9, 22, 12, 0, 0)
    current_time = datetime.now()

    if current_time < booking_open_time:
        print(f"{RED}Bookings are currently off. Please come back on 22nd September at 12:00 PM.{RESET}")
        return False
    else:
        print(f"{GREEN}Bookings are now open!{RESET}")
        return True

def select_seat_and_price():
    print(f"{BLUE}Select seat category:{RESET}")
    print("1. Standing (Floor) - ₹6450")
    print("2. Seated (Level 1 - E & L) - ₹3500")
    print("3. Seated (Level 1 - A & P) - ₹4000")
    print("4. Seated (Level 1 - B, C, D, M, N, & O) - ₹4500")
    print("5. Seated (Level 2 - E & L) - ₹9000")
    print("6. Seated (Level 2 - A & P) - ₹9500")
    print("7. Seated (Level 2 - B, C, D, M, N, & O) - ₹12500")
    print("8. Seated (Level 3 - E & L) - ₹2500")
    print("9. Seated (Level 3 - A & P) - ₹3000")
    print("10. Seated (Level 3 - B, C, D, M, N, & O) - ₹3500")
    print("11. Lounge - ₹35000")
    
    seat_choice = int(input(f"{BLUE}Enter the number corresponding to your seat choice: {RESET}"))
    
    seat_map = {
        1: 6450,
        2: 3500,
        3: 4000,
        4: 4500,
        5: 9000,
        6: 9500,
        7: 12500,
        8: 2500,
        9: 3000,
        10: 3500,
        11: 35000
    }
    
    if seat_choice in seat_map:
        num_seats = int(input(f"{BLUE}Enter the number of seats you want to book: {RESET}"))
        total_price = seat_map[seat_choice] * num_seats
        print(f"{GREEN}You selected {num_seats} seats. Total price: ₹{total_price}{RESET}")
        return total_price
    else:
        print(f"{RED}Invalid seat selection! Please try again.{RESET}")
        return select_seat_and_price()

def fake_payment_process(driver):
    print(f"{BLUE}Simulating payment options...{RESET}")

    print("\nChoose your payment method:")
    print("1. UPI")
    print("2. Credit/Debit Card")
    print("3. Net Banking")
    print("4. Wallet (Paytm, PhonePe)")

    payment_method = input(f"{BLUE}Enter the number of your preferred payment method: {RESET}")

    if payment_method == '1':
        print(f"{YELLOW}You selected UPI.{RESET}")
        upi_id = input(f"{BLUE}Enter UPI ID: {RESET}")
        print(f"{BLUE}Processing UPI ID: {upi_id}... Please wait.{RESET}")
        time.sleep(3)
        print(f"{GREEN}UPI payment successful! 🎉{RESET}")

    elif payment_method == '2':
        print(f"{YELLOW}You selected Credit/Debit Card.{RESET}")
        card_number = input(f"{BLUE}Enter Card Number (16 digits): {RESET}")
        expiry = input(f"{BLUE}Enter Expiry Date (MM/YY): {RESET}")
        cvv = input(f"{BLUE}Enter CVV: {RESET}")
        print(f"{BLUE}Processing card details... Please wait.{RESET}")
        time.sleep(3)
        print(f"{GREEN}Card payment successful! 🎉{RESET}")

    elif payment_method == '3':
        print(f"{YELLOW}You selected Net Banking.{RESET}")
        bank_name = input(f"{BLUE}Enter your bank name: {RESET}")
        user_id = input(f"{BLUE}Enter User ID: {RESET}")
        password = input(f"{BLUE}Enter Password: {RESET}")
        print(f"{BLUE}Processing Net Banking login... Please wait.{RESET}")
        time.sleep(3)
        print(f"{GREEN}Net Banking payment successful! 🎉{RESET}")

    elif payment_method == '4':
        print(f"{YELLOW}You selected Wallet (Paytm, PhonePe, etc.).{RESET}")
        wallet_number = input(f"{BLUE}Enter Wallet Mobile Number: {RESET}")
        otp = input(f"{BLUE}Enter OTP: {RESET}")
        print(f"{BLUE}Processing Wallet payment... Please wait.{RESET}")
        time.sleep(3)
        print(f"{GREEN}Wallet payment successful! 🎉{RESET}")

    else:
        print(f"{RED}Invalid selection! Please try again.{RESET}")
        fake_payment_process(driver)

driver = webdriver.Chrome()

driver.get("https://in.bookmyshow.com/events/coldplay-music-of-the-spheres-world-tour/ET00412466")
driver.maximize_window()

time.sleep(5)

# Check if bookings are open
if not check_booking_time():
    driver.quit()
else:
    try:
        book_button = driver.find_element(By.XPATH, "//button[contains(text(),'Book Tickets')]")
        book_button.click()
        time.sleep(5)
    except Exception as e:
        print(f"{RED}Error finding the 'Book Tickets' button: {e}{RESET}")
        driver.quit()

    print(f"{BLUE}Selecting seats for the Coldplay event...{RESET}")

    total_price = select_seat_and_price()

    print(f"{BLUE}Redirecting to the payment gateway... Total price: ₹{total_price}{RESET}")

    time.sleep(2)
    fake_payment_process(driver)

    driver.quit()
