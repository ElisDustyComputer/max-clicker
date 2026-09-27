define M = Character("Max", color="#0000FF")

default click_count = 0
default show_explosion = False

init python:
    def explode_char():
        store.click_count += 1
        renpy.play("audio/explosion.mp3")
        store.show_explosion = True
        renpy.restart_interaction()

        def say_while_keeping_max(text):
            renpy.show_screen("clickable_Max")   # keeps Max on screen during the dialogue
            renpy.say(store.M, text)

        if store.click_count == 5:
            renpy.invoke_in_new_context(say_while_keeping_max, "just stop already!")
        elif store.click_count == 20:
            renpy.invoke_in_new_context(say_while_keeping_max, "What is wrong with you?")
        elif store.click_count == 30:
            renpy.invoke_in_new_context(say_while_keeping_max, "Owie wowie zowie")
        elif store.click_count == 50:
            renpy.invoke_in_new_context(say_while_keeping_max, "haha... jokes over STOP EXPLODING ME")
        elif store.click_count == 100:
            renpy.invoke_in_new_context(say_while_keeping_max, "how bored can you be huh?")
        elif store.click_count == 200:
            renpy.invoke_in_new_context(say_while_keeping_max, "ill get harvey to beat you up!")

screen clickable_Max():
    modal True

    text "Clicks: [click_count]" xalign 0 yalign 0.1 size 40

    imagebutton:
        idle "max happy"
        hover "max happy"
        focus_mask True
        xalign 0.5
        yalign 1.0
        action Function(explode_char)

        background None
        hover_background None
        selected_background None
        selected_hover_background None

    # Explosion sits on top of Max and auto-hides
    if show_explosion:
        add "explosion":
            xalign 0.5
            yalign 0.55
            zoom 0.35
        timer 1.5 action SetVariable("show_explosion", False)

label start:
    scene MaxClicker1000
    show screen clickable_Max
    play music "audio/backgroundmusic.mp3"

    M "hey! im max this is max clicker, click max to iniciate a special surprise, made by Eli elis first time coding"
    
    M "Ow"

    $ renpy.pause(hard=True)

    hide screen clickable_Max



