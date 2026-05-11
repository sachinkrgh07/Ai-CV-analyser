import streamlit as st
import mysql.connector
import time
with st.spinner("Loading..."):
       time.sleep(2)
c1,c2,c3=st.columns(3)
mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="cv")
my=mydb.cursor()
st.header("U s e r P r o f i l e")
str1=st.session_state['username']
str2=st.session_state['password']
st.success(f"Welcome:{str1}")
if c1.button("See Profile"):
       query="select * from user_info where username="+"'"+str1+"'"+" and pass="+"'"+str2+"'"+""
       my.execute(query)
       res=my.fetchall()
       for x in res:
              st.success(f"Username:{x[0]}")
              st.success(f"Password:{x[1]}")
              st.success(f"Course  :{x[2]}")
              st.success(f"Address :{x[4]}")
              st.success(f"User Dob:{x[5]}")
       

if c2.button("Change Password"):
       pass
if c3.button(" CV Analysis"):
       pass


