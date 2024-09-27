import tkinter as tk

#商品の価格設定
products = {"ハリルマムーン": 2000, "メデューサ": 3000, "ソフトドリンク": 500}

#商品の数量を保持する辞書
quantities = {product: 0 for product in products}

#合計金額を計算して表示する関数
def show_total():
    total = 0
    for product in products:
        total += products[product]* quantities[product]
    total_label.config(text=f"合計金額:{total}円")

#商品の数量を増やす関数
def add_item(product):
    quantities[product] += 1
    update_quantity_labels()
    show_total()

#商品の数量ラベルを更新する関数
def update_quantity_labels():
    for product in products:
        quantity_labels[product].config(text=f"{quantities[product]}個")

#ウインドウを作る
window = tk.Tk()
window.title("メニュー表")

#商品ごとのボタンと数量表示を作る
quantity_labels={}
for i, product in enumerate(products):
    tk.Label(window,text=f"{product}({products[product]}円)").grid(row=i,column=0)

    button = tk.Button(window, text="追加", command = lambda p=product: add_item(p))
    button.grid(row=i, column=1)

    label = tk.Label(window, text="0個")
    label.grid(row = i, column = 2)

    quantity_labels[product] = label

#合計金額を表示するラベル
total_label = tk.Label(window, text="合計:0円")
total_label.grid(row = len(products), columnspan = 3)

#ウインドウを表示する
window.mainloop()
