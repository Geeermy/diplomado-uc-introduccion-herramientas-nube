#! /usr/bin/env python
import argparse
import psycopg2

parser = argparse.ArgumentParser()

# Argumentos para la ejecución de la consulta.
parser.add_argument('--database', required=True)
parser.add_argument('--host', required=True)
parser.add_argument('--port', required=True)
parser.add_argument('--user', required=True)
parser.add_argument('--password', required=True)
parser.add_argument('--table_name', required=True)


'''
MODO DE EJECUCIÓN:
> python3 ec2_table_select.py --database nombre_base_de_datos --host nombre_host --port numero_puerto --user nombre_usuario --password contraseña --table_name nombre_tabla_a_consultar
Para que esto funcione correctamente, es necesario instalar la librería psycopg2.
Recuerde que al crear instancias con AWS RDS con motor PostgreSQL, el nombre por defecto de la base de datos es "postgres".
'''
if __name__ == "__main__":
    # Obtención de argumentos.
    args = parser.parse_args()
  
    connection = psycopg2.connect(
      database = args.database,
      host = args.host,
      port = args.port,
      user = args.user,
      password = args.password,
    )
    cursor = connection.cursor()
    sql = f'SELECT * FROM {args.table_name};'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
      print(row)
    connection.close()