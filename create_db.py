import sqlite3

class DB:
    # Connect to SQLite database (or create it if it doesn't exist)
    def __init__(self):
        self.conn = sqlite3.connect('db/job_applications.db')
        self.c = self.conn.cursor()

        # Create Applications table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                position TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                interview_stage TEXT,
                notes TEXT
            )
        ''')
        self.conn.commit()

    def close_connection(self):
        if self.conn:
            self.conn.close()
    
    def insert_application(self,company_name, position, email, password, interview_stage, notes):
        self.c.execute('''
            INSERT INTO applications (company_name, position, email, password, interview_stage, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (company_name, position, email, password, interview_stage, notes))
        self.conn.commit()
        
    def get_all_applications(self):
        self.c.execute('SELECT * FROM applications')
        return self.c.fetchall()
        
    def update_interview_stage(self, app_id, new_stage):
        self.c.execute('''
              UPDATE applications
              SET interview_stage = ?
              WHERE id = ?
        ''', (new_stage, app_id))
        self.conn.commit()

    def delete_application(self, app_id):
        self.c.execute('''
            DELETE FROM applications
            WHERE id = ?
        ''', (app_id,))
        self.conn.commit()

    def print_all_applications(self):
        #Should be able to parse through the applications and return a string that is seperated by new lines
        applications = self.get_all_applications()

        for app in applications:
            id, company_name, position, email, password, interview_stage, notes = app
            print(f"Application ID: {id}")
            print(f"Company Name: {company_name}")
            print(f"Position: {position}")
            print(f"Email: {email}")
            print(f"Password: {password}")
            print(f"Interview Stage: {interview_stage}")
            print(f"Notes: {notes}")
            print("-" * 40)  # Separator line for readability




    # Example usage:
    # db = DB()
    # db.insert_application('Company A', 'Developer', 'email@example.com', 'password123', 'Initial Screening', 'Some notes')
    #  applications = db.get_all_applications()
    # print(applications)
    # db.close_connection()
    #db = DB()
    #for x in range(0, 99):
    #    db.insert_application('Company ' + str(x), 'Developer', 'email@example.com', 'password123', 'Initial Screening', 'Some notes')
    #db.print_all_applications()
    #db.close_connection()

