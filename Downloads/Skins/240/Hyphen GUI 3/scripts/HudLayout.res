// TEAM HYPHEN GUI
// BY KLUTCH
// www.teamhyphen.org


"Resource/HudLayout.res"
{
	HudHealth
	{
		"fieldName"		"HudHealth"
		"xpos"	"6"
		"ypos"	"445"
		"wide"	"70"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		
		"PaintBackgroundType"	"2"		
		
		"icon_xpos"	"2"
		"icon_ypos"	"-2"
		"digit_xpos" "20"
		"digit_ypos" "0"
		"textAlignment"	"east"
		
		"LowHealthColor"	"HudIcon_Red"
	}
    "xhair1"
	{
		"ControlName"	        "ImagePanel"
		"xpos"				"c0"
		"ypos"				"c-4"
		"zpos"					"5"
		"wide"		            "1"
		"tall"		            "2"
		"visible"				"1"
		"enabled"				"1"	
	}
	"xhair2"
	{
		"ControlName"	        "ImagePanel"
		"xpos"				"c-4"
		"ypos"				"c0"
		"zpos"					"5"
		"wide"		            "2"
		"tall"		            "1"
		"visible"				"1"
		"enabled"				"1"	
		//"fillcolor"			"255 255 255 64"
	}
	"xhair3"
	{
		"ControlName"	        "ImagePanel"
		"xpos"				"c0"
		"ypos"				"c3"
		"zpos"					"5"
		"wide"		            "1"
		"tall"		            "2"
		"visible"				"1"
		"enabled"				"1"	
		//"fillcolor"			"255 255 255 64"
	}
	"xhair4"
	{
		"ControlName"	        "ImagePanel"
		"xpos"				"c3"
		"ypos"				"c0"
		"zpos"					"5"
		"wide"		            "2"
		"tall"		            "1"
		"visible"				"1"
		"enabled"				"1"	
		//"fillcolor"			"255 255 255 64"
	}
	HudArmor
	{
		"fieldName"		"HudArmor"
		"xpos"	"81"
		"ypos"	"445"
		"wide"	"70"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		"textAlignment"	"east"

		"PaintBackgroundType"	"2"	
		
		"icon_xpos"	"2"
		"icon_ypos"	"-2"
		"digit_xpos" "20"
		"digit_ypos" "0"
	}
	
	HudC4
	{
		"fieldName" "HudC4"
		"xpos"	"6"
		"ypos"	"240"
		"wide"	"35"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
	

		"PaintBackgroundType"	"2"	
		"icon_xpos"	"2"
		"icon_ypos"	"0"
		"IconColor"			"White"
		"FlashColor"		"HudIcon_Red"

	}

	HudDefuser
	{
		"fieldName" "HudDefuser"
		"xpos"	"6"
		"ypos"	"240"
		"wide"	"28"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		
		"PaintBackgroundType"	"2"	
		"IconColor"				"White"

	}
	HudShoppingCart
	{
		"fieldName" "HudShoppingCart"
		"xpos"	"r160"
		"ypos"	"445"
		"wide"	"20"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		
		"PaintBackgroundType"	"2"	
		"IconColor"			"White"

	}
	
	HudScenarioIcon 
	{
		"fieldName" "HudScenarioIcon"
		"xpos"	"c-15"
		"ypos"	"445"
		"wide"	"35"
		"zpos"	"2"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		"IconColor"			"White"
		"PaintBackgroundType"	"2"	
	}
		HudVoiceSelfStatus
	{
		"fieldName" "HudVoiceSelfStatus"
		"visible" "1"
		"enabled" "1"
		"xpos"	"c-15"
		"ypos"	"400"
		"wide"	"30"
		"tall"  "30"
		
		"PaintBackgroundType"	"2"	
	}
	HudRoundTimer
	{
		"fieldName" "HudRoundTimer"
		"xpos"	"c-45"
		"ypos"	"445"
		"wide"	"85"
		"zpos"	"1"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"2"	

		"FlashColor"		"255 0 0 255"	
		"Color"		"255 255 255 255"	
		
		"icon_xpos"	"8"
		"icon_ypos"	"-1"
		"digit_xpos" "29"
		"digit_ypos" "0"
		
		//"icon_xpos"		"20"
		//"icon_ypos"		"2"
		//"digit_xpos"	"45"
		//"digit_ypos"	"2"
		"backgroundtype" "0"
	}
	overview
	{
		"fieldname"				"overview"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"0"
		"ypos"					"480"
		"wide"					"0"
		"tall"					"0"
	}
	HudCommentary
	{
		"fieldName" "HudCommentary"
		"xpos"	"c-190"
		"ypos"	"350"
		"wide"	"380"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"
		
		"PaintBackgroundType"	"2"	
		
		"bar_xpos"		"50"
		"bar_ypos"		"20"
		"bar_height"	"8"
		"bar_width"		"320"
		"speaker_xpos"	"50"
		"speaker_ypos"	"8"
		"count_xpos_from_right"	"10"	// Counts from the right side
		"count_ypos"	"8"
		
		"icon_texture"	"vgui/hud/icon_commentary"
		"icon_xpos"		"0"
		"icon_ypos"		"0"		
		"icon_width"	"40"
		"icon_height"	"40"
	}
	
	HudHDRDemo
	{
		"fieldName" "HudHDRDemo"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"640"
		"tall"  "480"
		"visible" "0"
		"enabled" "1"
		
		"Alpha"	"255"
		"PaintBackgroundType"	"2"	
		
		"BorderColor"	"0 0 0 255"
		"BorderLeft"	"16"
		"BorderRight"	"16"
		"BorderTop"		"16"
		"BorderBottom"	"64"
		"BorderCenter"	"0"
		
		"BorderThickness" "1"
		
		"TextColor"		"255 255 255 255"
		"LeftTitleY"	"422"
		"RightTitleY"	"422"
	}

	TargetID
	{
		"fieldName" "TargetID"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
		"PaintBackgroundType"	"2"	
	}
	
	HudSuit
	{
		"fieldName"		"HudSuit"
		"xpos"	"140"
		"ypos"	"432"
		"wide"	"108"
		"tall"  "36"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"	

		
		"text_xpos" "8"
		"text_ypos" "20"
		"digit_xpos" "50"
		"digit_ypos" "2"
	}

	HudProgressBar
	{
		"fieldName" "HudProgressBar"
		"xpos"	"c-150"
		"ypos"	"300"
		"wide"	"300"
		"tall"  "15"
		"visible" "1"
		"enabled" "1"

		"BorderThickness" "1"

		"PaintBackgroundType"	"2"	
		
	}


	HudHostageRescueZone
	{
		"fieldName" "HudHostageRescueZone"
		"xpos"	"96"
		"ypos"	"415"
		"wide"	"35"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"
	

		"PaintBackgroundType"	"2"	
		"IconColor"			"White"
		"FlashColor"		"HudIcon_Red"
	}

	HudAccount
	{
		"fieldName" "HudAccount"
		"xpos"	"r126"
		"ypos"	"390"
		"wide"	"120"
		"tall"  "50"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"	
		
		"icon2_xpos"	"15"
		"icon2_ypos"	"-2"
		"digit2_xpos"	"93"
		"digit2_ypos"	"0"
		
		"icon_xpos"	"10"
		"icon_ypos"	"18"
		"digit_xpos" "93"
		"digit_ypos" "20"
	}

	HudAmmo
	{
		"fieldName" "HudAmmo"
		"xpos"	"r126"
		"ypos"	"445"
		"wide"	"120"
		"tall"  "30"
		"visible" "1"
		"enabled" "1"

		"TextColor"	"255 255 255 255"
		
		"PaintBackgroundType"	"2"	

		"digit_xpos" "4"
		"digit_ypos" "0"
		"digit2_xpos" "49"
		"digit2_ypos" "0"
	
		"bar_xpos"		"51"
		"bar_ypos"		"6"
		"bar_height"	"17"
		"bar_width"		"1"

		"icon_xpos"		"95"
		"icon_ypos"		"6"
	}
	
	HudFlashlight
	{
		"fieldName" "HudFlashlight"
		"visible" "1"
		"enabled" "1"
		"xpos"	"16"
		"ypos"	"370"
		"wide"	"102"
		"tall"	"20"
		
		"text_xpos" "8"
		"text_ypos" "6"
		"TextColor"	"255 170 0 220"

		"PaintBackgroundType"	"2"	
	}
	
	HudDamageIndicator
	{
		"fieldName" "HudDamageIndicator"
		"visible" "1"
		"enabled" "1"
		"DmgColorLeft" "255 0 0 0"
		"DmgColorRight" "255 0 0 0"
		
		"dmg_xpos" "30"
		"dmg_ypos" "100"
		"dmg_wide" "36"
		"dmg_tall1" "240"
		"dmg_tall2" "200"
	}

	HudZoom
	{
		"fieldName" "HudZoom"
		"visible" "1"
		"enabled" "1"
		"Circle1Radius" "0"//"66"
		"Circle2Radius"	"0"//"74"
		"DashGap"	"16"
		"DashHeight" "4"
		"BorderThickness" "88"
	}

	HudWeaponSelection
	{
		"fieldName" "HudWeaponSelection"
		"xpos"	"r640"
		"wide"	"640"
		"ypos" 	"16"
		"visible" "1"
		"enabled" "1"
		"SmallBoxSize" "60"
		"LargeBoxWide" "108"
		"LargeBoxTall" "80"
		"BoxGap" "8"
		"SelectionNumberXPos" "4"
		"SelectionNumberYPos" "4"
		"SelectionGrowTime"	"0.4"
		"IconXPos" "8"
		"IconYPos" "0"
		"TextYPos" "68"	
		"TextColor" "SelectionTextFg"
		"MaxSlots"	"5"
		"PlaySelectSounds"	"1"
	}

	HudCrosshair
	{
		"fieldName" "HudCrosshair"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudDeathNotice
	{
		"fieldName" "HudDeathNotice"
		"visible" "1"
		"enabled" "1"
		"xpos"	 "r640"
		"ypos"	 "12"
		"wide"	 "628"
		"tall"	 "468"

		"MaxDeathNotices" "4"
		"LineHeight"	  "22"
		"RightJustify"	  "1"	// If 1, draw notices from the right
		
		"TextFont"				"HyphenDeath"
		"CTTextColor"			"CT_Blue"
		"TerroristTextColor"	"T_Red"	
		
		"PaintBackgroundType"	"2"	
	}

	HudVehicle
	{
		"fieldName" "HudVehicle"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}


	CVProfPanel
	{
		"fieldName" "CVProfPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	ScorePanel
	{
		"fieldName" "ScorePanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudTrain
	{
		"fieldName" "HudTrain"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMOTD
	{
		"fieldName" "HudMOTD"
		"visible" "0"
		"enabled" "0"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMessage
	{
		"fieldName" "HudMessage"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMenu
	{
		"fieldName"	 "HudMenu"
		"visible" 	"1"
		"enabled" 	"1"
		"wide"	 	"640"
		"tall"		"480"
		"zpos" 		"50"

		"TextFont"				"HyphenSpec"
		"ItemFont"				"ScoreboardPlayersAlive"
		"ItemFontPulsing"		"ScoreboardPlayersAlive"

	}

	HudCloseCaption
	{
		"fieldName" "HudCloseCaption"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudHistoryResource 
	{
		"fieldName" "HudHistoryResource"
		"visible" "1"
		"enabled" "1"
		"xpos"	 "r640"
		"wide"	 "640"
		"tall"	 "330"
		"history_gap" "55"
	}

	HudGeiger
	{
		"fieldName" "HudGeiger"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HUDQuickInfo
	{
		"fieldName" "HUDQuickInfo"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudWeapon
	{
		"fieldName" "HudWeapon"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	HudAnimationInfo
	{
		"fieldName" "HudAnimationInfo"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	CBudgetPanel
	{
		"fieldName" "CBudgetPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	CTextureBudgetPanel
	{
		"fieldName" "CTextureBudgetPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudPredictionDump
	{
		"fieldName" "HudPredictionDump"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudRadar
	{
		"fieldName" "HudRadar"
		"visible"	"1"
		"enabled"	"1"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"120"
		"tall"		"120"
		"PaintBackgroundType"	"0"
	}

	HudLocation
	{
		"fieldName" "HudLocation"
		"visible"	"1"
		"enabled"	"1"
		//"xpos"		"16"
		//"ypos"		"112"
		//"wide"		"96"
		//"tall"		"16"
		"xpos"	"c-60"
		"ypos"	"435"
		"wide"	"120"
		"tall"  "40"
		"textAlignment"	"north"
	}

	HudScope
	{
		"fieldName" "HudZoom"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	HudVoiceStatus
	{
		"fieldName" "HudVoiceStatus"
		"visible" "1"
		"enabled" "1"
		"xpos" "c-100"
		"ypos" "0"
		"wide" "200"
		"tall" "400"

		"item_tall"	"16"
		"item_wide"	"195"
		"item_spacing" "2"
		
		"show_avatar"		"1"
		"show_friend"		"1"
		"show_voice_icon"	"0"
		"show_dead_icon"	"1"

		"dead_xpos"	"0"
		"dead_ypos"	"0"
		"dead_wide"	"16"
		"dead_tall"	"16"

		"avatar_xpos"	"14"
		"avatar_ypos"	"0"
		"avatar_wide"	"16"
		"avatar_tall"	"16"
		
		"text_xpos"	"42"
		
		"fade_in_time" "0.1"
		"fade_out_time" "0.6"
	}

	HudFlashbang
	{
	}
	
	HudHintDisplay
	{
		"fieldName"	"HudHintDisplay"
		"visible"	"0"
		"enabled" "1"
		"xpos"		"c-240"
		"ypos"		"c60"
		"wide"		"480"
		"tall"		"100"
		"text_xpos"	"8"
		"text_ypos"	"8"
		"center_x"	"0"	// center text horizontally
		"center_y"	"-1"	// align text on the bottom
		"HintSize"	"1"
	}

	HudHintKeyDisplay
	{
		"fieldName"	"HudHintKeyDisplay"
		"visible"	"0"
		"enabled" 	"1"
		"xpos"		"r120"
		"ypos"		"r340"
		"wide"		"100"
		"tall"		"200"
		"text_xpos"	"8"
		"text_ypos"	"8"
		"text_xgap"	"8"
		"text_ygap"	"8"
		"TextColor"	"255 255 255 255"

		"PaintBackgroundType"	"2"
	}

	HudTerritory
	{
		"fieldName" "HudTerritory"
		"visible" "1"
		"enabled" "1"
		"xpos"	"240"
	    "ypos"	"432"
	    "wide" "240"
	    "tall" "48"
	}

	TerritorySCore
	{
	    "fieldName" "TerritoryScore"
	    "visible" "0"
	    "enabled" "0"
	    "xpos"	"240"
	    "ypos"	"450"
	    "wide" "200"
	    "tall" "200"
	    "text_xpos" "8"
	    "text_ypos" "4"
	}
	"HudChat"
	{
	"ControlName"	 "EditablePanel"
	"fieldName" "HudChat"
	"visible" "1"
	"enabled" "1"
	"xpos"	 "10"	[$WIN32]
	"xpos"	 "42"	[$X360]
	"ypos"	 "275"
	"wide"	 "320"
	"tall"	 "120"
	"PaintBackgroundType"	"2"
	}
	WinPanel_Round
	{
		"fieldName"				"WinPanel_Round"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"c-110"
		"ypos"					"287"		
		"zpos"					"0"		
		"wide"					"220"
		"tall"					"138"		
		"PaintBackgroundType"	"2"	
	}
	
	WinPanel_Match
	{
		"fieldName"				"WinPanel_Match"	
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"c-150"
		"ypos"					"c-175"
		"wide"					"300"
		"tall"					"350"
		"PaintBackgroundType"	"2"	
	}
	
	FreezePanel
	{
		"fieldName"				"FreezePanel"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"f0"
		"tall"					"480"
	}

	FreezePanelCallout
	{
		"fieldName"				"FreezePanelCallout"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"200"
		"ypos"					"200"
		"wide"					"100"
		"tall"					"50"
	}
	
	AchievementAnnouncePanel
	{
		"fieldName"				"AchievementAnnouncePanel"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"f0"
		"tall"					"480"
	}
	
	StatPanel
	{
		"fieldName"				"StatPanel"
		"visible"				"0"
		"enabled"				"1"
	}
	
	AchievementNotificationPanel
	{
		"fieldName"				"AchievementNotificationPanel"
		"visible"				"0"
		"enabled"				"1"
	}
	
	HUDAutoAim
	{
		"fieldName"				"HUDAutoAim"
		"visible"				"0"
		"enabled"				"1"
	}

	"HudAchievementTracker"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HudAchievementTracker"
		"xpos"			"10"
		"NormalY"		"120"
		"EngineerY"		"170"
		"zpos"			"20"
		"wide"			"250"
		"tall"			"280"
		"visible"		"1"
		"enabled"		"1"	
	}
	
	"CHudVote"
	{
		"fieldName"		"CHudVote"
		"visible"		"0"
		"enabled"		"0"
	}
	"HLTVText"
	{
		"ControlName"		"Label"
		"fieldName"			"HLTVText"
		"labelText"			"You are playing Counter-Strike: Source"
		"textAlignment"		"center"
		"xpos"		        "c-300"
		"ypos"				"c65"
		"zpos"				"90"
		"wide"		        "600"
		"tall"				"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"font"				"HyphenHLTV"
		"fgcolor_override"		"255 177 0 0" 
		"bgcolor_override"		"0 0 0 0"
	}
	"HLTVText1"
	{
		"ControlName"		"Label"
		"fieldName"			"HLTVText1"
		"labelText"			"Visit the official CS web site @"
		"textAlignment"		"center"
		"xpos"		        "c-300"
		"ypos"				"c85"
		"zpos"				"90"
		"wide"		        "600"
		"tall"				"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"font"				"HyphenHLTV"
		"fgcolor_override"		"255 177 0 0" 
		"bgcolor_override"		"0 0 0 0"
	}
	"HLTVText2"
	{
		"ControlName"		"Label"
		"fieldName"			"HLTVText2"
		"labelText"			"www.counter-strike.net"
		"textAlignment"		"center"
		"xpos"		        "c-300"
		"ypos"				"c105"
		"zpos"				"90"
		"wide"		        "600"
		"tall"				"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"font"				"HyphenHLTV"
		"fgcolor_override"		"255 177 0 0" 
		"bgcolor_override"		"0 0 0 0"
	}
}