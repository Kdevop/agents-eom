# **UPlan — Personalised Hobby & Event Discovery Agent**
*A conversational AI that learns your interests, remembers your preferences, and fetches real‑time events from Ticketmaster.*

---

## 🌟 Overview

UPlan is an AI‑powered hobby and event discovery assistant designed to help users explore new interests, discover passions, and find real events happening near them. It combines:

- Conversational intelligence  
- Long‑term memory  
- Live event retrieval via Ticketmaster  
- Personalised recommendations  
- A clean Streamlit chat interface  
- Deployment via Docker + Google Cloud Run  

The system is built using **n8n**, **Mistral AI**, and **Streamlit**, with a multi‑agent architecture that separates responsibilities cleanly.

---

## 🧠 Architecture

UPlan uses a **two‑agent system** orchestrated through n8n:

### **1. Brain AI (Tool‑Calling Agent)**  
Responsible for:
- Understanding user intent  
- Extracting location, event type, date range, budget, constraints  
- Calling the **Fetch Ticketmaster Events** tool  
- Updating long‑term memory  
- Returning raw event data  

This agent uses a strict tool‑calling prompt to ensure:
- No hallucinations  
- No invented events  
- Always uses real Ticketmaster data  

---

### **2. Sub AI (Response Formatter)**  
Responsible for:
- Taking the user’s original request  
- Taking the raw Ticketmaster API response  
- Formatting a friendly, helpful, conversational answer  
- Highlighting event names, dates, venues, prices  
- Limiting to 5 recommendations  
- Handling “no results” gracefully  

This agent ensures the final output feels human, warm, and tailored.

---

## 🧩 Memory System

UPlan maintains two layers of memory:

### **Short‑term (Session Memory)**  
Handled by Streamlit’s `st.session_state`:
- Stores chat history  
- Maintains session ID  
- Supports multi‑turn conversations (5–7 turns)

### **Long‑term (User Preferences)**  
Stored in n8n:
- Budget  
- Interests  
- Location  
- Constraints  
- Genre preferences  

This allows UPlan to recall preferences across sessions.

---

## 🔌 Tools & Integrations

### **Ticketmaster Discovery API**  
Used to fetch real, live event data.  
The Brain AI calls this tool with parameters extracted from the user message.

### **n8n Workflow**  
Handles:
- Agent orchestration  
- Memory storage  
- Tool execution  
- Passing data between agents  
- Returning final responses to the UI  

### **Streamlit Frontend**  
A lightweight chat interface that:
- Displays user and assistant messages in chat bubbles  
- Sends user input to n8n  
- Renders formatted responses  
- Maintains session state  

---

## 🖥️ Frontend (Streamlit)

The UI is built using Streamlit’s modern chat components:

- `st.chat_message("user")`  
- `st.chat_message("assistant")`  
- `st.chat_input()`  

This creates a clean, readable chat interface similar to ChatGPT.

### **Key Features**
- Chat bubbles for readability  
- Automatic scrolling  
- Markdown support  
- Session persistence  
- UUID‑based session IDs  

---

## 🐳 Deployment

UPlan is deployed using:

- **Docker** (containerising the Streamlit app)  
- **Google Cloud Run** (serverless hosting)  

This ensures:
- Scalability  
- HTTPS by default  
- Zero‑maintenance infrastructure  

---

## 📁 Project Structure
