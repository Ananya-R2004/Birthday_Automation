import pandas as pd
import datetime
import pywhatkit as kit
import time
import os
import sys 
sys.stdout.reconfigure(encoding="utf-8") #for acceptance of emoji


os.chdir(r"C:\Users\ananya\Pictures\Birthday_Msgs")

# Function to send WhatsApp messages
def send_whatsapp_message(phone, message):
    try:
        phone = str(phone).strip()  # Ensure phone is a string
        if not phone.startswith("+"):  # Auto-add country code if missing
            phone = "+91" + phone  # Change country code as needed

        print(f"DEBUG: Sending WhatsApp message to {phone}...")
        kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)
        print(f"✅ Message sent to {phone}!")
    except Exception as e:
        print(f"❌ ERROR: Could not send message to {phone}. Reason: {e}")

if __name__ == "__main__":
    # Read Excel file, ensure 'Phone' is a string
    try:
        df = pd.read_excel("data.xlsx", dtype={"Phone": str})
        print("✅ Excel file loaded successfully!")
    except Exception as e:
        print(f"❌ ERROR: Could not load Excel file. Reason: {e}")
        exit()

    # Print first few rows to check data
    print("\n🔍 Checking Excel data:\n", df.head())

    # Get today's date
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = str(datetime.datetime.now().year)  # Ensure it's a string

    print(f"\n📅 Today's Date: {today}")

    writeInd = []

    for index, item in df.iterrows():
        if pd.isna(item["Birthday"]):  # Skip if Birthday is empty
            print(f"⚠️ Skipping row {index}: Birthday is missing")
            continue

        try:
            bday = item["Birthday"].strftime("%d-%m")
        except Exception as e:
            print(f"⚠️ ERROR reading birthday for row {index}: {e}")
            continue

        print(f"🔍 Checking {item['Name']}: {bday} vs {today}")

        if today == bday and yearNow not in str(item["Year"]):
            print(f"🎉 Sending birthday message to {item['Name']} ({item['Phone']})")
            send_whatsapp_message(item["Phone"], item["Dialogue"])
            writeInd.append(index)

    # Update Excel so the same person doesn't receive duplicate messages in a year
    for i in writeInd:
        df.loc[i, "Year"] = str(df.loc[i, "Year"]) + ", " + yearNow  # Ensure "Year" is a string

    # Save updated Excel file
    try:
        df.to_excel("data.xlsx", index=False)
        print("\n✅ Excel file updated successfully!")
    except Exception as e:
        print(f"❌ ERROR: Could not save Excel file. Reason: {e}")