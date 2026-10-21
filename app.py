import streamlit as st
import numpy as np
from PIL import Image
from scipy.ndimage import median_filter, minimum_filter, maximum_filter
import io, zipfile, matplotlib.pyplot as plt

# --- Utility Functions ---
def add_salt_pepper_noise(image, prob=0.05):
    noisy = np.array(image).copy()
    rnd = np.random.rand(*noisy.shape)
    noisy[rnd < (prob/2)] = 0        # pepper
    noisy[rnd > 1 - (prob/2)] = 255  # salt
    return noisy

def mse(ref, img):
    return np.mean((ref.astype(np.float64) - img.astype(np.float64)) ** 2)

def psnr(ref, img):
    err = mse(ref, img)
    return float("inf") if err == 0 else 10 * np.log10(255.0**2 / err)

# --- Streamlit UI ---
st.title("Noise Generation & Filtering Comparison")
st.write("Upload an image to test Median, Min, and Max filters for salt-and-pepper noise removal.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Load and convert to grayscale
    img = Image.open(uploaded_file).convert("L")
    img_array = np.array(img)
    st.image(img_array, caption="Original Grayscale Image", use_container_width=True)

    # Add noise
    noisy_img = add_salt_pepper_noise(img_array, prob=0.05)
    st.image(noisy_img, caption="Image with Salt-and-Pepper Noise", use_container_width=True)

    # Apply filters
    median_img = median_filter(noisy_img, size=3)
    min_img = minimum_filter(noisy_img, size=3)
    max_img = maximum_filter(noisy_img, size=3)

    # Show outputs side-by-side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(median_img, caption="Median Filter Output", use_container_width=True)
        buf_median = io.BytesIO()
        Image.fromarray(median_img).save(buf_median, format="PNG")
        st.download_button("Download Median", buf_median.getvalue(), "median.png", "image/png")
    with col2:
        st.image(min_img, caption="Min Filter Output", use_container_width=True)
        buf_min = io.BytesIO()
        Image.fromarray(min_img).save(buf_min, format="PNG")
        st.download_button("Download Min", buf_min.getvalue(), "min.png", "image/png")
    with col3:
        st.image(max_img, caption="Max Filter Output", use_container_width=True)
        buf_max = io.BytesIO()
        Image.fromarray(max_img).save(buf_max, format="PNG")
        st.download_button("Download Max", buf_max.getvalue(), "max.png", "image/png")

    # --- Download All as ZIP ---
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("median.png", buf_median.getvalue())
        zf.writestr("min.png", buf_min.getvalue())
        zf.writestr("max.png", buf_max.getvalue())
    st.download_button("🗂️ Download All Results (ZIP)", zip_buffer.getvalue(), "filtered_results.zip", "application/zip")

    # --- Quantitative Results ---
    st.subheader("Quantitative Results")
    psnr_values = {
        "Median Filter": psnr(img_array, median_img),
        "Min Filter": psnr(img_array, min_img),
        "Max Filter": psnr(img_array, max_img),
    }
    mse_values = {
        "Median Filter": mse(img_array, median_img),
        "Min Filter": mse(img_array, min_img),
        "Max Filter": mse(img_array, max_img),
    }

    for k in psnr_values:
        st.write(f"**{k}** → PSNR: {psnr_values[k]:.2f} dB, MSE: {mse_values[k]:.2f}")

    # --- Bar Chart for PSNR ---
    st.subheader("📊 PSNR Comparison Chart")
    fig, ax = plt.subplots()
    ax.bar(psnr_values.keys(), psnr_values.values(), color=["#4CAF50", "#2196F3", "#FF9800"])
    ax.set_ylabel("PSNR (dB)")
    ax.set_title("Filter Performance Comparison")
    st.pyplot(fig)
