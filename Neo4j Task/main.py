from neo4j import GraphDatabase
import pandas as pd

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "your_password"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return pd.DataFrame([record.data() for record in result])

query_1 = """
MATCH (t:Teacher)-[:TEACHES]->(c:COURSE)
RETURN t.name AS teacher, collect(c.name) AS courses
"""

query_2 = """
MATCH (s:STUDENT)-[:ENROLLED_IN]->(c:COURSE)
RETURN s.name AS student, collect(c.name) AS enrolled_courses
"""

print("-------------------------------------------------------------------")
print("\n1. Teachers and the courses they teach")
print(run_query(query_1))
print("-------------------------------------------------------------------")
print("\n2. Students and their enrolled courses")
print(run_query(query_2))
print("-------------------------------------------------------------------")

driver.close()
