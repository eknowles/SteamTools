// Netcode Illuminati Gui
// Created by Ethos_
// Last Modified                               _____________
//___________________________________________.(º 9/20/2011 º)
//¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"GameMenu"
{
	"1"
	{
		"label" "[ Netcode Illuminati ]"
		"command" "engine clear; toggleconsole; exec netcode_gui/intro.scr"
	}
	
	"2"
	{
		"label" " "
		"command" " "
	}
	"3"
	{
		"label" "#GameUI_GameMenu_ResumeGame"
		"command" "ResumeGame"
		"OnlyInGame" "1"
	}
	"4"
	{
		"label" "#GameUI_GameMenu_Disconnect"
		"command" "Disconnect"
		"OnlyInGame" "1"
	}
	"5"
	{
		"label" "#GameUI_GameMenu_PlayerList"
		"command" "OpenPlayerListDialog"
		"OnlyInGame" "1"
	}
	"6"
	{
		"label" ""
		"command" ""
		"OnlyInGame" "1"
	}
	"7"
	{
		"label" "NETCODE D2 DEATHMATCH"
		"command" "engine connect ncidm.eoreality.net:27015"
	}
	"8"
	{
		"label" ""
		"command" ""
	}
	"9"
	{
		"label" "#GameUI_GameMenu_FindServers"
		"command" "OpenServerBrowser"
	}
	"10"
	{
		"label" "#GameUI_GameMenu_CreateServer"
		"command" "OpenCreateMultiplayerGameDialog"
	}
	"11"
	{
		"label" " "
		"command" " "
		"OnlyInGame" "1"
	}
	"12"
	{
		"label" "    zBlock: Status"
		"command" "engine zb_status"
		"OnlyInGame" "1"
	}
	"13"
	{
		"label" "    zBlock: Netinfo"
		"command" "engine zb_netinfo"
		"OnlyInGame" "1"
	}
	"14"
	{
		"label" "    zBlock: Lo3"
		"command" "engine rcon zb_matchconfig cevo.cfg; rcon zb_lo3"
		"OnlyInGame" "1"
	}
	"15"
	{
		"label" "    Execute: Pregame"
		"command" "engine rcon exec pregame.cfg"
		"OnlyInGame" "1"
	}
	"16"
	{
		"label" " "
		"command" " "
		"OnlyInGame" "1"
	}
	"17"
	{
		"label" "WATCH DEMO"
		"command" "engine demoui"
	}
	"18"
	{
		"label" "#GameUI_GameMenu_Options"
		"command" "OpenOptionsDialog"
	}
	"19"
	{
		"label" "#GameUI_GameMenu_Quit"
		"command" "Quit"
	}
	"20"
	{
		"label" " "
		"command" " "
	}
	"21"
	{
		"label" "Powered by EOReality.net"
		"command" "engine clear; toggleconsole; exec netcode_gui/intro.scr"
	}

}


