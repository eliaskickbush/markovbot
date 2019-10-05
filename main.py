import sqlite3,random


class DatabaseDriver:
    def __init__(self, name):
        self.db = sqlite3.connect(f'{name}.db')
        cur = self.db.cursor()
        cur.execute("create table if not exists dataset (word STRING, succesor STRING, times INT);")
        self.db.commit()

    def insert_combination(self, word, succesor, times):
        cur = self.db.execute('select times from dataset where word=? and succesor=?', (word,succesor))
        res = cur.fetchall()
        if len(res) == 0:
            self.db.execute('insert into dataset values(?,?,?)', (word, succesor, times))
        else:
            times = times + int(res[0][0])
            self.db.execute('update dataset set times = ? where word=? and succesor=?', (times, word, succesor))
        self.db.commit()

    def get_word_info(self, word):
        cur = self.db.execute('select succesor, times from dataset where word=?', (word,))
        return cur.fetchall()

    def clean_word(self, word):
        self.db.execute('delete from dataset where word=?', (word,))

class MarkovBot:
    def __init__(self, database):
        self.db_driver = DatabaseDriver(database)

    def digest_text(self, text):
        words = text.split()
        for i in range(len(words)-1):
            self.db_driver.insert_combination(words[i], words[i+1], 1)

    def build_intervals(self, word_info):
        total_elements = 0
        probs = 0
        intervals = []

        for i in range(len(word_info)):
            this_elements_weight = word_info[i][1]
            total_elements += this_elements_weight
        print(total_elements)
        for i in range(len(word_info)):
            this_elements_weight = word_info[i][1]
            intervals.append((probs, probs + this_elements_weight / total_elements, word_info[i][0]))
            probs += this_elements_weight/total_elements
        return intervals

    def generate_text(self, begin_with, word_cap):
        text = begin_with
        current_word = text.split()[-1]
        word_info = self.db_driver.get_word_info(current_word)
        i = 0
        while i < word_cap and len(word_info) != 0:
            next_word = ""
            intervals = self.build_intervals(word_info)
            rand = random.random()
            for interval in intervals:
                if interval[0] <= rand < interval[1]:
                    next_word = interval[2]
                    break
            text = text + f" {next_word}"
            word_info = self.db_driver.get_word_info(next_word)
            i += 1
        return text

if __name__ == '__main__':
    a = MarkovBot("pepito")
    elem_info = a.db_driver.get_word_info("la")
    print(elem_info)
    print(a.build_intervals(elem_info))
    print(a.generate_text("la", 10))