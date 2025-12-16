# AI-Powered Early Kidney Stone Detection (MVP)

## Overview
This project is a web-based MVP that provides early awareness of potential kidney stone risk  
by analyzing uploaded kidney images.

This system is intended for early awareness only and does not replace professional medical diagnosis.

## Problem
Kidney stones are often detected late, causing severe pain and medical complications.  
Early awareness can help people seek medical attention sooner.

## Solution
A simple AI-powered web application where users upload kidney images and receive early  
risk feedback.

## How It Works (MVP)
1. User uploads a kidney image  
2. Image is preprocessed (resized and normalized)  
3. AI-based decision logic simulates analysis  
4. Result is displayed on the web page  

## Technology Used
- Python  
- Flask  
- Image Processing  
- HTML  
- Future: Azure Custom Vision  

---

## Microsoft AI Services Usage

This MVP demonstrates the system logic using a local prototype.

In the full production deployment, the solution is designed to be built on **two Microsoft AI services**:

- **Azure Machine Learning** – for training, hosting, and deploying the medical image analysis model.
- **Azure AI Foundry** – for AI-driven explanation, user guidance, and responsible AI interaction.

These Microsoft AI services are required in the production architecture to ensure scalability,
responsible AI usage, and clinical safety.

---

## Future Improvements
- Train a real AI model using medical datasets  
- Integrate Azure Custom Vision  
- Improve accuracy with deep learning  
- Add confidence score  
- Doctor review dashboard  

## Ethical Considerations
- This is not a medical diagnosis  
- Used only for early awareness  
- Clear disclaimer shown to users  

## Development Note
AI-assisted tools were used during development to support learning, debugging, and rapid prototyping.  
The project design, system integration, and implementation decisions were made by me.

## Author
Aaditya Balaji  
Grade 11 Student  
Microsoft Imagine Cup 2026
