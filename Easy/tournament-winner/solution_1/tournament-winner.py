# SOLUTION 1
# Tournament Winner
# Time O(n) | Space O(k) space
# n is the number of competitions
# k is the number of teams competing in the tournament

HOME_TEAM_WON = 1;

def tournamentWinner(competitions, results) {
  currentBestTeam = ""
  scores = {currentBestTeam: 0 }

  for idx, competition in enumerate(competitions):
    result = results[idx]
    homeTeam, awayTeam = competition

    winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

    updateScores(winningTeam, 3, scores)

    if scores[winningTeam] > scores[currentBestTeam]:
      curresntBestTeam = winningTeam
  
  retirn currentBestTeam
}

def updateScores(team, points, scores):
  if team not in scores:
    scores[team] = 0

  scores[team] += points