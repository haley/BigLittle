from py2neo import Graph, Schema

create_index = '''CREATE INDEX ON :{entity}(ID)'''

def _csv_to_neo(path, entity):
    return f'''
        LOAD CSV WITH HEADERS FROM "{path}" AS row
        CREATE (n:{entity})
        SET n = row
        RETURN n
    '''

def _create_relationship(relater, relatee, relation):
    return f'''
        MATCH (n:{relater}),(m:{relatee})
        WHERE n.ID = m.{relater}ID
        CREATE (n)-[:{relation}]->(m)
    '''

graph = Graph(auth=("neo4j", "137137137"))
graph.delete_all()

tx = graph.begin()
tx.run('''CREATE INDEX ON :Members(ID)''')
tx.run('''CREATE INDEX ON :Organizations(ID)''')
tx.run('''CREATE INDEX ON :Users(ID)''')
tx.commit()

tx = graph.begin()
tx.run(_csv_to_neo(path="file:///data/Members.csv", entity="Members"))
tx.run(_csv_to_neo(path="file:///data/Organizations.csv", entity="Organizations"))
tx.run(_csv_to_neo(path="file:///data/Users.csv", entity="Users"))
tx.commit()

tx = graph.begin()
tx.run(_create_relationship(relater="User", relatee="Member", relation="PARTICIPATES"))
tx.run(_create_relationship(relater="Member", relatee="Organization", relation="IN"))
tx.commit()
