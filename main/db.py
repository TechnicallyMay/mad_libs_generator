import sqlite3


class WordDatabase():

    def __init__(self):
        self.open_database()
        self.build_database()


    def open_database(self):
        self.conn = sqlite3.connect('../data/word_database.db')
        self.crsr = self.conn.cursor();


    def close_database(self):
        self.conn.commit()
        self.conn.close()


    def build_database(self):
        command = """CREATE TABLE IF NOT EXISTS words (
                     word STRING UNIQUE,
                     pos STRING NOT NULL,
                     pos2 STRING);"""
        self.execute(command)


    def add_word(self, word, parts_of_speech):
        command = """INSERT INTO words
                     VALUES (?, ?, ?)"""
        values = []
        values.append(word)
        for pos in parts_of_speech:
            values.append(pos)
        if len(values) == 2:
            values.append(None)
        self.execute(command, values)


    def execute(self, command, values=None):
        if values:
            self.crsr.execute(command, values)
        else:
            self.crsr.execute(command)
