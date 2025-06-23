# 🛡️ AI Threat Detection Dashboard

A powerful, production-style Streamlit app to **detect and classify AI prompt injection threats** — from command injections to social engineering attacks. Inspired by real-world AI safety challenges at companies like Google, OpenAI, and Anthropic.

---

## 🚀 Features

✅ Real-time prompt testing  
✅ Threat classification with categories like:
- 🔓 Prompt Injection  
- 🧑‍💻 Command Injection  
- 🎭 Jailbreak / Role Play  
- 🕵️ Social Engineering  

✅ Malicious flagging (True/False)  
✅ Threat level badges: 🟢 Low, 🟡 Medium, 🔴 High  
✅ Exportable logs: `CSV` and `JSON`  
✅ Interactive dashboard with charts  
✅ Unit-tested core logic

---

## 💡 Use Case

Prompt injection is a rising attack vector in LLM applications. This project mimics what AI security engineers at Google or OpenAI might build to audit, detect, and visualize unsafe input targeting AI models.

---

## 📸 Dashboard Screenshot

![AI Threat Dashboard](assets/Screenshot%202025-06-23%20124138.png)

---

## 📂 File Structure
prompt-injection-playground/

├── prompt_injection_test.py        (CLI to test one prompt at a time)

├── batch_test_prompts.py           (Runs multiple prompts in a batch)

├── threat_dashboard.py             (Streamlit dashboard (dark mode + charts))

├── prompt_logs.csv                 (CSV log (auto-created))

├── test_prompt_injection.py        (Unit tests for threat detection)

├── assets/                         (Dashboard assets)

│   └── dashboard.png               (Dashboard screenshot)

└── README.md                       (You’re here!)

---

## 🧪 Run Tests

```bash
# Run unit tests
python -m unittest test_prompt_injection.py

# Run test interface
python prompt_injection_test.py

# Run dashboard
streamlit run threat_dashboard.py
```
### Make sure Ollama is running with Mistral:

```bash
ollama run mistral
```
## 🔗 Live Demo
Try the app here: [Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/ai-threat-detector)

## 🧠 Technologies

Python 🐍

[Ollama](https://ollama.com) + Mistral

Streamlit 📊

Mistral via Ollama 🧠

Altair (visualizations)

Pandas (data wrangling)

UnitTest (testing)

## 📤 Export Capabilities

📁 prompt_logs.csv for CSV logging

🔄 Download JSON + Download CSV in dashboard

## 🌟 Star If You Like It!
If you're an AI researcher, engineer, or student exploring prompt security, give this repo a ⭐!

## 👩‍💻 Author
Madhavi Neerati
