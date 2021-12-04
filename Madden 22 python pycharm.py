"""Python based fantasy football game"""
__author__ = "Khang Phan"
import time
import random
import os
import sys


def yay():
    """ defining the function "yay" as an option to respond to a yes input"""
    print("Great! Let's get started then shall we?")
    # command to print out "Great! let's get started shall we?"


def nay():
    """ defining the function "yay" as an option to respond to a no input"""
    print('"OK YOU LITTLE BABY GO CRY TO YOUR MAMA THEN!"')
    time.sleep(1.75)
    exit()

    return name, twitter_name


def greet_menu():
    """greeting menu to pick if the user want to enter the program"""
    print("1. Yes,I'm all in")
    print("2. No, I'm too scared...")


def first_menu():
    """This function is a menu to select the quarterbacks"""
    print("+ Who do you wish to be your QB1? (enter a SINGLE UPPER-CASE"
          "LETTER only)")
    time.sleep(2)
    print("A. Russell Wilson")
    print("B. Tom Brady")
    print("C. Aaron Rodgers")
    print("D. Pat Mahomes")
    print("X. Trevor Lawrence")


def second_menu():
    """This function is a menu to select the wide receivers"""
    print("+ So who would you like to select for your starting wide-receiver?"
          " (enter a SINGLE UPPER-CASE LETTER only)")
    time.sleep(2)
    print("A. Tyreek Hill")
    print("B. Devante Adams")
    print("C. DeAndre Hopkins")
    print("D. D.K. Metcalf")
    print("X. Odell Beckham Jr.")


def third_menu():
    """This function is a menu to select the running backs"""
    print("+ Who would you pick if you want to run the ball, your running "
          "back? (enter a SINGLE UPPER-CASE LETTER only)")
    time.sleep(2)
    print("A. Christian McCaffrey")
    print("B. Derrick Henry")
    print("C. Dalvin Cook")
    print("D. Alvin Kamara")
    print("X. Saquon Barkley")


def fourth_menu():
    """This function is a menu to select the tight ends"""
    print("+ Which of these following Tight Ends that you would like for "
          "your team (enter a SINGLE UPPER-CASE LETTER only)")
    time.sleep(2)
    print("A. Travis Kelce")
    print("B. George Kittle")
    print("C. Mark Andrews")
    print("D. Rob Gronkowski")
    print("X. Kyle Pitts")


def fifth_menu():
    """This function is a menu to select the defense"""
    print("+ So which of these brick walls would you like to select?")
    time.sleep(2)
    print("A. Rams' defense")
    print("B. Packers' defense")
    print("C. Steelers' defense")
    print("D. Patriots' defense")
    print("X. 85-86 Bears' defense")


def coach_selection():
    """This function is a menu to select the coaches"""
    print("+ Who would you like to be the head coach of your franchise?")
    time.sleep(2)
    print("A. Mike Tomlin")
    print("B. Pete Caroll")
    print("C. Bill Belichich")
    print("D. Andy Reid")
    print("X. John Madden")


def goat_talk():
    """A menu with two basketball players for the debate of the greatest of
    all time """
    print("Sort of off topic, but who do you think is the G.O.A.T of "
          "basketball?")
    time.sleep(2)
    print("A. Lebron James")
    print("B. Michael Jordan")

# def clutch_moment():
#    """ this function is a mini-game that could potentially determine the
#    outcome of the result, it is not implemented into the program since the
#    result is determined by the team average, will find a way to implement
#    in the future."""
#    print("X. Passing play \nO. Run it!")

#    selection = input("Enter a choice (CAPITAL LETTERS only): ")
#    while selection != "X" and selection != "O":
#        print("Invalid input, please choose again.")
#        selection = input("Enter a choice: ")

#    if selection == "X":
#        print("You have decided to go with a passing play.")
#        if qb_rating >= 88 and wr_rating >= 90:
#            print(qb, "threw a tight spiral to", wr,
#                  ", who lost his man and cut towards the corner of the "
#                  "endzone.")
#            print("What a dime by", qb, ".", wr, just completed a
#            one-handed catch and dragged his feet in "
#                  "the endzone for a massive touch down for your team.")
#           team_average += 3
#        else:
#           print(qb, "decided to call his own passing play. He threw it "
#                      "towards", wr,"that has a defender on him. The throw "
#                      "was short. \nThe defender intercepted the ball for a "
#                      "pick-six to win  the game for the opponent's team. "
#                      "What a poor execution coming from your team.")
#            team_average -= 3
#    if selection == "O":
#        print("You decided to go with a running play")
#        if rb_rating >= 90:
#            print(rb , "plowed through opponent's intimidating defense for "
#                       "the touchdown and won the game for the", city_name,
#                  team_name + ".")
#            team_average += 3
#        else:
#            print("The running-back got tackled right away after receiving "
#                  "that ball. Your team turned it over on downs. "
#                  "\nWhat a terrible effort from the guys.")
#            team_average -= 3


def product_of(a, b):
    """this function contains a parameter to calculate the rating of the
    opponent."""
    product = a * b
    return product
# * operator
# function parameter


def main():
    """ This function import everything under a single "main" function"""
    print("Hello, \nWelcome to Madden 22 Python Edition")
    name = (input("First, please enter your full name? \n"))
    twitter_name = (input("What do you want your social media "
                          "@ to be? \n"))
    print("Hi " + name + ", you're going to be the General Manager of "
          "your new NFL team and potentially bring your team to the Super "
          "Bowl with your strategic mind. \nAre you up for the challenge?")
# How to make menu tutorial https://www.youtube.com/watch?v=63nw00JqHo0&t=273s
    # Easter Eggs IDK
    greet_menu()
    selection = input("Enter a choice: ")
    while selection != "1" and selection != "2":
        print("You know how to read right?")
        selection = input("Enter an option between 1 or 2: ")
    if selection == "1":
        yay()
    elif selection == "2":
        nay()
    time.sleep(1.5)
    city_name = str(input("+ Now, what city would you like to build your "
                          "stadium in? \n"))
    team_name = str(input("+ What would you like to name your franchise? \n"))
    time.sleep(1.25)
    print("You're rocking with the " + city_name, team_name, sep=" ")
    time.sleep(1)
    # to print with combined strings and string variables
    # sep= formatting
    print("Remember, obtaining the 1st overall draft is less likely than "
          "getting an A in one of your classes", end=". ")
    # end= formatting
    time.sleep(1.5)
    print("Your selection may propel your team to being a contender or set "
          "you back for years and destroy your reputation as an organization.")
    time.sleep(3)
    print("So choooose wisely!")
    time.sleep(2)
    print('"Quarterbacks are like the minds and the hearts of football teams',
          end=". ")
    print('They are your captain', end=". ")
    print(
        'Choosing someone to sail your boat is a hard decision, but it will '
        'be worth it with a exemplary captain."')
    time.sleep(4)
    first_menu()
    # quarterback menu

    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" \
            and selection != "D" and selection != "X":
        print("Invalid input, please choose again.")
        selection = input("Enter a choice: ")
    # while loop and !=

    if selection == "A":
        print('Commissioner: "With the 1st pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the quarterback '
              'out of the University of Wisconsin, Russell Wilson."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Wilson is an accurate passer. He is a very '
              'mechanical quarterback who is consistent in his drop step '
              'and thoroughly understands how to move within the pocket and '
              'evade when the pocket collapses. He is an athlete and can '
              'torque his body to make any sort of throw on the run, and '
              'is accurate in this setting. He is a born signal caller '
              'who shows command of the offense. He has the arm strength '
              'to make the deep throws and the touch to put it on a receiver '
              'in stride. He is effective when scrambling and is a classic '
              'play extender although height will be his biggest inhibitor '
              'at the next level and the largest reason for his late-round '
              'value. It remains to be seen if he can throw effectively '
              'from the pocket at the next level."')
        qb_rating = 94
        qb = "Russell Wilson"
    # set qb value and name
    # if elif statements
    elif selection == "B":
        print('Announcer: "With the 1st pick of the 2022 NFL Draft, the ' +
              city_name, team_name + ' has selected the quarterback out of '
                                     'the University of Michigan, Tom Brady."')
        time.sleep(3)
        print('Reporter: "Brady measured 6-4.3, 211 pounds at the NFL '
              'scouting combine with a 5.24-second 40-yard dash and a '
              'vertical jump of 24 ½ inches.There were 15 offensive lineman '
              'at that combine that both ran faster and jumped higher than '
              'Brady.Scouts ranked Brady as the seventh quarterback on his '
              'draft board, a sixth-round value."')
        qb_rating = 90
        qb = "Tom Brady"

    elif selection == "C":
        print('Commissioner: "With the 1st pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the quarterback '
              'out of the University of California Berkley, Aaron Rodgers.')
        print(" ")
        time.sleep(3)
        print('Reporter: "He has outstanding arm strength. Has one of the '
              'strongest arms in the quarterback class of this year. Shows '
              'the ability to make all the necessary throws in the NFL. '
              'Has great zip on his deep out route and shows the ability to '
              'fit the ball into tight spots. He has terrific fundamentals '
              'and mechanics. Also has very good touch and timing. Shows the '
              'consistent ability to lay the ball in between the linebackers'
              ' and safeties in coverage. Impressive deep accuracy. '
              'Will also show the ability to take some velocity off of his '
              'underneath throws. He is poised in the pocket and is not '
              'afraid to wait until the last possible second to deliver the '
              'ball while taking a blow. He gets set quickly and does a fine '
              'job of seeing the entire field. His ability to make progression'
              'reads and look off receivers has improved greatly to the point'
              ' where he is among the elite in this class in those facets. '
              'He has terrific awareness in the pocket. Lacks prototypical '
              'quarterback size. He shows adequate quickness in the pocket '
              'and the ability to buy many second chances with his awareness '
              'and feet. Is a tough quarterback with good leadership skills '
              'and no character concerns. Coaches speak very highly of him in '
              'terms of his character and work ethic."')
        qb_rating = 86
        qb = "Aaron Rodgers"

    elif selection == "D":
        print('Commissioner: "With the 1st pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the quarterback'
              'out of Texas Tech Univerity, Patrick Mahomes.')
        print(" ")
        time.sleep(3)
        print('Reporter: "Mahomes broke onto the field as a freshman and '
              'completed 57 percent of his passes for 1,547 yards with 16 '
              'touchdowns and four interceptions. He made a big jump as a '
              'sophomore when he was the full-time starter, completing '
              '64 percent for 4,653 yards with 36 touchdowns and 15 '
              'interceptions."')
        qb_rating = 90
        qb = "Patrick Mahomes"

    elif selection == "X":
        print('Commisioner: "With the 1st pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the quarterback '
              'out of Clemson University, Trevor Lawrence."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Lawrence, 21, is one of the most prized quarterback '
              'prospects in history. He was rated as the sixth-best recruit in'
              ' college football history by 247Sports when he came out of '
              'Cartersville High School in Georgia, and he had no trouble '
              'living up to those sky-high expectations at Clemson. '
              'The 2020 ACC Player of the Year completed 66.6 percent of '
              'his throws for 10,098 yards with 90 touchdowns and 17 '
              'interceptions across 40 appearances for the Tigers. He added '
              '943 rushing yards and 18 scores on the ground to further '
              'establish himself as the top choice in a star-studded QB '
              'class."')
        time.sleep(3)
        print('" Hmm...." \n"I see that you prefer a new school approach to '
              'things instead of an established veteran QB." \n"Though it was '
              'not a bad choice, he could developed into a superstar!"')
        qb_rating = 79
        qb = "Trevor Lawrence"

    time.sleep(2)

    time.sleep(3.5)
    print("NICE!")
    time.sleep(2)
    print("You got your starting quarterback.")
    time.sleep(.75)
    print("It's pretty useless for the quarterback to throw the ball to no "
          "one right?")
    time.sleep(1.5)
    second_menu()
    # widereceiver menu
    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" and \
            selection != "D" and selection != "X":
        print("Invalid input, please choose again.")
        selection = input("Enter a choice: ")

    if selection == "A":
        print('Commissioner: "With the 2nd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the '
              'wide-receiver out of the University of West Alabama, '
              'Tyreek Hill."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Standing in at 5-foot-9, 185 pounds, Hill was '
              'originally a running back. He got kicked off the team at '
              'Oklahoma State after being charged with domestic violence, '
              'ending up at Division II West Alabama. He is under-sized '
              'in the Tavon Austin mold. He will start out on special teams '
              'in ' + city_name + ' if he can crack the 53-man roster."')
        wr_rating = 96
        wr = "Tyreek Hill"

    elif selection == "B":
        print('Commissioner: "With the 2nd pick of the 2022 NFL Draft, the ' +
              city_name, team_name + ' has selected the wide-receiver out of '
              'California State University Fresno, Devante Adams.')
        print(" ")
        time.sleep(3)
        print('Reporter: "The most prolific passing duo in college football '
              'last season was featured by Fresno State with Adams and '
              'quarterback Derek Carr. Over the past two seasons, this '
              'tandem put up video-game totals with a ton of points for '
              'the Fresno State offense.Adams made a big impact as a redshirt '
              'freshman in 2012, catching 102 passes for 1,312 yards with 14 '
              'touchdowns.He and Carr worked very well together as they '
              'carved up defenses."')
        wr_rating = 99
        wr = "Devante Adams"

    elif selection == "C":
        print('Commissioner: With the 2nd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the '
              'wide-receiver out of Clemson University, DeAndre Hopkins."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Over the past couple of seasons, Clemson has '
              'featured one of the most high-powered offenses in college '
              'football. Quarterback Tajh Boyd has produced some big point '
              'totals and Hopkins was one of his best weapons.Hopkins made '
              'a quick impact for the Tigers. He hauled in 52 passes for '
              '637 yards with four scores as a freshman in 2010. Hopkins '
              'was a secondary receiver to Sammy Watkins in 2011, but Hopkins '
              'still caught 72 passes for 978 yards and five touchdowns. '
              'The Clemson offense spread the ball around to a variety of '
              'play-makers like tight end Dwayne Allen and running back '
              'Andre Ellington."')
        wr_rating = 94
        wr = "DeAndre Hopkins"

    elif selection == "D":
        print('Commissioner: "With the 2nd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the '
              'wide-receiver out of the Univerity of Mississippi, '
              'D.K. Metcalf."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Even though Metcalf is an incredible physical '
              'talent he did not catch a lot of passes during his collegiate'
              ' career. He played in 21 games for Ole Miss, totaling 67 '
              'receptions for 1,228 yards and 14 touchdowns. As a freshman, '
              'Metcalf played in two games, catching two passes for 13 yards'
              ' and two touchdowns. The 2017 season was the only year he '
              'played in 12 games, hauling in 39 passes for 346 yards and '
              'seven scores. In 2018, Metcalf went out for the year with a '
              'neck injury after seven games. Prior to that, he was playing '
              'well, exploiting a lot of man coverage with teams focused on '
              'stopping A.J. Brown. In his final season, Metcalf totaled 26 '
              'receptions for 569 yards and five touchdowns."')
        wr_rating = 90
        wr = "D.K. Metcalf"

    elif selection == "X":
        print('Commissioner: "With the 2nd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the '
              'wide-receiver out of Louisiana State University, Odell Beckham '
              'Jr."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Beckham has the speed to stretch the field and has '
              'demonstrated the potential to make game-changing plays. '
              'Beckham is extremely fast and he uses that to constantly gain'
              ' separation from defensive backs. He has enough size to '
              'line up on the outside and can burn corner-backs on go routes '
              'running down the field. Beckham also is fast enough to burn '
              'double coverage with safety help over the top. He good hands '
              'and is a gritty player. With his elite speed, Beckham earned '
              'playing time as a true freshman when he caught 41 passes'
              ' for 475 yards and two touchdowns. As a sophomore, Beckham led'
              ' LSU in receiving with 713 yards on 43 catches and two '
              'touchdowns. He averaged 9.1 yards per punt return."')
        time.sleep(3)
        print('"Alright, alright..."')
        time.sleep(1.5)
        print('"You are picking the guy who wears a $400,000 Patek watch '
              'during a football game."')
        time.sleep(2)
        print('"I guess you are the kind of person who considers flashiness '
              'as a big factor in football."')
        time.sleep(1)
        print("But you have not watch football for a long time, haven't you?")
        wr_rating = 88
        wr = "Odell Beckham Jr."
    else:
        print(" ")
    time.sleep(2.5)
    print('"That was a wise choice young one."')
    time.sleep(1)
    third_menu()
    # Runningback menu
    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" and \
            selection != "D" and selection != "X":
        print("Invalid input, please choose again.")
        selection = input("Enter a choice: ")

    if selection == "A":
        print('Commissioner: "With the 3rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the running-back'
              'out of Stanford University, Christian McCaffrey."')
        print(" ")
        time.sleep(3)
        print('Reporter: "McCaffrey spent the last two season as one of the '
              'most consistent and devastating running backs in college '
              'football. In my opinion, McCaffrey should have won '
              'the 2015 Heisman Trophy because he carried Stanford while '
              'Alabamas Derrick Henry had tons of pro talent around him on '
              'both sides of the ball. Still, both players had great seasons.'
              ' McCaffrey averaged six yards per carry that season on his '
              'way 2,019 yards with eight touchdowns. As a receiver, he had '
              '45 catches for 645 yards and five scores."')
        rb_rating = 97
        rb = "Christian McCaffrey"

    elif selection == "B":
        print('Commissioner: "With the 3rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the running-back '
              'out of the University of Alabama, Derrick Henry."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Henry averaged 5.62 yards per carry (395 carries) '
              'in 2015 for 2,219 yards with 28 touchdowns with 11 receptions '
              'for 91 yards. Late in the year, he ran over opponents like '
              'Auburn, Texas A&M and LSU. Henry totaled 90 carries in his '
              'last two regular-season games. He had four games over '
              '200 yards during the regular season and was only the third '
              'back in SEC history to accomplish that."')
        rb_rating = 95
        rb = "Derrick Henry"

    elif selection == "C":
        print('Commissioner: "With the 3rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the running-back '
              'out of Florida State University, Dalvin Cook."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Cook was an impactful player for the Seminoles from '
              'his first day with the program. As a freshman, he beat out '
              'more experienced backs to be the feature runner who replaced '
              'Devonta Freeman. With Jameis Winston under center, Cook turned '
              'in an excellent true freshman season in 2014, averaging 5.9 '
              'yards per carry for 1,008 yards and eight touchdowns. He '
              'caught 22 passes for 203 yards."')
        rb_rating = 92
        rb = "Dalvin Cook"

    elif selection == "D":
        print('Commissioner: "With the 3rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the running-back '
              'out of the Univerity of Tennessee, Alvin Kamara."')
        time.sleep(3)
        print('Reporter: "Coming out of the University of Tennessee, Kamara '
              'was a polarizing prospect. He was a classic “shooting up draft '
              'boards” prospect late in the process after a stellar combine. '
              'The knocks on him were his lack of experience, ball security '
              'issues, and a perceived lack of durability. He started just '
              'eight games in college, and never as the full time number one '
              'player. He did not once get 20 carries in a college game, '
              'and had just five games with over 15 carries. He missed a '
              'few games due to injury and his smaller frame led to some '
              'worry over his durability."')
        rb_rating = 90
        rb = "Alvin Kamara"

    elif selection == "X":
        print('Commissioner: "With the 3rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the running-back '
              'out of Pennsylvania State University, Saquon Barkley."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Saquon Barkley was the Big 10 Offensive Player of '
              'the Year in each of the past two seasons (2016 and 2017) at '
              'Pennsylvania State University, after scoring a combined 45 '
              'touchdowns over those two years. In 2016, He led the FBS in '
              'broken tackles. His box score statistics in 2017 don’t really '
              'tell an accurate story in favor of Barkley, as teams devoted '
              'their entire defensive game plans to selling out to stop the '
              'run, and forcing Penn State to beat them in literally any '
              'other way besides handing the ball to Barkley. Yet he still '
              'finished with the 5th-most total touchdowns (23) in the FBS '
              'last year. He was the only player in the nation to score at '
              'least 18 rushing touchdowns on less than 220 carries; in other'
              ' words: he averaged almost 1.4 touchdowns per game despite '
              'carrying the ball less than 18 times per game."')
        time.sleep(2.5)
        print('"You probably call him "Saquad" and never miss a leg day. '
              'But personally, I do not believe in the hype. \nYeah he is good'
              ' but he wasted his talent in purgatory of a franchise like '
              'the Giants during his prime."')
        rb_rating = 89
        rb = "Saquon Barkley"

    else:
        print("")

    time.sleep(3.5)

    print("Alright, I see you! \nThe quarterback that you draft would "
          "appreciate it if you have a big boy on your team that always "
          "shows up and has your quarterback's back.")
    time.sleep(2)
    fourth_menu()
    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" and \
            selection != "D" and selection != "X":
        print("Invalid input, please choose again.")

        selection = input("Enter a choice: ")
    if selection == "A":
        print('Commissioner: "With the 4rd pick of the 2022 NFL Draft, '
              'the' + city_name, team_name + ' has selected the tight end '
              'from the University of Cincinnati, Travis Kelce.')
        print(" ")
        time.sleep(3)
        print('Reporter: "Cincinnati senior Travis Kelce (younger brother of '
              'Eagles center, Jason Kelce) might have the most complete '
              'skill set of them all, though. A 6ft6" 260 pound sledgehammer '
              'with speed and strength. he averaged 3 catches per game for '
              '55 receiving yards -- impressive production for a tight end '
              'primarily used as a blocker. With 45 catches for 722 yards on '
              'the season, Kelce exploded in his final season. And he saved'
              ' the best for last, finishing his career at Cincinnati with'
              ' 123 receiving yards in the Belk Bowl against Duke."')
        te_rating = 99
        te = "Travis Kelce"

    elif selection == "B":
        print('Commissioner: "With the 4rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the tight end '
              'from the University of Iowa, George Kittle."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Iowa has produced some very good football players '
              'and athletes over the years, but Kittle blew the other tight '
              'ends out of the water with his testing numbers. Kittle was the'
              ' top performer in each athletic test Iowa had. '
              'He jumped 37.5” in the vertical. We’re splitting hairs,'
              ' but George actually ran a 4.51 40-yard dash during Iowa’s '
              'spring testing. He’s a freak athlete."')
        te_rating = 96
        te = te = "George Kittle"
    elif selection == "C":
        print('Commissioner: "With the 4rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the tight end '
              'from the University of Oklahoma, Mark Andrews."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Oklahoma has featured a high-scoring offense over '
              'the past few seasons with dynamic running backs and wide '
              'receivers. Andrews went under the radar to a degree as a '
              'result, but he proved to be one of the most consistent '
              'receiving tight ends in college football after breaking out '
              'with the Sooners. In 2015, Andrews totaled 19 catches for '
              '318 yards and seven touchdowns. As a sophomore, Andrews took '
              'his game to another level, totaling 31 receptions for 489 '
              'yards and seven touchdowns for the year. He was Oklahomas '
              'third leading receiver after Dede Westbrook and Joe Mixon. '
              'In 2017, the junior tight end put together his best season, '
              'catching 62 passes for 958 yards and eight touchdowns."')
        te = "Mark Andrews"
        te_rating = 88
    elif selection == "D":
        print('Commissioner: "With the 4rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the tight end '
              'from the Univerity of Arizona, Rob Gronkowski.')
        print("")
        time.sleep(3)
        print('Reporter: "Gronkowski is a very well-rounded tight end '
              'prospect and will likely come off the board in the second '
              'round, but if team doctors have very serious concerns with his'
              ' back (and some certainly should) then he could really fall '
              'in the 2010 NFL Draft. Back issues are probably the worst '
              'kind of injury for an athlete and generally these athletes '
              'have injury problems throughout their careers. Gronkowski '
              'will never be an elite tight end in the NFL, but if he stays '
              'healthy he should certainly be a productive contributor and '
              'starter."')
        te_rating = 86
        te = "Rob Gronkowski"

    elif selection == "X":
        print('Commissioner: "With the 4rd pick of the 2022 NFL Draft, '
              'the ' + city_name, team_name + ' has selected the rookie '
              'Tight End from the University of Florida, Kyle Pitts."')
        print(" ")
        time.sleep(3)
        print('Reporter: "Genetically, Kyle Pitts is an absurd athlete. '
              'Kyle Pitts measures in at 6-foot-6, 245 pounds, but he moves '
              'with the grace and the suddenness of a wide receiver, not '
              'a tight end. He has excellent change-of-direction skills, and '
              'he also shows impressive nuance with his route running.'
              'Pitts saw playing time as a true freshman for Florida,'
              ' catching three passes for 73 yards and a score. Right there, '
              'he showed a flash of his big-play ability, and in 2019, his '
              'sophomore season, he was unleashed in his entirety. His rise'
              ' coinciding with an uptick in quarterback play, Pitts became'
              ' a premier weapon in the SEC, logging 54 catches for 649 yards'
              ' and five scores.Even before attaining his draft eligibility,'
              ' Pitts had become a star on college football’s biggest stage,'
              ' and his performance in 2020 showed that he’s far from '
              'finished. Kyle Pitts 2020 season. Week in and week out in 2020,'
              ' Kyle Pitts’ presence alone unsettled defenders. Acrobatic '
              'catches and spider-like snares became expectations for the'
              ' Florida tight end, and his performance has him listed as a '
              'near consensus Top 5 prospect. Pitts produced with absurd '
              'efficiency in 2020, hauling in 43 passes for 770 yards and'
              ' 12 touchdowns."')
        te_rating = 82
        te = "Kyle Pitts"
        time.sleep(3)
        # string multiply operator
        print(" GOOOOOO GATORS!!!!" * 5)
        time.sleep(1.5)
        print("No?")
        time.sleep(1)
        print("Understandable")
        time.sleep(.5)
        print("You went with the new school approach. Pitts it's only 20 "
              "years old and is currently a rookie, but he has proven that "
              "he's worth every dime considering he was the top prospect in "
              "his class.")
        # or boolean
        if qb == "Trevor Lawrence" or te == "Kyle Pitts":
            print("I see that you were either born yesterday or just an avid "
                  "fan of recent college football.")
    else:
        print("")

    print("Hmm...? Interesting choice to say the least.")
    time.sleep(3.5)

    print('"They say that defense wins games."')
    time.sleep(1)
    fifth_menu()
    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" and \
            selection != "D" and selection != "X":
        print("Invalid input, please choose again.")
        selection = input("Enter a choice: ")

    if selection == "A":
        print("Commissioner: With the last pick of the 2022 NFL Draft, "
              "the" + city_name, team_name + " has selected the Los Angeles "
              "Rams' defense.")
        time.sleep(1)

        print("Reporter: Ranked 1st overall")
        df_rating = 95
        df = "Rams' defense"

    elif selection == "B":
        print("Commissioner: With the 4rd pick of the 2022 NFL Draft, "
              "the " + city_name, team_name + " has selected the Green Bay "
              "Packers' defense.")
        time.sleep(1)
        print("Reporter: Ranked 9th overall.")
        df_rating = 87
        df = "Packers' defense"

    elif selection == "C":
        print("Commissioner: With the 4rd pick of the 2022 NFL Draft, "
              "the " + city_name, team_name + " has selected the Pittsburgh "
              "Steelers' defense.")
        time.sleep(1)
        print("Reporter: Ranked 18th overall.")
        df_rating = 82
        df = "Steelers' defense"

    elif selection == "D":
        print("Commissioner: With the 4rd pick of the 2022 NFL Draft, "
              "the " + city_name, team_name + " has selected the New England"
              "Patriots' defense.")
        time.sleep(1)
        print("Reporter: Ranked 22nd overall.")
        df_rating = 79
        df = "Patriots' defense"

    elif selection == "X":
        print("Commissioner: With the 4rd pick of the 2022 NFL Draft, "
              "the " + city_name, team_name + " has selected the 1985-1986 "
              "Chicago Bears' defense.")
        print('Reporter: "Some may argue that this was the best defensive '
              'team to ever be assembled in NFL history."')
        df_rating = 100
        df = "85-86 Bears' defense"
        time.sleep(3)
        print('"You have unlocked a legendary defensive team, this team is the'
              ' definition of "Defense wins championships."')
        time.sleep(3)
        print('"1985-1986 Chicago Bears defense ran over their opponent to end'
              ' their regular season with a near perfect season. They then '
              'went on to win the first ever Super Bowl as a franchise."')

    else:
        print("")

    time.sleep(1)
    print('"Last but not least, good students have to have a good teacher."')
    time.sleep(1)
    print(" ")
    print('"Having a quality coaching staff is perhaps the more important '
          'aspect of football."')
    time.sleep(2)
    coach_selection()

    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B" and selection != "C" and \
            selection != "D" and selection != "X":
        print("Invalid input, please choose again.")
        selection = input("Enter a choice: ")

    if selection == "A":
        print("The " + city_name, team_name + " have selected Mike Tomlin to "
              "be their head coach this season")
        time.sleep(1)
        print("Mike Tomlin was the head coach for the Pittsburgh Steelers "
              "last season")
        hc_rating = 86
        hc = "Mike Tomlin"
    elif selection == "B":
        print("The " + city_name, team_name + " have selected Pete Carroll to "
              "be their head coach this season")
        time.sleep(1)
        print("Pete Carroll was the head coach for the Seattle Seahawks "
              "last season")
        hc_rating = 91
        hc = "Pete Carroll"

    elif selection == "C":
        print("The " + city_name, team_name, "have selected Bill Belichich to "
              "be their head coach this season")
        time.sleep(1)
        print("Bill Belichich was the head coach for the New England Patriots"
              "last season")
        hc_rating = 95
        hc = "Bill Belichich"
    elif selection == "D":
        print("The " + city_name, team_name + " have selected Andy Reid to be "
              "their head coach this season")
        time.sleep(1)
        print("Mike Tomlin was the head coach for the San Francisco 49ers "
              "last season")
        hc_rating = 93
        hc = "Andy Reid"

    elif selection == "X":
        print("The " + city_name, team_name + " have selected John Madden to "
              "be their head coach this season")
        time.sleep(2)
        print('You have selected a legendary coach. As you can tell by the '
              'name, he is the reason why the video games franchise '
              '"Madden NFL 22" is a thing today. A moment of silence to '
              'remember John Madden, a one of a kind coach...')
        hc_rating = int(10 ** 2)
        hc = "John Madden"
    else:
        print(" ")
    # **operator, John Madden is a 100 points overall coach.
    time.sleep(2)
    print("....")
    print(" ")
    time.sleep(2)
    print("The " + city_name, team_name + " have finalized their roster with "
          "the following players for the following NFL season: ")
    time.sleep(1)
    print(" ")
    print("Quarterback   : {}".format(qb))
    time.sleep(1)
    print("Wide-receiver : {}".format(wr))
    time.sleep(1)
    print("Running-back  : {} ".format(rb))
    time.sleep(1)
    print("Tight-end     : {}".format(te))
    time.sleep(1)
    print("Defensive Team: {}".format(df))
    time.sleep(1.5)
    print("HEAD COACH    : {}".format(hc))
    combined = (qb_rating + wr_rating + rb_rating + te_rating + df_rating +
                hc_rating)
    team_average = int(combined / 6)
    # /operator, team_average is the user's team's rating (the average of
    # every personnel)
    string_team_average = str(team_average)
    print("Your team has overall rating of: " + string_team_average)
    other_team = product_of(13, 7)
    # passing the function product_of() parameter from  above
    # * operator, the rating of the opponent is 91
    time.sleep(3)
    print(" ")
    time.sleep(1)
    print("Your team is all set and ready for the new season.")
    time.sleep(2)
    print("Your team is going to the Super Bowl with a regular season record "
          "of 15-2.")
    time.sleep(2)
    print("The Super Bowl is here.")
    time.sleep(2)
    print("Your team is matching up against the Dallas Cowboys.")
    time.sleep(2)
    print("Things changed for them after picking up a savior of a rookie "
          "quarterback that led them to the Super Bowl.")
    time.sleep(3)
    print(" ")
    print('"Answering the following below will let your team successfully '
          'intimidate the opponent and outsmart them"')
    time.sleep(2)
    goat_talk()
    time.sleep(1)
    selection = input("Enter a choice: ")
    while selection != "A" and selection != "B":
        print("Invalid choice, please chose again")
        selection = input("Enter a choice: ")
    if selection == "A":
        time.sleep(1)
        print('"Heyyyo, you do have a good sports knowledge, '
              'you deserve this!"')
        bonus = int(14 % 4)
        # modulus operator is 2 points
        final_vs_rating = int(other_team - bonus)
        # subtraction operator reduce opponent team's rating by 2
    elif selection == "B":
        print("All of a sudden, you have the urge to tweet about this...\n ")
        time.sleep
        print(name + " ✔")
        print("@" + twitter_name)
        print("                        ")
        time.sleep(1)
        tweet = "@kingjames @NBA Idc what anybody else says. It's time " \
                "to end the #GOAT debate. IMO it's MJ tbh. \n#lastdance " \
                "#airness #6rings #96bullsftw"
        # for in command
        for char in tweet:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)
        time.sleep(1)
        print("                                                              ")
        print("\n        ccat 10:26 p.m. - 21 Sep 2021     Twitter for Python")
        print("______________________________________________________________")
        print("    3,253 Retweets      10.1k Likes      1,234 Comments       ")
        print("--------------------------------------------------------------")
        print(" ")
        print(" ")
        time.sleep(3)
        print('"Wow, you really are an old head. No wonder why your resume '
              'is so vast. To win you can not live in the past"')
        print(" ")
        time.sleep(2)
        print(" ")
        print('"The opposition team thinks that your tweet is a joke and '
              'unprofessional, and now your legitimacy is going down..."')
        final_vs_rating = int(other_team // .989)
        # type writing effect https://www.youtube.com/watch?v=2h8e0tXHfk0
    else:
        print("What are you a Kobe fan?")
        time.sleep(1)
        time.sleep(2)
        print(" ")
        print(" ")
    time.sleep(2)
    print(" ")
    print("The opponent's team ended the regular season with the record of "
          "13-4 with a", final_vs_rating, "OVR TEAM RATING.")
    print(" ")
    time.sleep(1)
    print('You are required to toss a coin to decide who is receiving. '
          '"heads" or "tail"? (Please enter in lower case.)')
    # coin flip simulator helped by Jakeb Brown
    pick = str(input())
    opponents_pick = 0
    heads = 0
    tails = 1
    for i in range(1):
        # for-in iterative structures
        result = random.randint(0, 1)
        time.sleep(1)
        if result == 0:
            print("heads")
            result = "heads"
        elif result == 1:
            print("tails")
            result = "tails"
        if pick == "heads":
            opponents_pick = "tails"
        elif pick == "tails":
            opponents_pick = "heads"
    if result == pick:
        print("You won the coin toss, you are receiving the ball.")
        final_vs_rating -= 1
    # shortcut operator
    # not boolean loop
    elif not result == pick:
        print("You lost the coin toss, you are kicking off")
        team_average -= 1
    time.sleep(.2)
    print("COMPUTING MATCH RESULT...")
    time.sleep(.5)
    print("PLEASE WAIT...")
    time.sleep(3)
    # if-else statement
    # > operator
    if team_average < int(final_vs_rating):
        print("Unfortunately, they were too strong for your team.")
        time.sleep(2)
        print(" ")
        print("Under the management of head coach " + hc + ", " + qb + " had "
              "a rough night completing passes to his receiver. " + te + ""
              "looked sluggish out there like he's out of shape. " + rb + "" 
              "went -23 yards tonight. It's a tough night for the " +
              city_name, team_name)
        time.sleep(3)
        print("The Dallas Cowboys have beaten the " + city_name, team_name +
              " 21-13 in the Superbowl.")
        time.sleep(2)
        print(" ")
        print("You've missed out on the Super Bowl LIII Title. \nBut hey, "
              "they're always next year. \nBetter luck next time!")
    else:
        print("Congratulations!!!!!, the Lombardy Trophy has belonged to"
              "" + name + " and the " + city_name, team_name + ".")
        time.sleep(2)
        print(" ")
        print("Under the leadership of head coach " + hc + ", " + qb + " had"
              " an amazing night completing 23 out of 28 passes with 3 of "
              "them resulting in touchdowns. \nOn the other end, " + te + ""
              " and " + wr + " have a combined 3 touchdowns. " + rb + " has a"
              " total of 126 rushing yards.")
        time.sleep(3)
        print("It was a hard fought battle but your team came out on top "
              "beating the opponent 23-7.")
        time.sleep(2)
        print(" ")
        print("WOOOOOOO!!!!!, LET'S POP THE CHAMPAGNE")
        print(" ")
    time.sleep(5)
    print("HIGH SCORE")
    time.sleep(.5)
    print("-Khang Phan: 100")
    time.sleep(.5)
    print("-Tim Tebow : 98")
    time.sleep(.5)
    print("-Joe Burreaux: 89")
    time.sleep(.5)
    print("-" + name + ":", team_average)

    print("------------------")
    time.sleep(2.25)
    print("CREDIT: ")
    print("DEVELOPED BY KHANG PHAN STUDIOS Copyrighted 2021. All rights "
          "reserved to Phan Studios, 2021 \nPhan Studios, a division of "
          "Electronic Arts. TM")
    print("version 3.0 ")
    print('          ______|_______________________________________________|__'
          '___            ')
    time.sleep(.1)
    print('          |     |""1|0""2|0""3|0""4|0""5|0""4|0""3|0""2|0""1|0""|  '
          '   |           ')
    time.sleep(.1)
    print('          |  +  |   |    |    |    |    |    |    |    |    |   |* '
          '   |           ')
    time.sleep(.1)
    print('          |     |   |    |    |    |    |    |    |    |    |   |  '
          '   |           ')
    time.sleep(.1)
    print('          |+    |   |    |    |    |    |    |    |    |    |   |* '
          ' * |           ')
    time.sleep(.1)
    print('          |  T  |   |    |    |    |    |    |    |    |    |   |  '
          'T  |           ')
    time.sleep(.1)
    print('          |  O  |   |    |    |    |    |    |    |    |    |   |  '
          'O  |           ')
    time.sleep(.1)
    print('          |  U +|"" | "" | "" | "" | "" | "" | "" | "" | "" | ""|  '
          'U  |           ')
    time.sleep(.1)
    print('====||    |  C  |   |    |    |    |    |    |    |    |    |   |  '
          'C  |     ||====')
    time.sleep(.1)
    print('    ||____|  H  |   |    |    |    |    |    |    |    |    |   |  '
          'H  |_____||    ')
    time.sleep(.1)
    print('    |=====|     |   |    |    |    |    |    |    |    |    |   |  '
          '   |=====||    ')
    time.sleep(.1)
    print('====||    |  D  |"" | "" | "" | "" | "" | "" | "" | "" | "" |   |  '
          'D  |     ||====')
    time.sleep(.1)
    print('          |  O  |   |    |    |    |    |    |    |    |    |   |  '
          'O  |           ')
    time.sleep(.1)
    print('          |  W  |   |    |    |    |    |    |    |    |    |   |  '
          'W  |           ')
    time.sleep(.1)
    print('          |  N  |   |    |    |    |    |    |    |    |    |   |* '
          'N  |           ')
    time.sleep(.1)
    print('          |     |   |    |    |    |    |    |    |    |    |   |  '
          '   |           ')
    time.sleep(.1)
    print('          |  +  |   |    |    |    |    |    |    |    |    |   |  '
          ' * |           ')
    time.sleep(.1)
    print('          |+   +|""1|0""2|0""3|0""4|0""5|0""4|0""3|0""2|0""1|0""|* '
          '   |           ')
    time.sleep(.1)
    print('          |_____|___|____|____|____|____|____|____|____|____|___|__'
          '___|           ')
    time.sleep(.1)
    print('          ========================================================='
          '====           ')
    time.sleep(6)


# run everything from main function helped by Andrew Krupp
main()
exit()
