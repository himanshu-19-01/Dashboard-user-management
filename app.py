from flask import Flask,render_template, request,jsonify,redirect,url_for
import random
from datetime import datetime
import pyscript
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import pyodbc
import requests ## pip install requests
import time
import smtplib
import pandas as pd
import re 
from sqlalchemy import create_engine, MetaData, Table, select, Column, Numeric, Integer, VARCHAR, update, delete   
import sqlalchemy
from six.moves import urllib
from http.client import HTTPConnection, socket
import pyodbc
import urllib
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import urllib3
import psutil
import json
from threading import Thread
import requests ## pip install requests
import time
import smtplib
import pandas as pd
import re 
from sqlalchemy import create_engine, MetaData, Table, select, Column, Numeric, Integer, VARCHAR, update, delete   
import sqlalchemy
from six.moves import urllib
from http.client import HTTPConnection, socket
import pyodbc
import urllib
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
import urllib3
import psutil
import json
from threading import Thread
import requests ## pip install requests
import time
import smtplib
from sqlalchemy import create_engine, MetaData, Table, select, Column, Numeric, Integer, VARCHAR, update, delete   
import sqlalchemy
from six.moves import urllib
from http.client import HTTPConnection, socket
import urllib
#from fake_useragent import UserAgent
import urllib3
import psutil
import json
import win32com.client as client    #pip install pywin32==228
import pandas as pd
import re
links=["https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9",
       "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9"
       ]
report_list=['AEPS_Analysis','DMT_Analysis','Service_Report','Sahibnk_Report','AEPS_Failure_Report','DMT_Failure_Report','VAS_Failure_Report']
user_list=["Aeps Users","DMT Users","Service Report Users", "Sahibank Users", "AEPS Report Users","DMT Failure Report Users","Vas Failure Report Users"]
list1=[]
server = 'DESKTOP-SAAQPQ1'  # server name
database = 'Dashboard'# database name
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';trusted_connection=YES;''UID=sa;''PWD=914913;')
cursor = conn.cursor()
print("Database connected succesfully")
urllib3.disable_warnings()
clients=["https://www.ralphlauren.com/","https://www.quera.com/","https://www.infosys.com/", "https://www.saddi.com/","https://www.facebook.com/"]  #Gauges input  
#--------------------------------------------------------------------------------------------------------------------
quary1= '''SELECT  [Universal_time]
          ,[Status_url1]
          ,[Exec_Time_url1]
          ,[Status_Code_url1]
          ,[Status_url2]
          ,[Exec_Time_url2]
          ,[Status_Code_url2]
          ,[Status_url3]
          ,[Exec_Time_url3]
          ,[Status_Code_url3]
          ,[Status_url4]
          ,[Exec_Time_url4]
          ,[Status_Code_url4]
          ,[Status_url5]
          ,[Exec_Time_url5]
          ,[Status_Code_url5]
         
      FROM [Data]
      WHERE Universal_time >= DATEADD(DAY,-1,GETDATE())  ;'''  


quary2= '''SELECT  [Universal_time]
          ,[Status_url1]
          ,[Exec_Time_url1]
          ,[Status_Code_url1]
          ,[Status_url2]
          ,[Exec_Time_url2]
          ,[Status_Code_url2]
          ,[Status_url3]
          ,[Exec_Time_url3]
          ,[Status_Code_url3]
          ,[Status_url4]
          ,[Exec_Time_url4]
          ,[Status_Code_url4]
          ,[Status_url5]
          ,[Exec_Time_url5]
          ,[Status_Code_url5]
         
      FROM [Data]
      WHERE Universal_time >= DATEADD(DAY,-20,GETDATE())  ;'''

quary4=''' SELECT [Exec_Time_url4] FROM [Data] ;'''
quary5=''' SELECT [Exec_Time_url5] FROM [Data] ;'''
#---------------------------------------------------------------------------------------------------------------------
def site_up():
    ''' function to monitor up time '''
  
    ct = datetime.now().replace(second=0, microsecond=0) # universal time (Last updated 5 mins:)
    time1=str(ct)
    vol = []
    for client in clients:
        try:
            start = datetime.now()
            r = requests.get(client, verify=False)
            end = datetime.now()
            exec_time=str(end-start)[5:]    

            if r.status_code == 200 or r.status_code == 403:
                r=str(r)     #status code
                status = 'Site up'
                #print (time1,client, status,exec_time,r)
            else:
                status = 'Site down'
                r=str(r)
                #print (time1,client, status,exec_time,r)
        
        
        except socket.error:
                #status = 'Time out'
                exec_time='10.00'    #convert this to string to int
                r = "<Response [12002]>"
                r=str(r)
                #print (time1,client, status,exec_time,r)               
            

        except requests.ConnectionError:
                status = 'Network_or_proxy_issue'
                exec_time='00.00'
                r = "Other"
                r=str(r)
                #print (time1,client, status,exec_time,r)

        vol.extend((status, exec_time,r)) # time1, removed
        vol5 = vol.copy()
    #converting the List into Dataframe ....       
    if (vol5[0] =='Site up' or vol5[3]=='Site up' or vol5[6]=='Site up') and vol5[9]=='Site up'and (vol5[12]=="Site up"):
        overall_status="Site up"
    else:
        overall_status="Site down"
        
    print(vol5)
    print("reading exel file")
    # reading Excel file 
    df = pd.read_excel("static\Reports\DMT data.xlsx")
    success = df["Trxn_status"].value_counts()
    success_count=(success["Success"])
    Refund_count=(success["Refund"])
    Fail_count=(success["Fail"])   #"{:.2f}".format(site_up_percentage)
    total=success_count+Refund_count+Fail_count
    success_per=(success_count/total)*100
    Refund_per=(Refund_count/total)*100
    Fail_per=(Fail_count/total)*100
    dmt_report={"Success_per":success_per,"Refund_per":Refund_per,"Fail_per":Fail_per}
    
    # sencod Report :
    df = pd.read_excel("static\Reports\Aeps yesterday data.xlsx")
    success = df["Remarks."].value_counts()
    success_count1=(success["Success"])
    Invalid_count=(success["Invalid Account"])
    not_sufficient_count=(success["Not sufficient funds"])   #"{:.2f}".format(site_up_percentage)
    total1=success_count1+Invalid_count+not_sufficient_count 
    success_per1=(success_count1/total1)*100
    Invalid_per=(Invalid_count/total1)*100
    not_sufficient_per=(not_sufficient_count/total1)*100

    aeps_reports={"Success_count1":success_per1,"invalid_count":Invalid_per,"Not_Sufficient":not_sufficient_per}
    # third report 
    df = pd.read_excel("static\Reports\VAS data.xlsx")
    success = df["Trxn_status"].value_counts()
    success_count3=(success["Success"])
    Pending_count=(success["Pending"])
    total3=success_count3+Pending_count
    success_per3=(success_count3/total3)*100
    pending_per=(Pending_count/total3)*100 
    vas_report={"Success_per3":success_per3,"Pending_per":pending_per}
    df=pd.read_sql(quary4,conn)
    df2=df['Exec_Time_url4'].tail(5)
    val={"list":list(df2)}
    df3=pd.read_sql(quary5,conn)
    df3=df3['Exec_Time_url5'].tail(5)
    val1={"list1":list(df3)}
    with open ("static/doughnut_data.json","w")as f:
        json.dump([dmt_report,aeps_reports,vas_report,val,val1],f)
    json_data = [{"Universal_time": time1,              
    "Status_url1":vol5[0],
    "Exec_Time_url1":vol5[1],   # ---str ,int(gauges)
    "Status_Code_url1":vol5[2],
    "Status_url2":vol5[3],
    "Exec_Time_url2":vol5[4],
    "Status_Code_url2":vol5[5],              
    "Status_url3":vol5[6],
    "Exec_Time_url3":vol5[7],
    "Status_Code_url3":vol5[8],             
    "Status_url4":vol5[9],
    "Exec_Time_url4":vol5[10],
    "Status_Code_url4":vol5[11],
    "Status_url5":vol5[12],
    "Exec_Time_url5":vol5[13],
    "Status_Code_url5":vol5[14],
    "Overall_Status":overall_status}]
    
    with open ("static/variables.json","w") as file:
        json.dump(json_data,file)
        print("data dump succesfully !")  
      
def per_24_hours():
    ct = datetime.now().replace(second=0, microsecond=0) # universal time (Last updated 5 mins:)
    time1=str(ct)
    table_name = 'Data'
    cursor = conn.cursor()
    with open("static/variables.json")as file:
        data=json.load(file)
    #Inserting the values in sql server .....
    values=(time1,data[0]["Status_url1"],data[0]["Exec_Time_url1"],data[0]["Status_Code_url1"],data[0]["Status_url2"],data[0]["Exec_Time_url2"],data[0]["Status_Code_url2"],data[0]["Status_url3"],data[0]["Exec_Time_url3"],data[0]["Status_Code_url3"],data[0]["Status_url4"],data[0]["Exec_Time_url4"],data[0]["Status_Code_url4"],data[0]["Status_url5"],data[0]["Exec_Time_url5"],data[0]["Status_Code_url5"],)
    query = f"INSERT INTO {table_name} (Universal_time,Status_url1,Exec_Time_url1,Status_Code_url1,Status_url2,Exec_Time_url2,Status_Code_url2,Status_url3,Exec_Time_url3,Status_Code_url3,Status_url4,Exec_Time_url4,Status_Code_url4,Status_url5,Exec_Time_url5,Status_Code_url5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
    
    cursor.execute(query, values)
    conn.commit()
    cursor.close()  
    try:
            print("i am in try senction")
            cursor = conn.cursor()
            df_24=pd.read_sql(quary1,conn)
            cursor.close()
            print("Quary Success !")
#             ct = datetime.datetime.now().replace(second=0, microsecond=0) # universal time for 
#             time1=str(ct)
            def flag_df(df_24):
                if (df_24[1] =='Site up'or df_24[4]=='Site up'or df_24[7]=='Site up') and df_24[10]=='Site up'and df_24[13]=='Site up':
                    return 'Site up'
                elif (df_24[1] =='Site down' and  df_24[4]=='Site down' and df_24[7]=='Site down') or df_24[10]=='Site down'or df_24[13]=='Site down':
                    return 'Site down'
                else:
                    return 'Time out/Network issue'
            df_24['Overall_Status'] = df_24.apply(flag_df,axis = 1)
            Overall_Status_tail1=df_24['Overall_Status'].tail(1)    #every 5 mins 
            Overall_Status_tail1=list(Overall_Status_tail1)
            
            


            site_down_count_Overall_Status = df_24.Overall_Status[df_24.Overall_Status=='Site down'].count()
            site_up_count_Overall_Status= df_24.Overall_Status[df_24.Overall_Status=='Site up'].count() 

            Row_count=len(df_24)

            site_down_percentage = (site_down_count_Overall_Status/Row_count)*100
            site_up_percentage = 100 - site_down_percentage
            str_num = "{:.2f}".format(site_up_percentage)
            print("site up Percentage  =>"+str_num) 
            return str_num 
        
    except Exception as e:
            print(e)                   
    # Persentage for 20 days site up ...............
def percentage_of_20_days():    
    try:
            print("i am in try senction")
            cursor = conn.cursor()
            df_20_days=pd.read_sql(quary2,conn)
            cursor.close()
            print("Quary Success !")
#             ct = datetime.datetime.now().replace(second=0, microsecond=0) # universal time for 
#             time1=str(ct)
            def flag_df(df_20_days):
                if (df_20_days[1] =='Site up'or df_20_days[4]=='Site up'or df_20_days[7]=='Site up') and df_20_days[10]=='Site up'and df_20_days[13]=='Site up':
                    return 'Site up'
                elif (df_20_days[1] =='Site down' and  df_20_days[4]=='Site down' and df_20_days[7]=='Site down') or df_20_days[10]=='Site down'or df_20_days[13]=='Site down':
                    return 'Site down'
                else:
                    return 'Time out/Network issue'
            df_20_days['Overall_Status'] = df_20_days.apply(flag_df,axis = 1)
            Overall_Status_tail1=df_20_days['Overall_Status'].tail(1)    #every 5 mins 
            Overall_Status_tail1=list(Overall_Status_tail1)
            
            


            site_down_count_Overall_Status = df_20_days.Overall_Status[df_20_days.Overall_Status=='Site down'].count()
            site_up_count_Overall_Status= df_20_days.Overall_Status[df_20_days.Overall_Status=='Site up'].count() 

            Row_count=len(df_20_days)

            site_down_percentage = (site_down_count_Overall_Status/Row_count)*100
            site_up_percentage = 100 - site_down_percentage
            str_num_1 = "{:.2f}".format(site_up_percentage)
            print("site up Percentage  =>"+str_num_1) 
            return str_num_1
        
    except Exception as e:
            print(e)          
    

app=Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def login_page():
    if request.method == "POST": 
        list1.clear()
        user = request.form["userName"]
        password = request.form["password"]
        print(user)
        print(password)
        cursor.execute("select * from login_details where login_details.Name = ? and login_details.Password=?",user,password)
        record = cursor.fetchone()
        print(record) 
        for item in report_list:
            cursor.execute(f"SELECT {item} FROM login_details WHERE login_details.Name=? and login_details.Password=?",user,password)   
            r=cursor.fetchone()
            list1.append(r[0])  
        print(list1) 
        data_list=list1   
        if record:
            return render_template("home.html",lis=data_list,report=report_list,link=links)
            
        else:
            msg = 'Forget Password ? Contact to data analyst team .'
            return render_template("Login.html", error=msg)       
    return render_template("login.html")
@app.route("/reports")
def reports():
     return render_template("reports.html",lis=list1,report=report_list,link=links)
 
@app.route("/Home")
def Home():
    print("sending")
    return render_template("home.html",lis=list1,report=report_list,link=links)
@app.route("/dashbord", methods=["GET", "POST"])
def Dashbord():
    site_up()
    per_24_hour=per_24_hours() 
    per_20_days=percentage_of_20_days()
    with open("static/variables.json")as file:
        data=json.load(file)
        time=data[0]["Universal_time"]
        status=data[0]["Overall_Status"]
    return render_template("dashbord.html",date=time,stat=status,percentage=per_24_hour,p_20_days=per_20_days)
@app.route("/add", methods=["GET","POST"])
def Add():
    dfs=Dataframe()
    return render_template('table.html',reports=report_list,users=user_list,dfs=dfs,lis=list1,link=links)
# @app.route("/remove", methods=["GET","POST"])
# def remove():
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM Login')
#     rows = cursor.fetchall()
#     return render_template('remove_admin.html', rows=rows)
# @app.route('/delete/<string:report_name>', methods=['GET','POST'])
# def delete(report_name):
#     cursor = conn.cursor() 
#     cursor.execute(f"ALTER TABLE login_details DROP COLUMN {report_name};")
#     conn.commit() 
#     report_list.remove(report_name)
#     user_list.remove(report_name)
#     del links[-1]
#     dfs=Dataframe();
#     return render_template('table.html',reports=report_list,users=user_list,dfs=dfs,lis=list1,link=links)
@app.route('/delete-report', methods=['GET','POST'])
def delete_report():
    if request.method =="POST":
        report_name = request.form['report_name']
        report_link = request.form['report_link']
        if report_name in report_list and report_link in links:
            report_list.remove(report_name)
            user_list.remove(report_name)
            links.remove(report_link)
            print(report_list)
            cursor=conn.cursor()
            cursor.execute(f"ALTER TABLE login_details DROP COLUMN {report_name};")
            conn.commit()
            dfs=Dataframe()
            return render_template('table.html',reports=report_list,lis=list1,link=links,users=user_list,dfs=dfs)
        else:
            msg="Invalid Report Name or Link"
            return render_template("delete_report.html",reports=report_list,lis=list1,link=links,msg=msg)    
    return render_template("delete_report.html",reports=report_list,lis=list1,link=links)    
@app.route("/try",methods=["GET","POST"])
def t():
    if request.method == "POST": 
        username = request.form['username']
        password = request.form['password']
        reports = request.form.getlist('reports[]')
        category = request.form['report-category']
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO login_details (Name, Password, Access) VALUES (?,?,?)", (username, password, category))
        conn.commit()
        
        list3 = [0]  # initialize the list with a 0 value
      
        print(reports)
        for itm in report_list:
            if itm in reports:
                list3.append(1)
                cursor.execute(f"UPDATE login_details SET [{itm}] = ? WHERE Name = ? AND Password = ?", (list3[-1], username, password))
                conn.commit()    
            else:
                list3.append(0)
                cursor.execute(f"UPDATE login_details SET [{itm}] = ? WHERE Name = ? AND Password = ?", (list3[-1], username, password))
                conn.commit()    
                    
            
            
        print(username)
        print(password)
        print(reports)
        print(category)
        return render_template("add_user.html", msg="User Added Successfully!", lis1=report_list,lis=list1,link=links)

    print(list1)
    print("list 1")
    return render_template("add_user.html",lis1=report_list,lis=list1,link=links)     
 
def Dataframe():
    dfs = []
    for item in report_list:
        quary=f"select id,Name,Password,Access from  login_details where {item}=1" 
        df = pd.read_sql(quary, conn)
        dfs.append(df)
    conn.commit()
    return dfs
@app.route("/edit/<int:row_index>",methods=["GET","POST"])
def edit(row_index):

    user_access_quary=f"select Name from login_details where {report_list[(row_index-1)]}=1" 
    user_df=pd.read_sql(user_access_quary,conn)
    column_names = list(user_df.columns)
    rows = list(user_df.values)
    
   
 
    print(user_df)
     
    return render_template("edit_user.html",lis=list1,columns=column_names,value=rows,reports=report_list)
@app.route('/submit-report', methods=['GET','POST'])
def submit_report():
    if request.method =="POST":
        report_name = request.form['report_name']
        report_link = request.form['report_link']
        report_list.append(report_name)
        user_list.append(report_name)
        links.append(report_link)
        print(report_list)
        coloumn=report_name.replace(" ","_")
        cursor=conn.cursor()
        cursor.execute(f"ALTER TABLE login_details ADD {coloumn} smallint")
        conn.commit()
        dfs=Dataframe()
        return render_template('table.html',reports=report_list,lis=list1,link=links,users=user_list,dfs=dfs)
    return render_template("add_report.html",reports=report_list,lis=list1,link=links)    
@app.route("/manage_access/<username>", methods=['GET','POST'])
def manage_access(username):
  # Retrieve data for user from database
  query = f"SELECT {','.join(report_list)} FROM login_details WHERE Name = '{username}'"
  df = pd.read_sql(query, conn)
  df = df.fillna(0) 
  report_data = {}
  for i, report in enumerate(report_list):
    report_data[report] = int(df.iloc[0][i])
  # Return data as dictionary
  print(report_data)
  return jsonify(report_data)

@app.route("/update",methods=["GET","POST"])
def update():
    if request.method == "POST": 
        username = request.form['username']
        password = request.form['password']
        reports = request.form.getlist('reports[]')
        category = request.form['report-category']
        list3 = [0]  # initialize the list with a 0 value
      
        print(reports)
        for itm in report_list:
            if itm in reports:
                list3.append(1)
                cursor.execute(f"UPDATE login_details SET [{itm}] = ? WHERE Name = ? AND Password = ?", (list3[-1], username, password))
                conn.commit()    
            else:
                list3.append(0)
                cursor.execute(f"UPDATE login_details SET [{itm}] = ? WHERE Name = ? AND Password = ?", (list3[-1], username, password))
                conn.commit()    
                    
            
            
        print(username)
        print(password)
        print(reports)
        print(category)
        return render_template("add_user.html", msg="User updated Successfully!", lis1=report_list,lis=list1,link=links)

    print(list1)
    print("list 1")
    return render_template("add_user.html",lis1=report_list,lis=list1,link=links)     

if __name__ =="__main__":
    app.run(debug=True)



#   <script>
#               {     
#                   setTimeout(function(){
#                   document.getElementById('btn1').click();
#               }, 3 * 1000); 
#               }
#   </script> 

#<div class="div1" style="font-size:70px;text-align:center;color:lightgreen;margin-top:50px;">SahiPay Health Dahbord</div>




#  {%if(lis[1][0]==1)%}
#                     <li><a class="color" href="#" data-href="https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >AEPS Analysis</a></li> 
#                     {% endif %}
#                     {%if(lis[1][1]==1)%}
#                     <li><a class="color" href="#" data-href="https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >DMT Analysis</a></li>
#                     {% endif %}
#                     {%if(lis[1][2]==1)%}
#                     <li><a class="color" href="#" data-href="https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >Service Report</a></li>
#                     {% endif %}
#                     {%if(lis[1][3]==1)%}
#                     <li><a class="color" href="#" data-href= "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >Sahibnk Report</a></li> 
#                     {% endif %}
#                     {%if(lis[1][4]==1)%}
#                     <li><a class="color" href="#" data-href= "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >AEPS Failure Report</a></li>
#                     {% endif %}
#                     {%if(lis[1][5]==1)%}
#                     <li><a class="color" href="#" data-href= "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >DMT Failure Report</a></li>
#                     {% endif %}
#                     {%if(lis[1][6]==1)%}
#                     <li><a class="color" href="#" data-href= "https://app.powerbi.com/view?r=eyJrIjoiZWJjMzc5NDAtZmM4NC00MTUzLTk0ZWItZDBmM2Y4OTEwMjU4IiwidCI6IjI2ZmY2MmEwLTAzYmQtNDcyZS05NzYxLTc5ZGE0ZGYwMzlmNSJ9" rel="nofollow" >VAS Failure Report</a></li>
#                     {% endif %}
                
                