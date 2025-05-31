

# 🚀 Agent AI Class 1: Pehla Project 🤖

Ye **Agent AI** course ka pehla class project hai. Isme hum Google Gemini API ka use karenge aur `uv` tool ke sath Python environment aur packages manage karenge. Ye guide beginners ke liye hai aur aapko step-by-step setup aur API key ke bare mein batayega.

---

## 📋 Zaroori Cheezein

- Python 3.8 ya isse zyada version installed
- Koi code editor (jaise VS Code)
- [`uv` tool](https://github.com/astral-sh/uv) installed (for fast package management)
- Google Gemini API key (free, niche dekhein kaise hasil karna hai)

---

## 🔑 Google Gemini API Key Kaise Hasil Karein

Google Gemini API ke liye free API key hasil karne ke liye in steps ko follow karein:

1. [Google AI Studio](https://aistudio.google.com/apikey) par jayein.
2. Apna Google account se sign in karein (agar nahi hai to sign up karein).
3. **Get API Key** ya **Create API Key** par click karein.
4. API key copy karein aur safe jagah rakhein (publicly share na karein).
5. Project folder mein `.env` file banayein aur key is tarah add karein:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🛠️ Project Setup

Follow these steps to set up your project and start using the Gemini API.

### 1. **Project Initialize Karein**

`uv` tool ke sath project ka basic structure banayein:

```bash
uv init
```

*Ye command project ke liye zaroori files aur structure banata hai.*

---

### 2. **Virtual Environment Banayein**

Ek alag Python environment banayein taake project ke packages system se alag rahen:

```bash
uv venv
```

*Ye command ek `.venv` folder banata hai jisme aapke project ka environment hoga.*

---

### 3. **Virtual Environment Activate Karein**

Virtual environment ko activate karein taake aapka Python aur packages usi environment se chalain:

**Windows ke liye:**

```bash
.venv\Scripts\activate
```

**Mac/Linux ke liye:**

```bash
source .venv/bin/activate
```

> **Note**: Agar aap `uv run` command use karenge (niche dekhein), to environment manually activate karne ki zarurat nahi.

---

### 4. **Zaroori Packages Install Karein**

`python-dotenv` package install karein, jo environment variables (jaise API key) ko manage karta hai:

```bash
uv add python-dotenv
```

*Ye command `python-dotenv` ko aapke project mein add karta hai.*

> **Optional**: Agar aap Google Gemini API ke liye aur packages (jaise `google-generativeai`) use karna chahte hain, to unhe bhi install kar sakte hain:

```bash
uv add google-generativeai
```

---

### 5. **API Key Set Up Karein**

Ensure karein ke `.env` file mein `GEMINI_API_KEY` sahi se add kiya gaya hai aur aapka project isse load kar sakta hai.

---

### 6. **AI Agent Banayein**

Apna pehla AI agent banayein jo Gemini API ke sath kaam kare. Aap isse tasks jaise text generation, translation, ya question answering ke liye use kar sakte hain.

---

### 7. **Agent Chalayein**

Apne Python script (jaise `main.py`) ko run karke agent test karein. Do tareeke hain:

**Standard tareeka (virtual environment ke sath):**

```bash
python main.py
```

**Agar `uv` use kar rahe hain:**

```bash
uv run main.py
```

> **Note**: `uv run main.py` directly script chalata hai aur virtual environment ko automatically handle karta hai, isliye manual activation ki zarurat nahi.

---

## 📝 Zaroori Baatein

- `.env` file mein `GEMINI_API_KEY` ko apni actual API key se replace karein.
- `python main.py` chalane se pehle virtual environment activate karein, lekin `uv run main.py` ke liye ye zaruri nahi.
- Ensure karein ke `uv` aur zaroori packages installed hain.
- API key ko kabhi bhi publicly share na karein.

---

## 🔧 Troubleshooting

- **API Key Error**: Check karein ke `.env` file project ke root mein hai aur `GEMINI_API_KEY` sahi format mein hai.
- **Module Not Found**: Confirm karein ke `python-dotenv` (aur agar use kar rahe hain to `google-generativeai`) installed hai:
  ```bash
  uv pip list
  ```
- **Command Not Found**: Agar `uv` commands kaam nahi karte, to ensure karein ke `uv` installed hai ([installation guide](https://github.com/astral-sh/uv)).
- **Rate Limits**: Agar API rate limit ka issue aaye, to [Google AI Studio](https://aistudio.google.com/) par apna plan check karein.

---

## 🌟 Agle Qadam

- Apne AI agent ko aur behtar banayein, jaise translation, summarization, ya custom tasks add karke.
- [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) explore karein.
- Aur AI development ke liye [xAI API services](https://x.ai/api) check karein.

---
