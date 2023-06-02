import mysql.connector #python -m pip install mysql-connector-python

from mysql.connector.constants import ClientFlag

theConnection = mysql.connector.connect(
    host="1.2.3.4", # replace with your host
    user="admin", # replace with your user, if you did create one
    password="admin.123", # use you password
    #client_flags=[ClientFlag.SSL], # signal that SSL must be used
    #ssl_ca="server-ca.pem", # provide your *.pem files
    #ssl_cert="client-cert.pem",
    #ssl_key="client-key.pem"
)

print(theConnection)

theConnection.close()
