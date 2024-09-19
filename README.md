# BookMyShow-Coldplay-TicketsScript
This Script will allow you to buy tickets of coldplay as soon as the portal opens at september 22 12 pm ist.



**Contributing**
Contributions are welcome! If you'd like to improve the script or add new features, feel free to submit a pull request or open an issue.

**Coldplay Concert Ticket Booking Automation**

**Overview**

This Python script automates the process of booking tickets for the Coldplay "Music of the Spheres" World Tour on BookMyShow. It navigates to the event page, selects seats, and simulates a real-world payment process. The script integrates multiple payment modes like UPI, Credit/Debit Cards, Net Banking, and Wallets (Paytm, PhonePe, etc.), ensuring a seamless experience from booking to payment.

The script is designed for users who want to experience an automated ticket booking workflow, useful for those familiar with Python and Selenium WebDriver.

**Features**

**Automatic Navigation to Event Page:**

The script automatically navigates to the Coldplay World Tour event page on BookMyShow and maximizes the browser window for a smooth user experience.
Seat Selection Simulation:

It simulates the seat selection process for two tickets. You can easily modify the number of tickets and pricing in the script as needed.

**Multiple Payment Methods:
**
The script supports a variety of payment options for the final step, including:
UPI (Unified Payment Interface)
Credit/Debit Cards
Net Banking
Digital Wallets (Paytm, PhonePe, etc.)
Customizable:

The script is fully customizable, allowing you to adjust parameters like event URL, ticket price, and other details to suit different booking scenarios.

**Requirements**
To run this script, the following software and dependencies must be installed:

1. Python
Ensure you have Python 3.x installed on your machine. Download Python here.

2. Selenium WebDriver
Install Selenium using pip to enable browser automation.

pip install selenium
3. Chrome and ChromeDriver
Download ChromeDriver that matches your installed version of Google Chrome.

Download ChromeDriver here.

Ensure ChromeDriver is added to your system’s PATH or specify its location in the script.
Setup and Usage Instructions
Clone the Repository: Clone the repository to your local machine using Git:

git clone https://github.com/your-username/Coldplay-Ticket-Booking.git
Install Required Dependencies: Navigate to the project directory and install dependencies using pip:

pip install -r requirements.txt
Set Up ChromeDriver: Download ChromeDriver and ensure it's correctly configured in your system’s PATH or modify the script to point to the exact path where it's located.

Run the Script: Open your terminal, navigate to the project folder, and run the script:

python coldplay_booking.py
Follow the On-Screen Prompts: The script will guide you through the booking process, including ticket selection and payment.

How to Customize
You can modify several aspects of the script to suit different needs:

Event URL: Change the event URL in the script to book tickets for a different event.

**Disclaimer**
This script simulates the process of booking tickets and interacting with a payment gateway, but it does not perform any real transactions. Use it to automate workflows, demo processes, or practice automation skills.
