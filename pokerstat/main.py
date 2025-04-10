import tkinter as tk
from Deck import Deck
from Hand import Hand

class PokerApp:
    def __init__(self, master):
        self.master = master
        master.title("Poker Game")

        self.deck = Deck()
        self.deck.shuffle()
        self.hand = Hand(self.deck, 5)

        self.deck_label = tk.Label(master, text="Deck:")
        self.deck_label.pack()

        self.deck_display = tk.Text(master, height=10, width=30)
        self.deck_display.tag_config('red_card', foreground="red")
        self.deck_display.tag_config('black_card', foreground="black")
        self.deck_display.pack()
        self.update_deck_display()

        self.hand_label = tk.Label(master, text="Your Hand:")
        self.hand_label.pack()

        self.hand_display = tk.Text(master, height=10, width=30)
        self.hand_display.tag_config('red_card', foreground="red")
        self.hand_display.tag_config('black_card', foreground="black")
        self.hand_display.pack()
        self.update_hand_display()

        self.board_label = tk.Label(master, text="Game Board:")
        self.board_label.pack()

        self.board_display = tk.Text(master, height=10, width=30)
        self.board_display.pack()

    def update_deck_display(self):

        self.deck_display.delete(1.0, tk.END)
        for card in self.deck.cards:
            if card.suit == 'Hearts' or card.suit == 'Diamonds':
                self.deck_display.insert(tk.END, f"{card}\n", 'red_card')
            else:
                self.deck_display.insert(tk.END, f"{card}\n", 'black_card')

    def update_hand_display(self):
        self.hand_display.delete(1.0, tk.END)
        for card in self.hand.cards:
            if card.suit == 'Hearts' or card.suit == 'Diamonds':
                self.hand_display.insert(tk.END, f"{card}\n", 'red_card')
            else:
                self.hand_display.insert(tk.END, f"{card}\n", 'black_card')
            

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerApp(root)
    root.mainloop()