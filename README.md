# Pokémon Guessing Game (CLI)

A command-line guessing game built with Python that integrates with the public [PokéAPI](https://pokeapi.co/).
The application randomly selects a Pokémon from the original 151 entries and challenges the user to guess which one it is, providing attribute-based hints after each attempt.

---

## Overview

This project demonstrates practical backend fundamentals, including:

* API consumption using `requests`
* JSON data parsing
* Conditional game logic
* Loop control and state management
* Basic input validation
* Terminal UI enhancement with `colorama`

The game continues running until the user correctly guesses the selected Pokémon.

---

## How It Works

1. A random Pokémon ID (1–151) is generated.
2. The application fetches its data (name, height, and weight) from the PokéAPI.
3. The user inputs a Pokémon name or ID.
4. The application:

   * Validates if the Pokémon exists.
   * Compares the guessed Pokémon’s attributes with the target Pokémon.
   * Displays color-coded hints:

     * **Green** → Correct attribute
     * **Yellow** → Attribute is higher or lower (↑ ↓ indicators)
     * **Red** → Incorrect guess or invalid Pokémon
5. The number of attempts is tracked and displayed.

The loop terminates when the correct Pokémon name is guessed.

---

## Technologies Used

* Python 3
* Requests (HTTP client)
* Colorama (terminal color formatting)
* PokéAPI (external REST API)

---

## Example Features

* Real-time API integration
* Attribute comparison logic (height and weight)
* Incremental feedback system
* Attempt counter
* Simple and interactive CLI experience

---

## Installation

```bash
pip install requests colorama
```

Run the application:

```bash
python main.py
```

---

## Learning Objectives

This project reinforces:

* Working with external APIs
* Handling HTTP responses and status codes
* Structuring simple game logic
* Improving user experience in terminal applications
* Writing maintainable and readable procedural code

---

## Future Improvements

* Modularization (MVC or layered architecture)
* Input normalization and validation enhancements
* Difficulty modes
* Score system
* Docker support
* Unit tests
* Logging system
