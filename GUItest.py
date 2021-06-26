from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk  # 콤보박스, progress bar
import time
from tkinter import filedialog
# from tkinter.tix import *  # 창 자체 스크롤


def clickButton():
    first.config(text="파일 넣기 완료!!!!")

    for i in range(1, 101):
        time.sleep(0.01)

        P_var2.set(i)
        progressbar2.update()

    messagebox.showinfo("실행", "실행완료!!")
    # messagebox.showerror("에러", "오류발생!!")


def btncmd():
    print(txt.get("1.0", END))  # 1.0: 첫번째라인, 0번째 컬럼부터 끝까지(END)
    print(ent.get())  # get은 위의 위치에 해당하는 글자를 가져옴.

    txt.delete("1.0", END)
    ent.delete(0, END)  # 0부터 끝까지 없애기

    listbox.delete(END)  # 맨 뒤에꺼부터 없애기

    print("선택된 항목: ", listbox.curselection())
    #listbox.size(),  listbox.get(0,2)


def btcchekc():
    print(chkclick.get())


def fileload():
    window.filename = filedialog.askopenfilenames(
        initialdir="C:/", title="choose your file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    print(window.filename)
    data = open(window.filename, 'rt', encoding="utf-8")


# ---------------------------------------------------------------

# """창 만들기"""
window = Tk()
window.title("testfile")
window.geometry("1200x800")
# win_scroll = ScrolledWindow(window, width=320, height=240)
# win_scroll.pack()
# window.resizable(width=TRUE, height=TRUE)


# """프레임 만들기"""
id_pw = Frame(window, relief="solid", bd=3)
id_pw = LabelFrame(window, text="데이터를 끌어넣어주세요")
id_pw.pack()
editBox = Entry(id_pw, width=10, bg='white')  # 한줄입력 가능 -> 아이디나 PW
editBox.pack(padx=10, pady=10)

# """글 입력창 만들기"""
txt = Text(window, width=30, height=10)
txt.pack()
txt.insert(END, "글자를 입력하세요.")

# """한줄만 가능 글 입력창 만들기"""
ent = Entry(window, width=30)
ent.pack()
ent.insert(0, "한줄입력")

# """리스트 박스 만들기"""
listbox = Listbox(window, selectmode="extended", height=0, bg='orange')
listbox.insert(0, "대한민국")
listbox.insert(1, "독일")
listbox.insert(2, "미국")
listbox.insert(3, "호주")
listbox.insert(END, "뉴질랜드")  # 여러개 누르려면 ctrl or 끌기 등
listbox.pack()

# """라벨(그냥 글) 만들기"""
first = Label(window, text="data 파일을 넣어주세요")
first.pack()

# 체크 버튼 위젯 만들기
chkclick = IntVar()  # chkclick에 int형으로 값을 저장.
chkbox = Checkbutton(window, text="오늘 하루 그만 보기", variable=chkclick)
# chkbox.select()
chkbox.pack()

# 진행 바 만들기
progressbar = ttk.Progressbar(
    window, maximum=100, mode="indeterminate")  # indeterminate
progressbar.start(10)
progressbar.pack()
progressbar.stop()

P_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(
    window, maximum=100, length=150, variable=P_var2)
progressbar2.pack()


# """버튼 만들기"""
버튼1 = Button(window, text="실행",  command=clickButton)
버튼1.pack(side=LEFT)

버튼2 = Button(window, text="나는야버튼", command=btncmd)
버튼2.pack()

버튼3 = Button(window, text="체크확인", command=btcchekc)
버튼3.pack()

버튼4 = Button(window, text="파일 불러오기", command=fileload)
버튼4.pack()

window.mainloop()
