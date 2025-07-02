import streamlit as st
import time
import requests

# 🛠️ Static Config
WASSENGER_API_KEY = '6a4e3923600906e7d721b0ef7ae085294a9bf14ede5cc1571c422c4740a768b262cf07074469d69a'
WHATSAPP_GROUP_ID = '120363400582679816@g.us'

# 📄 Static document URL and message
STATIC_DOCUMENT_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
STATIC_MESSAGE = """🚨 *Shipment Status Alert*

Dear Team,

Check the Jobs whose Shipment Handover is pending and awaiting your response."""

# 🌐 Streamlit UI
st.title("📤 Delay WhatsApp Message (Wassenger)")

delay_seconds = st.number_input("⏱ Enter delay in seconds", min_value=1, max_value=3600, value=10)

if st.button("✅ Start Timer and Send"):
    st.info(f"Waiting {delay_seconds} seconds before sending message...")
    time.sleep(delay_seconds)

    final_message = f"{STATIC_MESSAGE}\n\n{STATIC_DOCUMENT_URL}"

    response = requests.post(
        f"https://api.wassenger.com/v1/messages?token={WASSENGER_API_KEY}",
        json={"group": WHATSAPP_GROUP_ID, "message": final_message},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        st.success("✅ Message sent successfully via Wassenger!")
    else:
        st.error(f"❌ Failed to send message: {response.status_code}\n{response.text}")
