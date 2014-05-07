#!/usr/bin/python2

from __future__ import print_function

import sys

from espeak import core, espeak


class ESpeak:
    """ Class to implement high level text-to-speech methods using
        python-espeak.
    """

    def __init__(self, voice = None, capitals = None, pitch = None,
                    punctuation = None, rate = None, volume = None,
                    wordgap = None):
        """ Initialize certain parameters. """
        self.set_parameters(voice = voice, capitals = capitals,
                            pitch = pitch, punctuation = punctuation,
                            rate = rate, volume = volume,
                            wordgap = wordgap)

    def get_parameters(self):
        """ Return a dictionary of current espeak parameters. """
        return dict(
                voice = espeak.get_voice(),
                capitals = espeak.get_parameter(core.parameter_CAPITALS),
                pitch = espeak.get_parameter(core.parameter_PITCH),
                punctuation = espeak.get_parameter(core.parameter_PUNCTUATION),
                rate = espeak.get_parameter(core.parameter_RATE),
                volume = espeak.get_parameter(core.parameter_VOLUME),
                wordgap = espeak.get_parameter(core.parameter_WORDGAP))

            
    def set_parameters(voice = None, capitals = None, pitch = None,
                    punctuation = None, rate = None, volume = None,
                    wordgap = None):
        """ Set espeak parameters. """
        result = True
        if voice is not None:
            voices = self.list_voices()
            if voice not in voices:
                print('WARNING: Voice ', voice, ' not supported by espeak.',
                    'Using default voice instead.', file = sys.stderr)
                voice = 'default'
            if not espeak.set_voice(voice):
                print('WARNING: Voice ', voice, ' could not be set.',
                    file = sys.stderr)
                result = False

        if capitals is not None:
            if not espeak.set_parameter(core.parameter_CAPITALS, capitals):
                print('WARNING: Parameter capitals could not be set to',
                    capitals, file = sys.stderr)
                result = False
        if pitch is not None:
            if not espeak.set_parameter(core.parameter_PITCH, pitch):
                print('WARNING: Parameter pitch could not be set to',
                    pitch, file = sys.stderr)
                result = False
        if punctuation is not None:
            if not espeak.set_parameter(core.parameter_PUNCTUATION, punctuation):
                print('WARNING: Parameter punctuation could not be set to',
                    punctuation, file = sys.stderr)
                result = False
        if rate is not None:
            if not espeak.set_parameter(core.parameter_RATE, rate):
                print('WARNING: Parameter rate could not be set to',
                    rate, file = sys.stderr)
                result = False
        if volume is not None:
            if not espeak.set_parameter(core.parameter_VOLUME, volume):
                print('WARNING: Parameter volume could not be set to',
                    volume, file = sys.stderr)
                result = False
        if wordgap is not None:
            if not espeak.set_parameter(core.parameter_WORDGAP, wordgap):
                print('WARNING: Parameter wordgap could not be set to',
                    wordgap, file = sys.stderr)
                result = False
        return result

    def list_voices(self):
        """ List all available espeak voices. """
        return [v[identifier] for v in espeak.list_voices()]

    def speak(self, message):
        """ Speak the given text message. """
        return espeak.synth(message)

#>>> dir(espeak)
#['Gender', 'Parameter', 'Punctuation', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_repr', 'cancel', 'core', 'event_END', 'event_MARK', 'event_MSG_TERMINATED', 'event_PHONEME', 'event_PLAY', 'event_SENTENCE', 'event_WORD', 'get_parameter', 'is_playing', 'list_voices', 'set_SynthCallback', 'set_parameter', 'set_voice', 'synth']
#>>> espeak.list_voices()
#[{'gender': 1, 'age': None, 'identifier': 'af', 'variant': None, 'name': 'afrikaans'}, {'gender': None, 'age': None, 'identifier': 'bg', 'variant': None, 'name': 'bulgarian-test'}, {'gender': 1, 'age': None, 'identifier': 'bs', 'variant': None, 'name': 'bosnian'}, {'gender': 1, 'age': None, 'identifier': 'ca', 'variant': None, 'name': 'catalan'}, {'gender': 1, 'age': None, 'identifier': 'cs', 'variant': None, 'name': 'czech'}, {'gender': 1, 'age': None, 'identifier': 'cy', 'variant': None, 'name': 'welsh-test'}, {'gender': 1, 'age': None, 'identifier': 'da', 'variant': None, 'name': 'danish'}, {'gender': 1, 'age': None, 'identifier': 'de', 'variant': None, 'name': 'german'}, {'gender': 1, 'age': None, 'identifier': 'el', 'variant': None, 'name': 'greek'}, {'gender': 1, 'age': None, 'identifier': 'default', 'variant': None, 'name': 'default'}, {'gender': 1, 'age': None, 'identifier': 'en/en-sc', 'variant': None, 'name': 'en-scottish'}, {'gender': 1, 'age': None, 'identifier': 'en/en', 'variant': None, 'name': 'english'}, {'gender': 1, 'age': None, 'identifier': 'en/en-n', 'variant': None, 'name': 'lancashire'}, {'gender': 1, 'age': None, 'identifier': 'en/en-rp', 'variant': None, 'name': 'english_rp'}, {'gender': 1, 'age': None, 'identifier': 'en/en-wm', 'variant': None, 'name': 'english_wmids'}, {'gender': 1, 'age': None, 'identifier': 'en/en-us', 'variant': None, 'name': 'english-us'}, {'gender': 1, 'age': None, 'identifier': 'en/en-wi', 'variant': None, 'name': 'en-westindies'}, {'gender': 1, 'age': None, 'identifier': 'eo', 'variant': None, 'name': 'esperanto'}, {'gender': 1, 'age': None, 'identifier': 'es', 'variant': None, 'name': 'spanish'}, {'gender': 1, 'age': None, 'identifier': 'es-la', 'variant': None, 'name': 'spanish-latin-american'}, {'gender': None, 'age': None, 'identifier': 'et', 'variant': None, 'name': 'estonian'}, {'gender': 1, 'age': None, 'identifier': 'fi', 'variant': None, 'name': 'finnish'}, {'gender': 1, 'age': None, 'identifier': 'fr-be', 'variant': None, 'name': 'french (Belgium)'}, {'gender': 1, 'age': None, 'identifier': 'fr', 'variant': None, 'name': 'french'}, {'gender': 1, 'age': None, 'identifier': 'test/grc', 'variant': None, 'name': 'greek-ancient'}, {'gender': 1, 'age': None, 'identifier': 'hi', 'variant': None, 'name': 'hindi'}, {'gender': 1, 'age': None, 'identifier': 'hr', 'variant': None, 'name': 'croatian'}, {'gender': 1, 'age': None, 'identifier': 'hu', 'variant': None, 'name': 'hungarian'}, {'gender': 1, 'age': None, 'identifier': 'hy', 'variant': None, 'name': 'armenian'}, {'gender': 1, 'age': None, 'identifier': 'hy-west', 'variant': None, 'name': 'armenian-west'}, {'gender': 1, 'age': None, 'identifier': 'id', 'variant': None, 'name': 'indonesian-test'}, {'gender': 1, 'age': None, 'identifier': 'is', 'variant': None, 'name': 'icelandic-test'}, {'gender': 1, 'age': None, 'identifier': 'it', 'variant': None, 'name': 'italian'}, {'gender': None, 'age': None, 'identifier': 'test/jbo', 'variant': None, 'name': 'lojban'}, {'gender': None, 'age': None, 'identifier': 'ka', 'variant': None, 'name': 'georgian-test'}, {'gender': None, 'age': None, 'identifier': 'kn', 'variant': None, 'name': 'kannada'}, {'gender': 1, 'age': None, 'identifier': 'ku', 'variant': None, 'name': 'kurdish'}, {'gender': 1, 'age': None, 'identifier': 'la', 'variant': None, 'name': 'latin'}, {'gender': 1, 'age': None, 'identifier': 'lv', 'variant': None, 'name': 'latvian'}, {'gender': 1, 'age': None, 'identifier': 'mk', 'variant': None, 'name': 'macedonian-test'}, {'gender': 1, 'age': None, 'identifier': 'ml', 'variant': None, 'name': 'malayalam'}, {'gender': 1, 'age': None, 'identifier': 'test/nci', 'variant': None, 'name': 'nahuatl - classical'}, {'gender': 1, 'age': None, 'identifier': 'nl', 'variant': None, 'name': 'dutch-test'}, {'gender': 1, 'age': None, 'identifier': 'no', 'variant': None, 'name': 'norwegian'}, {'gender': None, 'age': None, 'identifier': 'test/pap', 'variant': None, 'name': 'papiamento-test'}, {'gender': 1, 'age': None, 'identifier': 'pl', 'variant': None, 'name': 'polish'}, {'gender': 1, 'age': None, 'identifier': 'pt', 'variant': None, 'name': 'brazil'}, {'gender': 1, 'age': None, 'identifier': 'pt-pt', 'variant': None, 'name': 'portugal'}, {'gender': 1, 'age': None, 'identifier': 'ro', 'variant': None, 'name': 'romanian'}, {'gender': 1, 'age': None, 'identifier': 'ru', 'variant': None, 'name': 'russian_test'}, {'gender': 1, 'age': None, 'identifier': 'sk', 'variant': None, 'name': 'slovak'}, {'gender': 1, 'age': None, 'identifier': 'sq', 'variant': None, 'name': 'albanian'}, {'gender': 1, 'age': None, 'identifier': 'sr', 'variant': None, 'name': 'serbian'}, {'gender': 1, 'age': None, 'identifier': 'sv', 'variant': None, 'name': 'swedish'}, {'gender': 1, 'age': None, 'identifier': 'sw', 'variant': None, 'name': 'swahili-test'}, {'gender': 1, 'age': None, 'identifier': 'ta', 'variant': None, 'name': 'tamil'}, {'gender': 1, 'age': None, 'identifier': 'tr', 'variant': None, 'name': 'turkish'}, {'gender': 1, 'age': None, 'identifier': 'vi', 'variant': None, 'name': 'vietnam'}, {'gender': 1, 'age': None, 'identifier': 'zh', 'variant': None, 'name': 'Mandarin'}, {'gender': 1, 'age': None, 'identifier': 'zh-yue', 'variant': None, 'name': 'cantonese'}]
#>>> dir(espeak.core)
#['__doc__', '__file__', '__name__', '__package__', 'cancel', 'error', 'event_END', 'event_MARK', 'event_MSG_TERMINATED', 'event_PHONEME', 'event_PLAY', 'event_SENTENCE', 'event_WORD', 'get_parameter', 'is_playing', 'list_voices', 'parameter_CAPITALS', 'parameter_PITCH', 'parameter_PUNCTUATION', 'parameter_RANGE', 'parameter_RATE', 'parameter_VOLUME', 'parameter_WORDGAP', 'punctuation_ALL', 'punctuation_NONE', 'punctuation_SOME', 'set_SynthCallback', 'set_parameter', 'set_voice', 'synth']
