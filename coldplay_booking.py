from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def check_booking_time():
    # Define the time when booking will open (22nd September 12:00 PM)
    booking_open_time = datetime(2024, 9, 22, 12, 0, 0)
    current_time = datetime.now()

    if current_time < booking_open_time:
        print(f"Bookings are currently off. Please come back on 22nd September at 12:00 PM.")
        return False
    else:
        print(f"Bookings are now open!")
        return True


def select_seat_and_price():
    print("Select seat category:")
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
    
    seat_choice = int(input("Enter the number corresponding to your seat choice: "))
    
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
        num_seats = int(input("Enter the number of seats you want to book: "))
        total_price = seat_map[seat_choice] * num_seats
        print(f"You selected {num_seats} seats. Total price: ₹{total_price}")
        return total_price
    else:
        print("Invalid seat selection! Please try again.")
        return select_seat_and_price()


def fake_payment_process(driver):
    print("Simulating payment options...")

    print("\nChoose your payment method:")
    print("1. UPI")
    print("2. Credit/Debit Card")
    print("3. Net Banking")
    print("4. Wallet (Paytm, PhonePe)")

    payment_method = input("Enter the number of your preferred payment method: ")

    if payment_method == '1':
        print("You selected UPI.")
        upi_id = input("Enter UPI ID: ")
        print(f"Processing UPI ID: {upi_id}... Please wait.")
        time.sleep(3)
        print("UPI payment successful! 🎉")

    elif payment_method == '2':
        print("You selected Credit/Debit Card.")
        card_number = input("Enter Card Number (16 digits): ")
        expiry = input("Enter Expiry Date (MM/YY): ")
        cvv = input("Enter CVV: ")
        print("Processing card details... Please wait.")
        time.sleep(3)
        print("Card payment successful! 🎉")

    elif payment_method == '3':
        print("You selected Net Banking.")
        bank_name = input("Enter your bank name: ")
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")
        print("Processing Net Banking login... Please wait.")
        time.sleep(3)
        print("Net Banking payment successful! 🎉")

    elif payment_method == '4':
        print("You selected Wallet (Paytm, PhonePe, etc.).")
        wallet_number = input("Enter Wallet Mobile Number: ")
        otp = input("Enter OTP: ")
        print("Processing Wallet payment... Please wait.")
        time.sleep(3)
        print("Wallet payment successful! 🎉")

    else:
        print("Invalid selection! Please try again.")
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
        print("Error finding the 'Book Tickets' button:", e)
        driver.quit()

    print("Selecting seats for the Coldplay event...")

    total_price = select_seat_and_price()

    print(f"Redirecting to the payment gateway... Total price: ₹{total_price}")

    time.sleep(2)
    fake_payment_process(driver)

    driver.quit()
