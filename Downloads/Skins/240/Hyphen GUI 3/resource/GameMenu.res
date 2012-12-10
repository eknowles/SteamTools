// TEAM HYPHEN GUI
// BY KLUTCH
// www.teamhyphen.org

"GameMenu"
{

	"1"
	{
		"label" "Hyphen GUI"
		"command" "engine toggleconsole"
		"OnlyInGame" "0"
	}
	"2"
	{
		"label" ""
		"command" ""
		"OnlyInGame" "1"
	}
	"3"
	{
		"label" "WARMUP CONFIG"
		"command" "engine exec hyphen/warmup.cfg"
		"OnlyInGame" "1"
	}
	"4"
	{
		"label" "ZBLOCK LO3"
		"command" "engine rcon zb_lo3"
		"OnlyInGame" "1"
	}
	"5"
	{
		"label" ""
		"command" ""
		"OnlyInGame" "0"
	}
	"6"
	{
		"label" "Retry"
		"command" "engine retry"
		"OnlyInGame" "1"
	}
	"7"
	{
		"label" "Disconnect"
		"command" "Disconnect"
		"OnlyInGame" "1"
	}
	"8"
	{
		"label" "#GameUI_GameMenu_PlayerList"
		"command" "OpenPlayerListDialog"
		"OnlyInGame" "1"
	}
	"9"
	{
		"label" ""
		"command" ""
		"OnlyInGame" "1"
	}
	"10"
	{
		"label" "REVIEW DEMO"
		"command" "engine demoui"
		"OnlyInGame" "0"
	}
	"11"
	{
		"label" "START LAN"
		"command" "OpenCreateMultiplayerGameDialog"
	}
	
	"12"
	{
		"label" ""
		"command" ""
		"OnlyInGame" "0"
	}
	"13"
	{
		"label" "#GameUI_GameMenu_FindServers"
		"command" "OpenServerBrowser"
	}
	"14"
	{
		"label" "#GameUI_GameMenu_Options"
		"command" "OpenOptionsDialog"
	}
	"15"
	{
		"label" "#GameUI_GameMenu_Quit"
		"command" "Quit"
	}
}

