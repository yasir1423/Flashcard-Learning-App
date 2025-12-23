import json
import os
#Flash cards Classes
class flashcard:
    def __init__(self,question,answer,correct=0,wrong=0):
        self.question=question
        self.answer=answer
        self.correct=correct
        self.wrong=wrong
    def to_dictionary(self):
        return{"question":self.question,"answer":self.answer,"correct":self.correct,"wrong":self.wrong}
#flashcard App class
class flashcardApp:
    def __init__(self,filename="flashcards.json"):
        self.filename=filename
        self.cards=self.load_cards()
    #Load cards from the json file
    def load_cards(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as f:
                data=json.load(f)
                return{q:flashcard(**info) for q, info in data.items()}
            return{}
    #Save cards to file
    def save_cards(self):
        data={q:card.to_dictionary() for q, card in self.cards.items()}
        with open(self.filename,"w") as file:
            json.dump(data,file,indent=4)
    #Add new flash cards
    def add_card(self):
        question=input("Enter Question/Word:")
        answer=input("Enter Answer/Meaning:")
        self.cards[question]=flashcard(question,answer)
        self.save_cards()
        print("FlashCard added Successfully!!!!")
    #Reveiw all flash cards
    def review_cards(self):
        if not self.cards:
            print("No FlashCards available!!!")
            return
        for card in self.cards.values():
            print(f"Q:{card.question}")
            input("Press Enter to show the answer....")  
            print(f"Ans:{card.answer}")
            print(f"Correct:{card.correct},Wrong:{card.wrong}")
    #Test Mode 
    def test_user(self):
        if not self.cards:
            print("No FlashCards Available!!!")
            return
        print("===Test Mode===")
        for card in self.cards.values():
            print(f"Q:{card.question}")
            user_answer=input("Your Answer:")
            if user_answer.strip().lower()==card.answer.lower():
                print("Correct Answer.")
                card.correct+=1
            else:
                print(f"Wrong Answer!!!Correct answer is '{card.answer}'")
                card.wrong+=1
        self.save_cards()
        print("Test Completed!Progress saved Successfully.")
    #Main Menu
    def main(self):
        while True:
            print("FLASHCARD LEARNING APP")
            print("1.Add FlashCard.")
            print("2.Review FlashCards.")
            print("3.Take a test.")
            print("4.Save & Exit.")
            choice=input("Enter your choice(1-4):")
            if choice=="1":
                self.add_card()
            elif choice=="2":
                self.review_cards()
            elif choice=="3":
                self.test_user()
            elif choice=="4":
                self.save_cards()
                print("Progress saved and exiting the program....God bye")
                break
            else:
                print("Invalid choice!!!")
#start the app
app=flashcardApp()
app.main()




         