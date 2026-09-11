# Test-log
poetry run python -m app.main
Type 'exit' to quit.
Ask a question: How do I reset my forgotten PIN?

--- Retrieved Sources ---
  Chunk 1 [002_Resetting_a_Forgotten_PIN.txt]: "**Resetting a Forgotten PIN**  If you have forgotten your PIN, you can reset it ..."
  Chunk 2 [002_Resetting_a_Forgotten_PIN.txt]: " in the required field. 2. Click the "Next" button to proceed.  **Step 4: Reset ..."
  Chunk 3 [002_Resetting_a_Forgotten_PIN.txt]: "Helpdesk for assistance. * It is recommended to keep your PIN confidential and n..."

--- Final Answer ---
To reset your forgotten PIN, follow these steps:

1. Access the PIN Reset Tool by clicking on the "IT Support" link, then select "PIN Reset" and login with your credentials.
2. Verify your identity by answering your security question.
3. Enter a new PIN in the required field, following the minimum requirements (at least 8 characters long and a mix of characters).
4. Re-enter your new PIN in the confirmation field.
5. Click the "Reset PIN" button to complete the process.
6. Confirm PIN reset by clicking "OK" on the confirmation message.

Source: 002_Resetting_a_Forgotten_PIN.txt
------------------------------

Ask a question: How do I configure VPN access for a remote worker?

--- Retrieved Sources ---
  Chunk 1 [003_Configuring_VPN_Access_for_Remote_Workers.txt]: "**Configuring VPN Access for Remote Workers**  **Overview**  This article provid..."
  Chunk 2 [003_Configuring_VPN_Access_for_Remote_Workers.txt]: "has changed to a company-assigned IP address. * If you continue to experience is..."
  Chunk 3 [003_Configuring_VPN_Access_for_Remote_Workers.txt]: "Run the installer and follow the prompts to install the software. 3. Once instal..."

--- Final Answer ---
To configure VPN access for a remote worker, follow these steps:

1. Install the VPN client software from the company's software portal.
2. Launch the VPN client software and configure the connection by:
        * Clicking on "New Connection" and selecting "Company VPN".
        * Entering the company's VPN server address (`vpn.company.com`).
        * Entering your company login credentials (username and password).
        * Selecting the "Save" button to save the connection settings.
3. Establish the VPN connection by clicking the "Connect" button.
4. Authenticate with two-factor authentication (2FA) if prompted.
5. Verify connection to the company VPN.

Source: 003_Configuring_VPN_Access_for_Remote_Workers.txt
------------------------------

Ask a question: How do I set up a company email account on a mobile device?

--- Retrieved Sources ---
  Chunk 1 [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt]: "**Setting Up a Mobile Device for Company Email**  **Prerequisites:**  * Mobile d..."
  Chunk 2 [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt]: "evice**  1. Go to the Settings app on your mobile device. 2. Select "Mail" or "E..."
  Chunk 3 [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt]: "ation, try restarting your device or checking the email account settings.  **Add..."

--- Final Answer ---
To set up a company email account on a mobile device, follow these steps:

1. Ensure MDM profile is installed (if required) and go to the Settings app.
2. Select "Mail" or "Email" and tap "Add Account" or "Create a new account".
3. Select "Exchange" or "Corporate" as the account type and enter your company email address and password.
4. Enter the company's email server address (if prompted) and select synchronization options.
5. Configure email settings by selecting "Advanced" or "Security" and enabling "Use SSL/TLS" and setting the authentication method.
6. If necessary, enter the company's email domain and set up additional security measures as required by company policy.

Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt
------------------------------

Ask a question: who is sovichea?

--- Retrieved Sources ---
  Chunk 1 [008_Setting_Up_a_Secure_Wireless_Network.txt]: "isks. Configure the guest network with a different SSID and password.  **Step 6:..."
  Chunk 2 [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt]: "ation, try restarting your device or checking the email account settings.  **Add..."
  Chunk 3 [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt]: "evice**  1. Go to the Settings app on your mobile device. 2. Select "Mail" or "E..."

--- Final Answer ---

There is not enough information in the documents to answer that.
------------------------------

# Reflection

Building this baseline RAG application helped me understand how the different parts of a RAG pipeline work together. The part that worked well was connecting document ingestion, chunking, embeddings, ChromaDB retrieval, and local LLM generation into one pipeline. I also learned that the LLM does not directly search the documents. Instead, the system retrieves relevant chunks first and then gives those chunks to the model as context.

One thing that was harder than I expected was choosing and testing the chunking strategy. A chunk that is too large can contain unnecessary information, while a chunk that is too small may lose important context. I used fixed-size character chunking with 800 characters and 120 characters of overlap as a simple baseline. Testing the retrieved chunks was useful because it showed whether the retrieval step was finding information that actually matched the question.

For a future improvement, I would try **re-ranking**. The current system retrieves the top-k chunks directly from ChromaDB based on vector similarity. A re-ranking step could evaluate those retrieved chunks again and put the most relevant chunks first before sending them to the LLM. This could improve answer quality, especially for questions where several chunks are similar.
