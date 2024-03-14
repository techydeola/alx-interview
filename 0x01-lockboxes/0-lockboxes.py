#!/usr/bin/python3
""" A module that solves the lockboxes challenge """


def canUnlockAll(boxes):
    """ This is module that determines if all the boxes can be opened

    Keyword arguments:
    boxes -- A list of list containing keys
    Return: True is all boxes can be unlocked
            otherwise return false
    """
    keyLists = [0]
    checked_boxes = set([0])

    for key in keyLists:
        for box_key in boxes[key]:
            if box_key not in checked_boxes:
                checked_boxes.add(box_key)
                if box_key not in keyLists:
                    keyLists.append(box_key)

    for i in range(len(boxes)):
        if i not in checked_boxes:
            return False

    return True
