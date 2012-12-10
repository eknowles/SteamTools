//             ______________________
//___________.( h0lmGUI™v4.1 by h0lm ).___________
//¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
//
// TRACKER SCHEME RESOURCE FILE
//
// sections:
//		colors			- all the colors used by the scheme
//		basesettings	- contains settings for app to use to draw controls
//		fonts			- list of all the fonts used by app
//		borders			- description of all the borders
//
//
Scheme
{
	//Name - currently overriden in code
	//{
	//	"Name"	"ClientScheme"
	//}

	//////////////////////// COLORS ///////////////////*d////////
	Colors
	{
		// base colors
		"HudColor"			"200 200 200 150"
		"HudMaxHealthColor"		"0 128 255 255"
		"HudMinHealthColor"		"255 0 0 255"
		"HudHealthFlash"		"255 0 0 255"
		"HudHealthNormal"		"200 200 200 150"
		"HudMoneyPlus"			"0 128 255 255"
		"HudMoneyMinus"			"255 255 255 255"
		"TimerFlash"			"255 255 255 255"
		"CTColor"			"0 128 192 255"
		"TerroColor"			"255 0 0 255"
		"CSLogoColor"			"200 200 200 150"
		"SourceLogoColor"		"0 128 255 255"
		"ChatColor"			"50 50 50 255"
		"Orange"			"255 255 255 255"
		"OrangeDim"			"255 255 255 100"
		"LightOrange"			"255 255 255 50"
		
		"Red"				"0 128 255 255"
		"Black"				"0 0 0 255"
		"TransparentBlack"		"0 0 0 196"
		"TransparentLightBlack"		"0 0 0 90"

		"Blank"				"0 0 0 0"
		"ForTesting"			"255 0 0 32"
		"ForTesting_Magenta"		"255 0 255 255"
		"ForTesting_MagentaDim"		"255 0 255 120"		
		"Yellowish"			"0 128 255 255"
		"Caution"			"200 200 200 150"
		"Normal"			"0 128 255 255"

	}

	///////////////////// BASE SETTINGS ////////////////////////
	// default settings for all panels
	// controls use these to determine their settings
	BaseSettings
	{
		// vgui_controls color specifications
		Border.Bright					"0 0 0 255"	// the lit side of a control
		Border.Dark						"0 0 0 255"		// the dark/unlit side of a control
		Border.Selection				"0 128 255 255"			// the additional border color for displaying the default/selected button
		Border.BuyPreset				"Orange"

		Button.TextColor				"White"
		Button.BgColor					"255 255 255 14"
		Button.ArmedTextColor			"White"
		Button.ArmedBgColor				"0 128 255 50"
		Button.DepressedTextColor		"White"
		Button.DepressedBgColor			"0 128 255 128"
		Button.FocusBorderColor			"Black"

		CheckButton.TextColor				"Orange"
		CheckButton.SelectedTextColor			"0 128 255 255"
		CheckButton.BgColor				"TransparentBlack"
		CheckButton.Border1  			"0 128 255 128"		// the left checkbutton border
		CheckButton.Border2  			"0 128 255 128"	// the right checkbutton border
		CheckButton.Check				"0 128 255 255"				// color of the check itself
		CheckButton.HighlightFgColor		"0 128 255 128"
		CheckButton.ArmedBgColor		"Blank"
		CheckButton.DepressedBgColor		"Blank"
		CheckButton.DisabledBgColor	   	"Blank"
		
		ComboBoxButton.ArrowColor		"0 128 255 128"
		ComboBoxButton.ArmedArrowColor	"0 128 255 255"
		ComboBoxButton.BgColor			"0 0 0 255"
		ComboBoxButton.DisabledBgColor	"0 0 0 255"

		Frame.BgColor					"TransparentBlack"
		Frame.OutOfFocusBgColor			"TransparentBlack"
		Frame.FocusTransitionEffectTime	"0.0"	// time it takes for a window to fade in/out on focus/out of focus
		Frame.TransitionEffectTime		"0.0"	// time it takes for a window to fade in/out on open/close
		Frame.AutoSnapRange				"0"
		FrameGrip.Color1				"Blank"
		FrameGrip.Color2				"Blank"
		FrameTitleButton.FgColor		"Blank"
		FrameTitleButton.BgColor		"Blank"
		FrameTitleButton.DisabledFgColor	"Blank"
		FrameTitleButton.DisabledBgColor	"Blank"
		FrameSystemButton.FgColor		"Blank"
		FrameSystemButton.BgColor		"Blank"
		FrameSystemButton.Icon			""
		FrameSystemButton.DisabledIcon	""
		FrameTitleBar.TextColor			"Orange"
		FrameTitleBar.BgColor			"Blank"
		FrameTitleBar.DisabledTextColor	"Orange"
		FrameTitleBar.DisabledBgColor	"Blank"

		GraphPanel.FgColor				"Orange"
		GraphPanel.BgColor				"TransparentBlack"

		Label.TextDullColor				"Orange" // Header3
		Label.TextColor					"Orange" // Header1
		Label.TextBrightColor				"Orange" // Header2
		Label.SelectedTextColor				"Orange"
		Label.BgColor					"Blank"
		Label.DisabledFgColor1				"Blank"
		Label.DisabledFgColor2				"LightOrange"

		ListPanel.TextColor				"Orange"
		ListPanel.BgColor				"TransparentBlack"
		ListPanel.SelectedTextColor			"Black"
		ListPanel.SelectedBgColor			"Red"
		ListPanel.SelectedOutOfFocusBgColor		"Red"
		ListPanel.EmptyListInfoTextColor		"Orange"

		Menu.TextColor					"Orange"
		Menu.BgColor					"TransparentBlack"
		Menu.ArmedTextColor				"Orange"
		Menu.ArmedBgColor				"Red"
		Menu.TextInset					"6"

		Chat.TypingText					"50 50 50 255"

		Panel.FgColor					"HudColor"
		Panel.BgColor					"Blank"

		HTML.BgColor					"Black"

		"BuyPreset.BgColor"				"0 0 0 128"
		"BuyPresetListBox.BgColor"			"0 0 0 128"
		"Popup.BgColor"					"0 0 0 230"

		ProgressBar.FgColor				"ProgressBarColor"
		ProgressBar.BgColor				"TransparentBlack"

		PropertySheet.TextColor			"Orange"
		PropertySheet.SelectedTextColor		"Orange"
		PropertySheet.TransitionEffectTime	"0.25"	// time to change from one tab to another

		RadioButton.TextColor			"Orange"
		RadioButton.SelectedTextColor		"Orange"

		RichText.TextColor			"Orange"
		RichText.BgColor			"Blank"
		RichText.SelectedTextColor		"Orange"
		RichText.SelectedBgColor		"Red"

		ScrollBarButton.FgColor			"Orange"
		ScrollBarButton.BgColor			"Blank"
		ScrollBarButton.ArmedFgColor		"Orange"
		ScrollBarButton.ArmedBgColor		"Blank"
		ScrollBarButton.DepressedFgColor	"Orange"
		ScrollBarButton.DepressedBgColor	"Blank"

		ScrollBarSlider.FgColor			"Blank"		// nob color
		ScrollBarSlider.BgColor			"Blank"		// slider background color

		SectionedListPanel.HeaderTextColor	"Orange"
		SectionedListPanel.HeaderBgColor	"Blank"
		SectionedListPanel.DividerColor		"Black"
		SectionedListPanel.TextColor		"Orange"
		SectionedListPanel.BrightTextColor	"Orange"
		SectionedListPanel.BgColor			"TransparentLightBlack"
		SectionedListPanel.SelectedTextColor			"Black"
		SectionedListPanel.SelectedBgColor				"Red"
		SectionedListPanel.OutOfFocusSelectedTextColor	"Black"
		SectionedListPanel.OutOfFocusSelectedBgColor	"255 255 255 32"

		Slider.NobColor				"108 108 108 255"
		Slider.TextColor			"255 255 255 255"
		Slider.TrackColor			"31 31 31 255"
		Slider.DisabledTextColor1	"117 117 117 255"
		Slider.DisabledTextColor2	"30 30 30 255"

		TextEntry.TextColor		"Orange"
		TextEntry.BgColor		"TransparentBlack"
		TextEntry.CursorColor		"Orange"
		TextEntry.DisabledTextColor	"Orange"
		TextEntry.DisabledBgColor	"Blank"
		TextEntry.SelectedTextColor	"Black"
		TextEntry.SelectedBgColor	"Red"
		TextEntry.OutOfFocusSelectedBgColor	"Red"
		TextEntry.FocusEdgeColor	"TransparentBlack"

		ToggleButton.SelectedTextColor	"Orange"

		Tooltip.TextColor			"TransparentBlack"
		Tooltip.BgColor				"Red"

		TreeView.BgColor			"TransparentBlack"

		WizardSubPanel.BgColor		"Blank"

		// scheme-specific colors
		"MainMenu.DepressedTextColor"	"0 128 255 128"
		"FgColor"		"0 0 0 1" //"0 128 255 255" BLÅT IKON
		"BgColor"		"0 0 0 1" //"TransparentBlack" BAGGRUNDEN

		"ViewportBG"		"Blank"
		"team0"			"204 204 204 255" // Spectators
		"team1"			"CTColor" // CT's
		"team2"			"TerroColor" // T's

		"MapDescriptionText"	"Orange" // the text used in the map description window
		"CT_Blue"			"153 204 255 255"
		"T_Red"				"255 64 64 255"
		"Hostage_Yellow"	"Panel.FgColor"
		"HudIcon_Green"		"200 200 200 150"
		"HudIcon_Red"		"255 0 0 255"
		"HudShopColor"			"0 128 255 255"
		"ProgressBarColor"		"0 128 255 255"
		"ScenarioColor"			"0 128 255 255"
		"C4Color"			"0 128 255 255"
		"C4FlashColor"			"255 255 255 255"
		"HostagesColor"			"0 128 255 255"
		"DefuseColor"			"0 128 255 255"

		// CHudMenu
		"ItemColor"		"255 255 255 255"	// default 255 167 42 255
		"MenuColor"		"255 255 255 255"
		"MenuBoxBg"		"0 128 255 80"

		// weapon selection colors
		"SelectionNumberFg"		"0 128 255 255"
		"SelectionTextFg"		"255 255 255 255"
		"SelectionEmptyBoxBg" 		"0 0 0 0"
		"SelectionBoxBg" 		"0 0 0 255"
		"SelectionSelectedBoxBg" 	"0 0 0 140" //If you are expiriencing scaling issues, you can set this command to "0 0 0 0" to remove the background of weapon selections.

		// Hint message colors
		"HintMessageFg"			"255 255 255 255"
		"HintMessageBg" 		"0 128 255 80"

		"ProgressBarFg"			"255 255 255 50"

		// Top-left corner of the "Counter-Strike" on the main screen
		"Main.Title1.X"		"155"
		"Main.Title1.Y"		"142"
		"Main.Title1.Color"	"CSLogoColor"

		// Top-left corner of the "SOURCE" on the main screen
		"Main.Title2.X"		"450"
		"Main.Title2.Y"		"142"
		"Main.Title2.Color"	"SourceLogoColor"

		// Top-left corner of the "BETA" on the main screen
		"Main.Title3.X"		"460"
		"Main.Title3.Y"		"-10"
		"Main.Title3.Color"	"255 255 0 255"

		// Top-left corner of the menu on the main screen
		"Main.Menu.X"		"32"
		"Main.Menu.Y"		"248"

		// Blank space to leave beneath the menu on the main screen
		"Main.BottomBorder"	"32"
		
	}

	//
	//////////////////////// FONTS /////////////////////////////
	//
	// describes all the fonts
	Fonts
	{
		// fonts are used in order that they are listed
		// fonts listed later in the order will only be used if they fulfill a range not already filled
		// if a font fails to load then the subsequent fonts will replace
		"Default"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"480 599"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"600 767"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"768 1023"
				"antialias"	"1"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"1024 1199"
				"antialias"	"1"
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"1200 6000"
				"antialias"	"1"
			}
			"6"
			{
				"name"		"Verdana"
				"tall"		"12"
				"range" 		"0x0000 0x00FF"
				"weight"		"900"
			}
			"7"
			{
				"name"		"Arial"
				"tall"		"12"
				"range" 		"0x0000 0x00FF"
				"weight"		"800"
			}

			
		}
		"DefaultUnderline"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"500"
				"underline" "1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
			"2"
			{
				"name"		"Arial"
				"tall"		"11"
				"range" 		"0x0000 0x00FF"
				"weight"		"800"
			}
		}
		"DefaultSmall"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"0"
				"range"		"0x0000 0x017F"
				"yres"	"480 599"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"0"
				"range"		"0x0000 0x017F"
				"yres"	"600 767"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"0"
				"range"		"0x0000 0x017F"
				"yres"	"768 1023"
				"antialias"	"1"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"0"
				"range"		"0x0000 0x017F"
				"yres"	"1024 1199"
				"antialias"	"1"
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"0"
				"range"		"0x0000 0x017F"
				"yres"	"1200 6000"
				"antialias"	"1"
			}
			"6"
			{
				"name"		"Arial"
				"tall"		"12"
				"range" 		"0x0000 0x00FF"
				"weight"		"0"
			}
		}
		"DefaultVerySmall"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"480 599"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"600 767"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"768 1023"
				"antialias"	"1"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"1024 1199"
				"antialias"	"1"
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"	"1200 6000"
				"antialias"	"1"
			}
			"6"
			{
				"name"		"Verdana"
				"tall"		"12"
				"range" 		"0x0000 0x00FF"
				"weight"		"0"
			}
			"7"
			{
				"name"		"Arial"
				"tall"		"11"
				"range" 		"0x0000 0x00FF"
				"weight"		"0"
			}
		}
		HudHintText
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"700"
				"yres"	"480 599"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"700"
				"yres"	"600 767"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"700"
				"yres"	"768 1023"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"700"
				"yres"	"1024 1199"
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"700"
				"yres"	"1200 10000"
			}
		}
		HudNumbersSmall
		{
			"1"
			{
				"name"		"Tahoma" //"Arial"
				"tall"		"1" //"16"
				"weight"	"0" //"1000"
				"additive"	"1"
				"antialias" "1"
				"range"		"0x0000 0x017F"
			}
		}

		HudSelectionNumbers
		{
			"1"
			{
				"name"		"h0lmGUIHUDNUMBERS" //"Verdana"
				"tall"		"11" //"11"
				"weight"	"0" //"1000"
				"antialias" 	"1"
				"dropshadow"	"0"
				"additive"	"1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"custom" "1"
			}
		}

		HudSelectionText
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"11"
				"weight"	"700"
				"antialias" "1"
				"yres"	"1 599"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"additive"	"1"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"11"
				"weight"	"700"
				"antialias" "1"
				"yres"	"600 767"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"additive"	"1"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"900"
				"antialias" "1"
				"yres"	"768 1023"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"16"
				"weight"	"900"
				"antialias" "1"
				"yres"	"1024 1199"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"17"
				"weight"	"1000"
				"antialias" "1"
				"yres"	"1200 10000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}

		BudgetLabel
		{
			"1"
			{
				"name"		"Courier New"
				"tall"		"14"
				"weight"	"400"
				"outline"	"1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		DebugOverlay
		{
			"1"
			{
				"name"		"Courier New"
				"tall"		"14"
				"weight"	"400"
				"outline"	"1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		CSType
		  {
		   "1"
		   {
			"name"  "cs" // cs.ttf
			"tall"  "80"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
		   }
		  }

		CSweapons // weapon selection
		  {
		   	"1"
			{
			"name"  "Counter-Strike"
			"tall"  "38"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1 599"
			"custom" "1"
			}
			"2"
			{
			"name"  "Counter-Strike"
			"tall"  "48"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"600 767"
			"custom" "1"
			}
			"3"
			{
			"name"  "Counter-Strike"
			"tall"  "62"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"768 1023"
			"custom" "1"
			}
			"4"
			{
			"name"  "Counter-Strike"
			"tall"  "85"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1024 1199"
			"custom" "1"
			}
			"5"
			{
			"name"  "Counter-Strike"
			"tall"  "90"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1200 10000"
			"custom" "1"
			}
		  }

		CSweaponsSmall 
		  {
		   	"1"
			{
			"name"  "Counter-Strike"
			"tall"  "38"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1 599"
			"custom" "1"
			}
			"2"
			{
			"name"  "Counter-Strike"
			"tall"  "48"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"600 767"
			"custom" "1"
			}
			"3"
			{
			"name"  "Counter-Strike"
			"tall"  "62"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"768 1023"
			"custom" "1"
			}
			"4"
			{
			"name"  "Counter-Strike"
			"tall"  "85"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1024 1199"
			"custom" "1"
			}
			"5"
			{
			"name"  "Counter-Strike"
			"tall"  "90"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"yres"	"1200 10000"
			"custom" "1"
			}
		  }

		
		CSTypeSmall
		  {
		   "1"
		   {
			"name"  "cs" // cs.ttf
			"tall"  "40"
			"weight" "20"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
		   }
		  }
		  
		  CSTypelr
		  {
		   "1"
		   {
			"name"  "cs" // cs.ttf
			"tall"  "30"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
		   }
		  }

		  CSTypeDeath
		  {
		   "1"
		   {
			"name"  "csd" // csd.ttf
			"tall"  "42"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"outline" "0"
			"custom" "1"
		   }
		  }
		
		Icons
		{
			"1"
			 {
			"name"  "Counter-Strike" // Cstrike.ttf
				"tall"  "28"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
			 }
			"2"
			 {
			"name"  "Counter-Strike" // Cstrike.ttf
			"tall"  "28"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
			 }
		}
		IconsSmall
		{
			"1"
			 {
			"name"  "Counter-Strike" // Cstrike.ttf
			"tall"  "20"
			"weight" "0"
			"additive" "0"
			"antialias" "1"
			"custom" "1"
			 }
		}
	
		SpecIconsTimer
		{
			"1"
			 {
			"name"  "Counter-Strike" // Cstrike.ttf
			"tall"  "15"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
			 }
		}
		
		BombIconLabel
		{
			"1"
			 {
			"name"  "BombIcon"
			"tall"  "26"
			"weight" "0"
			"additive" "1"
			"antialias" "1"
			"custom" "1"
			 }
		}
		
		CTTBG
		{
			"1"
			 {
			"name"  "BombIcon"
			"tall"  "40"
			"weight" "0"
			"additive" "0"
			"antialias" "1"
			"custom" "1"
			 }
		}

		ClientTitleFont
		{
			"1"
			{
				"name"  "Counter-Strike Logo" // CSlogo.ttf
				"tall"  "50"
				"weight" "0"
				"additive" "1"
				"antialias" "1"
				"custom" "1"
			}
		}
		
		CounterLogoFont
		{
			"1"
			{
				"name"  "CounterLogo"
				"tall"  "28"
				"weight" "0"
				"additive" "0"
				"antialias" "1"
				"custom" "1"
			}
		}
		
		MenuLogogo
		{
			"1"
			{
				"name"  "Counter-Strike Logo" // CSlogo.ttf
				"tall"  "15"
				"weight" "0"
				"additive" "0"
				"antialias" "1"
				"custom" "1"
			}
		}

		"BetaFont"
		{
			"1"
			{
				"name"		"Courier New"
				"tall"		"90"
				"weight"	"900"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"0"
			}
		}

		HudNumbers
		{
			"1"
			{
				"name"  "h0lmGUIHUDNUMBERS"
				"tall"  "22" //23
				"weight" "0"
				"additive" "1"
				"antialias" "1"
				"custom" "1"
			}
			"2"
			{
				"name"  "Verdana"
				"tall"  "28"
				"weight" "0"
				"additive" "1"
				"antialias" "1"
			}
		}
		HudNumbersGlow
		{
			"1"
			{
				"name"  "h0lmGUIHUDNUMBERS"
				"tall"  "22"
				"weight" "0"
				"additive" "1"
				"scanlines"	"4"
				"blur"	"5"
				"antialias" "1"
				"custom" "1"
			}
		}
		"CloseCaption_Normal"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		"CloseCaption_Italic"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
				"italic"	"1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		"CloseCaption_Bold"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		"CloseCaption_BoldItalic"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"900"
				"italic"	"1"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		// this is the symbol font
		"Marlett"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"11"
				"weight"	"0"
				"symbol"	"1"
				"range"		"0x0000 0x007F"	//	Basic Latin
			}
		}
		"MenuTitle"
		{
			"1"
			{
				"name"		"Verdana Bold"
				"tall"		"18"
				"weight"	"500"
			}
		}
		"Trebuchet24"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"24"
				"weight"	"900"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		"Trebuchet20"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"20"
				"weight"	"900"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		"Trebuchet18"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"18"
				"weight"	"900"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		"TargetID"
		{
		   "1"
			{
			   "name"		"Verdana"
			   "tall"		"12"
			   "weight"	"700"
			   "yres"	"480 599"
			   "dropshadow"	"0"
		   }
		   "2"
		   {
			   "name"		"Verdana"
			   "tall"		"13"
			   "weight"	"700"
			   "yres"	"600 767"
			   "dropshadow"	"0"
		   }
		   "3"
		   {
			   "name"		"Verdana"
			   "tall"		"14"
			   "weight"	"700"
			   "yres"	"768 1023"
			   "dropshadow"	"0"
		   }
		   "4"
		   {
			   "name"		"Verdana"
			   "tall"		"20"
			   "weight"	"700"
			   "yres"	"1024 1199"
			   "dropshadow"	"0"
		   }
		   "5"
		   {
			   "name"		"Verdana"
			   "tall"		"24"
			   "weight"	"700"
			   "yres"	"1200 10000"
			   "dropshadow"	"0"
		   }
		}
		"ChatFont"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"8.5"
				"weight"	"700"
				"yres"	"480 599"
				"dropshadow"	"1"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"700"
				"yres"	"600 767"
				"dropshadow"	"1"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"700"
				"yres"	"768 1023"
				"dropshadow"	"1"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"700"
				"yres"	"1024 1199"
				"dropshadow"	"1"
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"700"
				"yres"	"1200 10000"
				"dropshadow"	"1"
			}
		}
		"AchievementTitleFont"
		{
			"1"
			{
				"name"		"Verdana" [!$OSX]
				"name"		"Verdana Bold" [$OSX]
				"tall"		"16"
				"weight"	"1200"
				"antialias" "1"
				"outline" "1"
			}
		}
		"AchievementDescriptionFont"
		{
			"1"
			{
				"name"		"Verdana" [!$OSX]
				"name"		"Verdana Bold" [$OSX]
				"tall"		"12"
				"weight"	"1200"
				"antialias" "1"
				"outline" "1"
				"yres"		"0 480"
			}
			"2"
			{
				"name"		"Verdana" [!$OSX]
				"name"		"Verdana Bold" [$OSX]
				"tall"		"16"
				"weight"	"1200"
				"antialias" "1"
				"outline" "1"
				"yres"	 "481 10000"
			}
		}	
		
		
		AchievementItemTitle	[$WIN32]
		{
			"1"
			{
				"name"		"Arial" [!$OSX]
				"name"		"Helvetica Bold" [$OSX]
				"weight"		"1200"
				"tall"			"11"
				"antialias"		"1"
			}
		}
		
		AchievementItemDescription	[$WIN32]
		{
			"1"
			{
				"name"		"Arial" [!$OSX]
				"name"		"Helvetica" [$OSX]
				"weight"		"800"
				"tall"			"9"
				"antialias"		"1"
			}
		}
		
		"FreezeSmall"
		{		
			"1"
			{
				"name"		"Verdana Bold" [!$OSX]
				"name"		"Helvetica" [$OSX]
				"tall"		"9"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A			
				"antialias"	"1" [!$OSX]
			}	
		}
		
		"FreezeMedium"	// used by the freeze panel
		{		
			"1"
			{
				"name"		"Verdana Bold" [!$OSX]
				"name"		"Helvetica" [$OSX]
				"tall"		"14"
				"weight"	"600"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A				
				"antialias"	"1"
			}	
		}
		
		"FreezeLarge"
		{	
			"1"
			{
				"name"		"Verdana Bold" [!$OSX]
				"name"		"Helvetica" [$OSX]
				"tall"		"18"
				"weight"	"600"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A				
				"antialias"	"1"
			}	
		}

		"WinPanelLarge"
		{
			"1"
			{
				"name"		"Verdana" [!$OSX]
				"name"		"Helvetica" [$OSX]
				"tall"		"14"
				"weight"	"700"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1" [!$OSX]
			}
		}

		"WinPanelTiny"
		{
			"1"
			{
				"name"		"Verdana Bold" [!$OSX]
				"name"		"Verdana" [$OSX]
				"tall"		"9" 
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1" [!$OSX]
			}
		}

		WinPanelClock
		{
			"1"
			{
				"name"		"Counter-Strike" // Cstrike.ttf
				"tall"		"14"
				"weight"	"0"
				"additive"	"1"
				"antialias"	"1"
				"custom" "1"
			}
		}

		"HUDAchievementTiny"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"6"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"480 599"
			}
			"2"
			{
				"name"		"Verdana"
				"tall"		"8"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"600 767"
			}
			"3"
			{
				"name"		"Verdana"
				"tall"		"10"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"768 959"
				"antialias"	"1"
			}
			"4"
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"960 1023"
				"antialias"	"1" [!$OSX]
			}
			"5"
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"1024 1199"
				"antialias"	"1" [!$OSX]
			}
			"6"
			{
				"name"		"Verdana"
				"tall"		"16"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"1200 6000"
				"antialias"	"1" [!$OSX]
			}
		}

		"ScoreboardHeader"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"8"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"1"
			}
		}

		"ScoreboardTeamName"
		{
			"1"
			{
				"name"		"Dead Kansas"
				"tall"		"17"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"dropshadow"	"0"
				"additive"	"0"
				"custom" "1"
			}
		}

		"ScoreboardScore"
		{
			"1"
			{
				"name"		"Dead Kansas"
				"tall"		"33"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"dropshadow"	"0"
				"outline"	"0"
				"custom" "1"
			}
		}

		"SpecScoreboardTeamName"
		{
			"1"
			{
				"name"		"Dead Kansas"
				"tall"		"19"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"dropshadow"	"0"
				"additive"	"0"
				"custom" "1"
			}
		}
		
		"SpecScoreboardTimeLabel"
		{
			"1"
			{
				"name"		"Dead Kansas"
				"tall"		"24"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"dropshadow"	"0"
				"additive"	"0"
				"custom" "1"
			}
		}

		"SpecInfo"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"9"
				"weight"	"1000"
				"antialias"	"1"
			}
		}
		"SpecScoreboardScore"
		{
			"1"
			{
				"name"		"Dead Kansas"
				"tall"		"41"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"dropshadow"	"0"
				"additive"	"0"
				"custom" "1"
			}
		}
		"SpecPlayer"
		{
			"1"
			{
				"name" 		"Steelfish Eb"
				"tall"		"27"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}

		"SpecPlayerName"
		{
			"1"
			{
				"name"		"Tahoma"//Verdana
				"tall"		"11"
				"weight"	"1000"
				"yres"		"480 599"
				"outline"	"1"
			}
			"2"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"1000"
				"yres"		"600 767"
				"outline"	"1"
			}
			"3"
			{
				"name"		"Tahoma"
				"tall"		"13"
				"weight"	"1000"
				"yres"		"768 1023"
				"outline"	"1"
			}
			"4"
			{
				"name"		"Tahoma"
				"tall"		"14"
				"weight"	"1000"
				"yres"		"1024 1199"
				"outline"	"1"
			}
			"5"
			{
				"name"		"Tahoma"
				"tall"		"21"
				"weight"	"1000"
				"yres"		"1200 10000"
				"outline"	"1"
			}
		}

		"ScoreboardColumns"
		{
			"1"
			{
				"name"		"Tahoma"//Verdana
				"tall"		"10"
				"weight"	"1000"
				"yres"		"480 599"
				"outline"	"0"
				"antialias"	"1"
			}
			"2"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"1000"
				"yres"		"600 767"
				"outline"	"1"
			}
			"3"
			{
				"name"		"Tahoma"
				"tall"		"13"
				"weight"	"1000"
				"yres"		"768 1023"
				"outline"	"1"
			}
			"4"
			{
				"name"		"Tahoma"
				"tall"		"14"
				"weight"	"1000"
				"yres"		"1024 1199"
				"outline"	"1"
			}
			"5"
			{
				"name"		"Tahoma"
				"tall"		"21"
				"weight"	"1000"
				"yres"		"1200 10000"
				"outline"	"1"
			}
		}
		
		"ScoreboardPlayersAlive"
		{
			"1"
			{
				"name"		"PlayersAlive"
				"tall"		"20"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"custom" "1"
			}
		}

		"ScoreboardPlayersAliveGlow"
		{
			"1"
			{
				"name"		"PlayersAlive"
				"tall"		"20"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
				"blur"		"3"
				"additive" "1"
				"custom" "1"
			}
		}
		
		"ScoreboardPlayersAliveSuffix"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"9"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
			}
		}

		"DeathNoticeText"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"11"
				"weight"	"1000"
				"yres"		"480 599"
				"outline"	"1"
			}
			"2"
			{
				"name"		"Tahoma" 
				"tall"		"10" [!$OSX]
				"tall"		"11" [$OSX]
				"weight"	"1000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"1"
				"dropshadow"	"0"
			}
		}

		"ScoreboardBody_1"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"11"
				"weight"	"1000"
				"yres"		"480 599"
				"outline"	"1"
				"antialias"	"0"
			}
			"2"
			{
				"name"		"Tahoma" 
				"tall"		"10" [!$OSX]
				"tall"		"11" [$OSX]
				"weight"	"1000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"1"
				"antialias"	"0"
			}
		}
		
		"ScoreboardBody_2"
		{
			"1"
			{
				"name"		"Tahoma" 
				"tall"		"8" [!$OSX]
				"tall"		"9" [$OSX]
				"weight"	"1000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"1"
			}
		}
		
		"ScoreboardBody_second"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"11"
				"weight"	"1000"
				"yres"		"480 599"
				"outline"	"0"
				"antialias"	"1"
				"dropshadow"	"1"
			}
			"2"
			{
				"name"		"Tahoma" 
				"tall"		"10" [!$OSX]
				"tall"		"11" [$OSX]
				"weight"	"1000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"0"
				"antialias"	"1"
				"dropshadow"	"1"
			}
		}

		"ScoreboardBody_3"
		{
			"1"
			{
				"name"		"Tahoma" 
				"tall"		"7" [!$OSX]
				"tall"		"8" [$OSX]
				"weight"	"1000"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"outline"	"1"
			}
		}

		"ScoreboardMVP"
		{
			"1"
			{
				"name"		"Verdana"
				"tall"		"10"
				"weight"	"0"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Suppantialiastin Extended-A
				"antialias"	"1"
			}
		}

		"TeamMenuHeadLine"
		{
			"1"
			{
				"name" 		"Dead Kansas"
				"tall"		"19"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}
		
		"TeamMenuHeadLine2"
		{
			"1"
			{
				"name" 		"Dead Kansas"
				"tall"		"21"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}
			
		"TeamMenuOption"
		{
			"1"
			{
				"name" 		"Dead Kansas"
				"tall"		"17"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}
		
		"TeamMenuOption2"
		{
			"1"
			{
				"name" 		"Dead Kansas"
				"tall"		"13"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}
		
		"TeamMenuHeadLine3"
		{
			"1"
			{
				"name" 		"Tahoma"
				"weight"	"1000"
				"tall"		"19"
				"antialias"	"1"
				"dropshadow"	"0"
			}
		}

		"TeamMenuLargeNumber"
		{
			"1"
			{
				"name" 		"Dead Kansas"
				"tall"		"25"
				"antialias"	"1"
				"dropshadow"	"0"
				"custom" "1"
			}
		}

	}

	//
	//////////////////// BORDERS //////////////////////////////
	//
	// describes all the border types
	Borders
	{
		BaseBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}
		
		TitleButtonBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDisabledBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BgColor"
					"offset" "1 0"
				}
			}
			Top
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDepressedBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}

		ScrollBarButtonBorder
		{
			"inset" "1 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		ScrollBarButtonDepressedBorder
		{
			"inset" "2 2 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}
		
		ButtonBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		FrameBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "0 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "0 0"
				}
			}
		}

		TabBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}

		TabActiveBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "6 2"
				}
			}
		}


		ToolTipBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		// this is the border used for default buttons (the button that gets pressed when you hit enter)
		ButtonKeyFocusBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		ButtonDepressedBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}

		ComboBoxBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}

		MenuBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}
		}
		BrowserBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "0 0"
				}
			}
		}
		BuyPresetBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Border.BuyPreset"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.BuyPreset"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.BuyPreset"
					"offset" "1 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Border.BuyPreset"
					"offset" "0 0"
				}
			}
		}

		BuyPresetButtonBorder
		{
			"inset" "0 0 0 0"
			Left
			{
				"1"
				{
					"color" "Blank"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "Border.Dark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "Border.Bright"
					"offset" "1 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "Blank"
					"offset" "0 0"
				}
			}
		}
	}

	//////////////////////// CUSTOM FONT FILES /////////////////////////////
	//
	// specifies all the custom (non-system) font files that need to be loaded to service the above described fonts
	CustomFontFiles
	{
		"1"		"resource/cs.ttf"
		"2"		"resource/csd.ttf"
		"3"		"resource/Cstrike.ttf"
		"4"		"resource/CSlogo.ttf"
		"5"		"resource/Dead Kansas.ttf"
		"6"		"resource/PlayersAlive.ttf"
		"7"		"resource/h0lmGUIHUDNUMBERS.ttf"
		"8"		"resource/CounterLogo.ttf"
		"9"		"resource/steelfish.otf"
		"10"	"resource/BombIcon.ttf"
	}

}
//________________________________________________
//¯¯¯¯¯¯¯¯¯¯¯'( h0lmGUI™v4.1 by h0lm )'¯¯¯¯¯¯¯¯¯¯¯
//             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯