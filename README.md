# Python Password Generator

A simple command-line password generator built using Python. Users can generate random passwords with customizable lengths and character types.

## Features

- **Custom Password Length:** Choose a password length between 1 and 100 characters.
- **Optional Numbers:** Choose whether to include numbers (0–9).
- **Optional Special Characters:** Choose whether to include symbols such as !, @, and #.
- **Multiple Passwords:** Generate multiple passwords in a single run.
- **Input Validation:** Prevents invalid password lengths and password quantities.
- **Secure Random Generation:** Uses Python's `secrets` module to generate random passwords.

## Requirements

- Python 3
- No external libraries required

## How to Run

1. Download or clone this GitHub repository.
2. Open the project in PyCharm or another Python IDE.
3. Run the `main.py` file:

   ```bash
   python main.py
   ```

4. Follow the instructions in the terminal to generate your passwords.

## Example Output

```text
Password must be between 1 and 100 characters
Enter the length of the password: 12
Would you like to include numbers: y/n y
Would you like to include special characters: y/n y
How many passwords would you like to generate?: 2

Generated Password: K9!mP2@xL7#q
Generated Password: aB4$kT8&vR2!
```

*Passwords are randomly generated, so results will differ each time.*

## How It Works

The program uses Python's built-in `string` module to create a collection of allowed characters based on the user's selections.

The `secrets` module then randomly selects characters from this collection to construct passwords of the requested length.

Choosing to include numbers or special characters makes those character types available for selection, but does not guarantee that each generated password contains them.

## Future Improvements

- Guarantee that passwords contain selected character types.
- Add an option to generate another set of passwords without restarting the program.
- Create a graphical user interface (GUI).
- Add automated tests.