import tkinter as tk
import time
import random

##跳出訊息視窗提醒休息 
##原本在python中用localtime及sleep來排程 後來改成搭配windows工作排程 (搜尋列打task)呼叫
##C:\Users\Teddy\.pyenv\pyenv-win\versions\3.10.11\pythonw.exe D:\Coding\Python\DailyLifeKit\toast.pyw
##pyw 代表隱藏視窗


def show_random_reminder():
    reminders = [
    "相信你自己，你就已經完成了一半的工作。",
    "每一個失敗，都是一次學習的機會。",
    "成功的關鍵在於不放棄。",
    "做自己喜歡的事情，你就不會有壓力。",
    "不要害怕挑戰，它們讓你變得更強大。",
    "不要等待機會，而是創造機會。",
    "信心來自於努力，勇氣來自於挑戰。",
    "改變世界的人往往是那些瘋狂夢想的人。",
    "每過一分鐘，就過了六十秒，別浪費它！",
    "每個靈魂，都值得被自己珍視欣賞。",
    "想像中最棒的自己會怎麼做？",
    "一定要相信自己，一定要過得快樂",
    "晚安，瑪卡巴卡",
    "人生三樂，自得其樂，知足常樂，助人為樂。",
    "寧願失敗地做你喜愛的事情，也不要成功地做你討厭的事情。",
    "唯有那些異想天開的人，才能完成不可能的事。",
    "心中有愛，才會人見人愛。",
    "有時煩惱是來自不合理的欲望。"
    ]
    message = random.choice(reminders)
    return message
    
    
def show_reminder(message):
    root = tk.Tk()
    root.title("休息提醒")
    font = ("微軟正黑體", 16)
    label = tk.Label(root, text=message, font=font)
    label.pack(padx=40, pady=40)

    root.after(30000, root.destroy)  # 30秒後自動關閉視窗

    root.attributes("-topmost", True) # 將視窗移動到最前景
    root.mainloop()

def main():
    # while True:
    #     current_time = time.localtime()
    #     if current_time.tm_min ==0:
    #         show_reminder("到了整點，該休息一下了！")
    #         # 可以根據需要調整提醒的內容
    #     time.sleep(60)
    msg = show_random_reminder()
    show_reminder(msg)

if __name__ == "__main__":
    main()
