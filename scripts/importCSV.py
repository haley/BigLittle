# pip install neo4j-driver

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "137137137"))
session = driver.session()

def _csv_to_neo(tx, path, entity):
    result = tx.run(f'''
        LOAD CSV WITH HEADERS FROM "{path}" AS row
        CREATE (n:{entity})
        SET n = row
        RETURN n
    ''', path=path, entity=entity)
    return result

def _create_relationship(tx, relater, relatee, relation):
    result = tx.run(f'''
        MATCH (n:{relater}),(m:{relatee})
        WHERE n.{relatee}ID = m.ID
        CREATE (n)-[:{relation}]->(m)
    ''', relater=relater, relatee=relatee, relation=relation)
    return result

result = session.run(f'''MATCH (n) DELETE n''')
for record in result:
    print(record)

result = session.run('''CREATE INDEX ON :Members(ID)''')
for record in result:
    print(record)

result = session.run('''CREATE INDEX ON :Organization(ID)''')
for record in result:
    print(record)

result = session.run('''CREATE INDEX ON :Users(ID)''')
for record in result:
    print(record)

result = session.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/Members.csv" AS row
    CREATE (n:Members)
    SET n = row
    RETURN n
''')
for record in result:
    print(record)

result = session.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/Organizations.csv" AS row
    CREATE (n:Organizations)
    SET n = row
    RETURN n
''')
for record in result:
    print(record)

result = session.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/Users.csv" AS row
    CREATE (n:Users)
    SET n = row
    RETURN n
''')
for record in result:
    print(record)

result = session.run('''
    MATCH (n:User),(m:Member)
    WHERE n.MemberID = m.ID
    CREATE (n)-[:PARTICIPATES]->(m)
''')
for record in result:
    print(record)

result = session.run('''
    MATCH (n:Member),(m:Organization)
    WHERE n.OrganizationID = m.ID
    CREATE (n)-[:IN]->(m)
''')
for record in result:
    print(record)

session.close()
