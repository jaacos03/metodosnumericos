# room2.py
# The function draws and activates a room2
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell, test_code
import math
import random
import sympy as sp
import metodos


def room2(win, inventory):
  # setting base variables
  continueGame = True
  lost = False

  # drawing room
  img2 = Image(Point(20, 10), "rooms/room2.gif")
  img2.draw(win)

  # drawing user
  user = Image(Point(28,1), "rooms/thief.gif")
  user.draw(win)

  inventLabel = Text(Point(5, 19), "")
  inventLabel.setStyle("bold")
  inventLabel.draw(win)

  get_item = Button(win, Point(5, 2), 8, 2, "")
  observe = Button(win, Point(5, 5), 8, 2, "")

  inventoryTexts = []
  last = 17
  for x in inventory:
      inventoryTexts.append(Text(Point(5, last), x))
      last = last - 1
  for x in inventoryTexts:
      x.draw(win)

  observed = False

  things_in_room = {"Point(23.0,12.0)": "llave", "Point(15.0,15.0)": "magia"}
  observe_in_room = {"Point(14.0,3.0)": ""}

  storytell(win, "Entras a otra habitacion")
  while continueGame is True and lost is False:
      # ask for key input (arrows)
      k = win.getKey()
      # check which arrow was pressed and move the user accordingly
      # while also checking that the user doesn't go outside the room's
      # borders
      if k == "Right" and user.getAnchor().getX() != 30:
          user.move(1, 0)
      if k == "Left" and user.getAnchor().getX() != 10:
          user.move(-1, 0)
      if k == "Up" and user.getAnchor().getY() != 20:
          user.move(0, 1)
      if k == "Down" and user.getAnchor().getY() != 0:
          user.move(0, -1)

      # key for getting an item
      if k == 'G' or k == 'g':
          if get_item.active:
              inventory.append(item)
              inventoryTexts.append(Text(Point(5, last), item))
              last = last - 1
              inventoryTexts[-1].draw(win)

      # key for observing an item
      if k == 'O' or k == 'o':
          if observe.active:
              storytell(win,observed_display)

      # Getting user location
      usx = user.getAnchor().getX()
      usy = user.getAnchor().getY()

      user_pos = "Point({0},{1})".format(usx, usy)

      # Activating a pickup button if the user is standing on an item that they can pick up.
      if user_pos in things_in_room.keys() and things_in_room[user_pos] not in inventory:
          item = things_in_room[user_pos]
          get_item.activate()
      else:
          get_item.deactivate()

      # activating an observe button if the user is standing on an item that they can observe.
      if user_pos in observe_in_room.keys():
          observed_display = observe_in_room[user_pos]
          observe.activate()
      else:
          observe.deactivate()

      # checking the door
      if usx >= Point(18.0, 12.0).getX() and usx <= Point(22.0, 12.0).getX() and usy >= Point(10.0,13.0).getY() and usy <= Point(
              10.0, 19.0).getY():
          # checking if a user has essential item
          if observed:
              storytell(win,"")
              user.undraw()
              img2.undraw()
              for i in inventoryTexts:
                  i.undraw()
              get_item.undrawButton(win)
              observe.undrawButton(win)
              # and return the state
              return True, False, inventory
          else:
              metodos.metrand()
              print()
              storytell(win, "Resuelve la siguiente funcion por ", )
              observed = test_code(win, , )
              if observed:
                storytell(win, "Correcto, no olvidas nada.")

  return continueGame, lost, inventory