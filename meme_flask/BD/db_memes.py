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

DB_NAME = "dbmemes" #schema
TABLE_URLS_NAME = "tUrls"
CREATE_DB_STATEMENT = "CREATE DATABASE IF NOT EXISTS %s"

CREATE_TABLE_STATEMENT = "create table if not exists `%s`.`%s` (\
    id int not null auto_increment,\
    url varchar(512),\
    title text,\
    context text,\
    whenFound datetime not null,\
    primary key (id)\
);"

INSERT_RECORD_STATEMENT = "insert into `%s`.`%s` values(\
    null,\
    '%s',\
    '%s',\
    '%s',\
    '%s'\
);"


from datetime import date, datetime
def utilNowYMDHMS():
    dateToday = date.today()
    y, m, d = dateToday.year, dateToday.month, dateToday.day
    sy = str(y)
    sm = ""
    sd = ""

    if (m < 10):
        sm = "0" + str(m)
    else:
        sm = str(m)

    if (d < 10):
        sd = "0" + str(d)
    else:
        sd = str(d)

    strYMD = "%s-%s-%s" % (sy, sm, sd)

    timeNow = datetime.now()
    hh, mm, ss = timeNow.hour, timeNow.minute, timeNow.second
    shh = ""
    smm = ""
    sss = ""
    if (hh < 10):
        shh = "0" + str(hh)
    else:
        shh = str(hh)

    if (mm < 10):
        smm = "0" + str(mm)
    else:
        smm = str(mm)

    if (ss < 10):
        sss = "0" + str(ss)
    else:
        sss = str(ss)

    strHMS = "%s:%s:%s" % (shh, smm, sss)

    strRet = "%s %s" % (strYMD, strHMS)

    return strRet
# def utilNowYMDHMS

#obter a instrução de criação de schema / base de dados
def getCreateDBSt(
    pDBName:str=DB_NAME
)->str:
    st:str=CREATE_DB_STATEMENT%(pDBName)
    return st
#def getCreateDBSt

#obter a instrução para criação da tabela
def getCreateTableSt(
    pDBName:str=DB_NAME,
    pTableName:str=TABLE_URLS_NAME
)->str:
    st:str=CREATE_TABLE_STATEMENT%(pDBName, pTableName)
    return st
#def getCreateTableSt

#gera uma instrução de insert
def getInsertUrlSt(
    pStrUrl:str,
    pStrTitle:str,
    pStrContext:str="",
    pDBName:str=DB_NAME,
    pTableName:str=TABLE_URLS_NAME,

)->str:
    strNow = utilNowYMDHMS()
    st:str=INSERT_RECORD_STATEMENT%(
        pDBName,
        pTableName,
        pStrUrl,
        pStrTitle,
        pStrContext,
        strNow
    )
    return st
#def getInsertUrlSt

if(theConnection):
    cursor = theConnection.cursor()

    stCreateDB = getCreateDBSt()
    print("Will exec: ", stCreateDB)
    executeResultIsAlwaysNone = cursor.execute(stCreateDB)
    theConnection.commit()
    print(executeResultIsAlwaysNone)

    stCreateTable = getCreateTableSt()
    print("Will exec: ", stCreateTable)
    executeResultIsAlwaysNone = cursor.execute(stCreateTable)
    theConnection.commit()
    print(executeResultIsAlwaysNone)

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
#if