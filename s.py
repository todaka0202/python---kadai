import tkinter as tk
# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
frame1 = tk.Frame(height=100, width=500, pady=10, padx=10)
frame1.place(x=180,y=80)
def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button1.config(text=":白い丸:︎")
def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button2.config(text=":白い丸:︎")
def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button3.config(text=":白い丸:︎")
def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button4.config(text=":白い丸:︎")
def button_action5():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button5.config(text=":白い丸:︎")
def button_action6():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button6.config(text=":白い丸:︎")
def button_action7():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button7.config(text=":白い丸:︎")
def button_action8():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button8.config(text=":白い丸:︎")
def button_action9():  # 関数の定義 ※ボタンが押されたときの動き
     label1.config(text=f"")  # 画面に出力
     button9.config(text=":白い丸:︎")
button1 = tk.Button(frame1, text="", command=button_action1)
button1.grid(row=5, column=1, padx=10)
button2 = tk.Button(frame1, text="", command=button_action2)
button2.grid(row=5, column=3, padx=10)
button3 = tk.Button(frame1, text="", command=button_action3)
button3.grid(row=5, column=5, padx=10)
button4 = tk.Button(frame1, text="", command=button_action4)
button4.grid(row=6, column=1, padx=10)
button5 = tk.Button(frame1, text="", command=button_action5)
button5.grid(row=6, column=3, padx=10)
button6 = tk.Button(frame1, text="", command=button_action6)
button6.grid(row=6, column=5, padx=10)
button7 = tk.Button(frame1, text="", command=button_action7)
button7.grid(row=7, column=1, padx=10)
button8 = tk.Button(frame1, text="", command=button_action8)
button8.grid(row=7, column=3, padx=10)
button9 = tk.Button(frame1, text="", command=button_action9)
button9.grid(row=7, column=5, padx=10)
# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.grid(pady=10)
label2 = tk.Label(window, text="あなたは:白い丸:︎です", bg=bg_color, fg=fg_color)
label2.place(x=180,y=30)
label3 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label3.grid(pady=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑