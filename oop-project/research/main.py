import google.generativeai as genai



class NlpModel:
    def get_Model(self):
        google_apiKey = "AIzaSyCw-Jd3yfjCYz0lJ-9gN1tpEiAphdWseHM"
        try:
            genai.configure(api_key=google_apiKey)
            model=genai.GenerativeModel("models/gemini-1.5-flash")
            return model
        except Exception as e:
            print("Error in loading the model:", e)
                
    
class NlpApp(NlpModel):
    def __init__(self):
        self.database = {}
        self.first_Menu()

    def first_Menu(self):
        first_inp = input("""Welcome to the NLP App! Please choose an option:\n
                          1. Register a new user
                            2. Login to an existing user
                            3. Exit the app""")
        if first_inp == "1":
            # Register a new user
            self.__register_user()
        elif first_inp == "2":
            # Login to an existing user
            self.__login_user()
        else:
            print("Exiting the app. Goodbye!")
            exit()

    def second_menu(self):
        sec_inp = input("""  hey: How WOULD YOU LIKE TO USE THE NLP MODEL?\n
                            1. Sentiment Analysis
                            2. Language transilation
                            3. Language Detection ::::::
        
        
""")         
        if sec_inp == "1":
            # Sentiment Analysis
            self.__sentiment_analysis()
        elif sec_inp == "2":
            # Language Translation
            self.__language_translation()
        elif sec_inp == "3":
            # Language Detection
            self.__language_detection()
        else:
            print("Invalid option. Please try again.")
            self.second_menu()    


    def __register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        email = input("Enter an email: ")
        if email in self.database:
            print("Email already exists. Please try again.")
        else:
            self.database[email] = [
                username,
                password
            ]
            print("User registered successfully! Now you can login.")
            self.first_Menu()
    def __login_user(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email in self.database and self.database[email][1] == password:
            print(f"Welcome back, {self.database[email][0]}!")
            self.second_menu()
        else:
            print("Invalid email or password. Please try again.")
            self.__login_user()      
         
    def __sentiment_analysis(self):
        u_text = input("Please enter the text for sentiment analysis: ")
        model = super().get_Model()
        prompt = f"Analyze the sentiment of the following sentence and reply with only one word: Positive, Negative, or Neutral.\nSentence: {u_text}"
        response = model.generate_content(prompt)
        result = response.text.strip()
        print("Sentiment:", result)
        self.second_menu()

    def __language_translation(self):    
        u_text = input("Please enter the text for language translation: ")
        model = super().get_Model()
        response = model.generate_content(f"Translate this word to Urdu and reply with one word {u_text}")
        result= response.text
        print(response)
        self.second_menu()


    def __language_detection(self):
        u_text = input("Please enter the text for language detection: ")
        model = super().get_Model()
        response = model.generate_content(f"Detect the language of this word and reply just single statement {u_text}")
        result= response.text
        print(response)
        self.second_menu()

if __name__ == "__main__":            
    nlp_app = NlpApp()
    