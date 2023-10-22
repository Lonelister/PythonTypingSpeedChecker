import time
from colorama import Fore, Style

# Zdefiniuj poziomy trudności i plik CustomLevel.txt
difficulty_levels = {
    "Challenges": {
        "Runner": "A long sentence is a sentence that has a lot of words and is difficult to understand. Often such sentences are unnecessarily complicated and unclear. Therefore, it is important to write short and concise sentences that are easy to read and understand.",
        "Jumper": "In an imaginary world, there seemed to be a unique cinema in which every apple became carcinogenic during screening. This cinematic impact was a source of constant anxiety and fascination among the audience. The problem of understanding this phenomenal issue of the piece remained unresolved due to the difficult phonetic difference in the description of the phenomenon. The characterisation of the character who discovered the secret of this unusual cinematography became the key to exploring the mysterious phenomenon.",
        "Amateur": "In a small garden, a rose blossom was in full bloom, attracting a bee who paid homage to it. It was a story of love and longing between them, but sadly loss came when a sudden change in the weather destroyed their paradisiacal nook. However, life had another chapter planned, which brought a return to a loved one. Together they went through difficulties and in the end lived happily ever after.",
        "Threadripper": "In the not-so-distant Cockroach Valley, where life was lived on the edge of poverty and abundance, there was an emerald pit about which many legends circulated. In this tiny community, where every position seemed above board and every inhabitant had their own irreplaceable place, the concept of luxury had a slightly different meaning. It was in the Cockroach Valley that a Chicago plumber, a man of extraordinary skill, found his way here in search of new challenges. For a long time, the Emerald Pit was merely a place of legends and stories, and its doors remained locked forever. But when a Chicago plumber decided to change his life and take on the challenge of repairing plumbing in this extraordinary valley, the huge doors of this mysterious place stood before him. It was a turning point that changed the life not only of the plumber, but of the entire cockroach valley. This is the story of the incredible transformation that began with the opening of that huge door.",
        "Librarian": "The bear was visible in the forest, and he knew how to break effectively. She read the lead story in the newspaper, while the knight night was dark and full of terrors. I saw a great grate in the kitchen, and the principal of the school is highly respected. She could not accept the dessert desert, so the band played their new song on the beach. He passed the ball to his teammate, and the wind made the sail a great success. Can you write with your left hand? She wears her hair in a bun as a hare leaped across the meadow. The peace piece of art was breathtaking, and he knew the flower was a key ingredient in baking."
    },
    "Learn": {
        "F & J Position": "FFF JJJ FJF JFJ FFJ JJF FFF JJF JJJ FFJ JFF FJJ F J FJ JF JFJJF FJFFJ",
        "QAZ & WSX Training": "WAS QAZ ASX WAX ZAW ZAQ SAQ SAW SAX WAD WSD WSX XSD XDD SSD ASD ADD ADX XAD DXD",
        "EDC, RFV & TGB Training": "ERT TVG RTV GED GDC DCG DEC DEG TEG TDG TGF FER DER FER TRE DRE GRE TRT TGR GER RET",
        "UIOP & HJKL Training": "UIOP HJKL KLHJ OIUPO HUKI PLIU HIKL UKHP HUPN KULN",
        "A-L Test": "ALL GKS FGA DAD JKA LDJ SAD JAA JSS KDD DKK JFF DKA LDM LSD",
        "Q-P Test": "QUO TIR OPE PEW WTY UWY OWP RUW ROQ TOQ TUW UWO EIW WPO RIW PRO WER IWO EIR",
        "Z-M Test": "ZMX NZN CNX VBC MZV XNX CMZ NDN ZMB CVB XBZ MXC",
        "Alphabet Test": "AAD BBO CCF DDE EED FFR GGT HHY IIK JJU KKO LLO MMK NNJ OOK PPL RRD SSZ TTG UUK YYH ZQQ",
        "Sentence Test": "Natural gas, also known as methane, is a valuable energy resource. It is odorless and colorless and comes from underground deposits. Natural gas is widely used as a fuel for heating, electricity generation and in the chemical industry. Its popularity is due to its efficiency, low environmental impact, and wide availability.",
        "Symbol Training": "1!1 2@2 3#3 4$4 5%5 6^6 7&7 8*8 9(9 0)0 T€T H£H D$D Z%Z",
        "Symbol Test": "I arrived at the party, and it was incredible! There were balloons, confetti, music, dancing, and so much food: pizza, burgers, hot dogs, tacos, sushi... you name it! Everyone was having a blast - laughing, singing, and enjoying the night. The atmosphere was electric, and I couldn't believe my eyes! It was a night I'll never forget!!! #Chillout #WTF? #FantasticParty @AlexWelsh @Fagg!rTheHero"
    },
    "Special": {
        "Low Fingers Distance Writing Errors": "TP AL JQ ZU DQ VA OX BQ PS EJ GA KD VQ OD PW EL OS",
        "Letter Misplacing": "Palm oil is a type of vegetable cooking oil extracted from the fruit of the oil palm tree. It is one of the most important vegetable oils in the world and is widely used in the food industry. Palm oil is valued for its properties such as durability and stability at high temperatures, making it often used for frying and baking. However, its production is controversial due to its negative environmental impact, particularly on rainforests and biodiversity. Organizations and consumers are highlighting the need for sustainable management of palm oil crops to reduce the negative impacts of its production. Palm oil is also present in many food products, so it is increasingly important for consumers to make informed choices and avoid products containing this ingredient.",
        "Index-Finger Writing Issue": "Maltodextrin, often used as a thickening agent in the food industry, is a starch derivative. It is one of the most commonly used compounds in the food industry due to its functional properties. Maltodextrin is usually odorless and tasteless, which allows it to be used as a carrier of flavors and aromas. However, thanks to its ability to bind water, maltodextrin is also used in the production of products such as yogurts and ice creams, which remain smooth and creamy thanks to it. It is an important ingredient in the food industry that influences the texture, consistency, and taste of many food products."
    },
}

def choose_difficulty_level():
    print("Choose the category:")
    categories = list(difficulty_levels.keys())
    for i, category in enumerate(categories, start=1):
        print(f"[{i}] {category}")

    category_choice = int(input("Enter the number of your category choice: "))
    selected_category = categories[category_choice - 1]
    print("Choose the difficulty level:")
    levels = list(difficulty_levels[selected_category].keys())
    for i, level in enumerate(levels, start=1):
        print(f"[{i}] {level}")

    level_choice = int(input("Enter the number of your level choice: "))
    return selected_category, levels[level_choice - 1]

def speed_type_checker():
    while True:
        category, difficulty_level = choose_difficulty_level()
        prompt = difficulty_levels[category][difficulty_level]
        print(f"Type the following text as fast as you can:\n{prompt}")
        input("Press Enter to start...")

        start_time = time.time()

        user_input = input("Start typing: ")

        end_time = time.time()
        elapsed_time = end_time - start_time

        correct_characters = 0
        errors = 0
        for i in range(min(len(prompt), len(user_input))):
            if prompt[i] == user_input[i]:
                correct_characters += 1
            else:
                errors += 1

        words_per_minute = (correct_characters / 5) / (elapsed_time / 60)
        accuracy = (correct_characters / len(prompt)) * 100

        print("Results:")
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Errors: {errors}")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    speed_type_checker()