# app.py
import streamlit as st
from google import generativeai as genai
from google.generativeai import types
from PIL import Image
from io import BytesIO
import base64

# --- API Key Configuration ---
# IMPORTANT: Never hardcode your API key directly in production.
# Use environment variables or Streamlit secrets for security.
# For local development, you can put it directly for testing,
# but for deployment, use st.secrets.
# You can get your API key from Google AI Studio: https://aistudio.google.com/

# Configure the API key
# Replace with your actual key for local testing
API_KEY = "AIzaSyAK0LdUjH07p77HzhAwVKHf8KXlFXQmLkY" # <--- YOUR API KEY HERE
genai.configure(api_key=API_KEY)

st.title("💡 AI Assistant with Image Generation & Knowledge")
st.markdown("---")

st.sidebar.header("Options")
mode = st.sidebar.radio("Choose Mode:", ("Chat with AI", "Generate Image"))

# --- NEW: Model Availability Checker ---

# --- End NEW: Model Availability Checker ---

if mode == "Generate Image":
    st.header("🖼️ Image Generation")
    image_prompt = st.text_area("Enter prompt for image generation:", "")
    
    if st.button("Generate Image"):
        # Show the "paid feature" info message only after the button is clicked
        st.info("Note: This is a paid feature. Please ensure you have the necessary access to generate images.")
        
        # You can uncomment and add logic here to handle the actual image generation in the future when you're ready
        # if image_prompt:
        #     with st.spinner("Generating image..."):
        #         try:
        #             # Use the default image generation model
        #             image_model_name = "gemini-2.0-flash-preview-image-generation"
                    
        #             # Initialize the model
        #             image_model = genai.GenerativeModel(image_model_name)

        #             # Generate the image using the prompt
        #             response = image_model.generate_content(contents=image_prompt)

        #             # Debug: Output the raw response for better understanding
        #             st.write("Raw Response: ", response)

        #             image_found = False
        #             if response.candidates:
        #                 for part in response.candidates[0].content.parts:
        #                     if part.text:
        #                         st.write("AI's description:", part.text)
        #                     elif part.inline_data:
        #                         if part.inline_data.mime_type.startswith('image/'):
        #                             # Decode and display the image
        #                             image = Image.open(BytesIO(base64.b64decode(part.inline_data.data)))
        #                             st.image(image, caption="Generated Image", use_column_width=True)
        #                             image_found = True
        #                         else:
        #                             st.warning(f"Unexpected data type received: {part.inline_data.mime_type}")
                    
        #             if not image_found:
        #                 st.warning("No image was generated. The AI might have provided text only or an unexpected format.")
        #         except Exception as e:
        #             st.error(f"An error occurred during image generation: {e}")
        #             st.error("Please check the 'List Models' section in the sidebar for correct image generation model names.")
    else:
        st.warning("Please enter a prompt to generate an image.")



elif mode == "Chat with AI":
    st.header("💬 Chat with AI")
    user_query = st.text_input("Ask me anything:")

    if st.button("Get Response"):
        if user_query:
            with st.spinner("Getting response..."):
                try:
                    # Original chat model name. If it fails, check the "List Models" output.
                    chat_model_name = "gemini-2.0-flash" # Or "gemini-1.5-flash" for faster responses
                    
                    # You might need to change this based on List Models output
                    # Example if a new name is found: chat_model_name = "gemini-1.5-pro-latest"
                    
                    chat_model = genai.GenerativeModel(chat_model_name)
                    
                    chat_response = chat_model.generate_content(
                        contents=user_query
                    )
                    st.write("AI's Response:")
                    st.info(chat_response.text)
                except Exception as e:
                    st.error(f"An error occurred during chat: {e}")
                    st.error("Please check the 'List Models' section in the sidebar for correct chat model names.")
        else:
            st.warning("Please enter your query to chat with the AI.")

st.markdown("---")
st.caption("Developed with Google Gemini API and Streamlit")