#Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>

latter = '''Dear <|Name|>,
        You are selected!
        <|Date|>
            '''
print(latter.replace("<|Name|>", "Parth").replace("<|Date|>","15 oct 2024"))