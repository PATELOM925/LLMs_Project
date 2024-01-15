from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import sqlite3
import google.generativeai as ai

#configuring API key
ai.configure(api_key=os.getenv('key'))

#function to load google gemini model
#fucntion to provide sql querry as response

def gemini_response(ques,prompt):
    model = ai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],ques])
    return response.text 

#function to retrieve queery from sqllite database

def read_sql_querry(sql,db):
    connect_to_db = sqlite3.connect(db)
    cur = connect_to_db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    connect_to_db.commit()
    connect_to_db.close()
    
    #printing rows
    for row in rows:
        print(row)
        #return single row or all rows depending on the input
    return rows


#defining our prompt

prompt = [
    """Imagine you are an SQLlite expert and your main job is to convert englis into sql querry !!
    Consider our database named student having 5 columns : ame varchar(35), 
    age INTEGER, class varchar(20), section varchar(20), percentage INTEGER.
    you will receive questions such as : 1) how many records are present in the database
    where sql command would be like select count(*) from student; , 
    2) tell me student studying in 10th class and section B , where sql command would be
    like select class,section from student where class='10' & section = 'B';
    
    also while responding keep in mind that whatever sql querry response you give it should not 
    have ''' in the beginning or the end or else it will throw and error 
    and you would be fired.also in response remove '( ' , ')' , ','
    """
]


#streamlit APP
st.set_page_config(page_title="SQL AI")
st.header("SQL AI")

ques = st.text_input('Input: ',key='input')
submit = st.button("Submit & Wait!!")

#writing logic
if submit:
    response = gemini_response(ques,prompt)
    print(response)
    response = read_sql_querry(response,"Student.db")
    st.subheader("The Querry is: ")
    for row in response:
        print(row)
        st.header(row)