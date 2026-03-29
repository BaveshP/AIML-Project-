VIT Community Bank (CLI Simulator)
This is a simple, terminal-based banking application I built using Python. It allows users to manage basic bank accounts right from the command line. I designed this to practice how programs handle data and how to keep that data safe even after the program is closed.

 What this project does
Create New Accounts: You can open a new account by entering your name and an initial deposit.

Persistent Storage: All account data is saved in a file called bank_data.json. This means if you close the program and open it tomorrow, your money is still there!

Check Balance: Quickly see how much money is in your account by entering your name.

Deposits & Withdrawals: You can add or take out money. The system is smart enough to stop you if you try to withdraw more than you actually have.

Error Handling: I added checks to make sure the program doesn't crash if you type in a word where a number should be, or if you try to enter a negative amount.

How I built it
I used Python and focused on using its built-in tools:

JSON Module: To save and load your bank details.

OS Module: To check if the data file exists when the program starts.

Classes & Methods: I organized the code using a BankSystem class to keep the logic clean and easy to read.

 How to run it on your computer
Check for Python: Make sure you have Python installed.

Download the code: Save the script (e.g., as main.py) to a folder.

Open your Terminal: Navigate to that folder.

Launch the bank: Type the following command and hit Enter:
python main.py

Follow the Menu: Just type a number from 1 to 5 to start banking!

 What I learned
Building this helped me understand how to manage "State" in a program—meaning how to keep track of changing information (like a bank balance) over time. I also practiced making the interface "user-friendly" by adding clear error messages when something goes wrong.# AIML-Project-
