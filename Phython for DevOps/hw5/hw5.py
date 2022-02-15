#Task: There is some SQLite database example.db. 
# Create program that sets in database ports (ServerPorts.port_number)
# to 443 for all servers apache (ServerTypes.type_name is 'apache') in project 'Project3'.


import os, sqlite3

db = os.path.join(os.path.dirname(__file__), 'demo.db')
sql_update = '''UPDATE ServerPorts
                SET port_number = {}
                WHERE ServerPorts.id IN (
                    SELECT ServerPorts.id From ServerPorts
                    INNER JOIN Servers ON Servers.id = ServerPorts.servers_id
                    INNER JOIN ServerTypes ON ServerTypes.id = Servers.servertypes_id
                    INNER JOIN ServerProjects ON ServerProjects.servers_id = Servers.id
                    INNER JOIN Projects ON Projects.id = ServerProjects.projects_id
                    WHERE Projects.proj_name = '{}' AND ServerTypes.type_name = '{}'
                )
'''
sql_select = ''' SELECT port_number, proj_name FROM ServerPorts
                 INNER JOIN Servers ON Servers.id = ServerPorts.servers_id
                 INNER JOIN ServerTypes ON ServerTypes.id = Servers.servertypes_id
                 INNER JOIN ServerProjects ON ServerProjects.servers_id = Servers.id
                 INNER JOIN Projects ON Projects.id = ServerProjects.projects_id
                 WHERE Projects.proj_name = '{}' AND ServerTypes.type_name = '{}'          
'''
with sqlite3.connect(db) as conn:
    print("Current ports")
    cur = conn.cursor()
    cur.execute(sql_select)
    for result in cur:
        print(result)
    print("Ports after update")
    cur.execute(sql_update)
    cur.execute(sql_select)
    for result in cur:
        print(result)
