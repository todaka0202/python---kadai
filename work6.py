import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    # user_input = entry1.get()  # 入力値を取得
    label1.config(text=f"こんにちは")  # 画面に出力


# 入力フィールドの作成

# ボタンの作成
resetbutton = tk.Button(window, text="リセット", command=button_action1)
resetbutton.grid(column=2,row=5,padx=0)

button1 = tk.Button(window, text="", command=button_action1)
button1.grid(column=1,row=6,pady=10,padx=10)

button2 = tk.Button(window, text="", command=button_action1)
button2.grid(column=2,row=6,pady=10,padx=10)

button3 = tk.Button(window, text="", command=button_action1)
button3.grid(column=3,row=6,pady=10,padx=10)



# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.grid(column=2,row=2,pady=20)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
