casino_fail = 0
def main():
    import random
    import sys
    import time
    import main
    import string
    import os
    
    
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    GRAY = '\033[90m'
    BLACK = '\033[30m'
    WHITE_BACKGROUND = '\033[47m'
    
    def fail():
        print(f"{RED}{BOLD}FAIL!{RESET} ")
        global casino_fail
        casino_fail += 1
    # Establish game starting values
    player_suites = list()
    player_total = list()
    dealer_suites = list()
    dealer_total = list()
    drawn_cards = list()
    money = 25000
    victory = False
    loses = 0
    rig = False
    fail_count = 0
    
    # Choosing which game to play
    
        
    # Resetting card values and creating space
    def renew():
        print('')
        print('')
        player_total.clear()
        player_suites.clear()
        dealer_total.clear()
        dealer_suites.clear()
        drawn_cards.clear()
    
    # Erasing the line above
    def erase_cards(num_lines):
        for _ in range(num_lines):
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            
    
    # Generating cards & their suit
    def generate_cards(total_cards, suites, person):
        if rig == True and person == 'Player':
            if 21 - sum(total_cards) <= 10:
                card_value = 21-sum(total_cards)
            else:
                card_value = random.randint(1, 13)
        else:    
            card_value = random.randint(1, 13)
        suit = random.randint(1, 4)
        card_index = card_value * suit
        while card_index in drawn_cards:
            card_value = random.randint(1, 13)
            suit = random.randint(1, 4)
            card_index = card_value * suit
        if card_value > 10:
            card_value = 10
        total_cards.append(card_value)
        suites.append(suit)
        drawn_cards.append(card_index)
        
    # Displaying cards & their suit
    def display_cards(total_cards, suites):
        for i in range(len(total_cards)):
            symbols = {1:f"{RED}♦{RESET}", 2:f"{GRAY}♣{RESET}", 3:f"{RED}♥{RESET}", 4:f"{GRAY}♠{RESET}"}
            spacing = str(" " * i)
            blank = "  "
            if total_cards[i] == 10: blank = " "
            print(spacing + " ---- \n" + spacing + "|" + str(total_cards[i]) + blank + str(symbols[suites[i]]) + "|")
        print(spacing + "|" + '    ' + "|\n" + spacing + "|" + '    ' + "|")
        print(spacing + " ---- ")
    # Ending conditions
    def end(win):
        # Round win/loss overview
        if win == 2:
            print('No one won anything this round!')
        elif win == 1:
            print('You have won $' + str(bet) + ' this round!')
        else:
            
            print(f'You have lost ${bet} this round!')
           
        
        # All-time win/loss overview
        dealer_profit = 25000 - money
        player_profit = money - 25000
        if dealer_profit > 0:
            print('You have lost $' + str(dealer_profit) + ' to the house.')
            
        elif dealer_profit == 0:
            print("You haven't won or lost anything.")
            
        else:
            print('You have made $' + str(player_profit) + '!')
        
        # Death message and program exit
        death_message = random.randint(0, 2)
        if money < 1:
            print('')
            if death_message == 0:
                print("You've lost everything!!")
                
            elif death_message == 1:
                print('You gambled it all away, and the muscle man threw you out.')
            
            else:
                print("The house always wins...")
            fail()
            print('Well you have to restart anyway, so here play again.\n\n\n')
        
    while True:
        while True:
            # Victory parameter, out of end() due to local variable issues
            if money > 99999 and victory == False:

                print('')
                print("You've beat the odds, with some skill and a lot of luck. Let's see how much further you can go!")
                break
            elif money < 1:
                break
            
            renew()
            # Money overview and betting interaction
            print('Money: $' + str(money))
            bet = input('How much would you like to bet? ')
            while True:
                try:
                    if str.lower(bet) == 'all':
                        bet = money
                    else:
                        bet = int(bet)
                    break
                        
                except:
                    bet = input('Invalid Input: ')
    
            if bet > money: bet = money
            print('Your bet is $' + str(bet))
            print('Your cards:')
            # Generate starting card
            generate_cards(player_total, player_suites, 'Player')
            display_cards(player_total, player_suites)
            
            # Hit or stand prompt
            playerIn = str.lower(input('Would you like to hit or stand? '))
            ERASE_LINE = "\033[1A\033[K"
            sys.stdout.write(ERASE_LINE)
            sys.stdout.flush()
            
            # Next card generation & display + erasing duplicate lines
            while playerIn == 'hit':
                erase_cards((len(player_total)*2)+3)
                generate_cards(player_total, player_suites, 'Player')
                display_cards(player_total, player_suites)
                
                # Player bust
                if sum(player_total) > 21:
                    print('Your total ' + str(sum(player_total)))
                    print("Bust\n")
                    money = money - bet
                    playerIn = 'cont'
                    end(0)
                    continue
                
                # PLayer Blackjack
                if sum(player_total) == 21:
                    playerIn = 'stand'
                # Hit or stand prompt
                else: 
                    ERASE_LINE = "\033[1A\033[K"
                    playerIn = input('Would you like to hit or stand? ')
                    sys.stdout.write(ERASE_LINE)
                    sys.stdout.flush()
            if playerIn == 'cont':
                continue
            
            # Dealer interaction, card generation, & display
            print('Your total is ' + str(sum(player_total)))
            print('Dealer cards:')
            
            # Generates dealer's cards
            time.sleep(1)
            while sum(dealer_total) < sum(player_total):
                generate_cards(dealer_total, dealer_suites, 'Dealer')
                display_cards(dealer_total, dealer_suites)
                time.sleep(1)
                if sum(dealer_total) < sum(player_total):
                    erase_cards((len(dealer_total)*2)+3)
        
        
            print('Dealer total is ' + str(sum(dealer_total)))
            print('')
            
            # Dealer bust
            if sum(dealer_total) > 21:
                print('Dealer bust, you win!\n')
                money = money + bet
                end(1)
                continue
                
            # Player victory
            if sum(player_total) > sum(dealer_total):
                print('You win!\n')
                money = money + bet
                end(1)
                continue
            # Tie
            if sum(player_total) == sum(dealer_total):
                print('Tie!\n')
                end(2)
                continue
            
            # Dealer victory
            else:
                print('Dealer wins \n')
                money = money - bet
                end(0)
                continue
        if money > 99999:    
            ans = input('Do you want to keep playing? (y/n): ')
            #while ans.lower() != 'y' and ans.lower() != 'n':
           
            if ans.lower() == 'y':
                pass
            elif ans.lower() == 'n': 
                return casino_fail
            else:
                print("I don't know what you said so I am just restarting the game for you")
        loses += 1
        if loses == 1:
            rig = True
        money = 25000
        
        
        
    return casino_fail