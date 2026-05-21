import streamlit as st
import requests
from PIL import Image

# URL API Railway kamu
API_URL = "https://web-production-3899e.up.railway.app/api/v1/predict-with-advice"

st.set_page_config(
    page_title="Drowsiness Detection",
    page_icon="👁️",
    layout="centered"
)

st.title("👁️ Drowsiness Detection")
st.write("Upload gambar mata untuk mendeteksi kondisi mata.")

uploaded_file = st.file_uploader(
    "Pilih gambar",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Gambar yang diupload",
        use_container_width=True
    )

    if st.button("Prediksi"):

        with st.spinner("Menganalisis..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                API_URL,
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Prediksi berhasil")

                st.subheader("Hasil")

                st.write(
                    f"**Prediksi:** {result['prediction']}"
                )

                st.write(
                    f"**Confidence:** {result['confidence']:.2%}"
                )

                st.write(
                    f"**AI Advice:** {result['ai_advice']}"
                )

            else:
                st.error("API error")
                st.write(response.text)