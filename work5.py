import tkinter as tk
import random

#リストからランダムで要素を表示する
#入力を受け取る
#選択した要素と入力を比較する
#正解だったらまたランダムで要素を抽出
#不正解だったら「不正解」と表示する

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
str_list=["python","tkinter","javascript","toukyou"]


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    
    if label1.cget("text") == user_input:
        label1.config(text=random.choice(str_list))
        entry1.delete(0, tk.END)
        label2.config(text="")
    else:
        label2.config(text="×")

         # 画面に出力

label1 = tk.Label(window, text=random.choices(str_list), bg=bg_color, fg=fg_color)
label1.pack(pady=10)

label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
# label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
# label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑