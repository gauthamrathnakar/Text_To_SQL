import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#Configure API key
#genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key = "")

#Function to load Gemini model and give sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

#Function to retrive query from sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Define your prompt
prompt = ["""You are an expert in converting English questions to SQL queries. The SQL database has the name BUGS and has the
            following columns - TITLE, REPORTER, CURSTATE, PROJECT, TOOLVER, PRIORITY, and ASSIGNEE. Here TITLE refers to
            the title of the bug. REPORTER is the one who reported the bug. CURSTATE is the current state of the bug. It
            can be OPENED which means the bug is in an OPEN state, IMPLEMENTED which means the bug has been fixed and yet to be
            verified by the testing team, or CLOSED which means the bug has been closed. PROJECT means the Project that bug
            belongs to. It can be RGP (Radeon GPU Profiler), RMV (Radeon Memory Visualizer) or RRA (Radeon Raytracing Analyzer).
            TOOLVER refers to the version of the PROJECT. PRIORITY refers to the priority of the bug. It can be P1 which
            means high priority, P2 which means medium priority, and P3 which means lower priority. ASSIGNEE refers to who
            the bug is currently assigned to.

            For example,
            Example 1 -
            Provide the bugs whose PRIORITY is P1 and the SQL command looks like SELECT * from BUGS where PRIORITY = 'P1';

            Example 2 -
            What are all the bugs reported by Moily,Gautham? and the SQL command looks like SELECT * from BUGS where REPORTER = 'Moily,Gautham';

            Example 3 -
            Show me the titles of bugs that are currently OPENED and assigned to Hosier,Antony. and the SQL command looks like SELECT TITLE from BUGS where CURSTATE = 'OPENED' AND ASSIGNEE = 'Hosier,Antony';

            Example 4 -
            How many bugs are in the RGP project? and the SQL command looks like SELECT COUNT(*) from BUGS where PROJECT = 'RGP';

            Example 5 -
            List all bugs that are either in the IMPLEMENTED state or have a priority of P2. and the SQL command looks like SELECT * from BUGS where CURSTATE = 'IMPLEMENTED' OR PRIORITY = 'P2';

            Example 6 -
            Find bugs reported by Moily,Gautham for the RRA project. and the SQL command looks like SELECT * from BUGS where REPORTER = 'Moily,Gautham' AND PROJECT = 'RRA';

            Example 7 -
            Which bugs are not yet CLOSED? and the SQL command looks like SELECT * from BUGS where CURSTATE != 'CLOSED';

            Example 8 -
            Get the names of reporters and assignees for bugs with 'failed' in their title. and the SQL command looks like SELECT REPORTER, ASSIGNEE from BUGS where TITLE LIKE '%failed%';

            Example 9 -
            Show me all bugs ordered by priority from high to low. and the SQL command looks like SELECT * from BUGS ORDER BY PRIORITY;

            Example 10 -
            Find the distinct projects that have bugs. and the SQL command looks like SELECT DISTINCT PROJECT from BUGS;
            also the SQL code should not have ``` in beginning or end and sql word in output  
          """]




#Streamlit App
st.set_page_config(page_title = "I can retrieve any sql query")
st.header("Gemini app to retrieve SQL data")
question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

#if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "bugs.db")
    st.subheader("The response is:")
    for row in data:
        print(row)
        st.header(row)
