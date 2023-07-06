import pyodbc
from email.message import EmailMessage
import ssl
import smtplib

connection_string = ""
table_name = ''


def fetch_entries(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AllMenuData WHERE Name LIKE '%chicken%' OR Name LIKE '%kiwi%'")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def send_text():
    email_sender = ""
    email_password = ""
    email_receiver = ''
    subject = "DiningCourtMessenger"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)

        for entry in entries:
            date = entry[0]
            dining_court = entry[1]
            meal = entry[2]
            food = entry[3]
            body = f"""
                    {food} is being served at {dining_court} dining court for {meal} today, {date}!
                """
            em.set_content(body)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            

def main():
    conn = pyodbc.connect(connection_string)
    entries = fetch_entries(conn)

    if len(entries) == 0:
        print('No matches found.')
        return

    print(entries)

    send_text()

    print('finished!')


if __name__ == "__main__":
    main()
