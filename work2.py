import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

label2 = tk.Label(window, text="西暦を入力して下さい", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()
    if int(user_input) > 1911 and int(user_input) < 1926:  # 入力値を取得
        wareki = int(user_input) - 1911
        genngou = "大正"
        label1.config(text=f"{user_input}年は{genngou}{wareki}年")  # 画面に出力
    elif int(user_input) > 1925 and int(user_input) < 1989:
        wareki = int(user_input) - 1925
        genngou = "昭和"
        label1.config(text=f"{user_input}年は{genngou}{wareki}年")
    elif int(user_input) > 1988 and int(user_input) < 2019:
        wareki = int(user_input) - 1988
        genngou = "平成"
        label1.config(text=f"{user_input}年は{genngou}{wareki}年")
    elif int(user_input) > 2018 and int(user_input) < 2025:
        wareki = int(user_input) - 2018
        genngou = "令和"
        label1.config(text=f"{user_input}年は{genngou}{wareki}年")
    else:
        label1.config(text=f"この西暦は対応してないよ！")



# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="和暦に変換！", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成

label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
