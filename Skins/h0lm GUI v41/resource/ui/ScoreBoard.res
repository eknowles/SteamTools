//             ______________________
//___________.( h0lmGUI™v4.1 by h0lm ).___________
//¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"Resource/UI/ScoreBoard.res"
{
	"scores"
	{
		"ControlName"			"CCSClientScoreBoardDialog"
		"fieldName"				"scores"
		"xpos"					"0"
		"ypos"					"0"
		"zpos"					"90"
		"wide"					"f0"
		"tall"					"480"
		"settitlebarvisible"	"0"
	}
	   	"ScoreboardBackgroundLarge"
	{
		"ControlName"			"ImagePanel"
		"fieldName"			"ScoreboardBackground1"
		"xpos"				"0"
		"ypos"				"0"
		"zpos"				"0"
		"wide"				"2000"
		"tall"				"2000"
		"visible"			"1"
		"fillcolor"			"0 0 0 1"
	}
	 "ScoreboardBackground"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"ScoreboardBackground"
		"xpos"				"c-302"
		"ypos"				"c-117"
		"zpos"				"0"
		"wide"				"604"
		"tall"				"212"
		"visible"			"1"
		"fillcolor"			"0 0 0 160"
	}
	
   	"ScoreboardBackground1"
	{
		"ControlName"			"ImagePanel"
		"fieldName"			"ScoreboardBackground1"
		"xpos"				"c-300"
		"ypos"				"c-115"
		"zpos"				"0"
		"wide"				"600"
		"tall"				"208"
		"visible"			"1"
		"fillcolor"			"0 0 0 80"
	}

	"MapName"
	{
	}

	"ServerNameLabel"
	{
		"ControlName"			"Label"
		"fieldName"				"ServerNameLabel"
		"xpos"				"c-300"
		"ypos"				"c-115"
		"zpos"				"4"
		"wide"				"600"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"labelText"				""
		"textAlignment"			"center"
		"dulltext"				"0"
		"brighttext"			"1"
		"font"					"ScoreboardBody_second"
		"fgcolor_override"		"120 120 120 200"
	}

	"StatsStatus"
	{
	}

	"WinConditionLabel"
	{
		"ControlName"			"Label"
		"fieldName"				"WinConditionLabel"
		"xpos"					"4"
		"ypos"					"2"
		"zpos"					"4"
		"wide"					"80"
		"tall"					"15"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"labelText"				""
		"auto_wide_tocontents"	"1"
		"textAlignment"			"west"
		"font"					"ScoreboardHeader"
		"fgcolor_override"		"255 255 255 255"
		"pin_to_sibling"		"Icon_Clock"
		"pin_corner_to_sibling" "5"
		"pin_to_sibling_corner" "7"
	}

	"Icon_Clock"
	{
	}

	"CT_Label"
	{
		"ControlName"		"Label"
		"fieldName"			"CT_Label"
		"xpos"				"c-286"
		"ypos"				"c-97"
		"zpos"				"4"
		"wide"				"160"
		"tall"				"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"COUNTER-TERRORISTS"
		"textAlignment"		"north-west"
		"font"				"ScoreboardTeamName"
		"fgcolor_override"	"255 255 255 255"
	}

	"CTPlayersAliveBackground"
	{
		"ControlName"			"Label"
		"fieldName"			"CTPlayersAliveBackground"
		"xpos"				"c-283"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"			"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"5"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAlive"
		"fgcolor_override"		"255 255 255 90"
	}

	"CTPlayersAliveGlow"
	{
		"ControlName"			"Label"
		"fieldName"			"CTPlayersAliveGlow"
		"xpos"				"c-283"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"			"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%ct_alivecount%"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAliveGlow"
		"fgcolor_override"		"153 204 255 200"
	}

	"CTPlayersAlive"
	{
		"ControlName"			"Label"
		"fieldName"			"CTPlayersAlive"
		"xpos"				"c-283"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"			"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%ct_alivecount%"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAlive"
		"fgcolor_override"		"255 255 255 255"
	}
	
	"CTPlayersAliveSuffix"
	{
	}

	"CTTeamScore"
	{
		"ControlName"		"Label"
		"fieldName"			"CTTeamScore"
		"xpos"				"c-107"
		"ypos"				"c-102"
		"zpos"				"4"
		"wide"				"100"
		"tall"				"40"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%ct_totalteamscore%"
		"textAlignment"		"east"
		"font"				"ScoreboardScore"
		"fgcolor_override"	"255 255 255 255"
	}

	"T_Label"
	{
		"ControlName"		"Label"
		"fieldName"			"T_Label"
		"xpos"				"c+126"
		"ypos"				"c-97"
		"zpos"				"4"
		"wide"				"160"
		"tall"				"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"TERRORIST-FACTION"
		"textAlignment"		"north-east"
		"font"				"ScoreboardTeamName"
		"fgcolor_override"	"255 255 255 255"
	}
	"TPlayersAliveBackground"
	{
		"ControlName"			"Label"
		"fieldName"			"TPlayersAliveBackground"
		"xpos"				"c+220"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"5"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAlive"
		"fgcolor_override"		"255 255 255 90"
	}

	"TPlayersAliveGlow"
	{
		"ControlName"			"Label"
		"fieldName"			"TPlayersAliveGlow"
		"xpos"				"c+220"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"			"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%t_alivecount%"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAliveGlow"
		"fgcolor_override"		"255 64 64 200"
	}
	"TPlayersAlive"
	{
		"ControlName"		"Label"
		"fieldName"			"TPlayersAlive"
		"xpos"				"c+220"
		"ypos"				"c-83"
		"zpos"				"4"
		"wide"				"68"
		"tall"				"50"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%t_alivecount%"
		"textAlignment"			"north-west"
		"font"				"ScoreboardPlayersAlive"
		"fgcolor_override"	"255 255 255 255"
	}

	"TPlayersAliveSuffix"
	{
	}

	"TTeamScore"
	{
		"ControlName"		"Label"
		"fieldName"			"TTeamScore"
		"xpos"				"c+7"
		"ypos"				"c-102"
		"zpos"				"4"
		"wide"				"100"
		"tall"				"40"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"%t_totalteamscore%"
		"textAlignment"		"west"
		"font"				"ScoreboardScore"
		"fgcolor_override"	"255 255 255 255"
	}

	"CTClanLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"CTClanLabel"
		"xpos"				"c-275"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"45"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"Clan"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"153 204 255 255"
	}

	"CTPlayerLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"CTPlayerLabel"
		"xpos"				"c-228"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"60"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_PlayerName"
		"textAlignment"		"west"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"153 204 255 255"
	}

	"CTPlayerScoreLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"CTPlayerScoreLabel"
		"xpos"				"c-92"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"30"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Score"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"153 204 255 255"
	}

	"CTPlayerDeathsLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"CTPlayerDeathsLabel"
		"xpos"				"c-67"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"37"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Deaths"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"153 204 255 255"
	}

	"CTPlayerLatencyLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"CTPlayerLatencyLabel"
		"xpos"				"c-38"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"42"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Latency"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"153 204 255 255"
	}

	"TClanLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TClanLabel"
		"xpos"				"c+20"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"45"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"Clan"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"255 64 64 255"
	}

	"TPlayerLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TPlayerLabel"
		"xpos"				"c+67"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"60"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_PlayerName"
		"textAlignment"		"west"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"255 64 64 255"
	}

	"TPlayerScoreLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TPlayerScoreLabel"
		"xpos"				"c+203"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"30"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Score"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"255 64 64 255"
	}

	"TPlayerDeathsLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TPlayerDeathsLabel"
		"xpos"				"c+228"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"37"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Deaths"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"255 64 64 255"
	}

	"TPlayerLatencyLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TPlayerLatencyLabel"
		"xpos"				"c+257"
		"ypos"				"c-62"
		"zpos"				"4"
		"wide"				"42"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#Cstrike_SB_Latency"
		"textAlignment"		"center"
		"font"				"ScoreboardColumns"
		"fgcolor_override"	"255 64 64 255"
	}

	"CTPlayerArea"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerArea"
		"xpos"				"c-290"
		"ypos"				"c-46"
		"zpos"				"-1"
		"wide"				"287"
		"tall"				"130"
		"visible"			"1"
		"enabled"			"1"
		"fillcolor"			"0 0 0 50"
	}

	"CTPlayerAvatar0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerAvatar0"
		"xpos"				"c-290"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"14"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"CTPlayerClan0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerClan0"
		"xpos"				"c-275"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"45"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"CTPlayerName0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerName0"
		"xpos"				"c-228"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"135"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 0 0 64"
	}

	"CTPlayerStatus0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerStatus0"
		"xpos"				"c-100"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"14"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"CTPlayerScore0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerScore0"
		"xpos"				"c-92"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"30"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 0 0 64"
	}

	"CTPlayerDeaths0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerDeaths0"
		"xpos"				"c-67"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"37"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"CTPlayerLatency0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CTPlayerLatency0"
		"xpos"				"c-35"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"31"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"TPlayerArea"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerArea"
		"xpos"				"c+4"
		"ypos"				"c-46"
		"zpos"				"-1"
		"wide"				"287"
		"tall"				"130"
		"visible"			"1"
		"fillcolor"			"0 0 0 50"
	}

	"TPlayerAvatar0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerAvatar0"
		"xpos"				"c+5"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"14"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"TPlayerClan0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerClan0"
		"xpos"				"c+20"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"45"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"TPlayerName0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerName0"
		"xpos"				"c+67"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"135"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"TPlayerStatus0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerStatus0"
		"xpos"				"c+195"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"14"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"TPlayerScore0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerScore0"
		"xpos"				"c+203"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"30"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"TPlayerDeaths0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerDeaths0"
		"xpos"				"c+228"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"37"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"222 0 0 64"
	}

	"TPlayerLatency0"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerLatency0"
		"xpos"				"c+262"
		"ypos"				"c-40"
		"zpos"				"10"
		"wide"				"30"
		"tall"				"14"
		"visible"			"0"
		"fillcolor"			"0 222 0 64"
	}

	"FPlayerLatenc"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"FPlayerLatenc"
		"xpos"				"c+4"
		"ypos"				"c-100"
		"zpos"				"0"
		"wide"				"287"
		"tall"				"37"
		"visible"			"1"
		"fillcolor"			"40 6 6 100"
	}

	"FPlayerDeath"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TPlayerDeath"
		"xpos"				"c-290"
		"ypos"				"c-100"
		"zpos"				"0"
		"wide"				"287"
		"tall"				"37"
		"visible"			"1"
		"fillcolor"			"11 25 38 100"
	}

	"Backgroundx"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"Backgroundx"
		"xpos"				"c-302"
		"ypos"				"c+98"
		"zpos"				"0"
		"wide"				"604"
		"tall"				"18"
		"visible"			"1"
		"fillcolor"			"0 0 0 160"
	}
	
	"Spectators"
	{
		"ControlName"		"Label"
		"fieldName"			"Spectators"
		"labelText"			"%spectators%"
		"textAlignment"		"west"
		"xpos"				"c-295"
		"ypos"				"c+100"
		"zpos"				"90"
		"wide"				"495"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"font"				"ScoreboardBody_second"
		"fgcolor_override"	"200 200 200 255"
	}

	"SourceTV"
	{
		"ControlName"		"Label"
		"fieldName"			"SourceTV"
		"labelText"			"%sourcetv%"
		"textAlignment"		"east"
		"xpos"				"c+215"
		"ypos"				"c+100"
		"zpos"				"90"
		"wide"				"80"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"font"				"ScoreboardBody_second"
		"fgcolor_override"	"200 200 200 255"
	}
}
//________________________________________________
//¯¯¯¯¯¯¯¯¯¯¯'( h0lmGUI™v4.1 by h0lm )'¯¯¯¯¯¯¯¯¯¯¯
//             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯