class TextMessages:

    def calculate_last_word_length(self, value):
        x = value.split()
        print(len(x[-1]))


text_message =TextMessages()
text_message.calculate_last_word_length("ksdakdk dsakdkas")
