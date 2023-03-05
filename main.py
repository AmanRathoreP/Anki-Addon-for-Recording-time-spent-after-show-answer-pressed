from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from .src import my_logger
from .src import my_constants
from aqt import gui_hooks
import time

my_logger.add_log("all stuff imported")

last_card_id = None
last_card_taken_time = None


def save_card_data(card, sec):
    with open(f"{my_constants.user_data_dir}\data.csv", 'a') as f:
        f.write(f"{card.id},{sec}\n")


def card_answer_shown(card, *args):
    """This function does the stuff as soon as the card's answer is shown to the reviewer i.e. user
    It means that one the user had pressed the show answer button this function will run form hook
    """
    global last_card_taken_time
    global last_card_id
    last_card_id = card.id
    last_card_taken_time = time.time()
    my_logger.add_log(f"Card\'s answer is shown with card id: {last_card_id}")


def reviewing_completed(reviewer, card, *args):
    """This function done stuff after the completion of the reviewing of the specific card"""
    global last_card_taken_time
    global last_card_id
    if last_card_id == card.id:
        my_logger.add_log(
            f"Reviewing completed of card with card id: {last_card_id}")
        global last_card_taken_time
        last_card_taken_time = time.time()-last_card_taken_time
        save_card_data(card, last_card_taken_time)
    else:
        # my_logger.add_log(
        #     "Id of reviewed card and the previously shown card is not same", my_logger.logging.WARNING)
        my_logger.add_log(
            f"Previous id = {last_card_id}, Current id = {card.id}", my_logger.logging.WARNING)


gui_hooks.reviewer_did_show_answer.append(card_answer_shown)
gui_hooks.reviewer_did_answer_card.append(reviewing_completed)
