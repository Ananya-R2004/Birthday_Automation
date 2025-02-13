# 🎉 Birthday Automation Project

![image](https://github.com/user-attachments/assets/ef3e60f4-0890-4aba-ba08-aaea899495a4)


## 🚀 Overview

The **Birthday Automation Project** is a Python-based tool that automates the process of sending birthday greetings via **Email** and **WhatsApp**. This eliminates the hassle of remembering birthdays manually while ensuring timely and personalized wishes. 🎂✨

---

## 🌟 Features

🔹 **Seamless Automation** – Automatically sends birthday wishes via email and WhatsApp.
🔹 **Excel-Based Contact Management** – Maintain and update birthday details easily.
🔹 **Customizable Messages** – Personalize greetings with templates and dynamic content.
🔹 **Lightweight & Efficient** – Simple, fast, and easy to integrate.

---

## 🛠️ Tech Stack

🔹 **Languages**: Python\
🔹 **Libraries**: Pandas, PyWhatKit, Smtplib\
🔹 **Tools**: VS Code, Git, Excel

---

## 📂 Project Structure

```
📁 Birthday_Automation_Project
│-- 📂 Birthday_Emails
│   ├── main.py           # Script for sending emails
│   ├── contacts.xlsx     # Excel file containing email addresses
│-- 📂 Birthday_Msgs
│   ├── main.py           # Script for sending WhatsApp messages
│   ├── data.xlsx         # Excel file containing phone numbers
│-- .gitignore            # Excludes sensitive files
│-- README.md             # Project documentation
```

---

## 📑 Excel File Pre-Requirements

Before running the project, ensure that your **Excel files** are correctly formatted as follows:

### **1️⃣ Email Contacts (contacts.xlsx)**

| Sl.no | Name  | Birthday   | Dialogue         | Year | Email                                                      |
| ----- | ----- | ---------- | ---------------- | ---- | ---------------------------------------------------------- |
| 1     | John  | 12/04/2000 | Happy Birthday!  | 2024 | [john.doe@example.com](mailto\:john.doe@example.com)       |
| 2     | Alice | 25/08/1998 | Wishing you joy! | 2024 | [alice.smith@example.com](mailto\:alice.smith@example.com) |

### **2️⃣ WhatsApp Contacts (data.xlsx)**

| Name  | Phone      | Birthday   | Year | Dialogue                             |
| ----- | ---------- | ---------- | ---- | ------------------------------------ |
| Raj   | 9876543210 | 15/06/2001 | 2024 | "Happy Birthday, Raj! Have a blast!" |
| Priya | 8765432109 | 20/11/1999 | 2024 | "Many happy returns, Priya! 🎉"      |

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<Ananya-R2004>/Birthday_Automation.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Birthday_Automation
```

### 3️⃣ Install Dependencies

Ensure you have **Python 3.x** installed on your system before proceeding.

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Your Excel Files

- Open `contacts.xlsx` and add **email addresses & names**.
- Open `data.xlsx` and add **phone numbers & names**.

### 5️⃣ Run the Scripts

To send **emails**:

```bash
python Birthday_Emails/main.py
```

To send **WhatsApp messages**:

```bash
python Birthday_Msgs/main.py
```

---

## 📜 License

This project is licensed under the **MIT License** – feel free to modify and enhance it. See the [LICENSE](LICENSE) file for more details.

---

## 🔗 Connect With Me

🌟 **Stay Inspired, Stay Innovative!** 🚀  
Let's connect and build something amazing together!

