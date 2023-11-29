import tkinter
import requests
import json

def click() -> None:
    userDataDictionary: dict = getDictionaryUserData(text.get())
    newUserDataDictionary: dict = createNewDictionary(userDataDictionary)
    try:
        createJsonFile(newUserDataDictionary)
        tkinter.Label(window, text="Информация сохранена в файл 'repository_info.json'.").pack()
    except Exception as e:
        tkinter.Label(window, text=f"Ошибка при сохранении информации в файл 'repository_info.json': {e}").pack()
    

def getDictionaryUserData(user: str) -> dict:
    url: str = f"https://api.github.com/users/{user}"
    return json.loads(json.dumps(requests.get(url).json()))

def createNewDictionary(userDictionary: dict) -> dict:
    templateDictionary: dict = {
        "company": "",
        "created_at": "",
        "email": "",
        "id": "",
        "name": "",
        "url": ""
    }
    for i in templateDictionary.keys():
        templateDictionary[i] = userDictionary[i]
    return templateDictionary

def createJsonFile(dictionary: dict) -> None:
    with open("repository_info.json", 'w') as file:
        json.dump(dictionary, file, indent=4)

window = tkinter.Tk()
window.geometry("350x250")
window.title("GitHub Repository Info")

tkinter.Label(window, text="Введите имя репозитория: Например 'firehol'").pack()
text = tkinter.Entry(window, width=30)
text.pack(pady=2)

button = tkinter.Button(window, text="Получить файл", command=click)
button.pack(pady=2)
window.mainloop()