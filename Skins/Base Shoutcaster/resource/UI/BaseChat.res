"Resource/UI/BaseChat.res"
{
	"HudChat"
	{
		"ControlName"		      "EditablePanel"
		"fieldName" 		      "HudChat"
		"visible" 		        "1"
		"enabled" 		        "1"
		"xpos"			          "5"
		"ypos"			          "55"
		"wide"	 		          "405"
		"tall"	 		          "80"
		"PaintBackgroundType"	"0"
	}

	ChatInputLine
	{
		"ControlName"		      "EditablePanel"
		"fieldName" 		      "ChatInputLine"
		"visible" 		        "1"
		"enabled" 		        "1"
		"xpos"			          "5"
		"ypos"			          "395"
		"wide"	 		          "300"
		"tall"	 		          "2"
		"PaintBackgroundType"	"0"
	}

	"ChatFiltersButton"
	{
		"ControlName"		      "Button"
		"fieldName"		        "ChatFiltersButton"
		"xpos"			          "320"
		"ypos"			          "55"
		"wide"			          "60"
		"tall"			          "15"
		"autoResize"		      "1"
		"pinCorner"		        "0"
		"visible"		          "1"
		"enabled"		          "1"
		"tabPosition"		      "0"
		"labelText"		        "#chat_filterbutton"
		"textAlignment"		    "center"
		"dulltext"		        "0"
		"brighttext"		      "0"
		"Default"		          "0"		
	}

	"HudChatHistory"
	{
		"ControlName"		      "RichText"
		"fieldName"		        "HudChatHistory"
		"xpos"			          "5"
		"ypos"			          "5"
		"wide"	 		          "400"
		"tall"			          "30"
		"wrap"			          "1"
		"autoResize"		      "1"
		"pinCorner"		        "1"
		"visible"		          "1"
		"enabled"		          "1"
		"labelText"		        ""
		"textAlignment"		    "north-west"
		"font"			          "ChatFont"
		"maxchars"		        "-1"
	}
}