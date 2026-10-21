# Noise Generation & Filtering Comparison in Digital Image Processing

## 📌 Overview

This project presents a comparative study of Salt-and-Pepper (Impulse) Noise reduction techniques in Digital Image Processing. The system introduces noise into grayscale images and evaluates the effectiveness of different filtering approaches using both visual and quantitative analysis.

The application is developed using **Python** and **Streamlit**, allowing users to upload any image, generate Salt-and-Pepper noise, apply filtering operations, and evaluate the results through image quality metrics.

### Filters Evaluated
- Median Filter
- Min Filter
- Max Filter

---

## 🚀 Features

✅ Upload Images (PNG, JPG, JPEG)

✅ Automatic Grayscale Conversion

✅ Salt-and-Pepper Noise Generation

✅ Median Filter Implementation

✅ Min Filter Implementation

✅ Max Filter Implementation

✅ PSNR (Peak Signal-to-Noise Ratio) Calculation

✅ MSE (Mean Squared Error) Calculation

✅ Side-by-Side Filter Comparison

✅ Download Individual Filtered Images

✅ Download All Filtered Images as ZIP

✅ Interactive Performance Visualization

---

## 🛠 Technologies Used

- Python
- Streamlit
- NumPy
- SciPy
- Pillow (PIL)
- Matplotlib

---

## 🔄 Project Workflow

```text
Input Image
     ↓
Convert to Grayscale
     ↓
Add Salt-and-Pepper Noise
     ↓
Apply Median Filter
     ↓
Apply Min Filter
     ↓
Apply Max Filter
     ↓
Calculate PSNR & MSE
     ↓
Display Results
     ↓
Download Outputs
```

---

## 📊 Performance Results

| Filter | PSNR (dB) | MSE | Observation |
|----------|----------|----------|----------|
| Median Filter | 38.68 | 8.81 | Best Restoration |
| Min Filter | 12.74 | 3461.71 | Image Darkening |
| Max Filter | 11.48 | 4625.82 | Image Brightening |

---

## 🎯 Research Objective

The primary objective of this project is to evaluate the effectiveness of different image filtering techniques in removing Salt-and-Pepper noise from digital images. The study compares the visual quality and quantitative performance of the Median, Min, and Max filters to identify the most suitable method for image restoration.

---

## 🖥 Application Features

The web application enables users to:

- Upload any image
- Automatically convert images to grayscale
- Generate Salt-and-Pepper noise
- Apply Median, Min, and Max filters
- Compare outputs visually
- Calculate PSNR and MSE metrics
- Download processed images
- Export all results as a ZIP archive
- View graphical performance comparisons

---

## 🌍 Applications

- Medical Image Processing
- Satellite Image Enhancement
