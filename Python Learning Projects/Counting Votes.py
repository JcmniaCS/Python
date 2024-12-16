votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

#Extra study to practice
#Count votes
jake_votes = votes.count("Jake")
print("Jake has " + str(jake_votes) + " votes")
laurie_votes = votes.count("Laurie")
print("Laurie has " + str(laurie_votes) + " votes")
cassie_votes = votes.count("Cassie")
print("Cassie has " + str(cassie_votes) + " votes")

#Pick a winner
if laurie_votes > jake_votes and laurie_votes > cassie_votes:
  winning_name = "Laurie"
  winning_vote = laurie_votes
  print("The winner is " + winning_name + " with " + str(winning_vote) + " votes")

elif cassie_votes > jake_votes and cassie_votes > laurie_votes:
  winning_vote = cassie_votes
  winning_name = "Cassie"
  print("The winner is " + winning_name + " with " + str(winning_vote) + " votes")

elif jake_votes > cassie_votes and jake_votes > laurie_votes:
  winning_vote = jake_votes
  winning_name = "Jake"
  print("The winner is " + winning_name + " with " + str(winning_vote) + " votes")

#If there's a draw between winners
elif laurie_votes == cassie_votes and laurie_votes > jake_votes:
  winning_vote =  laurie_votes
  winning_names = "Laurie and Cassie"
  print("There has been a draw " + winning_name + str(winning_vote) )

elif laurie_votes == jake_votes and laurie_votes > cassie_votes:
  winning_vote = laurie_votes
  winning_names = "Laurie and Jake"
  print("There has been a draw " + winning_name + str(winning_vote) )

elif jake_votes == cassie_votes and jake_votes > laurie_votes:
  winning_vote = jake_votes
  winning_names = "Jake and Cassie"
  print("There has been a draw " + winning_name + str(winning_vote) )

elif jake_votes == cassie_votes and cassie_votes == laurie_votes:
  winning_vote = jake_votes
  winning_names = "Jake, Cassie and Laurie have received the same amount of votes"
  print (winning_names)

else:
  print("There has been no winner, no votes were registered")






