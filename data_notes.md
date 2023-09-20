# Notes on the Dataset

## Awards-Players Table
Represents an association between a player and an award they received.
- **playerID:** Player identifier
- **award:** Name of the award
- **year:** Year the player was awarded
- **lgID:** League identifier for the league where the player was awarded

## Coaches Table
Represents an association between a Coach, a year of the league, a team and the gathered stats about it.
- **coachID:** Indicates which coach the stats refer to
- **year:** Indicates the year the stats refer to
- **tmID:** Indicates the team the stats refer to
- **lgID:** Indicates the league the stats refer to
- **stint:** Period of time that a player, coach, or other individual spends with a particular team or in the league itself
- **won:** Number of matches won by the team in the specified year
- **lost:** Number of matches lost by the team in the specified year
- **post_wins:** Number of wins during playoffs
- **post_losses:** Number of losses during playoffs

## Players Table
Associates a series of stats with a player.
- **bioID:** Indicates the player the stats refer to.
- **pos:** Position the player plays in ???
- **firstseason:** (aparece todos os valores a 0)
- **lastseason:** (aparece todos os valores a 0)
- **height:** Player's height
- **weight:** Player's weight
- **college:** College the player attended to
- **collegeOther:** Another college the player attended to
- **birthDate:** Player's date of birth
- **deathDate:** Player's date of death ("0000-00-00" in case the player is still alive)

## Players-Teams Table

## Series Post Table

## Teams

## Teams Post Table
