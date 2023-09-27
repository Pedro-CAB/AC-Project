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
- **pos:** Position the player plays in 
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
- **GS:** Games Started
- **minutes:** Minutes Played
- **points:** Points Scored 
- **oRebounds:** Offensive Rebounds
- **dRebounds:** Defensive Rebounds
- **rebounds:** Total Rebounds
- **assists:** Assists
- **steals:** Steals
- **blocks:** Blocks
- **turnovers:** Turnovers
- **PF:** Personal fouls
- **fgAttempted:** Field Goals Attempted
- **fgMade:** Field Goals Made
- **ftAttempted:** Free Throws Attempted
- **ftMade:** Free Throws Made
- **threeAttempted:** Three Point Field Goals Attempted
- **threeMade:** Three Point Field Goals Made
- **dq:** Disqualifications (foul outs)
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
- **PostPF:** Personal fouls in the Playoffs
- **PostfgAttempted:** Attempted field goals in the Playoffs
- **PostfgMade:** Field goals made in the Playoffs
- **PostftAttempted:** Free throws attempted in the Playoffs
- **PostftMade:** Free throws made in the Playoffs
- **PostthreeAttempted:** Three point attempted in the Playoffs
- **PostthreeMade:** Three point made in the the Playoffs
- **PostDQ:** Disqualifications (foul outs) in the Playoffs

## Series Post Table
Stats related to the post season's series
- **year:** Year relating to the stats
- **round:** Playoff round the team reached
- **series:** Series's (match) identification letter
- **tmIDWinner:** ID of the series' winning team
- **lgIDWinner:** ID of the series winning team's league
- **tmIDLoser:** ID of the series' losing team
- **lgIDLoser:** ID of the series losing team's league
- **W:** Winning team's number of matches won
- **L:** Losing team's number of matches won

## Teams
Team related stats
- **year:** Year relating to the stats
- **lgID:** ID of the team's league
- **tmID:** ID of the team
- **franchID:** ID of the team's franchise
- **confID:** ID of the team's confederation (East/West)
- **divID:** ID of the team's division
- **rank:** Team's final place in the league
- **playoff:** Whether the team made the playoffs
- **seeded:** Team's seed in the playoffs (all 0, potentially made irrelevant by playoff format changes)
- **firstRound:** Team's result in the first round of the playoffs
- **semis:** Team's result in the semi-finals
- **finals:** Team's result in the finals
- **name:** Team's name
- **o_fgm:** Opponent's field goals made
- **o_fga:** Opponent's field goals attempted
- **o_ftm:** Opponent's field throws made
- **o_fta:** Opponent's field throws attempted
- **o_3pm:** Opponent's three point made
- **o_3pa:** Opponent's three point attempted
- **o_oreb:** Opponent's offensive rebounds
- **o_dreb:** Opponent's defensive rebounds
- **o_reb:** Opponent's total rebounds
- **o_asts:** Opponent's assists
- **o_pf:** Opponent's personal fouls
- **o_stl:** Opponent's steals
- **o_to:** Opponent's turnovers
- **o_blk:** Opponent's blocks
- **o_pts:** Opponent's points made
- **d_fgm:** Team's field goals made
- **d_fga:** Team's field goals attempted
- **d_ftm:** Team's field throws made
- **d_fta:** Team's field throws attempted
- **d_3pm:** Team's three point made
- **d_3pa:** Team's three point attempted
- **d_oreb:** Team's offensive rebounds
- **d_dreb:** Team's defensive rebounds
- **d_reb:** Team's total rebounds
- **d_asts:** Teamt's assists
- **d_pf:** Team's personal fouls
- **d_stl:** Team's steals
- **d_to:** Team's turnovers
- **d_blk:** Team's blocks
- **d_pts:** Team's points made
- **won:** Number of games won
- **lost:** Number of games lost
- **GP:** Number of games played
- **homeW:** Number of home wins
- **homeL:** Number of home losses
- **awayW:** Number of away wins
- **awayL:** Number of away losses
- **confW:** Number of wins within the confederation
- **confL:** Number of losses within the confederation
- **min:** Total minutes played
- **attend:** Total match attendance
- **arena:** Team arena's name

## Teams Post Table
Team's overall stats in the post season
- **year:** Year relating to the stats
- **tmID:** ID of the team
- **lgID:** ID of the league
- **W:** Team's total wins in the playoffs
- **L:** Team's total losses in the playoffs