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

DB_NAME = "meme_db"
TABLE_URLS_NAME = "tUrls"

def getInsertUrlSt(
    pStrMemeUrl:str,
    pStrRedditName:str,
    pStrAuthor:str="",
    pDBName:str=DB_NAME,
    pTableName:str=TABLE_URLS_NAME,

)->str:
    strNow = utilNowYMDHMS()
    st:str=INSERT_RECORD_STATEMENT%(
        pDBName,
        pTableName,
        pStrMemeUrl,
        pStrRedditName,
        pStrAuthor,
        strNow
    )
    return st
#def getInsertUrlSt

if(theConnection):
    cursor = theConnection.cursor()
    
    stInsert = getInsertUrlSt(
        pStrUrl="https://arturmarques.com/edu/cn",
        pStrContext="Cloud Computing",
        pStrTitle="Criado agora, em 2022-05-10"
    )
    
    
    print("Will exec: ", stInsert)
    executeResultIsAlwaysNone = cursor.execute(stInsert)
    theConnection.commit()
    print(executeResultIsAlwaysNone)

    #this is a property, not a callable
    iWhereInserted = cursor.lastrowid #Returns the value generated for an AUTO_INCREMENT column
    print(iWhereInserted)

    cursor.close()

    theConnection.close()
#if close