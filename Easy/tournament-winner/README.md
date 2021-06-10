# Tournament Winner

[**Link**](https://www.algoexpert.io/questions/Tournament%20Winner)

There's an algorithms tournament taking place in which teams of programmers
compete against each other to solve algorithmic problems as fast as possible.
Teams compete in a round robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each
competition, one team is designated the home team, while the other team is the
away team. In each competition there's always one winner and one loser; there
are no ties. A team receives 3 points if it wins and 0 points if it loses. The
winner of the tournament is the team that receives the most amount of points.

<p>
  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament. The input arrays are named
  <span>competitions</span> and <span>results</span>, respectively. The
  <span>competitions</span> array has elements in the form of
  <span>[homeTeam, awayTeam]</span>, where each team is a string of at most 30
  characters representing the name of the team. The <span>results</span> array
  contains information about the winner of each corresponding competition in the
  <span>competitions</span> array. Specifically, <span>results[i]</span> denotes
  the winner of <span>competitions[i]</span>, where a <span>1</span> in the
  <span>results</span> array means that the home team in the corresponding
  competition won and a <span>0</span> means that the away team won.
</p>
<p>
  It's guaranteed that exactly one team will win the tournament and that each
  team will compete against all other teams exactly once. It's also guaranteed
  that the tournament will always have at least two teams.
</p>

---

### Sample Input

<pre><span>competitions</span> = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
<span>results</span> = [0, 0, 1]
</pre>

### Sample Output

<pre>"Python"
<span>// C# beats HTML, Python Beats C#, and Python Beats HTML.</span>
<span>// HTML - 0 points </span>
<span>// C# -  3 points</span>
<span>// Python -  6 points</span>
</pre>

---

## **Hints**

1. Don't overcomplicate this problem. How would you solve it by hand? Consider that approach, and try to translate it into code.

2. Use a hash table to store the total points collected by each team, with the team names as keys in the hash table. Once you know how many points each team has, how can you determine which one is the winner?

3. Loop through all of the competitions, and update the hash table at every iteration. For each competition, consider the name of the winning team; if the name already exists in the hash table, update that entry by adding 3 points to it. If the team name doesn't exist in the hash table, add a new entry in the hash table with the key as the team name and the value as 3 (since the team won its first competition). While looping through all of the competitions, keep track of the team with the highest score, and at the end of the algorithm, return the team with the highest score.

---

## Solution 1

- [JavaScript](./solution_1/tournament-winner.js)
- [TypeScript](./solution_1/tournament-winner.ts)
- [Python](./solution_1/tournament-winner.py)

## Solution 2

- [JavaScript]()
- [TypeScript]()
- [Python]()
