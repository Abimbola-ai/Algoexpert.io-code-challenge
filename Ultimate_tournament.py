def tournamentWinner(competitions, results):
	current_winner = ""
	scores = {current_winner: 0}
    # Write your code here.
	for idx,lists in enumerate(competitions):
		result = results[idx]
		home, away  = lists
		# print(result)
		
		winning_team = home if result == 1 else away
		if winning_team not in scores:
			scores[winning_team] = 0
		scores[winning_team] += 3
		
		if scores[winning_team] > scores[current_winner]:
			current_winner = winning_team
	return current_winner


