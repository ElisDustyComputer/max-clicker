define M = Character("Max", color="#0000FF")

default click_count = 0

init python:
    def explode_char():
        store.click_count += 1
        renpy.play("audio/explosion.mp3")
        renpy.show("explosion", at_list=[Transform(xalign=0.5, yalign=0.6)])
        renpy.show_screen("clickable_Max")
        if store.click_count == 5:
            renpy.invoke_in_new_context(renpy.say, store.M, "just stop already!")
        elif store.click_count == 20:
            renpy.invoke_in_new_context(renpy.say, store.M, "What is wrong with you?")
        elif store.click_count == 30:
            renpy.invoke_in_new_context(renpy.say, store.M, "Owie wowie zowie")
        elif store.click_count == 50:
            renpy.invoke_in_new_context(renpy.say, store.M, "haha... jokes over STOP EXPLODING ME")
        elif store.click_count == 100:
            renpy.invoke_in_new_context(renpy.say, store.M, "how bored can you be? huh?")
        elif store.click_count == 200:
            renpy.invoke_in_new_context(renpy.say, store.M, "ill get harvey to beat you up!")

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

label start:
    scene bg
    show screen clickable_Max

    M "hey!"
    "click max!"
    M "ow"

    $ renpy.pause(hard=True)

    hide screen clickable_Max
    


