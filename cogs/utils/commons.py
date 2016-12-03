# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
DuckhuntV2 -- commons
"""


# noinspection PyGlobalUndefined
def init():
    import logging
    import gettext
    # Ducks

    global ducks_planned, ducks_spawned
    ducks_planned = {}  # format : {discord.channel: [list, of, int, timestamps]}
    ducks_spawned = []  # format : [{"channel": discord.channel, "spawned_at": int(timestamp), "is_super": True, "life": int(life), "max_life" : int(max_life)]

    # Stats

    global number_messages
    number_messages = 0

    # Settings, config & translation

    global lang, owners, support_server, defaultSettings, levels
    lang = "en_EN"  # Language specified here is for console messages, everything that is not sent to a server
    owners = ["138751484517941259"]
    support_server = [195260081036591104]

    class Domain:  # gettext config | http://stackoverflow.com/a/38004947/3738545
        def __init__(self, domain):
            self._domain = domain
            self._translations = {}

        def _get_translation(self, language):
            try:
                return self._translations[language]
            except KeyError:
                # The fact that `fallback=True` is not the default is a serious design flaw.
                rv = self._translations[language] = gettext.translation(self._domain, languages=[language], localedir="language", fallback=True)
                return rv

        def get(self, msg: str, language: str = lang):
            # logger.debug("Language > " + str(language))
            return self._get_translation(language).gettext(msg)

    def _(string):
        return string  # Fake definition pour la traduction

    def bool_(b):
        return str(b).lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

    defaultSettings = {
        "delete_commands"              : {
            "value": False,
            "type" : bool_
        },
        "ducks_per_day"                : {
            "value": 24,
            "type" : int
        },
        "interactive_topscores_enabled": {
            "value": True,
            "type" : bool_
        },
        "users_can_find_objects"       : {
            "value": True,
            "type" : bool_
        },
        "chance_to_kill_on_missed"     : {
            "value": 5,
            "type" : int
        },
        "pm_most_messages"             : {
            "value": False,
            "type" : bool_
        },
        "time_before_ducks_leave"      : {
            "value": 11 * 60,
            "type" : int
        },
        "bang_lag"                     : {
            "value": .5,
            "type" : float
        },
        "exp_won_per_duck_killed"      : {
            "value": 10,
            "type" : int
        },
        "language"                     : {
            "value": lang,
            "type" : str
        },
        "randomize_ducks"              : {
            "value": True,
            "type" : bool_
        },
        "super_ducks_chance"           : {
            "value": 10,
            "type" : int
        },
        "super_ducks_minlife"          : {
            "value": 3,
            "type" : int
        },
        "super_ducks_maxlife"          : {
            "value": 7,
            "type" : int
        },
        "super_ducks_exp_multiplier"   : {
            "value": 1.10,
            "type" : float
        },
        "duck_frighten_chance"         : {
            "value": 5,
            "type" : int
        },
        "global_scores"                : {
            "value": False,
            "type" : bool_
        },
        "clover_min_exp"               : {
            "value": 1,
            "type" : int
        },
        "clover_max_exp"               : {
            "value": 10,
            "type" : int
        },
        "randomize_mechanical_ducks"   : {
            "value": 0,
            "type" : int
        },
        "user_can_give_exp"            : {
            "value": True,
            "type" : bool_
        },
        "tax_on_user_give"             : {
            "value": 0,
            "type" : int
        },
        "prefix"                       : {
            "value": "!",
            "type" : str
        },
        "announce_level_up"            : {
            "value": True,
            "type" : bool_
        },
        "killed_mentions"              : {
            "value": True,
            "type" : bool_
        }
    }

    levels = [{
        "niveau"    : 0,
        "expMin"    : -999,
        "nom"       : _("public danger"),
        "precision" : 55,
        "fiabilitee": 85,
        "balles"    : 6,
        "chargeurs" : 1
    }, {
        "niveau"    : 1,
        "expMin"    : -4,
        "nom"       : _("tourist"),
        "precision" : 55,
        "fiabilitee": 85,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 2,
        "expMin"    : 20,
        "nom"       : _("noob"),
        "precision" : 56,
        "fiabilitee": 86,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 3,
        "expMin"    : 50,
        "nom"       : _("trainee"),
        "precision" : 57,
        "fiabilitee": 87,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 4,
        "expMin"    : 90,
        "nom"       : _("duck misser"),
        "precision" : 58,
        "fiabilitee": 88,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 5,
        "expMin"    : 140,
        "nom"       : _("member of the Comitee Against Ducks"),
        "precision" : 59,
        "fiabilitee": 89,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 6,
        "expMin"    : 200,
        "nom"       : _("duck hater"),
        "precision" : 60,
        "fiabilitee": 90,
        "balles"    : 6,
        "chargeurs" : 2
    }, {
        "niveau"    : 7,
        "expMin"    : 270,
        "nom"       : _("duck pest"),
        "precision" : 65,
        "fiabilitee": 93,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 8,
        "expMin"    : 350,
        "nom"       : _("duck hassler"),
        "precision" : 67,
        "fiabilitee": 93,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 9,
        "expMin"    : 440,
        "nom"       : _("duck plucker"),
        "precision" : 69,
        "fiabilitee": 93,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 10,
        "expMin"    : 540,
        "nom"       : _("hunter"),
        "precision" : 71,
        "fiabilitee": 94,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 11,
        "expMin"    : 650,
        "nom"       : _("inside out duck turner"),
        "precision" : 73,
        "fiabilitee": 94,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 12,
        "expMin"    : 770,
        "nom"       : _("duck clobber"),
        "precision" : 73,
        "fiabilitee": 94,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 13,
        "expMin"    : 900,
        "nom"       : _("duck chewer"),
        "precision" : 74,
        "fiabilitee": 95,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 14,
        "expMin"    : 1040,
        "nom"       : _("duck eater"),
        "precision" : 74,
        "fiabilitee": 95,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 15,
        "expMin"    : 1190,
        "nom"       : _("duck flattener"),
        "precision" : 75,
        "fiabilitee": 95,
        "balles"    : 4,
        "chargeurs" : 3
    }, {
        "niveau"    : 16,
        "expMin"    : 1350,
        "nom"       : _("duck disassembler"),
        "precision" : 80,
        "fiabilitee": 97,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 17,
        "expMin"    : 1520,
        "nom"       : _("duck demolisher"),
        "precision" : 81,
        "fiabilitee": 97,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 18,
        "expMin"    : 1700,
        "nom"       : _("duck killer"),
        "precision" : 81,
        "fiabilitee": 97,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 19,
        "expMin"    : 1890,
        "nom"       : _("duck skinner"),
        "precision" : 82,
        "fiabilitee": 97,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 20,
        "expMin"    : 2090,
        "nom"       : _("predator"),
        "precision" : 82,
        "fiabilitee": 97,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 21,
        "expMin"    : 2300,
        "nom"       : _("duck chopper"),
        "precision" : 83,
        "fiabilitee": 98,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 22,
        "expMin"    : 2520,
        "nom"       : _("duck decorticator"),
        "precision" : 83,
        "fiabilitee": 98,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 23,
        "expMin"    : 2750,
        "nom"       : _("duck fragger"),
        "precision" : 84,
        "fiabilitee": 98,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 24,
        "expMin"    : 2990,
        "nom"       : _("duck shatterer"),
        "precision" : 84,
        "fiabilitee": 98,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 25,
        "expMin"    : 3240,
        "nom"       : _("duck smasher"),
        "precision" : 85,
        "fiabilitee": 98,
        "balles"    : 2,
        "chargeurs" : 4
    }, {
        "niveau"    : 26,
        "expMin"    : 3500,
        "nom"       : _("duck breaker"),
        "precision" : 90,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 27,
        "expMin"    : 3770,
        "nom"       : _("duck wrecker"),
        "precision" : 91,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 28,
        "expMin"    : 4050,
        "nom"       : _("duck impaler"),
        "precision" : 91,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 29,
        "expMin"    : 4340,
        "nom"       : _("duck eviscerator"),
        "precision" : 92,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 30,
        "expMin"    : 4640,
        "nom"       : _("ducks terror"),
        "precision" : 92,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 31,
        "expMin"    : 4950,
        "nom"       : _("duck exploder"),
        "precision" : 93,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 32,
        "expMin"    : 5270,
        "nom"       : _("duck destructor"),
        "precision" : 93,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 33,
        "expMin"    : 5600,
        "nom"       : _("duck blaster"),
        "precision" : 94,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 34,
        "expMin"    : 5940,
        "nom"       : _("duck pulverizer"),
        "precision" : 94,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 35,
        "expMin"    : 6290,
        "nom"       : _("duck disintegrator"),
        "precision" : 95,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 36,
        "expMin"    : 6650,
        "nom"       : _("duck atomizer"),
        "precision" : 95,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 37,
        "expMin"    : 7020,
        "nom"       : _("duck annihilator"),
        "precision" : 96,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 38,
        "expMin"    : 7400,
        "nom"       : _("serial duck killer"),
        "precision" : 96,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 39,
        "expMin"    : 7790,
        "nom"       : _("duck genocider"),
        "precision" : 97,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 40,
        "expMin"    : 8200,
        "nom"       : _("unemployed due to extinction of the duck specie"),
        "precision" : 97,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 5
    }, {
        "niveau"    : 41,
        "expMin"    : 9999,
        "nom"       : _("duck toaster"),
        "precision" : 98,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 6
    }, {
        "niveau"    : 42,
        "expMin"    : 11111,
        "nom"       : _("old noob"),
        "precision" : 99,
        "fiabilitee": 99,
        "balles"    : 1,
        "chargeurs" : 7
    }]

    # other settings

    global canards_trace, canards_trace_tocheck, canards_portrait, canards_cri, canards_bye, aideMsg, inutilite

    canards_trace = ["-,_,.-'\`'°-,_,.-'\`'°", "-,..,.-'\`'°-,_,.-'\`'°", "-._..-'\`'°-,_,.-'\`'°", "-,_,.-'\`'°-,_,.-''\`"]
    canards_trace_tocheck = [w.replace("\\", "") for w in canards_trace] + canards_trace
    canards_portrait = ["\\_O<", "\\_o<", "\\_Õ<", "\\_õ<", "\\_Ô<", "\\_ô<", "\\_Ö<", "\\_ö<", "\\_Ø<", "\\_ø<", "\\_Ò<", "\\_ò<", "\\_Ó<", "\\_ó<", "\\_0<", "\\_©<", "\\_@<", "\\_º<", "\\_°<", "\\_^<", "/_O<", "/_o<", "/_Õ<", "/_õ<", "/_Ô<", "/_ô<", "/_Ö<", "/_ö<", "/_Ø<", "/_ø<", "/_Ò<", "/_ò<", "/_Ó<", "/_ó<", "/_0<", "/_©<", "/_@<", "/_^<", "§_O<", "§_o<", "§_Õ<", "§_õ<", "§_Ô<", "§_ô<", "§_Ö<", "§_ö<", "§_Ø<", "§_ø<", "§_Ò<", "§_ò<", "§_Ó<", "§_ó<", "§_0<", "§_©<", "§_@<", "§_º<", "§_°<", "§_^<", "\\_O-", "\\_o-", "\\_Õ-", "\\_õ-", "\\_Ô-", "\\_ô-", "\\_Ö-", "\\_ö-", "\\_Ø-", "\\_ø-", "\\_Ò-", "\\_ò-", "\\_Ó-", "\\_ó-", "\\_0-", "\\_©-", "\\_@-", "\\_º-", "\\_°-", "\\_^-", "/_O-", "/_o-", "/_Õ-", "/_õ-", "/_Ô-", "/_ô-", "/_Ö-", "/_ö-", "/_Ø-", "/_ø-", "/_Ò-", "/_ò-", "/_Ó-", "/_ó-", "/_0-", "/_©-", "/_@-", "/_^-", "§_O-", "§_o-", "§_Õ-", "§_õ-", "§_Ô-", "§_ô-", "§_Ö-", "§_ö-", "§_Ø-", "§_ø-", "§_Ò-", "§_ò-", "§_Ó-", "§_ó-", "§_0-", "§_©-", "§_@-", "§_^-", "\\_O\{", "\\_o\{",
                        "\\_Õ\{", "\\_õ\{", "\\_Ô\{", "\\_ô\{", "\\_Ö\{", "\\_ö\{", "\\_Ø\{", "\\_ø\{", "\\_Ò\{", "\\_ò\{", "\\_Ó\{", "\\_ó\{", "\\_0\{", "\\_©\{", "\\_@\{", "\\_º\{", "\\_°\{", "\\_^\{", "/_O\{", "/_o\{", "/_Õ\{", "/_õ\{", "/_Ô\{", "/_ô\{", "/_Ö\{", "/_ö\{", "/_Ø\{", "/_ø\{", "/_Ò\{", "/_ò\{", "/_Ó\{", "/_ó\{", "/_0\{", "/_©\{", "/_@\{", "/_^\{", "§_O\{", "§_o\{", "§_Õ\{", "§_õ\{", "§_Ô\{", "§_ô\{", "§_Ö\{", "§_ö\{", "§_Ø\{", "§_ø\{", "§_Ò\{", "§_ò\{", "§_Ó\{", "§_ó\{", "§_0\{", "§_©\{", "§_@\{", "§_º\{", "§_°\{", "§_^\{"]
    canards_cri = ["COIN", "COIN", "COIN", "COIN", "COIN", "KWAK", "KWAK", "KWAAK", "KWAAK", "KWAAAK", "KWAAAK", "COUAK", "COUAK", "COUAAK", "COUAAK", "COUAAAK", "COUAAAK", "QUAK", "QUAK", "QUAAK", "QUAAK", "QUAAAK", "QUAAAK", "QUACK", "QUACK", "QUAACK", "QUAACK", "QUAAACK", "QUAAACK", "COUAC", "COUAC", "COUAAC", "COUAAC", "COUAAAC", "COUAAAC", "COUACK", "COUACK", "COUAACK", "COUAACK", "COUAAACK", "COUAAACK", "QWACK", "QWACK", "QWAACK", "QWAACK", "QWAAACK", "QWAAACK", "ARK", "ARK", "AARK", "AARK", "AAARK", "AAARK", "CUI ?", "PIOU ?", _("*cries*"), _("Hello world"), _("How are you today?"), _("Please don't kill me..."), "http://tinyurl.com/2qc9pl", _("Me too, I love you !")]

    canards_bye = [_("The duck went away  ·°'\`'°-.,¸¸.·°'\`"), _("The ducks went to another world  ·°'\`'°-.,¸¸.·°'\`"), _("The duck did not have time for this  ·°'\`'°-.,¸¸.·°'\`"), _("The duck left.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck dissipate in space-time.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck leave of boredoom.  ·°'\`'°-.,¸¸.·°'\`"), _("The duck don't want to be sniped.  ·°'\`'°-.,¸¸.·°'\`")]

    inutilite = [_("a stuffed duck."), _("a rubber ducky."), _("a vibrating duck."), _("a pile of feathers."), _("a chewed chewing gum."), _("a leaflet from CACAD (Coalition Against the Comitee Against Ducks)."), _("an old shoe."), _("a spring thingy."), _("a cow dung."), _("a dog dirt."), _("an expired hunting license."), _("a cartridge."), _("a cigarette butt."), _("a used condom."), _("a broken sight."), _("a broken infrared detector."), _("a bent silencer."), _("an empty box of AP ammo."), _("an empty box of explosive ammo."), _("a four-leaf clover with only 3 left."), _("a broken decoy."), _("a broken mirror."), _("a rusty mechanical duck."), _("a pair of sunglasses without glasses."), _("Donald's beret."), _("a half-melted peppermint."), _("a box of Abraxo cleaner."), _("a gun with banana peeled barrel."), _("an old hunting knife."), _("an old video recording: http://tinyurl.com/zbejktu"), _("an old hunting photo: http://tinyurl.com/hmn4r88"),
                 _("an old postcard: http://tinyurl.com/hbnkpzr"), _("a golden duck photo: http://tinyurl.com/hle8fjf"), _("a hunter pin: http://tinyurl.com/hqy7fhq"), _("bushes.")]

    # Logger
    global logger

    logger = logging.getLogger('duckhunt')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    # file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    steam_handler.setFormatter(formatter)
    logger.addHandler(steam_handler)

    # TRAD
    del _

    try:
        global _
    except SyntaxWarning:
        pass
    _ = Domain("default").get
