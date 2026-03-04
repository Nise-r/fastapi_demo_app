import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://127.0.0.1:8000/detect"

st.set_page_config(
    page_title="YOLO Object Detection",
    layout="centered"
)

st.title("YOLO Object Detection App")
st.write("Upload an image and detect objects using YOLO.")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Run Detection"):
        with st.spinner("Detecting objects..."):
            try:
                files = {
                    "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                }

                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result_image = Image.open(io.BytesIO(response.content))
                    st.success("Detection Complete")
                    st.image(result_image, caption="Detected Image", use_column_width=True)
                else:
                    st.error(f"Error: {response.status_code}")
                    st.text(response.text)

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to FastAPI server.")