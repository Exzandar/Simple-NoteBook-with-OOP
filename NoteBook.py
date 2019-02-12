import datetime
import sys

l_id = 1


class Note:
    def __init__(self, memo, tag=""):
        self.memo = memo
        self.tag = tag
        self.date = datetime.date.today()
        global l_id
        self.id = l_id
        l_id += 1


class NoteBook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tag=""):
        self.notes.append(Note(memo, tag))

    def modify_memo(self, i_d, new_memo):
        for note in self.notes:
            if note.id == int(i_d):
                note.memo = new_memo
                print("\nmemo is modified\n")
                break

    def modify_tags(self, id, tag=""):
        for note in self.notes:
            if note.id == id:
                note.tag = tag
                return True
        return False

    def match(self, match_word):
        x = 0
        for note in self.notes:
            if (match_word in note.memo) or (match_word in note.tag):
                print("match number [{}] is: [{}], it's ID: [{}], it's tag: [{}]\n"
                      .format(x, note.memo, note.id, note.tag))
                x += 1
        if x == 0:
            return "\nsorry, there is no match."


class Menu:
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {"1": self.show_notes,
                        "2": self.search_note,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit
                        }

    @staticmethod
    def show_menu():
        print(""" \n>>> Notebook Menu <<<\n
            1. Show all Notes
            2. Search Notes 
            3. Add Note 
            4. Modify Note 
            5. Quit """)

    def show_notes(self):
        for note in self.notebook.notes:
            print("ID: {}, memo: {}, tag: {}".format(note.id, note.memo, note.tag))

    def search_note(self):
        match = input("Search for: ")
        notes = self.notebook.match(match)
        print(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tg = input("enter the tag: ")
        self.notebook.new_note(memo, tg)
        print("\nYour note has been added.\t")

    def modify_note(self):
        id = int(input("Enter a note id: "))
        if id > l_id:
            print("\nsorry, Incorrect ID")
            return False
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Good Bye")
        sys.exit(0)

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nEnter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("\n{} is not a valid choice\n".format(choice))


if __name__ == "__main__":
    Menu().run()

