# Notes on the Dataset

## Awards-Players Table
Represents an association between a player and an award they received.
- **playerID:** Player identifier
- **award:** Name of the award
- **year:** Year the player was awarded with this award
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
Associates a player with a year, the team they played in that year and a set of stats on their performance.
- **playerID:** Identifies a player
- **year:** Year the player played in the team
- **stint:** ???
- **tmID:** Identifies the team the player played in
- **lgID:** Identifies the league the stats refer to
- **GP:** Games Played
- **GS:** Games Started(???)
- **minutes:** Minutes Played
- **points:** Points Scored (???)
- **oRebounds:** Offensive Rebounds
- **dRebounds:** Defensive Rebounds
- **rebounds:** Total Rebounds
- **assists:** Assists
- **steals:** Steals
- **blocks:** Blocks
- **turnovers:** Turnovers
- **PF:** ???
- **fgAttempted:** Field Goals Attempted
- **fgMade:** Field Goals Made
- **ftAttempted:** Free Throws Attempted
- **ftMade:** Free Throws Made
- **threeAttempted:** Three Point Field Goals Attempted
- **threeMade:** Three Point Field Goals Made
- **dq:** ???
- **PostGP:** Games Played in the Playoffs
- **PostGS:** Games Started in the Playoffs
- **PostMinutes:** Minutes Played in the Playoffs
- **PostPoints:** Points Scored in the Playoffs
- **PostoRebounds:** Offensive Rebounds in the Playoffs
- **PostdRebounds:** Defensive Rebounds in the Playoffs
- **PostRebounds:** Total Rebounds in the Playoffs
- **PostAssists:** Assists in the Playoffs
- **PostSteals:** Steals in the Playoffs
- **PostBlocks:** Blocks in the Playoffs
- **PostTurnovers:** Turnoves in the Playoffs
- **PostPF:** ???
- **PostfgAttempted:**
- **PostfgMade:**
- **PostftAttempted:**
- **PostftMade:**
- **PostthreeAttempted:**
- **PostthreeMade:**
- **PostDQ:**
## Series Post Table

## Teams

## Teams Post Table
