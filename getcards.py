import numpy as np

from mtgsdk import Card

cards = Card.all()
multiverseID = np.empty([len(cards), 1]) 
image_url = np.chararray([len(cards), 1], 77)

for i, card in enumerate(cards):
  multiverseID[i] = card.multiverse_id
  image_url[i] = card.image_url

card_matrix = np.column_stack((multiverseID, image_url)) 
np.savetxt("card_matrix.txt", card_matrix, fmt = '%s')


