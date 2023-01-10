import random
import os
from colorama import Fore
import time



#skin
def skin():
        skin_ = ["Black","White"]
        final_skin = random.choice(skin_)
        

def birth():
    birthmf = random.randint(1930,2005)
    print(f"Birth: {birthmf}")
    
def IDNumber():
    idnumber_ = random.randint(111111111, 999999999)
    print(f"IDNumber: {idnumber_}")

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⣿⠿⠻⢿⣿⣿⣿⡇⢸⣿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠃⠀⠀⠀⢹⣿⣿⡇⢸⣿⣏⣉⣉⣉⣉⣉⣉⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⡄⠀⠀⠀⣸⣿⣿⡇⢸⣿⣏⣉⣉⣿⣿⣉⣉⣉⣉⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠿⣦⣤⡾⠿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⡿⠁⠀⠀⠀⠀⠀⠘⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⡿⠁⠀⠀⠀⠀⠀⠀⠀⠸⡇⢸⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⣿⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
time.sleep(1)
maleorfemale = input("F or M?\n").lower()
if maleorfemale == "f":
    
    print("Generating ID, wait...")
    os.system('cls')
    
    time.sleep(1)
    def female():
        #name
        jmena_f = ["Olivia","Emma","Charlotte","Amelia","Ava","Sophia","Isabella","Mia","Evelyn","Harper","Raya","Wrenley","Angelique","Vida","Emberlynn","Flora","Murphy","Arleth","Ocean","Oakleig","Freyja","Mylah","Taytum","Elia","Jaylani","Zayla","Navy","Della","Clover","Nyra","Olivia","Emma","Charlotte","Amelia","Ava","Sophia","Isabella","Mia","Evelyn","Harper","Luna","Camila","Gianna","Elizabeth","Eleanor","Ella","Abigail","Sofia","Avery","Scarlett"]
        final_name_f = random.choice(jmena_f)
        #lastname
        prijmeni_f_m = ["Smit", "Johnson", "William", "Brow", "Jone", "Garci"," Mille", "Davi", "Rodriguez", "Martinez"," Hernandez", "Lopez", "Gonzalez", "Wilson","Anderson", "Thomas", "Taylor"," Moore", "Jackson", "Martin"," Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson","Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres"," Nguyen"," Hill"," Flores", "Green", "Adams", "Nelson", "Baker"," Hall", "Rivera"," Campbell"," Mitchell", "Carter", "Roberts"]
        final_lastn = random.choice(prijmeni_f_m)
        #state
        state = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","IllinoisIndiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts"",Michigan","Minnesota","Mississippi","Missouri","MontanaNebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode" "Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        final_state = random.choice(state)
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⣿⠿⠻⢿⣿⣿⣿⡇⢸⣿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠃⠀⠀⠀⢹⣿⣿⡇⢸⣿⣏⣉⣉⣉⣉⣉⣉⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⡄⠀⠀⠀⣸⣿⣿⡇⢸⣿⣏⣉⣉⣿⣿⣉⣉⣉⣉⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠿⣦⣤⡾⠿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⡿⠁⠀⠀⠀⠀⠀⠘⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⡿⠁⠀⠀⠀⠀⠀⠀⠀⠸⡇⢸⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⣿⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print(f"Name: {final_name_f}")
        print(f"Last: {final_lastn}")        
        print(f"State: {final_state}")
        skin() 
        birth() 
    female()  
elif maleorfemale == "m":
    print("Generating ID, wait...")
    
    time.sleep(1)
    def male():
        #name
        names = ["Liam","Noah","Oliver","Elijah","James","William","Benjamin","Lucas","Henry","Theodore","Jack","Levi","Alexander","Jackson","Mateo","Daniel","Michael","Mason","Sebastian","Ethan","Logan","Owen","Samuel","Jacob","Asher","Aiden","John","Joseph","Wyatt","David","Leo","Luke","Julian","Hudson","Grayson","Matthew","Ezra","Gabriel","Carter","Isaac","Jayden","Luca","Anthony","Dylan","Lincoln","Thomas","Maverick","Elia","Josiah","Charles","Caleb"]
        final_name_m = random.choice(names)
        #lastname
        last_name = ["Smit", "Johnson", "William", "Brow", "Jone", "Garci"," Mille", "Davi", "Rodriguez", "Martinez"," Hernandez", "Lopez", "Gonzalez", "Wilson","Anderson", "Thomas", "Taylor"," Moore", "Jackson", "Martin"," Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson","Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres"," Nguyen"," Hill"," Flores", "Green", "Adams", "Nelson", "Baker"," Hall", "Rivera"," Campbell"," Mitchell", "Carter", "Roberts"]
        final_lastn = random.choice(last_name)
        #state
        state_ = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","IllinoisIndiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts"",Michigan","Minnesota","Mississippi","Missouri","MontanaNebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode" "Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        final_state_ = random.choice(state_)
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⠀⠀
⠀⠀⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⣿⠿⠻⢿⣿⣿⣿⡇⢸⣿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠃⠀⠀⠀⢹⣿⣿⡇⢸⣿⣏⣉⣉⣉⣉⣉⣉⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⡄⠀⠀⠀⣸⣿⣿⡇⢸⣿⣏⣉⣉⣿⣿⣉⣉⣉⣉⣿⣿⠀⠀
⠀⠀⣿⡇⣿⣿⣿⠿⣦⣤⡾⠿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⣿⡿⠁⠀⠀⠀⠀⠀⠘⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⡇⡿⠁⠀⠀⠀⠀⠀⠀⠀⠸⡇⢸⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⣿⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣼⣿⠀⠀
⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print(f"Name: {final_name_m}")
        print(f"Last: {final_lastn}")
        print(f"State: {final_state_}")
        skin()
        birth()
        id
    male()
