import streamlit as st
import mysql.connector

mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="cv")
my=mydb.cursor()

st.title("SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password")
if st.button("SIGNIN"):
       str1="select * from user_info where username="+"'"+t1+"'"+" and pass="+"'"+t2+"'"+""
       my.execute(str1)
       res=my.fetchall()
       valid=0
       for x in res:
              st.success(f"Welcome:{x[0]}")
              valid=valid+1
              st.session_state['username']=x[0]
              st.session_state['password']=x[1]
              st.switch_page("pages/profile.py")
              
             
              
       if valid==0:

              st.success("Invalid Login")
              
       
