import os

import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd


import streamlit as st


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

service_account_path = 'key/aspirekey.json'

# https://aspire-1bcaf-default-rtdb.firebaseio.com

# Check if Firebase Admin has already been initialized
if  not firebase_admin._apps:

    cred = credentials.Certificate(service_account_path)
    
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://aspire-1bcaf-default-rtdb.firebaseio.com'
    })

ref  = db.reference('/')
data = ref.get()
# print(data)
database = data["CRS_PROFILE"]

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def Profiel():
    pass
    st.header("Profile1 Page")
    st.divider()
    
    with st.container():
    
        col = st.columns(4)
        # Define options for the radio button
        options = ["Create New Profile", "Read All Profile", "Update Profile", "Delete Profile"]

        # Display the radio button in a horizontal layout
    
        with col[0]:
            Create_New = st.checkbox("Create New Profile")
        with col[1]:
            Read_All = st.checkbox("Read All Profile")
        with col[2]:
            UpdateP = st.checkbox("Update Profile")
        with col[3]:
            DeleteP = st.checkbox("Delete Profile")
    st.divider()
    with st.container():
        if DeleteP:
            Delete_id = int(st.number_input("Enter The Id of tuple to delete",step=1))
            if Delete_id:
                ref2  = db.reference('/')
                data1 = ref2.get()
                try:
                    ref22  = db.reference('CRS_PROFILE')
                    newr= ref22.child("Sr_id")
                    srid = newr.get()
                    Delete_id = srid.index(Delete_id)
                    st.write("Sr_id "+ str(srid[Delete_id]))  
                    st.write("Name "+ str(data1["CRS_PROFILE"]["Name"][Delete_id]))  
                    st.write("Company Name "+ str(data1["CRS_PROFILE"]["Company Name"][Delete_id]))  
                    st.write("IEC "+ str(data1["CRS_PROFILE"]["IEC"][Delete_id]))    
                    
                    delete_button = st.button("Delete Profile Detail")
                    if delete_button:
                        
                        # print(data)
                        
                    
                        for i,key in enumerate(database):
                            
                            newr= ref22.child(key)
                        
                            val =  newr.get()
                            # print("--------------")
                            # print(val,key)
                            print(val[Delete_id])
                            val.remove(val[Delete_id])
                            newr.set(val)
                        st.success('Delete Sucessfully!', icon="✅")
                except:
                    st.warning("Serial Id not found", icon="⚠️")
                    
        if Read_All:
          # st.write("okok")
            # print(data["CRS_PROFILE"])@st.cache_data

            ref1  = db.reference('/')
            data = ref1.get()
            # print(data)
            dataf = pd.DataFrame.from_dict(data["CRS_PROFILE"])
            csv = convert_df(dataf)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name="large_df.csv",
                mime="text/csv",
            )
           
            
            st.table(dataf)
        
        if Create_New:
            col1 = st.columns(3)
            
            srnew =database["Sr_id"][-1]+1
            with col1[0]: 
                st.subheader("Serial Id :  " + str(srnew ))
                Address = st.text_area("Address")
                Mob_No = st.text_input("Mob No")
                Business_Nature = st.text_input("Business Nature")
                Physical_Meet = st.text_input("Physical Meet")
            with col1[1]: 
        
                Name = st.text_input("Name")
              


                State = st.selectbox(
                    "State",
                    (
                         "Andhra Pradesh",
                    "Arunachal Pradesh",
                    "Assam",
                    "Bihar",
                    "Chhattisgarh",
                    "Goa",
                    "Gujarat",
                    "Haryana",
                    "Himachal Pradesh",
                    "Jharkhand",
                    "Karnataka",
                    "Kerala",
                    "Madhya Pradesh",
                    "Maharashtra",
                    "Manipur",
                    "Meghalaya",
                    "Mizoram",
                    "Nagaland",
                    "Odisha",
                    "Punjab",
                    "Rajasthan",
                    "Sikkim",
                    "Tamil Nadu",
                    "Telangana",
                    "Tripura",
                    "Uttar Pradesh",
                    "Uttarakhand",
                    "West Bengal",
                    "Andaman and Nicobar Islands",
                    "Chandigarh",
                    "Dadra and Nagar Haveli and Daman and Diu",
                    "Lakshadweep",
                    "Delhi",
                    "Puducherry",),
                                    index=None,
                    placeholder="Select State ",
                )
                Member = st.text_input("Member/Not Member")
                Email = st.text_input("Email")
                Refrence = st.text_input("Refrence")
                Status = st.text_input("Status")
                
                
            with col1[2]: 
                Company_Name = st.text_input("Company Name")
                date_of_join = st.date_input("Date of join", value=None)
                
                city = st.text_input("City Name")
                IEC_code = st.text_input("IEC Code")
                Product_list = st.text_input("Product list")
                
                
            add_database = st.button("Add into database")
            
            if add_database:
                value_list  = [Address,Business_Nature,city,Company_Name,str(date_of_join),Email,IEC_code,Member,Mob_No,Name,Physical_Meet,Product_list,Refrence,srnew,State,Status]
                key_list = ["Address","Business Nature","City","Company Name","Date-of-Join","Email","IEC","Member","Mobile No","Name","Physical Meet","Product","Reference","Sr_id","State","Status"]
                  
                if State and Physical_Meet and Mob_No and Name and Company_Name and city and Business_Nature and Address and date_of_join and Email and Member and IEC_code and Product_list and Refrence and Status:
                    refence = ref.child("CRS_PROFILE")
                    # print(type(str(date_of_join)))
                    # print(State , Physical_Meet , Mob_No , Name , Company_Name , city , Business_Nature , Address , date_of_join , Email , Member , IEC_code , Product_list , Refrence and Status)
                    for i,key in enumerate(database):
                       
                        newr= refence.child(key)
                        val =  newr.get()
                        val.append(value_list[i])
                        newr.set(val)
                    st.success('This is a success message!', icon="✅")
                    
                else:
                    st.warning('Please Enter All entrys', icon="⚠️")
                    for i in range(len(value_list)):
                        print(key_list[i],value_list[i])
                   
           
               
              
               
                    

                # Optionally, add more functionality to retrieve or display data