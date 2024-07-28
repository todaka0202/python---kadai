import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
# bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
bgr = tk.PhotoImage(file="stone_00082.jpg")
window.configure(bg=bgr)
# ↑↑↑ お約束のコード ↑↑↑

# frame =  tk.Frame(window,padx=195,)
# frame.grid()
#forで繰り返しlist内を検索

frame1 = tk.Frame(height=100, width=500, pady=5, padx=5)
frame1.place(x=200,y=150)

frame2 = tk.Frame(height=100, width=500)
frame2.place(x=255,y=100)

list =[[1,2,3],
       [4,5,6],
       [7,8,9]]

victorymessage = "あなたの勝ちです！"


#ボタン

def resetbutton_action():
    # 1行目
    list[0][0] = 1
    list[0][1] = 2
    list[0][2] = 3
    # 2行目
    list[1][0] = 4
    list[1][1] = 5
    list[1][2] = 6
    # 3行目
    list[2][0] = 7
    list[2][1] = 8 
    list[2][2] = 9

    # 1行目
    button1.config(text="　")
    button2.config(text="　")
    button3.config(text="　")
    # 2行目
    button4.config(text="　")
    button5.config(text="　")
    button6.config(text="　")
    # 3行目
    button7.config(text="　")
    button8.config(text="　")
    button9.config(text="　")

    label1.config(text="")


# 横1行目
def button_action1():  
    button1.config(text="◯")
    list[0][0] = "◯"
    # 横1行目
    if list[0][0] == "◯" and list[0][1] == "◯" and list[0][2] == "◯":
        label1.config(text=victorymessage)
    # 縦1行目
    elif list[0][0] =="◯" and list[1][0] =="◯" and list[2][0] =="◯":
        label1.config(text=victorymessage)
    # 右斜め下
    elif list[0][0] =="◯" and list[1][1] =="◯" and list[2][2] =="◯":
        label1.config(text=victorymessage)

def button_action2():  
    button2.config(text="◯")
    list[0][1] = "◯"
    # 横1行目
    if list[0][0] == "◯" and list[0][1] == "◯" and list[0][2] == "◯":
        label1.config(text=victorymessage)
    # 縦2行目
    elif list[0][1] == "◯" and list[1][1] == "◯" and list[2][1] == "◯":
        label1.config(text=victorymessage)

def button_action3():  
    button3.config(text="◯")
    list[0][2] = "◯"
    # 横1行目
    if list[0][0] == "◯" and list[0][1] == "◯" and list[0][2] == "◯":
        label1.config(text=victorymessage)
    # 縦3行目
    elif list[0][2] == "◯" and list[1][2] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)
    # 左斜め下
    elif list[0][2] == "◯" and list[1][1] == "◯" and list[2][0] == "◯":
        label1.config(text=victorymessage)
    

# 横2行目
def button_action4():  
    button4.config(text="◯")
    list[1][0] = "◯"
    # 横2行目
    if list[1][0] == "◯" and list[1][1] == "◯" and list[1][2] == "◯":
        label1.config(text=victorymessage)
    # 縦1行目
    elif list[0][0] == "◯" and list[1][0] == "◯" and list[2][0] == "◯":
        label1.config(text=victorymessage)
    # 右斜め下
    elif list[0][0] =="◯" and list[1][1] =="◯" and list[2][2] =="◯":
        label1.config(text=victorymessage)

def button_action5():  
    button5.config(text="◯")
    list[1][1] = "◯"
    # 横2行目
    if list[1][0] == "◯" and list[1][1] == "◯" and list[1][2] == "◯":
        label1.config(text=victorymessage)
    # 縦2行目
    elif list[0][1] == "◯" and list[1][1] == "◯" and list[2][1] == "◯":
        label1.config(text=victorymessage)
    # 右斜め下
    elif list[0][0] =="◯" and list[1][1] =="◯" and list[2][2] =="◯":
        label1.config(text=victorymessage)
    # 左斜め下
    elif list[0][2] == "◯" and list[1][1] == "◯" and list[2][0] == "◯":
        label1.config(text=victorymessage)
    
def button_action6():  
    button6.config(text="◯")
    list[1][2] = "◯"
    # 横2行目
    if list[1][0] == "◯" and list[1][1] == "◯" and list[1][2] == "◯":
        label1.config(text=victorymessage)
    # 縦3行目
    elif list[0][2] == "◯" and list[1][2] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)


# 横3行目
def button_action7():  
    button7.config(text="◯")
    list[2][0] = "◯"
    # 横3行目
    if list[2][0] == "◯" and list[2][1] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)
    # 縦1行目
    elif list[0][0] =="◯" and list[1][0] =="◯" and list[2][0] =="◯":
        label1.config(text=victorymessage)
    # 左斜め下
    elif list[0][2] == "◯" and list[1][1] == "◯" and list[2][0] == "◯":
        label1.config(text=victorymessage)

def button_action8():  
    button8.config(text="◯")
    list[2][1] = "◯"
    # 横3行目
    if list[2][0] == "◯" and list[2][1] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)
    # 縦2行目
    elif list[0][1] == "◯" and list[1][1] == "◯" and list[2][1] == "◯":
        label1.config(text=victorymessage)

def button_action9():  
    button9.config(text="◯")
    list[2][2] = "◯"
    # 横3行目
    if list[2][0] == "◯" and list[2][1] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)
    # 縦3行目
    elif list[0][2] == "◯" and list[1][2] == "◯" and list[2][2] == "◯":
        label1.config(text=victorymessage)
    #右斜め下
    elif list[0][0] =="◯" and list[1][1] =="◯" and list[2][2] =="◯":
        label1.config(text=victorymessage)


# 入力フィールドの作成

# ボタンの作成
resetbutton = tk.Button(frame2, text="リセット", command=resetbutton_action)
resetbutton.grid(column=3,row=3,padx=0)

button1 = tk.Button(frame1, text="　", command=button_action1)
button1.grid(row=4, column=1, padx=5,pady=5)

button2 = tk.Button(frame1, text="　", command=button_action2)
button2.grid(row=4, column=3, padx=5,pady=5)

button3 = tk.Button(frame1, text="　", command=button_action3)
button3.grid(row=4, column=5, padx=5,pady=5)

button4 = tk.Button(frame1, text="　", command=button_action4)
button4.grid(row=5, column=1, padx=5,pady=5)

button5 = tk.Button(frame1, text="　", command=button_action5)
button5.grid(row=5, column=3, padx=5,pady=5)

button6 = tk.Button(frame1,text="　", command=button_action6)
button6.grid(row=5, column=5, padx=5,pady=5)

button7 = tk.Button(frame1, text="　", command=button_action7)
button7.grid(row=7, column=1, padx=5,pady=5)

button8 = tk.Button(frame1, text="　", command=button_action8)
button8.grid(row=7, column=3, padx=5,pady=5)

button9 = tk.Button(frame1, text="　", command=button_action9)
button9.grid(row=7, column=5, padx=5,pady=5)



label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.grid(column=3,row=1,pady=15)

label2 = tk.Label(window, text="あなたは◯です", bg=bg_color, fg=fg_color)
label2.grid(column=3,row=2,pady=5,padx=255)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
