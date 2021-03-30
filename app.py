import votechain
#In this file I am simulating an election using the blockchain based voting i wrote in the votechain.py file
#Lets simulate a Nigerian Presidential election using the blockchain voting system

#Lets first create a blockchain to represent the election
nigerian_election = votechain.BlockChain()

#Lets assume there are 2 candidates running [Matthew and Mark]
votechain.candidates.append("Matthew")
votechain.candidates.append("Mark")

# Now that we know the candidates running, People can register to be able to vote
# In this example, people will register based with their name and a unique_id
# In this case the unique id would the NIN (but in a student election scenario it could be the matriculation number)
# Once voters register they would be given a that can only be used to vote once
harry = votechain.Voter("Harry Potter", "34245678942") 
hermione = votechain.Voter("Hermione Granger", "23465789788") 
ron = votechain.Voter("Ron Weasley", "56746380231")

# Now Voters can create vote(vote) for candidates
# P.S: the blockchain system would a vote if the name specified is not a candidate
# Votes are created for each voter; and each voter can only vote once
harry_vote = votechain.Vote(harry.key, "Matthew") #harry votes for matthew
hermione_vote = votechain.Vote(hermione.key, "Mark") #hermione votes for Mark
ron_vote = votechain.Vote(ron.key, "Matthew") #ron votes for matthew

# The blockchain then creates blocks from the votes(where each vote is a block) 
nigerian_election.create_block(harry_vote)
nigerian_election.create_block(hermione_vote)
nigerian_election.create_block(ron_vote)

# The blockchain then performs a proof of work to validate each vote(block)
nigerian_election.validate_unvalidated_blocks()

# The blockchain can then check if every thing is valid and then return the election results!
nigerian_election.is_chain_valid()
nigerian_election.get_votes()

# This is a simple example of how the blockchain voting system works
# It can handles must mor complex and robust scenarios
# Feel free to run the code to better understand it
# Also feel free to edit to code and see if it still works
# Try making the same voter vote twice and see what happens or try changing a voters vote and see if the blockchain is still valid
# Try adding new voters and and votes and check if the vote count works correctly

