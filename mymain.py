import streamlit as st
import requests

# 🛠️ Config
WASSENGER_API_KEY = '6a4e3923600906e7d721b0ef7ae085294a9bf14ede5cc1571c422c4740a768b262cf07074469d69a'
WHATSAPP_GROUP_ID = '120363400582679816@g.us'

st.title("📤 WhatsApp Document Sender")

document_url = st.text_input("Document URL")
message_text = st.text_area("Message")

if st.button("Send to WhatsApp Group"):
    if not document_url or not message_text:
        st.error("Please enter both message and document URL.")
    else:
        final_message = f"{message_text}\n\n{document_url}"

        response = requests.post(
            f"https://api.wassenger.com/v1/messages?token={WASSENGER_API_KEY}",
            json={"group": WHATSAPP_GROUP_ID, "message": final_message},
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            st.success("✅ Message sent successfully!")
        else:
            st.error(f"❌ Failed to send message: {response.text}")
