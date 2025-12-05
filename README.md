# Simple Banking CLI Application

A lightweight command-line banking application in Python that allows users to manage a single bank account. You can check your balance, deposit, withdraw, and transfer money—all in a simple, interactive menu.

## Features

* **View account balance** – Check your current balance at any time.
* **Deposit money** – Add funds to your account safely.
* **Withdraw money** – Withdraw funds with automatic balance checks.
* **Transfer money** – Transfer money out of your account with validation.
* **Menu-driven interface** – Easy-to-use text-based menus.
* **Input validation** – Ensures only valid numeric entries are accepted.

## Requirements

* Python 3.x installed on your system.

## Getting Started

1. **Run the program**

```bash
python your_script_name.py
```

2. **Main Menu Options**

```
**Welcome to the bank!**
Pritisnite 1 da pristupite aplikaciji
Pritisnite 0 da izadjete iz programa
```

* Press `1` to access the banking menu.
* Press `0` to exit the application.

3. **Banking Menu Options**

```
Pritisnite 2 da vidite stanje racuna
Pritisnite 3 da uplatite novac na racun
Pritisnite 4 da prebacite novac na tudj racun
Pritisnite 5 da biste podigli novac sa racuna
Pritisnite 6 da se vratite na pocetni ekran
```

* `2` – Check current account balance.
* `3` – Deposit money into your account.
* `4` – Transfer money out of your account.
* `5` – Withdraw money from your account.
* `6` – Return to the main menu.

4. **Follow the prompts** to enter the amounts for deposits, withdrawals, or transfers. Invalid inputs or insufficient funds will display error messages.

## Example Workflow

1. Start the program.
2. Press `1` to access your account.
3. Press `3` to deposit 100 units.
4. Press `2` to check your updated balance.
5. Press `5` to withdraw 50 units.
6. Press `6` to return to the main menu or `0` to exit.

## Functions

* `StanjeNaRacunu()` – Display the current balance.
* `uplatiNovac()` – Deposit money into the account.
* `podigniNovac()` – Withdraw money from the account.
* `prebaciNovac()` – Transfer money to another account.

## Notes

* The application uses a global variable to store account balance, which resets when the program closes.
* All user inputs are validated to prevent errors from non-numeric entries.
* Currently designed for single-user simulation.

## Future Improvements

* Multi-user support with authentication.
* Persistent storage of balances (e.g., using files or a database).
* Enhanced security for transfers and withdrawals.

---
