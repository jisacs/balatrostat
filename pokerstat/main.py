import tkinter as tk
from pokerstat.Deck import Deck
from pokerstat.Hand import Hand
from pokerstat.Card import Card
from pokerstat.stats import get_stats

class PokerApp:
    def __init__(self, master):
        self.master = master
        master.title("Poker Game")

        self.initialize_game_objects()
        self.create_deck_display(master)
        self.create_hand_display(master)
        self.create_bin_display(master)
        self.create_statistics_display(master)

    def initialize_game_objects(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = Hand(self.deck, 10)
        self.bin = Deck(build=False)

    def create_deck_display(self, master):
        self.deck_label = tk.Label(master, text="Deck:", background='white')
        self.deck_label.pack()

        self.deck_display = tk.Text(master, height=5, width=100, background='white')
        self.configure_text_widget(self.deck_display)
        self.deck_display.pack()
        self.update_display(self.deck_display, self.deck.cards)

        self.move_to_hand_button = tk.Button(master, text="Move to Hand", 
        command=self.move_to_hand, background='white')
        self.move_to_hand_button.pack()

    def create_hand_display(self, master):
        self.hand_label = tk.Label(master, text="Your Hand:",
         background='white')
        self.hand_label.pack()

        self.hand_display = tk.Text(master, height=5, width=100,
         background='white')
        self.configure_text_widget(self.hand_display)
        self.hand_display.pack()
        self.update_hand_display()

        self.move_to_bin_button = tk.Button(master, text="Move to Bin", 
        command=self.move_to_bin, background='white')
        self.move_to_bin_button.pack()

    def create_bin_display(self, master):
        self.bin_label = tk.Label(master, text="Bin:", background='white')
        self.bin_label.pack()

        self.bin_display = tk.Text(master, height=5, width=100, background='white')
        self.configure_text_widget(self.bin_display)
        self.bin_display.pack()
        self.update_display(self.bin_display, self.bin.cards)

        self.move_from_bin_to_hand_button = tk.Button(master, text="Move from Bin to Hand",
         command=self.move_from_bin_to_hand, background='white')
        self.move_from_bin_to_hand_button.pack()

    def create_statistics_display(self, master):
        self.stat_label = tk.Label(master, text="Statistics:", background='black')
        self.stat_label.pack()

        self.stat_display = tk.Text(master, height=50, width=100, background='black')
        self.stat_display.pack()

        stats = get_stats([Card('2', 'Hearts'), Card('2', 'Clubs')], 
        self.deck)
        self.stat_display.insert(tk.END, f"{stats} ")

    def configure_text_widget(self, widget):
        widget.tag_config('red_card', foreground="red")
        widget.tag_config('black_card', foreground="black")       

    def move_from_bin_to_hand(self):
        try:
            selected_text = self.bin_display.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            selected_cards = selected_text.split(" ")  # Split selected cards by line
            for card_text in selected_cards:
                self.move_card(card_text.strip(), self.bin, self.hand)
            self.update_display(self.bin_display, self.bin.cards)
            self.update_hand_display()
        except tk.TclError:
            pass  # Handle case where no selection is made

    def move_to_hand(self):
        try:
            selected_text = self.deck_display.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            selected_cards = selected_text.split(" ")  # Split selected cards by line
            for card_text in selected_cards:
                self.move_card(card_text.strip(), self.deck, self.hand)
            self.update_display(self.deck_display, self.deck.cards)
            self.update_hand_display()
        except tk.TclError:
            pass  # Handle case where no selection is made

    def move_to_bin(self):
        try:
            selected_text = self.hand_display.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            selected_cards = selected_text.split(" ")  # Split selected cards by line
            for card_text in selected_cards:
                self.move_card(card_text.strip(), self.hand, self.bin)
            self.update_hand_display()
            self.update_display(self.bin_display, self.bin.cards)
        except tk.TclError:
            pass  # Handle case where no selection is made

    def move_card(self, card_text, source_deck, target_deck):
        for card in source_deck.cards:
            if str(card) == card_text:
                source_deck.cards.remove(card)
                target_deck.cards.append(card)
                break


    def group_and_sort_cards(self, cards, by_suit=True):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        value_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

        if by_suit:
            #result = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
            result = {suit: [] for suit in suits}

            # Group cards by suit
            for card in cards:
                result[card.suit].append(card)

            for suit in suits:
                result[suit].sort(key=lambda card: value_order[card.value], reverse=True)
        else:
             # Group cards without ergarding suit
            result = []
            for card in cards:
                result.append(card)
            result.sort(key=lambda card: value_order[card.value], reverse=True)
        return result


    def update_display(self, board, cards):
        board.delete(1.0, tk.END)
        suit_cards = self.group_and_sort_cards(cards)

        # Display cards by suit
        for suit, cards in suit_cards.items():
            for card in cards:
                tag = 'red_card' if suit in ['Hearts', 'Diamonds'] else 'black_card'
                board.insert(tk.END, f"{card} ", tag)
            board.insert(tk.END, "\n")

    def update_hand_display(self):
        self.hand_display.delete(1.0, tk.END)
        sorted_cards = self.group_and_sort_cards(self.hand.cards, by_suit=False)

        # Display cards by suit
        for card in sorted_cards:
            tag = 'red_card' if card.suit in ['Hearts', 'Diamonds'] else 'black_card'
            self.hand_display.insert(tk.END, f"{card} ", tag)
    
# Bind the methods to the PokerApp class
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background='white')
    app = PokerApp(root)
    root.mainloop()