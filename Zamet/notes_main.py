from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QLineEdit, QPushButton, QListWidget, QTextEdit, QInputDialog 
import json

app = QApplication([])

notes = {"Добро Пожаловать":{
    "текст":"Это самое лучшее приложение в мире!",
    "теги":["добро", "инструкция"]
    }
}
with  open('notes_data.json','w') as file:
    json.dump(notes, file)
notes_win = QWidget()

notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900,600)


list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

button_note_create = QPushButton('Создать заметку') 
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
field_text = QTextEdit()
fileld_tag = QLineEdit('')
fileld_tag.setPlaceholderText('Введите тег')

button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметку')

list_tag = QListWidget()
list_tag_label = QLabel('Списог тегов')

Layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QVBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tag_label)
col_2.addWidget(list_tag)
col_2.addWidget(fileld_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

Layout_notes.addLayout(col_1)
Layout_notes.addLayout(col_2)

notes_win.setLayout(Layout_notes)

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[name]["теги"])
def add_note():
    note_name, ok = QInputDialog.getText(
        notes_win, "Добавить Заметку", "Название Заметки:"   
    )
    if ok and note_name != "":
        notes[note_name] = {"Текст" : "", "теги" : []}
        list_notes.addItem(note_name)
button_note_create.clicked.connect(add_note)        
 
def del_note():
    if list_notes.selectedItems():
        key = list.notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json',"w") as file:
            json.dump(notes,file,sort_key = True)
    else:
       print("Заметка не выбрана")
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['Текст'] = field_text.toPlainText()
        with open('notes_data.json', "w") as file:
            json.dump(notes,file, sort_keys = True)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = fileld_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tag.addItem(tag)
            fileld_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print("Заметка для добавления тега не выбрана!")
    
def del_tag():
    if list_tag.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tag.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
              json.dump(notes, file, sort_keys=True)
    else:
        print("Тег для удаления не выбран!")
def search_tag():
    tag = field_tag.text()
    if button_tag_search.text() == "Искать Заметки по тегу" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        button_tag_search.setText("Сбросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif button_tag_search.text() == "Сбросить Поиск":
        field_tag.clear()
        list_notes.clear()
        list_tag.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("искать Заметки по тегу")
    else:
        pass



button_tag_del.clicked.connect(del_tag)
button_tag_add.clicked.connect(add_tag)



notes_win.show()
app.exec()