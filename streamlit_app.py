import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import json
import sqlite3
import hashlib

# Define client ID, secret, and scopes
CLIENT_ID = ''
CLIENT_SECRET = ''
SCOPES = ['https://www.googleapis.com/auth/userinfo.email']

# Database management functions
def create_usertable(conn):
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(conn, username, password):
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()

def login_user(conn, username, password):
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def view_all_users(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

# Security functions
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# Google Sign-up Button
def google_signup(client_id, client_secret, scopes):
    if 'google_credentials' not in st.session_state:
        flow = Flow.from_client_config(client_config={'client_id': client_id,
                                                      'client_secret': client_secret,
                                                      'redirect_uris': ['urn:ietf:wg:oauth:2.0:oob']},
                                       scopes=scopes)
        auth_url, _ = flow.authorization_url(prompt='consent')
        st.write('Sign up with Google')
        st.markdown(f'<a href="{auth_url}">Sign in with Google</a>', unsafe_allow_html=True)
    else:
        credentials = Credentials.from_authorized_user_info(st.session_state['google_credentials'])
        st.write('Logged in as ' + credentials.email)

# Main function
def main():
    """Marriage Compatibility Test"""

    st.set_page_config(page_title="Marriage Compatibility Test",
                       page_icon=":heart:")

    # Landing Page Title
    st.title("Welcome to the Marriage Compatibility Test!")

    # Welcome Message
    st.write("""
        Welcome to the Marriage Compatibility Test, the ultimate tool for couples to understand their relationship better! Are you wondering if you and your partner are compatible or not? Do you want to identify the strengths and weaknesses in your relationship and work towards a happy and long-lasting marriage? Look no further!
    """)

    # Test Description (cont.)
    st.write("""
        Our Marriage Compatibility Test is perfect for engaged couples who want to know if they are compatible, newlyweds who want to build a strong foundation for their marriage, or long-term couples who want to revitalize their relationship. With our test, you can gain a deeper understanding of your partner, improve communication, and build a happier and more fulfilling relationship.

        Are you ready to take the first step towards a happier marriage? Take our Marriage Compatibility Test today and discover the key to a successful and lasting relationship!
    """)

    # Google Sign-up Button
    google_signup(CLIENT_ID, CLIENT_SECRET, SCOPES)
