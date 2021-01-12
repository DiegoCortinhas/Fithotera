'''''''''''''''''''''''''''''''''
Código para validação da conexao com o dB
'''''''''''''''''''''''''''''''''
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', database='fithotera', user='root',password='admin')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado ao MySQL Server versão ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado a base de dados: ", record)

except Error as e:
    print("Erro na conexão com o MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexão com o MySQL fechada")