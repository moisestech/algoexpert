// resolve TypeScript error - Cannot redeclare block-scoped variable.
export {};

// SOLUTION 1
// Tournament Winner

// Complexity
// Average:  Time: | Space:
// Worst:    Time: | Space:

// Time O(n) | Space O(k) space
// n is the number of competitions
// k is the number of teams competing in the tournament

const HOME_TEAM_WON = 1;

export function tournamentWinner(competitions: string[][], results: number[]) {
  let currentBestTeam = "";
  const scores = { [currentBestTeam]: 0 };

  for (let idx = 0; idx < competitions.length; idx++) {
    const result = results[idx];
    const [homeTeam, awayTeam] = competitions[idx];

    const winningTeam = result === HOME_TEAM_WON ? homeTeam : awayTeam;

    updateScores(winningTeam, 3, scores);

    if (scores[winningTeam] > scores[currentBestTeam]) {
      currentBestTeam = winningTeam;
    }
  }

  return currentBestTeam;
}

function updateScores(
  team: string,
  points: number,
  scores: { [team: string]: number }
) {
  if (!(team in scores)) scores[team] = 0;

  scores[team] += points;
}
