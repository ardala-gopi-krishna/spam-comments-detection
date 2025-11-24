# 📌 Spam Detection Using DistilBERT (Transformer Model)

This project implements a **Spam/Ham message classifier** using **DistilBERT**, a lightweight Transformer model from Hugging Face.  
It includes data preprocessing, model fine-tuning, evaluation, and deployment using **Streamlit**.

---

## Project Overview

The goal is to classify SMS messages as **Spam** or **Ham (Not Spam)** using a state of the art NLP model.

Cleaned and preprocessed the raw dataset  
Tokenized text using DistilBERT tokenizer  
Fine-tuned a pretrained BERT-based model  
Evaluated performance  
Built a Streamlit web interface for predictions  

---

## Technologies Used

- **Python**
- **Transformers (Hugging Face)**
- **TensorFlow**
- **DistilBERT**
- **NumPy**
- **Pandas**
- **Streamlit**
- **Collections(WordCloud)**
- **Jupyter Notebook**

---

# Model Details

- **Base Model: DistilBERT (TFDistilBertForSequenceClassification)**
- **Task**: Binary Classification
- **Labels**:
            0 -> Ham
            1 -> Spam

The model was fine-tuned on a labeled SMS dataset.


