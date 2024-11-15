import tkinter as tk
import random
from tkinter import messagebox  # 引入messagebox模块

class GuessWordGame:
    def __init__(self, word_list):
        self.word_list = word_list #词汇列表
        self.current_word = '' #当前词
        self.shuffled_word = '' #打乱后的词
        self.window = tk.Tk()
        self.window.title("Word Game")
        self.label = tk.Label(self.window, text="Please guess the word:")
        self.label.pack(pady=10)
        self.word_label = tk.Label(self.window, font=('Arial', 24))
        self.word_label.pack(pady=20)
        self.entry = tk.Entry(self.window, font=('Arial', 18))
        self.entry.pack(pady=10)
        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)
        self.skip_button = tk.Button(self.window, text="Skip", command=self.new_word)
        self.skip_button.pack(pady=10)
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack(pady=10)
        self.new_word()

    def new_word(self): #生成新的单词
        self.current_word = random.choice(self.word_list) #从词汇表中随机选择一个单词
        self.shuffled_word = ''.join(random.sample(self.current_word, len(self.current_word))) #打乱该单词的字母顺序
        self.word_label.config(text=self.shuffled_word) #这个打乱后的单词被设置为标签 self.word_label 的文本
        self.entry.delete(0, tk.END) #清空输入框

    def check_guess(self): #检查玩家的猜测是否正确
        player_guess = self.entry.get().strip().lower()
        if player_guess == self.current_word.lower():
            messagebox.showinfo("Correct", "Your guess is correct!")  # 使用tkinter.messagebox
            self.new_word()
        else:
            messagebox.showerror("Incorrect", "Your guess is incorrect. Try again.")  # 使用tkinter.messagebox

    def start_game(self): #启动游戏的Tkinter主循环
        self.window.mainloop()

# Load word list from a text file
def load_word_list(filename): #从txt中获取单词列表
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    return word_list

if __name__ == "__main__":
    # 加载单词列表
    word_list = load_word_list('words.txt')

    # 创建 GuessWordGame 的实例
    game = GuessWordGame(word_list)

    # 启动游戏
    game.start_game()
