import cv2
import tkinter as tk
from PIL import Image, ImageTk
import Cards
import os
import VideoStream
import blackjack as bj
import threading

# Constants for camera settings
IM_WIDTH = 1280
IM_HEIGHT = 720 
FRAME_RATE = 10

frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize the video stream
videostream = VideoStream.VideoStream((IM_WIDTH, IM_HEIGHT), FRAME_RATE, 2, 0).start()

# Load card images
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks(path + '/Card_Imgs/')
train_suits = Cards.load_suits(path + '/Card_Imgs/')

# Initialize variables for hand and deck
hand = []
deck = bj.buildDeck()

# Function to detect cards
def detect_cards():
    global hand, deck
    while True:
        # Start timer (for calculating frame rate)
        t1 = cv2.getTickCount()

        # Grab frame from video stream
        frame = videostream.read()

        # Pre-process camera image (gray, blur, and threshold it)
        pre_proc = Cards.preprocess_image(frame)
        
        # Find and sort the contours of all cards in the image (query cards)
        cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

        # If there are no contours, do nothing
        if len(cnts_sort) != 0:
            # Initialize a new "cards" list to assign the card objects.
            cards = []
            k = 0

            # For each contour detected:
            for i in range(len(cnts_sort)):
                if cnt_is_card[i] == 1:
                    # Create a card object from the contour and append it to the list of cards.
                    cards.append(Cards.preprocess_card(cnts_sort[i], frame))

                    # Find the best rank and suit match for the card.
                    cards[k].best_rank_match, cards[k].best_suit_match, cards[k].rank_diff, cards[k].suit_diff = Cards.match_card(cards[k], train_ranks, train_suits)

                    # sending rank and suit to func
                    deck = bj.deckChange(deck, cards[k].best_rank_match, cards[k].best_suit_match)

                    # Draw center point and match result on the image.
                    frame = Cards.draw_results(frame, cards[k])
                    k += 1

            # Draw card contours on image
            if len(cards) != 0:
                temp_cnts = [card.contour for card in cards]
                cv2.drawContours(frame, temp_cnts, -1, (255, 0, 0), 2)

        # Update global variables
        hand = bj.createHand(deck)
        
        # Calculate framerate
        t2 = cv2.getTickCount()
        time1 = (t2 - t1) / freq
        frame_rate_calc = 1 / time1

# Function to update the GUI
def update_gui():
    root = tk.Tk()
    root.title("Card Detector GUI")

    # Create a label to display the video stream
    video_label = tk.Label(root)
    video_label.pack(side=tk.LEFT)

    # Create a frame for displaying hand and deck
    info_frame = tk.Frame(root)
    info_frame.pack(side=tk.RIGHT)

    # Create a label to display the hand
    hand_label = tk.Label(info_frame, text="Hand:")
    hand_label.pack()

    # Create a label to display the deck
    deck_label = tk.Label(info_frame, text="Deck:")
    deck_label.pack()

    # Function to update the hand and deck
    def update_info():
        global hand, deck
        while True:
            deck_text = ", ".join(str(card) for card in deck)
            hand_text = "\n".join(str(card) for card in hand)
            deck_label.config(text="Deck: " + deck_text)
            hand_label.config(text="Hand:\n" + hand_text)
            info_frame.after(1000, update_info)  # Update every second

    # Start updating the hand/deck info
    update_info()

    # Run the GUI
    root.mainloop()

# Start card detection and GUI update threads
t1 = threading.Thread(target=detect_cards)
t1.start()

update_gui()

# Clean up
cv2.destroyAllWindows()
videostream.stop()
