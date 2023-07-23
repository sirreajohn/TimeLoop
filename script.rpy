# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init python:

    default_screen_height = 1080
    default_screen_width = 1920

    default_sprite_height = 1200 / 2
    default_sprite_width = 1000 / 2

    center_y_offset_male = -250
    center_y_offset_female = center_y_offset_male - 20


    def italify(sentence):
        return "{i}" + sentence + "{/i}"

default preferences.text_cps = 40
default preferences.name_text_size = 10

define mc = Character("MC", color = "#ffffff")
define t1 = Character("Teacher 1", color = "#8de03f")
define t2 = Character("Teacher 2", color = "#e9e62d")
define n = Character("Neha", color = "#2c57e6")

image staff_room = im.Scale("images/bg staff room.png", default_screen_width, default_screen_height)
image corridor = im.Scale("images/bg corridor afternoon.webp", default_screen_width, default_screen_height)
image rooftop = im.Scale("images/bg rooftop dusk.webp", default_screen_width, default_screen_height)
image classroom = im.Scale("images/bg classroom dusk.webp", default_screen_width, default_screen_height)

image t2_neutral_sprite = im.Scale("T2_Neutral.png", default_sprite_width, default_sprite_height, xoffset = 0, yoffset = center_y_offset_male)
image t1_neutral_sprite = im.Scale("T1_Neutral.png", default_sprite_width, default_sprite_height, xoffset = 0, yoffset = center_y_offset_female)
image mc_neutral_sprite = im.Scale("MC_Neutral.png", default_sprite_width, default_sprite_height, xoffset = 0, yoffset = center_y_offset_male)
image neha_neutral_sprite = im.Scale("N_Neutral.png", default_sprite_width, default_sprite_height, xoffset = 0, yoffset = center_y_offset_female)

# im.Scale()


# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show text f"The hottest place in Hell is reserved for those \nwho remain neutral in times of great moral conflict. \n{'--unknown':>120}" with Dissolve(1.5)
    # with Dissolve (1.5)
    pause (5.0)
    hide text with Dissolve(1.5)
    # Show text "The Awakened" With Dissolve(1.5)
    # pause (1.0)
    # hide text
    # With Dissolve(1.5)

    scene staff_room with Fade(0.5, 0, 1, color = "#ffffff")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    t1 "Just tell us already, we cannot waste anymore time on this. \nDid you do it or not?"

    mc "I have no comment"

    show t2_neutral_sprite
    t2 "We know all the rumors about you being a creep. This photo--"
    "(he waves a photo)"
    t2 "If you come out on your own, You will need to write a formal apology and be suspended for a week."
    hide t2_neutral_sprite

    mc "I didn't do it, you keep hurling accusations at me, and that photo is not even clear. The only reason I am standing here is because of hearsay and not solid evidence."

    show t2_neutral_sprite
    t2 "(tsk){size=-10}if we only had solid evidence.{/size}"
    hide t2_neutral_sprite

    show t1_neutral_sprite
    t1 "management is concerned about the school's reputation. The jersey in the photo has the “02” on it. It belongs to you, right?"

    mc "Yes, but that isn't me, it was stolen. My classmates are lying, I was with them the whole time."
    hide t1_neutral_sprite

    show t2_neutral_sprite with vpunch
    t2 "Again with lies, they denied seeing you for the whole afternoon!"

    "(Teacher 1 waves politely at Teacher 2 to shut up.)"
    hide t2_neutral_sprite

    show t1_neutral_sprite

    t1 "its words of three versus one. Until you prove that wasn't you with solid evidence or alibi."

    t1 "you are the suspicious one. And if you don't confess, it will lead to expulsion or worse, the parents might take it to the police."
    
    mc "..."
    
    t1 "Listen, you have 7 days to produce any evidence, or confess."
    "{i}I blankly stare at teacher while this world decided my fate.{/i}"
    t1 "dismissed"

    hide t1_neutral_sprite
    
    mc "..."

    scene corridor with wipeleft

    "(MC exits the room, walks up to the vending machine at the end of the hallway,)"
    "(buys a cola. He takes the can and proceeds to the terrace of school)"

    scene rooftop with blinds

    "(Once reaching the terrace he leans on to the railing)"
    "(The evening sun glares at land with its red unforgiving eyes. MC glances at his watch)"
    mc "6.00pm"
    "(he makes note of time, opens the can and takes a sip.)"
    
    show mc_neutral_sprite with ease 
    
    mc "{i}ok, let's get the story straight,{/i}"

    $ mc(italify("a photo of a guy in a sports uniform standing on a box, peeking into the girl's locker room was circulated via social networks."))

    $ mc(italify("Rumor started spreading that it was me who did that, because the guy in the photo is wearing a jersey with “02” on its back."))
    
    $ mc(italify("Which is my number."))

    "(He takes a sip of cola)"

    $ mc(italify("but I was with Ria's group goofing off in the abandoned building behind the school at that time."))

    $ mc(italify("But, Ria and others denied seeing me that afternoon which left me with no alibi."))
    $ mc(italify("Things got worse, i started getting bullied and I was soon pressured to leave my soccer club."))
    $ mc(italify("Everything points to Ria being the mastermind behind this.."))
    $ mc(italify("Rumor started spreading that it was me who did that, because the guy in the photo is wearing a jersey with “02” on its back."))
    $ mc(italify("but why would she do it?"))

    $ mc(italify("I was nice to her and we got along well,"))
    $ mc(italify("or maybe someone is pressuring her to deny the alibi."))

    "(MC crushes the can, throws it into a dustbin. He starts walking towards the stairs.)"

    $ mc(italify("I should head home and think about what to do."))

    hide mc_neutral_sprite

    scene classroom with blinds

    mc "It's empty, I guess everyone left."

    "(MC starts packing his bag. The door opens, someone steps in, MC turns around.)"

    show neha_neutral_sprite with irisin

    n "Hi MC!"
    "(Neha notices that MC is a bit dull)"
    n "...everything ok?"

    mc "Yeah, everything's fine, thanks for asking. Isn't it a bit late? What are you still doing in school?"

    n "I was in the library reading a book and lost track of time."
    n "Next thing I know it's late evening."

    mc "What were you reading? Must be interesting if it got you hooked that hard."

    n "It's {b}Metamorphosis by Franz Kafka{/b}, interesting read!"
    n "it's an Exaggerated take on fragility of human relations."
    n "The lead character, {b}Gregor{/b} is a traveling salesman, who one day wakes up to find himself turned into a human sized cockroach."
    n "The book explores his so-called “we-support-you-unconditionally” family falling apart."

    mc "hmm, a rather cynical take on family, don't you think?"
    mc "Reality is a little different, you don't find people turning into bugs."

    n "Well yeah, but the cockroach here is a metaphor for depression."
    n "Gregor in the book is actually in depression."
    n "The inability of motivation, lack of strength to change, your own thoughts assaulting your self-confidence."
    n "The whole cockroach thing is an elaborate metaphor."

    mc "That's rather bleak, I didn't know you had interest in dark takes on humanity."

    n "I recently stumbled upon this genre when I was recovering from burnout from music."

    mc "hmm.. anyway, I will be heading home. you headed home too?"

    n "No, you can go ahead. I still have to pack my things."

    "(MC leaves the classroom)"


    



    # This ends the game.

    return
