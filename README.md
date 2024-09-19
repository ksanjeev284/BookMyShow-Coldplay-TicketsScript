# BookMyShow-Coldplay-TicketsScript
This Script will allow you to buy tickets of coldplay as soon as the portal opens at september 22 12 pm ist.




# Coldplay Concert Ticket Booking Automation

## Overview
This Python script automates the process of booking tickets for the **Coldplay "Music of the Spheres" World Tour** on BookMyShow. It navigates to the event page, selects seats, and simulates a real-world payment process. The script integrates multiple payment modes like **UPI**, **Credit/Debit Cards**, **Net Banking**, and **Wallets (Paytm, PhonePe, etc.)**, ensuring a seamless experience from booking to payment.

The script is designed for users who want to **experience** an automated ticket booking workflow, useful for those familiar with Python and Selenium WebDriver.

---

## Features

- **Automatic Navigation to Event Page**:
  - The script automatically navigates to the **Coldplay World Tour** event page on BookMyShow and maximizes the browser window for a smooth user experience.

- **Seat Selection Simulation**:
  - Simulates the seat selection process for two tickets. You can easily modify the number of tickets and pricing in the script as needed.

- **Multiple Payment Methods**:
  - Supports various payment options, including:
    - **UPI** (Unified Payment Interface)
    - **Credit/Debit Cards**
    - **Net Banking**
    - **Digital Wallets** (Paytm, PhonePe, etc.)

- **Customizable**:
  - The script is fully customizable, allowing adjustments to parameters like event URL, ticket price, and payment method options for different booking scenarios.

---

## Requirements

To run this script, the following software and dependencies must be installed:

### 1. Python
Ensure Python 3.x is installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### 2. Selenium WebDriver
Install Selenium using pip:
```bash
pip install selenium
```

### 3. Chrome and ChromeDriver
Download **ChromeDriver** to match your version of Google Chrome. You can download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure ChromeDriver is added to your system’s PATH or provide its location in the script.

---

## Setup and Usage

### 1. Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/your-username/Coldplay-Ticket-Booking.git
```

### 2. Install Required Dependencies
Navigate to the project directory and install the dependencies using pip:
```bash
pip install -r requirements.txt
```

### 3. Setup ChromeDriver
Download the correct version of ChromeDriver and ensure it’s properly configured in your system’s PATH, or modify the script to point to the path where it is located.

### 4. Run the Script
Open a terminal, navigate to the project folder, and run the script:
```bash
python coldplay_booking.py
```

### 5. Follow On-Screen Prompts
The script will guide you through the booking process, including ticket selection and payment.

---

## Customization

You can modify several aspects of the script to fit your needs:

- **Event URL**: Change the event URL to book tickets for another event.
  ```python
  driver.get("https://in.bookmyshow.com/events/coldplay-music-of-the-spheres-world-tour/ET00412466")
  ```

- **Ticket Price**: Adjust the total ticket price by modifying the following line:
  ```python
  print("Total price: ₹5000")
  ```

- **Payment Methods**: You can customize the available payment methods or add more options by editing the `fake_payment_process()` function in the script.

---

## Disclaimer
This script simulates the process of booking tickets and interacting with a payment gateway. It does not perform any real transactions. It is designed for automation demonstrations, testing, or practice purposes.
