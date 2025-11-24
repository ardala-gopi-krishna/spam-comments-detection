import streamlit as st
import tensorflow as tf
from transformers import DistilBertTokenizerFast, TFDistilBertForSequenceClassification
tokenizer=DistilBertTokenizerFast.from_pretrained("D:\downloads\spam_tokenizer")
model=TFDistilBertForSequenceClassification.from_pretrained("D:\downloads\spam_model")
st.title('Spam Detection Model')
input_text=st.text_area("Enter the text")
if st.button("predict"):
    if input_text=='':
        print("Enter the message")
    else:
        encoded=tokenizer(input_text,padding=True,truncation=True,max_length=128,return_tensors='tf')
        pred=model.predict(encoded).logits
        value=tf.argmax(pred,axis=1).numpy()[0]
        if value==0:
            st.write("ham")
        else:
            st.write("spam")
