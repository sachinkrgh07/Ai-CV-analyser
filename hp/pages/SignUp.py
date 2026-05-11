import streamlit as st
import random
import mysql.connector

st.header("SignUp")
c1,c2=st.columns(2)
name=c1.text_input("User Name")
Password=c1.text_input("Password")
c=c1.selectbox("Course",['BCA','IT','CS','AI & ML'])
g=c1.radio("Gender",['M','F'])
address=c2.text_area("Address")
dob=c2.date_input("DOB")
co=c2.color_picker("Select Color",value="#00f900")
b1=st.button("SAVE")
def get_data():
       st.success("Following Deatils are save successfully")
       st.write(name)
       st.write(Password)
       st.write(c)
       st.write(g)
       st.write(address)
       st.write(dob)
       st.write(co)
       mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="CV")
       my=mydb.cursor()
       my.execute("insert into user_info values("+"'"+name+"'"+","+"'"+Password+"'"+","+"'"+c+"'"+","+"'"+g+"'"+","+"'"+address+"'"+","+"'"+str(dob)+"'"+","+"'"+co+"'"+")")
       mydb.commit()
       
       
if b1:
       get_data()





                         










