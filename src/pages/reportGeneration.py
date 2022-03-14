import streamlit as st
from utils import db
from utils import questionClassifier

classifier = questionClassifier.BertQuestionAnswerClassifier("./resources_dir")

def main():

    st.markdown("""
    Select a dataset to generate a quality report on it.
    """, unsafe_allow_html=True)

    database = db.createConnection()

    selectorList = ["All"] 
    selectorList.extend(db.getCollections(database))
    dataset = st.selectbox("Select a DataSet", selectorList)
    run = st.button("Run")