class EnglishSpeaker:
    def speak_english(self, text):
        print(f'English Speaker: {text}')
class FrenchSpeaker:
    def speak_french(self, text):
        print(f'French Speaker: {text}')
class MaleVoice:
    def use_male_voice(self, text):
        print(f'Male Voice: {text}')
class FemaleVoice:
    def use_female_voice(self, text):
        print(f'Female Voice: {text}')


class TextToSpeechFacade:
    def __init__(self):
        self.__english_speaker = EnglishSpeaker()
        self.__french_speaker = FrenchSpeaker()
        self.__male_voice = MaleVoice()
        self.__female_voice = FemaleVoice()
    def speak_english_with_male_voice(self, text):
        self.__english_speaker.speak_english(text)
        self.__male_voice.use_male_voice(text)
    def speak_french_with_female_voice(self, text):
        self.__french_speaker.speak_french(text)
        self.__female_voice.use_female_voice(text)


def t_func():
    facade = TextToSpeechFacade()
    facade.speak_french_with_female_voice('Hi, world')
    facade.speak_english_with_male_voice('Hello world')


t_func()
