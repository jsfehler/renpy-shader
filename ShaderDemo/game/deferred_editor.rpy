screen setColorScreen(colorDict):
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 10
        ypadding 10

        vbox:
            xmaximum 400
            ymaximum 400
            spacing 5
            hbox:
                textbutton "Red:" xsize 150
                bar value DictValue(colorDict, "red", 100)
            hbox:
                textbutton "Green:" xsize 150
                bar value DictValue(colorDict, "green", 100)
            hbox:
                textbutton "Blue:" xsize 150
                bar value DictValue(colorDict, "blue", 100)
            hbox:
                textbutton "Strength:" xsize 150
                bar value DictValue(colorDict, "strength", 1000)
            hbox:
                textbutton "Back" action Hide("setColorScreen")


screen addLightScreen():
    on "show" action SetVariable("addLightInteractive", True)
    on "hide" action SetVariable("addLightInteractive", False)

    frame:
        yalign 1.0
        xpadding 10
        ypadding 10
        $ textWidth = 250
        vbox:
            spacing 2
            hbox:
                textbutton "Light x-position:" xsize textWidth
                bar value VariableValue("addLightX", 1000)
            hbox:
                textbutton "Light y-position:" xsize textWidth
                bar value VariableValue("addLightY", 1000)
            hbox:
                textbutton "Light z-offset:" xsize textWidth
                bar value VariableValue("addLightZOffset", 1000)
            hbox:
                textbutton "Light color" action Show("setColorScreen", None, addLightColor)
            hbox:
                textbutton "Add light" action [Function(addNewLight), Hide("addLightScreen")]
                textbutton "|"
                textbutton "Cancel" action Hide("addLightScreen")


screen deferredEditorScreen():
    frame:
        xpadding 10
        ypadding 10
        hbox:
            textbutton "Exit" action Return("")
            textbutton "|"
            vbox:
                textbutton "Mouse light" action ToggleVariable("mouseLight")
                if mouseLight:
                    textbutton "Light color" action Show("setColorScreen", None, mouseLightColor)
            textbutton "|"
            vbox:
                textbutton "Mouse sun" action ToggleVariable("mouseSun")
                if mouseSun:
                    textbutton "Sun color" action Show("setColorScreen", None, mouseSunColor)
            textbutton "|"
            textbutton "Ambient" action Show("setColorScreen", None, ambientLight)
            textbutton "|"
            textbutton "Add light" action Show("addLightScreen")
            textbutton "|"
            vbox:
                textbutton "DOF"
                bar value VariableValue("depthOfField", 100) xsize 100
            textbutton "|"
            vbox:
                textbutton "Shadow"
                bar value VariableValue("shadowStrength", 100) xsize 100
            textbutton "|"
            vbox:
                textbutton "Fog" action Show("setColorScreen", None, fogColor)
                bar value VariableValue("fogStart", 100) xsize 100
            if fogStart < 100:
                vbox:
                    textbutton ""
                    textbutton "Rain" action ToggleVariable("fogRainEnabled")
