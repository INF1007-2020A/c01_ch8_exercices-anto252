#!/usr/bin/env python
# -*- coding: utf-8 -*-




def compare(file_name1: str, file_name2: str):
    with open(file_name1, "r") as A, open(file_name2, "r") as B:

        same = True

        while same:
            a = A.read()
            b = B.read()

            if a != b:
                same = False

    return same


def space_extend(file_name):
    with open(file_name, "r") as A:
        f = A.read()

        new_text = f.replace(" ", "   ")
        with open(file_name, "w") as A:
            A.write(new_text)

    return file_name

def ligne_read():
    pass



compare("texte1.txt", "texte2.txt")
space_extend("espace.txt")
