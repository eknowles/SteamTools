"Resource/UI/SpectatorGUI.res"
{

//-------------------------------------
// TEAM 1
//-------------------------------------
"CTScoreLabel"
{
"labelText" "Team VeryGames" //%t1name%
"ControlName" "Label"
"fieldName" "CTScoreLabel"
"xpos" "c-260"
"ypos" "0"
"wide" "200"
"tall" "40"
"visible" "1"
"enabled" "1"
"textAlignment" "east"
"font" "TargetID"

}
"CTWEB"
{
"labelText" "" //%t1url%
"ControlName" "Label"
"xpos" "c-310"
"ypos" "10"
"wide" "200"
"tall" "30"
"visible" "1"
"enabled" "1"
"textAlignment" "south-east"
"font" "DefaultLarger"
"fgcolor_override" "255 255 255 100"
}
//-------------------------------------
// TEAM 2
//-------------------------------------
"TERScoreLabel"
{
"labelText" "Copenhagen WOLVES" //%t2name%
"ControlName" "Label"
"fieldName" "TERScoreLabel"
"xpos" "c+60"
"ypos" "0"
"wide" "200"
"tall" "40"
"zpos" "10"
"visible" "1"
"enabled" "1"
"textAlignment" "west"
"font" "TargetID"
}
"TWEB"
{
"labelText" "" //%t2url%
"ControlName" "Label"
"xpos" "c+110"
"ypos" "10"
"wide" "200"
"tall" "30"
"visible" "1"
"enabled" "1"
"textAlignment" "south-west"
"font" "DefaultLarger"
"fgcolor_override" "255 255 255 100"
}
"TTeamLogo"
{
"ControlName" "ScalableImagePanel"
"fieldName" "TTeamLogo"
"xpos" "c60"
"ypos" "1"
"zpos" "-200"
"wide" "40"
"tall" "40"
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1" 
}

//-------------------------------------
// OTHER STUFF
//-------------------------------------

"WOVLESTV"
{
"ControlName" "ScalableImagePanel"
"fieldName" "WOVLESTV"
"xpos" "0"
"ypos" "0"
"zpos" "-50"
"wide" "f0"
"tall" "f0"
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/wolvestv"
"scaleImage" "1" 
}
"CTScoreLabelShine"
{
"labelText" ""
"ControlName" "Label"
"fieldName" "CTScoreLabelShine"
"xpos" "10"
"ypos" "15"
"zpos" "0"
"wide" "310"
"tall" "15"
"visible" "1"
"enabled" "1"
"paintbackgroundtype" "2"
//"bgcolor_override" "255 255 255 32"
}
"CTLABELBG"
{
"labelText" ""
"ControlName" "Label"
"xpos" "10"
"ypos" "15"
"zpos" "-10"
"wide" "310"
"tall" "30"
"visible" "1"
"enabled" "1"
//"bgcolor_override" "0 0 0 150"
"paintbackgroundtype" "2"
}

"TLABELBG"
{
"labelText" ""
"ControlName" "Label"
"xpos" "r320"
"ypos" "15"
"wide" "310"
"tall" "30"
"zpos" "-10"
"visible" "1"
"enabled" "1"
//"bgcolor_override" "0 0 0 150"
"paintbackgroundtype" "2"
}
"TERScoreLabelShine"
{
"ControlName" "Label"
"fieldName" "TERScoreLabel"
"xpos" "r320"
"ypos" "15"
"wide" "310"
"zpos" "0"
"tall" "15"
"visible" "1"
"enabled" "1"
"labelText" ""
"paintbackgroundtype" "2"
//"bgcolor_override" "255 255 255 32"
}

"Version2"
{
"ControlName" "Label"
"xpos" "0"
"ypos" "10"
"wide" "f0"
"zpos" "-10"
"tall" "30"
"visible" "1"
"enabled" "1"
"labelText" ""
"paintbackgroundtype" "0"
"bgcolor_override" "0 0 0 0"
}

"SpectatorGUI"
{

"ControlName" "Frame"
"fieldName" "SpectatorGUI"
"tall" "480"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"tabPosition" "0"
"bgcolor_override" "255 255 255 0"
}
"topbar"
{
"ControlName" "Panel"
"fieldName" "topbar"
"xpos" "0"
"ypos" "0"
"tall" "0"
"wide" "640"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"tabPosition" "0"
"bgcolor_override" "255 255 255 0"
}
"bottombarblank"
{

"ControlName" "Panel"
"fieldName" "bottombarblank"
"xpos" "0"
"ypos" "528"
"tall" "55"
"wide" "640"
"visible" "1"
"enabled" "1"
"tabPosition" "0"
"bgcolor_override" "255 255 255 0"
}
"playerlabel"
{
"ControlName" "Label"
"fieldName" "playerlabel"
"xpos" "c-500"
"ypos" "440"
"wide" "1000"
"tall" "30"
"visible" "0"
"enabled" "1"
"textAlignment" "center"
"bgcolor_override" "0 0 0 0"
"font" "Player_ID1"
}
"VS"
{
"ControlName" "Label"
"fieldName" "vs"
"xpos" "c-15"
"ypos" "0"
"wide" "30"
"tall" "40"
"visible" "1"
"enabled" "1"
"labelText" "VS"
"textAlignment" "center"
"dulltext" "0"
"brighttext" "0"
"font" "PlayerBar"
"fgcolor_override" "255 255 255 255"//"CT_BLUE"
}
"CTScoreValue"
{
"ControlName" "Label"
"fieldName" "CTScoreValue"
"xpos" "c-60"
"ypos" "0"
"wide" "50"
"tall" "40"
"visible" "1"
"enabled" "1"
"labelText" ""
"textAlignment" "center"
"dulltext" "0"
"brighttext" "0"
"font" "TargetID"
"fgcolor_override" "255 255 255 255"//"CT_BLUE"
}
"TERScoreValue"
{
"ControlName" "Label"
"fieldName" "TERScoreValue"
"xpos" "c+10"
"ypos" "0"
"wide" "50"
"tall" "40"
"visible" "1"
"enabled" "1"
"labelText" ""
"textAlignment" "center"
"dulltext" "0"
"brighttext" "0"
"font" "TargetID"
"fgcolor_override" "255 255 255 255"//"T_RED"
}
"DividerBar"
{
"ControlName" "ImagePanel"
"fieldName" "DividerBar"
"xpos" "r94"
"ypos" "12"
"wide" "1"
"tall" "30"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"tabPosition" "0"
"fillcolor" "BorderBright"
"labelText" ""
"textAlignment" "center"
}
"timerclock"
{
"ControlName" "Label"
"fieldName" "timerclock"
"xpos" "c-50"
"ypos" "20"
"wide" "100"
"tall" "100"
"visible" "1"
"enabled" "1"
"textAlignment" "center"
"dulltext" "0"
"brighttext" "0"
"labelText" ""//"e"
"font" "Icons"
}
"timerlabel"
{
"ControlName" "Label"
"fieldName" "timerlabel"
"xpos" "c-30"
"ypos" "20"
"zpos" "-200"
"wide" "60"
"tall" "40"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"labelText" "00:00"
"textAlignment" "center"
"bgcolor_override" "0 0 0 128"
"paintbackgroundtype" "2"
"font" "Player_ID1"
"textinsety" "13"
}
"extrainfo"
{
"ControlName" "Label"
"fieldName" "extrainfo"
//"xpos" "r233"
//"ypos" "460"
"xpos" "15"
"ypos" "35"
"zpos" "-50"
"wide" "200"
"tall" "30"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"labelText" ""
"textAlignment" "west"
"dulltext" "0"
"brighttext" "0"
"font" "Default"
"fgcolor_override" "255 255 255 50"
}
"titlelabel"
{
"ControlName" "Label"
"fieldName" "titlelabel"
"xpos" "30"
"ypos" "450"
"zpos" "-50"
"tall" "30"
"wide" "0"//"200"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"font" "Default"
"labelText" ""
"font"	"Default"
"textAlignment" "west"
"dulltext" "0"
"brighttext" "0"
"fgcolor_override" "255 255 255 50"
}
"credit"
{
"ControlName" "Label"
"xpos" "15"
"ypos" "0"
"zpos" "-50"
"tall" "40"
"wide" "200"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"labelText" "SCGUI.COM"
"font"	"Athens"
"textAlignment" "west"
"dulltext" "0"
"brighttext" "0"
"fgcolor_override" "255 255 255 200"
}
"StreamDate"
{
"ControlName" "Label"
"fieldName" "StreamDate"
"xpos" "c-200"
"ypos" "447"
"wide" "400"
"tall" "40"
"autoResize" "0"
"pinCorner" "0"
"visible" "1"
"enabled" "1"
"labelText" ""
"textAlignment" "center"
"dulltext" "0"
"brighttext" "0"
"font" "Default"
"fgcolor_override" "255 255 255 50"
}

// OMG FLAGS!!!!!!!!!!!!!!

"ct1"
{
"ControlName" "ScalableImagePanel"
"fieldName" "ct1"
"xpos" "25"
"ypos" "329"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/France" //%t1flag%
"scaleImage" "1"
}
"ct2"
{
"ControlName" "ScalableImagePanel"
"fieldName" "ct2"
"xpos" "25"
"ypos" "355"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/France" //%t1flag%
"scaleImage" "1"
}

"ct3"
{
"ControlName" "ScalableImagePanel"
"fieldName" "ct3"
"xpos" "25"
"ypos" "380"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/France" //%t1flag%
"scaleImage" "1"
}
"ct4"
{
"ControlName" "ScalableImagePanel"
"fieldName" "ct4"
"xpos" "25"
"ypos" "406"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/France" //%t1flag%
"scaleImage" "1"
}
"ct5"
{
"ControlName" "ScalableImagePanel"
"fieldName" "ct5"
"xpos" "25"
"ypos" "432"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/France" //%t1flag%
"scaleImage" "1"
}

"t1"
{
"ControlName" "ScalableImagePanel"
"xpos" "r230"
"ypos" "329"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1"
}
"t2"
{
"ControlName" "ScalableImagePanel"
"xpos" "r230"
"ypos" "355"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1"
}

"t3"
{
"ControlName" "ScalableImagePanel"
"xpos" "r230"
"ypos" "380"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1"
}
"t4"
{
"ControlName" "ScalableImagePanel"
"xpos" "r230"
"ypos" "406"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1"
}
"t5"
{
"ControlName" "ScalableImagePanel"
"xpos" "r230"
"ypos" "432"
"zpos" "325"
"wide" "24"
"tall" "24" 
"visible" "1"
"enabled" "1"
"image" "../vgui/klutch/flags/Denmark" //%t2flag%
"scaleImage" "1"
}






}
