

# 🚀 Agent AI Class 1: using `dotenv`:

---

# Environment Variable Setup with `dotenv` – Gemini API Key

This example demonstrates how to securely load your Gemini API key from a `.env` file using the `python-dotenv` package.

---

## Technologies Used

* Python
* `python-dotenv` for managing environment variables
* `os` module to access environment variables

---

## Features

* Securely load API keys from a `.env` file
* Simple and easy to implement
* Keeps sensitive data out of your codebase

---

## Setup Instructions

### 1. Install the required package

```bash
pip install python-dotenv
```

### 2. Create a `.env` file in your project root directory

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Use the following Python code to load the key

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv("GEMINI_API_KEY")

print("Your Gemini API Key is:", API_KEY)
```

---

## Explanation

* `from dotenv import load_dotenv` — imports the function to load environment variables from a `.env` file.
* `import os` — imports the OS module to access environment variables.
* `load_dotenv()` — loads the variables from the `.env` file into the environment.
* `os.getenv("GEMINI_API_KEY")` — retrieves the value of `GEMINI_API_KEY` from the environment.

---

## Sample Project Structure

```
your-project/
├── .env
├── main.py
└── requirements.txt
```

---

## Optional: Create `requirements.txt`

To save your dependencies, run:

```bash
pip freeze > requirements.txt
```

---


