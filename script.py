from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
        upi_id = input("Enter UPI ID : ")  
        print(f"Processing UPI ID: {upi_id}... Please wait.")
        time.sleep(3)
        print("UPI payment successful! 🎉")
    
    elif payment_method == '2':
       
        print("You selected Credit/Debit Card.")
        card_number = input("Enter Card Number (16 digits, ): ")
        expiry = input("Enter Expiry Date (MM/YY, ): ")
        cvv = input("Enter CVV : ")
        print("Processing card details... Please wait.")
        time.sleep(3)
        print("Card payment successful! 🎉 ")
    
    elif payment_method == '3':
        
        print("You selected Net Banking.")
        bank_name = input("Enter your bank name : ")
        user_id = input("Enter User ID : ")
        password = input("Enter Password : ")
        print("Processing Net Banking login... Please wait.")
        time.sleep(3)
        print("Net Banking payment successful! 🎉 ")
    
    elif payment_method == '4':
       
        print("You selected Wallet (Paytm, PhonePe, etc.).")
        wallet_number = input("Enter Wallet Mobile Number : ")
        otp = input("Enter OTP : ")
        print("Processing Wallet payment... Please wait.")
        time.sleep(3)
        print("Wallet payment successful! 🎉 ")
    
    else:
        print("Invalid selection! Please try again.")
        fake_payment_process(driver)


driver = webdriver.Chrome()

driver.get("https://in.bookmyshow.com/events/coldplay-music-of-the-spheres-world-tour/ET00412466")
driver.maximize_window()

time.sleep(5)

try:
    book_button = driver.find_element(By.XPATH, "//button[contains(text(),'Book Tickets')]")
    book_button.click()
    time.sleep(5)
except Exception as e:
    print("Error finding the 'Book Tickets' button:", e)
    driver.quit()

print("Selecting seats for the Coldplay event...")

time.sleep(3)


print("You selected 2 tickets. Total price: ₹5000")


print("Redirecting to the payment gateway...")

time.sleep(2)
fake_payment_process(driver)

driver.quit()
