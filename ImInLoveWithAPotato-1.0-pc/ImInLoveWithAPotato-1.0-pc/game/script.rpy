define yn = Character("[name]")
define p = Character("Potato-chan")
define b = Character("Beetroot-kun")
define n = Character("Nagito")
define a = Character("Alexandria")
define a1 = Character("???")
define m = Character("Mr. Hoong")
define g = Character("Genie")
define audio.holiday = "audio/kodomoi-holiday.mp3"
define audio.mos = "audio/kodomoi-memory-of-summer.mp3"
define audio.end = "audio/juhani-junkala-gentle-casual-gaming-loop.mp3"

# The game starts here.

label start:

    $ love = 2
    $ councilr = 0
    $ friendr = 0
    $ beetrootr = 0
    $ councilroute = False
    $ friendroute = False
    $ beetrootroute = False
    scene outsidehome
    with fade
    play music holiday

    "Ah, it is a beautiful day outside."
    "It is a Monday morning and you are headed to school when you hear a voice behind you."

    p "Nee nee! Wait upppp!!!"

    show potato
    with dissolve

    "You turn around to find Potato-chan running behind you with a toast in her mouth."

    python:
        name = renpy.input("By the way, what's your name?")
        name = name.strip()

        if not name:
            name = "Pineapple-kun"

    yn "Konnichiwa, Potato-chan!"

    p "I finally caught up to you, [name]—WHOAH!"

    "She trips on a pebble and lands on me, her toast burning my face."
    "This is Potato-chan, my childhood friend who is also a tsundere who often acts like this around me."
    "After that incident, we walked to school as usual when we noticed someone eating a potato."

    p "Oh no, that's horrible!"

    menu:
        "What do you do?"

        "Say \"C'mon Potato-chan, let's ignore them.\"":
            p "B-But [name]..."

            "I ignored her pleas as I dragged her to school."
            $ love -= 1

        "Charge in and beat up the cannibal.":
            "You charge in and get beat up. You lose 5 HP. Not that it matters since this is a dating sim."
            "Potato-chan drags your pathetic body to the local hospital."

        "Throw Potato-chan at the assailant.":
            "Potato-chan shrieks even louder as you chuck her at the murderer. Roll for initiative!"
            "You got a nat 20!"
            "Potato-chan activates her secret razer blades and knock out the assailant."

            p "That was fun, [name]!!"

            "Her face flushed red, probably from the blood of the attacker."
            $ love += 1

    hide potato
    with dissolve
    scene school
    with fade

    "When we get to school, we're greeted by the student council president, Nagito Uzumaki Sharingan Sharingan Bible No Kyooosutsu Komaeda."

    show nagito
    with dissolve

    n "You're late."

    yn "Sorry, but we were off...doing our own things."

    "I blushed."
    "I glanced over at Potato-chan and realized that she was intimately staring into my eyes."

    n "Yare yare daze."

    "Nagito Uzumaki Mangekyo Sharingan Totsudo Tetsudo Soduko sighed."

    n "You two lovebirds get your own room. Just go back to your class."

    hide nagito
    with dissolve
    scene hallway
    with fade

    "We parted ways for period 1."
    "It felt like an eternity, the time that I spent without Potato-chan."
    "I kept thinking about the texture of her face and couldn't help daydreaming during boring Maths class."

    scene classroom
    with fade

    "When we met for period 2, I felt my senses arise as my oxytocin levels shot up through the roof as I powered up into my third form."
    "Surely, this was but a placebo effect brought on by the imagination, but it could turn into a reality if I was with Potato-chan—WAIT WHAT AM I THINKING?!"

    show potato
    with dissolve

    p "Ohayo, [name]!"

    hide potato
    with dissolve

    "Damn, I can't stop thinking about Potato-chan. It's even harder when she sits right in front of me in the most boring period ever; computer science."

    show beetroot
    with dissolve

    "NANI?! What's this?! It seems like my classmate Beetroot-kun is trying to pass Potato-chan a letter!"

    menu:
        "Gah! What should I do?!"

        "Get up out of my seat and punch Beetroot-kun in the face as hard as I can, intercepting the note sneakily.":
            "You slap Beetroot-kun and get sent outside for detention."

            hide beetroot
            with dissolve

        "Slap Potato-chan in the face.":
            hide beetroot
            with dissolve
            show potato
            with dissolve

            p "WTF?!"
            p "FRICKIN OUCH."
            $ love -= 1

            hide potato
            with dissolve

        "Do a backflip.":
            hide beetroot
            with dissolve
            "I suddenly get out of my seat. The teacher asks me what I'm doing."

            yn "Sorry, Mr. Karr, but I must do this."

            "I land an epic backflip and go down in history as the greatest backflipper ever."
            $ love += 1

            show potato
            with dissolve

            p "WAAAAAA!!! SUGOIIIIII!"
            p "I never knew you were so cool!"

            hide potato
            with dissolve

    scene hallway
    with fade

    "After that glory-fest with Potato-chan, I strutted out the classroom door with pride when Beetroot-kun stopped me."

    show beetroot
    with dissolve

    b "Wah'ssa big idea, eh? I'd stay outta mah way if I wer' u."

    menu:

        "Damn, I can't let him get away with this. Now his whole squad is laughing at me. Using my quick brain, I decide to insult his:"

        "Face.":
            yn "Your face is as ugly as..."

            "It is at that moment when you realize how truly handsome Beetroot-kun is with his majestic and lush skin and gorgeous face."

            yn "Tch. I'll get you next time."

            "I walk away."
            $ love -= 1

        "Hair.":
            yn "Lmao ur hair looks like a Barbie doll's hair."

            "Beetroot-kun starts breaking down emotionally and I exit the room as if I had an explosion behind me."
            $ love += 1
            $ beetrootr -= 1

        "Body.":
            yn "Your body is as ugly as..."

            "It is at that moment when you realize that Beetroot-kun's body is his head and how truly handsome Beetroot-kun is with his majestic and lush skin and gorgeous face."

            yn "Tch. I'll get you next time."

            "I walk away."
            $ love -= 1

    hide beetroot
    with dissolve
    scene classroom
    with fade

    "I proceed directly to my fourth period after that."
    "I sit down in my seat when a extremely cute and pretty 5'6\" anime girl with stars for eyes and lush silky white hair donned with a fedora and an awesome eyepatch with Hello Kitty stickers approached me."

    show alex
    with dissolve

    a1 "H-hey, you're in my seat; would you mind getting out, thank you..."

    "She was talking in almost a whisper, tipping her fedora."
    "Whoever this girl was, she had to be a chad because of her fedora."
    "The fedora was the only thing I could pay attention to until—"

    a1 "OI KISAMA, YOU'RE IN MY SEAT; PLEASE GET OUT, THANK YOU!"

    yn "No."

    "This was a battle between chads; a battle that I could not afford to lose."

    menu:
        "The girl suddenly lifts up her eyepatch to reveal an evil eye and starts chanting a spell! What do you (I) do?!"

        "Utilize your skills in Taijutsu—the gentle art of folding someone's clothes while they're still wearing it.":
            "You grab her hand and start activating your Taijutsu when Potato-chan suddenly walks in!"

            hide alex
            with dissolve
            show potato
            with dissolve

            p "W-Wh-WHAT ARE YOU DOING, [name]?!"
            p "I-I-I..."

            hide potato
            with dissolve

            "Potato-chan walks away."

            yn "MATTE! Potato-chan, it's not what it looks like!"

            show alex
            with dissolve

            "I tried to run after Potato-chan, but I realized that the girl was still holding my hand."
            $ love -= 1
            $ friendr += 1

        "Join her ritual and offer to be a virgin sacrifice for you have lost the battle of the chads.":
            yn "I shall offer you my body as sacrifice for I have lost."

            a1 "W-W-What are you...talking about..."
            a1 "I-I can really have full control of your whole entire body...?"

            hide alex
            with dissolve
            show potato
            with dissolve

            "Just when I was about to answer, I noticed Potato-chan in the corner of the room staring daggers into my soul."

            yn "Oh hi, Potato-chan! I didn't notice you there!"

            "Potato-chan kept staring daggers."

            hide potato
            with dissolve

        "Do a backflip.":
            hide alex
            with dissolve

            "I suddenly get out of my seat. The teacher asks me what I'm doing."

            yn "Sorry, Mr. Hoong, but I must do this."

            "I land an epic backflip and go down in history as the greatest backflipper ever."

            show potato
            with dissolve

            p "WAAAAAA!!! SUGOIIIIII!"
            p "I never knew you were so cool!"

            hide potato
            with dissolve
            show alex
            with dissolve

            a1 "Ugh, you're not a true chad."
            a1 "A true chad would've done a double backflip."
            $ love += 1
            $ friendr -= 1

    show alex
    with dissolve

    "After everything settled down, I finally asked the girl who she was."

    a "My name is Alexandria \"Maria\" Clausees the Fifth."
    a "I was born in a village full of chads who were blessed by the chad gods. But that all changed when the anti-chad nation attacked—"

    yn "Yeah, that's cool and all, but what's your relationship with Potato-chan?"

    a "What does it matter to you?"

    yn "It matters very much to me."

    hide alex
    with dissolve

    p "We're just friends!"

    show potato
    with dissolve

    "I spun around to see Potato-chan right there."

    p "What are you doing in my class, [name]?"

    hide potato
    with dissolve

    "I looked around and found everyone awkwardly staring at me."
    "I knew absolutely no one there. Not even the class pet."

    yn "I'm in the wrong class!"

    "I darted out of the classroom."

    p "Goodbye, [name]!"
    a "See ya soon~"

    scene hallway
    with fade

    "As the tardy bell rang, my mind filled with questions and Potato-chan."
    "What did Alexandria mean when she said \"See ya soon~\"?"
    "Was she going to camp out at my favorite Coca-Cola vending machine during lunch and wait for the right time to shank me?"
    "I shuddered at the thought and daydreamed about Potato-chan's perfect legs to keep me distracted."

    scene classroom
    with fade
    show beetroot
    with dissolve

    b "LMAO, THIS LOSER REALLY BE WALKING IN LATE."

    hide beetroot
    with dissolve

    "I did my best to hold in my murderous tendencies and walked to my seat."

    m "Settle down, children."
    m "Today, we are going to be doing a team exercise. We are going to graphic design."
    m "[name] and Beetroot-kun! You are team 1!"

    show beetroot
    with dissolve

    menu:
        b "Let's graphic design, loser. What should we make?"
        "An anti-bullying poster targeted towards Beetroot-kun.":
            b "Not cool."
            $ beetrootr -= 1
        "A weeaboo poster filled with Naruto-kun and Kirito-kun.":
            b "Haha, weeb."
            $ love += 1
        "A poster of a unicorn.":
            b "Unicorns are the sworn enemy of potatoes! WTF, MATE."
            $ love -= 1

    hide beetroot
    with dissolve

    "The coder is getting sleepy. Speedrun time. Lunch Time."

    scene cafeteria
    with fade

    show genie
    with dissolve
    "!!!"

    menu:
        "Wow, you met a genie in the cafeteria! You get one wish; what is it?"
        "Anime becomes real.":
            g "Haha, stupid weeb."

            hide genie
            with dissolve
            show nagito
            with dissolve

            "Nagito Ichiyama Nazedaya Jiraiya Enoshima, the student council president, approaches you."

            n "I see you are a true man of culture. It's rare these days to meet brave souls like you."
            $ councilr += 1

            hide nagito
            with dissolve

            "He walks off."
        "Fire hands.":
            g "What the—you'll die stupid idiot."

            hide genie
            with dissolve
            show alex
            with dissolve

            a "Not bad for a totally uncool guy. You have potential..."
            $ friendr += 1

            hide alex
            with dissolve
        "Potato-chan.":
            g "Right behind you."

            hide genie
            with dissolve
            show potato
            with dissolve

            p "KYAAAAAAAAAAAAAAAAAAA~!!!! BAKA BAKA BAKAAAAAAA~!!!"
            $ love += 1

            hide potato
            with dissolve
        "A metal bat.":
            g "Those are unsafe in a school environment."

            hide genie
            with dissolve
            show beetroot
            with dissolve

            b "RADICAL."
            $ beetrootr += 1

            hide beetroot
            with dissolve

    show hallway
    with fade

    "UH UH PERIOD 5."
    "As you head to your fifth period, you notice everyone (every named character) walking with you to Mr. Wasd's class."

    yn "Woah, I never knew we were all in the same class!"

    show classroom
    with fade

    menu:
        "The teacher is sick! Hooray! I mean...awwww. It's a free period! Spend it with whoever you want to."
        "Nagito Kirigiri Yamaha Sony Toyota Hanamura.":
            show nagito
            with dissolve

            n "Ho, you want to spend time with me?"
            n "I see that you have some questions for me. Well, then. Speak!"
            n "..."
            n "You are a fool to ask that. All I shall say is that my ultimate goal in life is to spread the message of animeeee—I MEAN JUSTICE!"
            n "I love Justice, more than anyone else! You shall be wise not to forget that!"

            "You and Nagito spend all of fifth period talking to one another."
            $ love -= 1
            $ councilr += 1

            hide nagito
            with dissolve
        "Alexandria \"Maria\" Clausees the Fifth.":
            show alex
            with dissolve

            a "Y-You wanna spend time w-with me...?!!"
            a "V-Very well then... let us hang out."

            "You spent some time learning how to become a chad with Alexandria. Alexandria has earned a new title: senpai."
            "You and Alexandria spend all of fifth period talking to one another."
            $ love -= 1
            $ friendr += 1

            hide alex
            with dissolve
        "Potato-chan.":
            show potato
            with dissolve

            p "WASSHOI!"

            "She glomps you hard."
            "You and Potato-chan then proceeded to have a deep spiritual conversation about the heat death of the universe."
            "You and Potato-chan spend all of fifth period talking to one another."
            $ love += 1

            hide potato
            with dissolve
        "Beetroot-kun.":
            show beetroot
            with dissolve

            b "Pssshhhh. Whaddya want?"
            b "Well?"
            b "..."
            b "HELL TO THE NAW AM I GONNA DO WHAT YOU JUST SAID! YOU'VE GOT BALLS, KID, ASKING ME SOMETHING LIKE THAT!"

            "You and Beetroot-kun spend all of fifth period talking to one another."
            $ love -= 1
            $ beetrootr += 1

            hide beetroot
            with dissolve

    scene hallway
    with fade

    "The bell rings and it's sixth period. None of your friends are in your sixth period. Aw."

    scene classroom
    with fade

    "You start reflecting on your life a bit and start thinking about your friends."

    show beetroot
    with dissolve

    "There's Beetroot-kun—he has a bad attitude and he's probably going for Potato-chan. That is unacceptable."

    hide beetroot
    with dissolve
    show alex
    with dissolve

    "There's Alexandria—the ultimate chad. She's cool."

    hide alex
    with dissolve
    show nagito
    with dissolve

    "There's Nagito whatever his last name is—he is shrouded in a dark mysterious aura, but he's just a closet weeb."

    hide nagito
    with dissolve
    show potato
    with dissolve

    "Finally, there's my beloved Potato-chan. There isn't much else to say."

    hide potato
    with dissolve
    scene school
    with fade

    "Wow, time flew by fast. Now school's out."

    show potato
    with dissolve

    p "HEY, WAIT! AREN'T YOU GOING TO GO TO THE GRADUATION CEREMONY?"

    hide potato
    with dissolve

    "Graduation ceremony? OH RIGHT, TODAY WAS THE DAY OF GRADUATION! I TOTALLY FORGOT!"

    play music end

    "Graduation commences..."

    if beetrootr == 2:
        $ beetrootroute = True

    if councilr == 2:
        $ councilroute = True

    if friendr == 3:
        $ friendroute = True

    if love <= 3 and beetrootroute == False and councilroute == False and friendroute == False:
        jump badend

    if 4 <= love <= 5 and beetrootroute == False and councilroute == False and friendroute == False:
        jump neutralend

    if beetrootroute == True:
        jump beetrootend

    if love <= 6 and councilroute == True:
        jump councilend

    if friendroute == True:
        jump friendend

    if love >= 6:
        jump goodend

    label badend:
        "After the graduation ceremony, I rushed to go find Potato-chan."

        show potato
        with dissolve

        "When I found her...it was too late as she had already said yes to Beetroot-kun's proposal."

        hide potato
        with dissolve

        "I walked alone back home."

        return
    label neutralend:
        "After the graduation ceremony, I rushed to go find Potato-chan. When I found her..."

        show potato
        with dissolve

        yn "I have really liked you ever since we entered high school together! So please! Be with me!"
        "Before I knew it, the words \"be with me\" rang out through the air. Potato-chan started to tear up."
        p "I'm sorry, [name]...I only like you as a friend."
        "You hold back your own tears and comfort Potato-chan."
        yn "It's alright, Potato-chan. I'll always be your friend."

        hide potato
        with dissolve

        "We walked home together, as childhood friends should."

        return
    label beetrootend:
        "After the graduation ceremony, I rushed to go find Potato-chan. When I found her..."

        show potato
        with dissolve

        yn "I have really liked you ever since we entered high school together! So please! Marry me!"
        "Before I knew it, the words \"Marry me\" rang out through the air. Potato-chan laughed it off as a joke and I walked alone back home."

        hide potato
        with dissolve

        b "Wait, before you go..."

        show beetroot
        with dissolve

        "I spun around to see Beetroot-kun standing there."
        b "I admire your spirit, nerd. I never knew a filthy loser like you could ever fit the bill, but if you can't do it with your mighty spirit, no one can."
        yn "What are you talking about—"
        b "Join my biker gang. You'll fit right in."

        hide beetroot
        with dissolve

        "I ended up joining Beetroot-kun's biker gang."

        return
    label friendend:
        "After the graduation ceremony, I rushed to go find Potato-chan. When I found her..."

        show potato
        with dissolve

        yn "I have really liked you ever since we entered high school together! So please! Stay by my side for all eternity!!"
        "Before I knew it, the words \"all eternity\" rang out through the air. Potato-chan laughed it off as a joke and I walked alone back home, stopping by my favorite vending machine."

        hide potato
        with dissolve

        a "Oi, where do you think you're going...?"

        show alex
        with dissolve

        "I spun around to see Alexandria standing there."
        a "NYAAAAHAHAHA! You got rejected!"
        yn "It's not something to laugh about!"
        "I felt tears welling up in my eyes."
        yn "I'm never gonna become a real chad like you, senpai!"
        a "Oh, you don't need to worry about becoming a chad when you have me..."

        hide alex
        with dissolve

        "I walked home together with Alexandria that night."

        return
    label councilend:
        "After the graduation ceremony, I rushed to go find Potato-chan. When I found her..."

        show potato
        with dissolve

        yn "I have really liked you ever since we entered high school together! So please! Kekkon Shite Kudasai!"
        "Before I knew it, the words \"Kekkon Shite\" rang out through the air. Potato-chan laughed it off as a joke and I walked alone back home."

        hide potato
        with dissolve

        n "Chotto matte kudasai..."

        show nagito
        with dissolve

        "I spun around to see Nagito standing there."
        n "HAHAHAHAHAHAAAA! II MONO, KUSO GAKI! MARRIAGE MAY BE TEMPORARY, BUT JUSTICE IS ETERNAL!"
        n "COME WITH ME AND LET US CREATE THE NEW WORLD ORDER!"
        "I smiled at the thought of becoming the next world leader alongside Nagito."

        hide nagito
        with dissolve

        "I ended up ruling the world with Nagito forevermore."

        return
    label goodend:
        "After the graduation ceremony, I rushed to go find Potato-chan. When I found her..."

        show potato
        with dissolve

        yn "I have really liked you ever since we entered high school together!"
        yn "When I first saw you beneath those cherry blossom trees, my heart went doki-doki as I imagined our future together."
        yn "I will stay forever by your side if you will stay by my side."

        hide potato
        with dissolve

        "Everything went quiet and what broke through the silence changed my life forever."

        show potato
        with dissolve

        p "I love you, [name]."

        return
