import discord
from discord.ext import commands 
from discord.ext import tasks, commands
from colorama import Fore
from psutil import users
import random
import requests
from collections import defaultdict
import os
import aiohttp
import asyncio
import re
import time
import subprocess
import string
import sys
import json


black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"  
pink = "\033[38;2;255;192;203m"
white = "\033[37m"
blue = "\033[34m"
black = "\033[30m"
light_green = "\033[92m" 
light_yellow = "\033[93m" 
light_magenta = "\033[95m" 
light_cyan = "\033[96m"  
light_red = "\033[91m"  
light_blue = "\033[94m"  

www = Fore.WHITE
mkk = Fore.BLUE
b = Fore.BLACK
ggg = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX 
pps = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
qqq = Fore.MAGENTA
lbb = Fore.LIGHTBLUE_EX
mll = Fore.LIGHTBLUE_EX
mjj = Fore.RED
yyy = Fore.YELLOW

name = ''

whore_wordlist = ["HOW\nDID\nYOU\nGET\nHOED\nLIKE\nTHAT\nLOLL\nYOUR\nA\nBITCH", "SIGN\nYOUR\nLIFE\nAWAY\nTO\nME\nLOSER\nASS\nPEDO\nLOLL","SHUT\nYOUR\nPUSSY\nASS\nMOUTH\nBITCH", "NIGGA\nGETS\nBULLIED\nON\nDAILY\nBASIS", "TRASH\nNIGGA\nOUTLAST\nME\nRETARD", "MORONIC\nASS\nLITTLE\nFAGGOT\nGET\nBACK\nUP", "WEAL\nASS\nCHAT\nSLAVE\nGET\nDOWN\nFUCK\nBOY", "NEVER\nCOMPETE\nWITH\nA\nGOD", "UR\nMY\nFUCKING\nSON\nPEASENT", "FOCUS\nUP\nRETARDED\nFUCKBOY\nLOLLOL", "NIGGA\nYOU\nCANT\nSTEP\nSHITTY\nLOSER", "SHUT\nTHE\nFUCK\nUP\nBITCHMADE\nLOSER", "LOL\nYOUR\nA\nSHITTY\nCOM\nREJECT\nLOSER", "YOUR\nDYING\nTO\nME\nLMFAOO", "STOP\nSTEPPING\nU\nSLOW\nBRAINED\nMORON", 
"EGOUL\nMEU\nE MAI\nMARE\nDECÂT\nPUIUL TĂU\nNEGRU", "NU POȚI\nPROGRAMA\nNU\nAI\nNICIO\nȘANSĂ\nÎMPOTRIVA\nMIEI\nPLÂNGE", "MY\nMOM\nTYPES\nFASTER\nTHAN\nTHIS\nWHAT\nTHE\nFUCK\nLMFAOO", "RETARDED\nMORON\nLOL\nUR\nFUCKING\nWORTHLESS", "ILL\nNEVER\nFOLD\nOR\nDIE", "GET\nDROWNED\nBY\nUR\nGOD", "STEP\nTHE\nFUCK\nDOWN\nBEFORE\nA\nREAL\nSTEPPER\nMURDERS\nYOU\nUR\nMY\nLAB\nDOG\nBARK\nFOR\nUR\nGOD\nYOU\nFEMBOY\nYOU\nHAVE\nA\nCUCK\nKINK", "YOUR\nMY\nSEEDLING\nI\nGREW\nYOU\nLIKE\nA\nPLANT\nWEAK\nFUCK\nBOY", "WHO\nIS\nTHIS\nWEAK\nLOWTIER\nCLOWN", "ILL\nTEAR\nYOUR\nGUTS\nOUT\nWEAK\nUGLY\nSLOW\nDORK\nLOLLL", "I\nBROKE\nTHIS\nNIGGAS\nNECK\nLOL\nWEAKLING", 
"SHUT\nTHE\nFUCK\nUP\nYOU\nCANT\nBEEF\nRETARD", "STREAM\nYOUR\nDEATH\nPETTIE\nFAGGOT", "YOUR\nDYING\nTO\nME\nFRAIL\nSLUT","UP\nME\nA\nPENNY\nPOOR\nPISS\nFUCK", "I\nSTABBED\nTHIS\nNIGGA\nIN\nHIS\nCHEST", "WEAK\nDYSLEXIC\nFUCK\nUR\nHORRID", "WE\nCAN\nGO\nFOREVER\nILL\nMURDER\nYOUR\nBLOODLINE\nDYKE", "NOBODY\nCAN\nSAVE\nYOU\nTRANNY\nDYKE", "YOUR\nA\nPUSSY\nASS\nKID\nWHY\nDID\nU\nSTEP\nAND\nGOT\nPUT\nTHE\nFUCK\nDOWN", "LOL\nYOUR\nJUS\nASS\nAINT\nYOU?😂", "SHUT\nTHE\nFUCK\nUP\nWEAK\nFUCKBOY", "BOW\nDOWN\nTO\nME\nSHITTY\nSLUT", "PEON\nASS\nNIGGA\nASKED\nA\nHOMELESS\nGUY\nFOR\nA\nDOLLAR", "WHO\nGAVE\nTHIS\nNIGGA\nTHE\nMIC\nLMFAOO", 
"DIRTY\nASS\nHOBO\nLIVES\nIN\nA\nCARDBOARD\nBOX", "WHO\nTHE\nFUCK\nASKED\nBITCHMADE\nLOSER", "UGLY\nASS\nBLACK\nTHUG", "nigga\nbuilt\nlike\na\nsumo\nwreslting\nairplane", "nigga\nyo\ngranny\nlevetaties\nwhen\nshe\nclicks\nher\nankles", "frog\nwith\nvampire\nteeth\nthat\nruns\naway\nfrom\nhumans", " you\nlook\nlike\nan\niguana\nwith\na\nrocket\nboot\non", "YOU\nSHOT\nA\nHOMELESS\nMAN\nFOR\nSELLING\nCANDY", "that\nnigga\nwhitebeard\nthrew\na\npocket\nknife\nat\nyo\ntooth", "YOU\nDORK\nASS\nRUNT\nDONT\nSTEP\nTO\nYOUR\nFOUNDER", "COME\nHERE\nILL\nCHOKE\nYOU\nDIRTY\nHINDU\nIDIAN", "ILL\nFUCKING\nMURDER\nYOU\nWEAK\nSKID", 
"ILL\nRIP\nYOUR\nINTESTINES\nOUT\nAND\nFEED\nIT\nTO\nMY\nDOG", "SAY\nIT\nWITH\nYOUR\nCHEST\nYOU\nCANT\nHANDLE\nTHE\nGREATEST", "ILL\nMAKE\nYOUR\nLIFE\nFLASH\nDUMB\nCUCK", "NIGGA\nGETS\nBEAT\nBY\nHIS\nDAD\nLOL", "YOU\nFLEX\nWEAKNESS\nAND\nCALL\nIT\nPERSONALITY\nDUMBASS\nNIGGA", "WE\nCOULD\nPUT\nU\nON\nA\nSHIRT\nRETARDED\nFUCKING\nPEDOPHILE", "WEIRD\nASS\nNIGGA\nTALKING\nTO\nME\nLIKE\nWE\nCOOL", "I\nWALK\nIN\nYOU\nVANISH\nTHATS\nREAL\nINFLUENCE", "UR\nA\nDIRTY,\nASS\nNIGGA\nAND\nNOBODY\nCARE", "UR\nMY\nFUCKING\nSON\nNIGGA\nDIED\nAND\nBLEW\nHIS\nFUCKING\nBRAINS\nOUT", "LETS\nALL\nPRAY\nFOR\nTHIS\nNIGGA\nLOOOL", "HOW\nARE\nYOU\nSO\nASS\nNIGGA\nLMAO", 
"get\nthe\nfuck\ndown\ni\nown\nyou", "TU\nMAMÁ\nES\nMI\nPUTA", "I'll\nrip\nur\nankles\noff\nweak\nbitch", "you\nlook\nlike\na\ndinosaur\nwith\nno\nteeth", "im\ngonna\ntake\nyour\nsoul\nnow", "your\nfucking\nslow\nand\nyour\na\nindian\nloser", "you\nso\nfucking\ntrash\nbitch\nboy", "you\nugly\nas\nfuck boy\nniggas\nwill\nput\nands\non\nyou", "ur\nso\nfucking\ndogshit\nweak\ncuck\nnow\nshut\nthe\nfuck\nup\nlike\nmy\ndog", "you\nsaw\nme\nand\nyo\nbody\nshook\npussy", "yo\nindian\nshut\nthe\nfuck\nup", "Nigga\nyou\nwas\nplaying\nagario\nand\ngot\ndouble\nsplitted\nby\na\nnigga\nnamed\nTimmyTwoThumbs\nboy\nyou\nugly\nass\nretarted\nfuck", 
"Nigga\nyou\ngot\nbanned\nfrom\nthe\nLGBTQ\nhideout\nbecause\nyou\nsaid\nsaid\nthe\ncolors\nof\nthe\nrainbow\nwere\nugly\nnigga\nyou\nstupid\nas\nfuck\nboy", "ill\nchuck\nyou\nin\na\nriver\nbitch", "even\ncancer\npatients\nhas\nmore\nlife\nthan\nyou", "this\nis\nbad\nyour\nslow\nand\ni\nown\nyou", "weird\nass\nliving\nspecial\ncreature", "ill\nput\nyou\nin\na\nchokehold\nand\nbody\nslam\nyou\nLOL", "ill\nrip\nyour\nscalp\noff\nyour\nskull", "niggas\nwill\nend\nyou\nfaggot\nthot", "slobby\ndepressed\nfuck\nshut\nthe\nfuck\nup", "shut\nthe\nfuck\nup\nyou\nadmitted\nto\nbeing\nmy\ngood\nlittle\nwhore\ndogshit\nfaggot", "nigga\nis\nsprinting\naway\nfrom\nme",
"ill\nbeat\nthe\nfuck\noutta\nyou", "im\nfaster\nden\nyou\nslow\nlittle\nbitch", "ay\nbitch\nshut\nthe\nfuck\nup\nugly\npussy", "ugly\nass\npedophile\ni\ndont\nfuck\nwith\nyou\nfaggot", "your\nlife\nis\non\n50/50cringe\nbitch", "ill\nhumiliate\nyou\nbitch\nyou\ngot\nhoed\nby\neveryone\ngarbage\nbitch", "ill\nput\na\nrifle\nin\nyour\nmouth\nbitch\nmade\nloser\nLOLL", "you\ngot\nelectrocut\nby\nmy\neel\nloser\ndork", "im\ndissing\nyou\nnow\nwhat\nweak\nass\ndying\nslut", "your\nso\nfucking\nweird\nugly\npedo\nstop\nfucking\nlooking", "ill\nthrow\nyou\nin\na\ndumpster\nslave\ndont\nfucking\ndie\nscumbag", "your\nmy\nloser\nlittle\nbitch\nyour\nass\nas\nfuck\nwhore",
"pedo\nfuck\nstay\naway\nfrom\nminors\nfucking\ntrash\nbitch", "ay\nfuck\nup\ndogshit\nqueer\ndo\ni\nneeda\nsmack\nthe\nfuck\noutta\nyou", "your\nmother\nisnt\nvisiting\nyour\nfuneral\nlonely\nfuck\nill\ntake\nyour\nsoul\nout\nusing\nmy\nbarehands", "bitchass\nnigga\nill bash ur head in pussy\nyour\nmy\nbitch\nweak\nfuck", "niggas\nwill\nshoot\nyour\nface\noff\nshut\nthe\nfuck\nup\nfat\nbitch", "stop\nbeing\nmy\nbitch\nfaggot\nyour\nass\nson\nand\nyour\naccuracy\nis\nshit" "watch\nthat\nfuckin\nmouth\nfaggot\nbitch\nyour\na\nnerdy\nshithead\nyour\nclit\nstinks\nim\nhere\nto\nkill\nyou", "cow\ndick\neating\nass\nnigga", "skanky\nlittle\nfaggot\nyour\nugly\nas\nfuck\nLOL", 
"yo\ngreasy\nfaggot\nfuck\nup\nill\nbeat\nthe\nfuck\noutta\nyou", "bitch\nill\nbreak\nyo\nnose\nsit\nthe\nfuck\ndown\nfaggot", "ugly\nfaggot\ndont\nrun\nwhy\nare\nyou\nnot\ndoing\ndamage", "Nigga\nyour\nhead\nlooks\nlike\na\ndorito\nmy\nnigga\nyou\ngot\nthat\nshit\nfrom\nphineas\nand\nferb\ntell\nme\nwhy\ni\nsaw\nyou\nbeating\nyour\ndick\nto\ndora\nthe\nexplora", "I'LL\nLEAVE\nTHIS\nIMPAIRED\nREJECTS\nBODY\nIN\nA\nDITCH", "NIGGA\nDIED\nBY\nFIRING\nSQUAD", "stop\ncrying\nget\nback\nup", "skanky\nlittle\nfaggot\nyour\nugly\nas\nfuck\nLOL", "ill\nmake\nyou\nend\nyour\nlife\nfrail\nass\nbitch", "Cállate\nla\nboca\nsucio\ncriatura\nespecial\nnegro\nEntraste\na\nmi\npaís\nen\nun\ncontenedor",
"988\nheres\nthe\nsuicide\nhotline\nfrustrated\npedo", "this\nis\nbad\ni\nfucking\nkilled\nyou" "BITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nLOLLOLOOL", "nigga\ni\ncaught\nu\nslapboxing\na\nnigga\nname\ndonitello\nfor\n20\nvbucks\nlike\nshit\nnigga\nyou\nwas\na\nknown\nschool\nthreat\nbecause\nyou\nbrought\na\nbaguette\nto\nschool\nfor\nbring\nyour\npet\nday\nsmelly\nnigga",
"nigga\nthats\nwhy\nyo\nnipples\nare\nbuilt\nlike\nfour\nleaf\nclovers\nthats\nwhy\byo\nmom\nuse\nto\nuppercut\nyou\nin\nfatboy”, “you\nsmoke\nvapes\nout\nyour\nasshole\nweirdo”, “SORRY\nASS\nNIGGA\nUR\nNOT\nSAFE\nFROM\nME\nWEAK\nVIRGIN\nASS\nNIGGA\nUR\nMISERABLE\nAS\nSHIT\nFUCKING\nFAGGOT\nASS\nPEDO\nLOLOL”, “NIGGA\nHOE\nASS\nNIGGA\nDIRTY\nASS\nNIGGA\nSHUT\nUP\nNIGGA\nYOU\nWASTED\nEIGHT\nYEARS\nOF\nYOUR\nLIFE\nIN\nA\nJUNGLE\nTRYNA\nFIND\nA\nLEGENDARY\nPOKEMON\nMY\nNIGGA\nCAUSE\nYOU\nDIRTY\nAS\nFUCK\nMY\nNIGGA\nYOU\nFEEL\nBURPS\nFORM\nIN\nYO\nTHROAT\nAND\nPISS\nYO\nPANTS\nMY\nNIGGA\nYO\nMOTHER\nIS\nA\nCRACK\nADICT\nLOLOO"

]

outlast_messages = ["HOW\nDID\nYOU\nGET\nHOED\nLIKE\nTHAT\nLOLL\nYOUR\nA\nBITCH", "SIGN\nYOUR\nLIFE\nAWAY\nTO\nME\nLOSER\nASS\nPEDO\nLOLL","SHUT\nYOUR\nPUSSY\nASS\nMOUTH\nBITCH", "NIGGA\nGETS\nBULLIED\nON\nDAILY\nBASIS", "TRASH\nNIGGA\nOUTLAST\nME\nRETARD", "MORONIC\nASS\nLITTLE\nFAGGOT\nGET\nBACK\nUP", "WEAL\nASS\nCHAT\nSLAVE\nGET\nDOWN\nFUCK\nBOY", "NEVER\nCOMPETE\nWITH\nA\nGOD", "UR\nMY\nFUCKING\nSON\nPEASENT", "FOCUS\nUP\nRETARDED\nFUCKBOY\nLOLLOL", "NIGGA\nYOU\nCANT\nSTEP\nSHITTY\nLOSER", "SHUT\nTHE\nFUCK\nUP\nBITCHMADE\nLOSER", "LOL\nYOUR\nA\nSHITTY\nCOM\nREJECT\nLOSER", "YOUR\nDYING\nTO\nME\nLMFAOO", "STOP\nSTEPPING\nU\nSLOW\nBRAINED\nMORON", 
"EGOUL\nMEU\nE MAI\nMARE\nDECÂT\nPUIUL TĂU\nNEGRU", "NU POȚI\nPROGRAMA\nNU\nAI\nNICIO\nȘANSĂ\nÎMPOTRIVA\nMIEI\nPLÂNGE", "MY\nMOM\nTYPES\nFASTER\nTHAN\nTHIS\nWHAT\nTHE\nFUCK\nLMFAOO", "RETARDED\nMORON\nLOL\nUR\nFUCKING\nWORTHLESS", "ILL\nNEVER\nFOLD\nOR\nDIE", "GET\nDROWNED\nBY\nUR\nGOD", "STEP\nTHE\nFUCK\nDOWN\nBEFORE\nA\nREAL\nSTEPPER\nMURDERS\nYOU\nUR\nMY\nLAB\nDOG\nBARK\nFOR\nUR\nGOD\nYOU\nFEMBOY\nYOU\nHAVE\nA\nCUCK\nKINK", "YOUR\nMY\nSEEDLING\nI\nGREW\nYOU\nLIKE\nA\nPLANT\nWEAK\nFUCK\nBOY", "WHO\nIS\nTHIS\nWEAK\nLOWTIER\nCLOWN", "ILL\nTEAR\nYOUR\nGUTS\nOUT\nWEAK\nUGLY\nSLOW\nDORK\nLOLLL", "I\nBROKE\nTHIS\nNIGGAS\nNECK\nLOL\nWEAKLING", 
"SHUT\nTHE\nFUCK\nUP\nYOU\nCANT\nBEEF\nRETARD", "STREAM\nYOUR\nDEATH\nPETTIE\nFAGGOT", "YOUR\nDYING\nTO\nME\nFRAIL\nSLUT","UP\nME\nA\nPENNY\nPOOR\nPISS\nFUCK", "I\nSTABBED\nTHIS\nNIGGA\nIN\nHIS\nCHEST", "WEAK\nDYSLEXIC\nFUCK\nUR\nHORRID", "WE\nCAN\nGO\nFOREVER\nILL\nMURDER\nYOUR\nBLOODLINE\nDYKE", "NOBODY\nCAN\nSAVE\nYOU\nTRANNY\nDYKE", "YOUR\nA\nPUSSY\nASS\nKID\nWHY\nDID\nU\nSTEP\nAND\nGOT\nPUT\nTHE\nFUCK\nDOWN", "LOL\nYOUR\nJUS\nASS\nAINT\nYOU?😂", "SHUT\nTHE\nFUCK\nUP\nWEAK\nFUCKBOY", "BOW\nDOWN\nTO\nME\nSHITTY\nSLUT", "PEON\nASS\nNIGGA\nASKED\nA\nHOMELESS\nGUY\nFOR\nA\nDOLLAR", "WHO\nGAVE\nTHIS\nNIGGA\nTHE\nMIC\nLMFAOO", 
"DIRTY\nASS\nHOBO\nLIVES\nIN\nA\nCARDBOARD\nBOX", "WHO\nTHE\nFUCK\nASKED\nBITCHMADE\nLOSER", "UGLY\nASS\nBLACK\nTHUG", "nigga\nbuilt\nlike\na\nsumo\nwreslting\nairplane", "nigga\nyo\ngranny\nlevetaties\nwhen\nshe\nclicks\nher\nankles", "frog\nwith\nvampire\nteeth\nthat\nruns\naway\nfrom\nhumans", " you\nlook\nlike\nan\niguana\nwith\na\nrocket\nboot\non", "YOU\nSHOT\nA\nHOMELESS\nMAN\nFOR\nSELLING\nCANDY", "that\nnigga\nwhitebeard\nthrew\na\npocket\nknife\nat\nyo\ntooth", "YOU\nDORK\nASS\nRUNT\nDONT\nSTEP\nTO\nYOUR\nFOUNDER", "COME\nHERE\nILL\nCHOKE\nYOU\nDIRTY\nHINDU\nIDIAN", "ILL\nFUCKING\nMURDER\nYOU\nWEAK\nSKID", 
"ILL\nRIP\nYOUR\nINTESTINES\nOUT\nAND\nFEED\nIT\nTO\nMY\nDOG", "SAY\nIT\nWITH\nYOUR\nCHEST\nYOU\nCANT\nHANDLE\nTHE\nGREATEST", "ILL\nMAKE\nYOUR\nLIFE\nFLASH\nDUMB\nCUCK", "NIGGA\nGETS\nBEAT\nBY\nHIS\nDAD\nLOL", "YOU\nFLEX\nWEAKNESS\nAND\nCALL\nIT\nPERSONALITY\nDUMBASS\nNIGGA", "WE\nCOULD\nPUT\nU\nON\nA\nSHIRT\nRETARDED\nFUCKING\nPEDOPHILE", "WEIRD\nASS\nNIGGA\nTALKING\nTO\nME\nLIKE\nWE\nCOOL", "I\nWALK\nIN\nYOU\nVANISH\nTHATS\nREAL\nINFLUENCE", "UR\nA\nDIRTY,\nASS\nNIGGA\nAND\nNOBODY\nCARE", "UR\nMY\nFUCKING\nSON\nNIGGA\nDIED\nAND\nBLEW\nHIS\nFUCKING\nBRAINS\nOUT", "LETS\nALL\nPRAY\nFOR\nTHIS\nNIGGA\nLOOOL", "HOW\nARE\nYOU\nSO\nASS\nNIGGA\nLMAO", 
"get\nthe\nfuck\ndown\ni\nown\nyou", "TU\nMAMÁ\nES\nMI\nPUTA", "I'll\nrip\nur\nankles\noff\nweak\nbitch", "you\nlook\nlike\na\ndinosaur\nwith\nno\nteeth", "im\ngonna\ntake\nyour\nsoul\nnow", "your\nfucking\nslow\nand\nyour\na\nindian\nloser", "you\nso\nfucking\ntrash\nbitch\nboy", "you\nugly\nas\nfuck boy\nniggas\nwill\nput\nands\non\nyou", "ur\nso\nfucking\ndogshit\nweak\ncuck\nnow\nshut\nthe\nfuck\nup\nlike\nmy\ndog", "you\nsaw\nme\nand\nyo\nbody\nshook\npussy", "yo\nindian\nshut\nthe\nfuck\nup", "Nigga\nyou\nwas\nplaying\nagario\nand\ngot\ndouble\nsplitted\nby\na\nnigga\nnamed\nTimmyTwoThumbs\nboy\nyou\nugly\nass\nretarted\nfuck", 
"Nigga\nyou\ngot\nbanned\nfrom\nthe\nLGBTQ\nhideout\nbecause\nyou\nsaid\nsaid\nthe\ncolors\nof\nthe\nrainbow\nwere\nugly\nnigga\nyou\nstupid\nas\nfuck\nboy", "ill\nchuck\nyou\nin\na\nriver\nbitch", "even\ncancer\npatients\nhas\nmore\nlife\nthan\nyou", "this\nis\nbad\nyour\nslow\nand\ni\nown\nyou", "weird\nass\nliving\nspecial\ncreature", "ill\nput\nyou\nin\na\nchokehold\nand\nbody\nslam\nyou\nLOL", "ill\nrip\nyour\nscalp\noff\nyour\nskull", "niggas\nwill\nend\nyou\nfaggot\nthot", "slobby\ndepressed\nfuck\nshut\nthe\nfuck\nup", "shut\nthe\nfuck\nup\nyou\nadmitted\nto\nbeing\nmy\ngood\nlittle\nwhore\ndogshit\nfaggot", "nigga\nis\nsprinting\naway\nfrom\nme",
"ill\nbeat\nthe\nfuck\noutta\nyou", "im\nfaster\nden\nyou\nslow\nlittle\nbitch", "ay\nbitch\nshut\nthe\nfuck\nup\nugly\npussy", "ugly\nass\npedophile\ni\ndont\nfuck\nwith\nyou\nfaggot", "your\nlife\nis\non\n50/50cringe\nbitch", "ill\nhumiliate\nyou\nbitch\nyou\ngot\nhoed\nby\neveryone\ngarbage\nbitch", "ill\nput\na\nrifle\nin\nyour\nmouth\nbitch\nmade\nloser\nLOLL", "you\ngot\nelectrocut\nby\nmy\neel\nloser\ndork", "im\ndissing\nyou\nnow\nwhat\nweak\nass\ndying\nslut", "your\nso\nfucking\nweird\nugly\npedo\nstop\nfucking\nlooking", "ill\nthrow\nyou\nin\na\ndumpster\nslave\ndont\nfucking\ndie\nscumbag", "your\nmy\nloser\nlittle\nbitch\nyour\nass\nas\nfuck\nwhore",
"pedo\nfuck\nstay\naway\nfrom\nminors\nfucking\ntrash\nbitch", "ay\nfuck\nup\ndogshit\nqueer\ndo\ni\nneeda\nsmack\nthe\nfuck\noutta\nyou", "your\nmother\nisnt\nvisiting\nyour\nfuneral\nlonely\nfuck\nill\ntake\nyour\nsoul\nout\nusing\nmy\nbarehands", "bitchass\nnigga\nill bash ur head in pussy\nyour\nmy\nbitch\nweak\nfuck", "niggas\nwill\nshoot\nyour\nface\noff\nshut\nthe\nfuck\nup\nfat\nbitch", "stop\nbeing\nmy\nbitch\nfaggot\nyour\nass\nson\nand\nyour\naccuracy\nis\nshit" "watch\nthat\nfuckin\nmouth\nfaggot\nbitch\nyour\na\nnerdy\nshithead\nyour\nclit\nstinks\nim\nhere\nto\nkill\nyou", "cow\ndick\neating\nass\nnigga", "skanky\nlittle\nfaggot\nyour\nugly\nas\nfuck\nLOL", 
"yo\ngreasy\nfaggot\nfuck\nup\nill\nbeat\nthe\nfuck\noutta\nyou", "bitch\nill\nbreak\nyo\nnose\nsit\nthe\nfuck\ndown\nfaggot", "ugly\nfaggot\ndont\nrun\nwhy\nare\nyou\nnot\ndoing\ndamage", "Nigga\nyour\nhead\nlooks\nlike\na\ndorito\nmy\nnigga\nyou\ngot\nthat\nshit\nfrom\nphineas\nand\nferb\ntell\nme\nwhy\ni\nsaw\nyou\nbeating\nyour\ndick\nto\ndora\nthe\nexplora", "I'LL\nLEAVE\nTHIS\nIMPAIRED\nREJECTS\nBODY\nIN\nA\nDITCH", "NIGGA\nDIED\nBY\nFIRING\nSQUAD", "stop\ncrying\nget\nback\nup", "skanky\nlittle\nfaggot\nyour\nugly\nas\nfuck\nLOL", "ill\nmake\nyou\nend\nyour\nlife\nfrail\nass\nbitch", "Cállate\nla\nboca\nsucio\ncriatura\nespecial\nnegro\nEntraste\na\nmi\npaís\nen\nun\ncontenedor",
"988\nheres\nthe\nsuicide\nhotline\nfrustrated\npedo", "this\nis\nbad\ni\nfucking\nkilled\nyou" "BITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nYOU\nCANT\nCOMPETE\nWITH\nYOUR\nGOD\nBITCH\nWHY\nAM\nI\nOVER\nYOU\nSTOP\nFUCKING\nDYING\nPIGFUCKER\nLOLLOLOOL", "nigga\ni\ncaught\nu\nslapboxing\na\nnigga\nname\ndonitello\nfor\n20\nvbucks\nlike\nshit\nnigga\nyou\nwas\na\nknown\nschool\nthreat\nbecause\nyou\nbrought\na\nbaguette\nto\nschool\nfor\nbring\nyour\npet\nday\nsmelly\nnigga",
"nigga\nthats\nwhy\nyo\nnipples\nare\nbuilt\nlike\nfour\nleaf\nclovers\nthats\nwhy\byo\nmom\nuse\nto\nuppercut\nyou\nin\nfatboy”, “you\nsmoke\nvapes\nout\nyour\nasshole\nweirdo”, “SORRY\nASS\nNIGGA\nUR\nNOT\nSAFE\nFROM\nME\nWEAK\nVIRGIN\nASS\nNIGGA\nUR\nMISERABLE\nAS\nSHIT\nFUCKING\nFAGGOT\nASS\nPEDO\nLOLOL”, “NIGGA\nHOE\nASS\nNIGGA\nDIRTY\nASS\nNIGGA\nSHUT\nUP\nNIGGA\nYOU\nWASTED\nEIGHT\nYEARS\nOF\nYOUR\nLIFE\nIN\nA\nJUNGLE\nTRYNA\nFIND\nA\nLEGENDARY\nPOKEMON\nMY\nNIGGA\nCAUSE\nYOU\nDIRTY\nAS\nFUCK\nMY\nNIGGA\nYOU\nFEEL\nBURPS\nFORM\nIN\nYO\nTHROAT\nAND\nPISS\nYO\nPANTS\nMY\nNIGGA\nYO\nMOTHER\nIS\nA\nCRACK\nADICT\nLOLOO"
]

autoreplies = [
    f"ur shit as fuck pedophile {name}",
    f"She is only 5 get that dick outta her nipples u pedo ",
    f"Yo fuck ass nigga named {name}, ur fuckin ass and u should hang urself with a dildo",
    f"Stop tryna hit me u fuckin diddy {name}",
    f"Fuck ass boy stop drinking horse semen",
    f"nigga ur fuckin ass u shemale pedophile {name}",
    f"{name} how about u kys now fucking twink",
    f"Nigga ur fuckin ass {name}",
    f"YO SHUT THE FUCK UP {name} LOL.",
    f"thats why ur dad left u fuckin loser named {name}",
    f"yo slut stop cutting ur self u fuckin retard",
    f"bitch ass boy named {name} u killed ur self",
    f"and this bitch ass nigga killed himself",
    f"yo\nbitch\nshut\nthe\nfuck\nup\npedo\nass\n{name}",
    f"stop sucking my dick u peon",
    f"ur fuckin ass lol kys now pedo",
    f"ur shit as fuck pedophile {name}",
    f"She is only 5 get that dick outta her nipples u pedo named {name}",
    f"Yo fuck ass nigga named {name}, ur fuckin ass and u should hang urself with a dildo",
    f"Stop tryna hit me u fuckin diddy {name}",
    f"Fuck ass boy stop drinking horse semen",
    f"nigga ur fuckin ass u shemale pedophile {name}",
    f"{name} how about u kys now fucking twink",
    f"Nigga ur fuckin ass {name}",
    f"YO SHUT THE FUCK UP {name} LOL.",
    f"thats why ur dad left u fuckin loser named {name}",
    f"yo slut stop cutting ur self u fuckin retard",
    f"bitch ass boy named {name} u killed ur self",
    f"and this bitch ass nigga killed himself",
    f"yo\nbitch\nshut\nthe\nfuck\nup\npedo\nass{name}",
    f"ur shit as fuck pedophile {name}",
    f"She is only 5 get that dick outta her nipples u pedo named {name}!",
    f"Yo fuck ass nigga named {name}, ur fuckin ass and u should hang urself with a dildo",
    f"Stop tryna hit me u fuckin diddy {name}",
    f"Fuck ass boy stop drinking horse semen",
    f"nigga ur fuckin ass u shemale pedophile {name}",
    f"{name} how about u kys now fucking twink",
    f"Nigga ur fuckin ass {name}",
    f"YO SHUT THE FUCK UP {name} LOL.",
    f"thats why ur dad left u fuckin loser named {name}",
    f"yo slut stop cutting ur self u fuckin retard {name} ",
    f"bitch ass boy named {name} u killed ur self {name} ",
    f"and this bitch ass nigga killed himself {name} ",
    f"yo\nbitch\nshut\nthe\nfuck\nup\npedo\nass{name}" "cringe pedophile {name} ","ugly faggot ass pedo","drop dead maggot","niggas spit on u everywhere u go","do u still cut yourself","isnt this the dork i made eat his on feces on cam LOL","ill cave yo teeth in","dork","soft ass queer","slit your throat pedophile","weak test tube baby","they watching me rip yo teeth out with pliers","sloppy mouth faggot","im ur diety","die faggot","ur weak bitch","ill rip your tongue out","ill erdacite whats left of your species","saggy breast loser","ill send u to god faggot","I WILL FUCKING MURDER YOU WITH MY BARE HANDS JEW","rape victim","insecure cunt","deformed man boobs LOL","pathetic leech make a name for yourself","I WILL STOMP YOUR HEAD IN FRAIL FAGGOT","YO BITCH I SAID SHUT THE FUCK UP WEAK TESTICA EATING FAGGOT ILL FUCKING END YOUR BLOODLINE","freak","ew your a pedo","cringe","yo remember when u used to eat your own feces on camera","u have no friends","illnfuckingnpunchnyournfacenoff","i invoke fear into your heart","saggy breast pedo","obese loser on discord with manboobs","dork with orge ears""dirty ass rodent molester" "u cant beef me","weakling","YO\nBITCH\nSHUT\nTHE\nFUCK\nUP\nWEAK\nASS\nPEDOPHILE\nCRINGE\nCHILDTOUCHER","ill crush every bone in your body slut","frail bitch","ill lynch u nigger","trash\nass\npedophile\nlame\ndork","YO BITCH SPEAK BACK IAN TELL U TO STOP","retard","dweeb","sloppy mouth faggot","your a nobody faggot","weak shitter","nigga cant up funds LOLOLOL lame pooron","ill break your teeth n make u cough blood up for weeks","ill snap your neck faggot","cuck","shit face","kys faggot""nb cares faggot", "YOU SUCK",
    f"dirty ass rodent molester {name} ",
    f"weak prostitute {name} ",
    f"stfu dork ass nigga {name} ",
    f"garbage ass slut {name} ",
    f"ur weak",
    f"why am i so above u rn",
    f"soft ass nigga",
    f"frail slut",
    f"ur slow as fuck",
    f"you cant beat me",
    f"shut the fuck up LOL",
    f"you suck faggot ass nigga be quiet",
]

gcn_messages = ["YOUR BELOW ME", "COMMIT SUICIDE LMAOAO", "LMAOO COME GET BACK IN DISCORD.GG/JUSTICE", "UR A SAD LITTLE PEDO LMAOO", "COME GET MAULED IN DISCORD.GG/JUSTICE",
"UR JUS AS AINT YOU LMAOOO", "JUSTICE RUN THIS SHITTTT", "DIRTY HINDU BITCH", "FEMBOY ASS NIGGA"
]

flood_messages = ["shut the fuck up son get flooded", "weak retard is drowning", "shut the fuck up low IQ retard", "niggas ugly as fuck",
"i dont wanna hear your little sob story faggot", "stop crying get back up", "loser ass fucking dork", "step the fuck up pussy", "u cant beef retard",
"lol ur so sad keep crying bitch", "LOLL i dont fucking like you", "ugly ass awkward loser", "stupid little cuck", 
]

ladder_messages = ["HOW\nDID\nYOU\nGET\nHOED\nLIKE\nTHAT\nLOLL\nYOUR\nA\nBITCH", "SIGN\nYOUR\nLIFE\nAWAY\nTO\nME\nLOSER\nASS\nPEDO\nLOLL","SHUR\nYOUR\nPUSSY\nASS\nMOUTH\nBITCH", "NIGGA\nGETS\nBULLIED\nON\nDAILY\nBASIS",
"TRASH\nNIGGA\nOUTLAST\nME\nRETARD", "MORONIC\nASS\nLITTLE\nFAGGOT\nGET\nBACK\nUP", "WEAL\nASS\nCHAT\nSLAVE\nGET\nDOWN\nFUCK\nBOY", "NEVER\nCOMPETE\nWITH\nA\nGOD",
"UR\nMY\nFUCKING\nSON\nPEASENT", "FOCUS\nUP\nRETARDED\nFUCKBOY\nLOLLOL", "NIGGA\nYOU\nCANT\nSTEP\nSHITTY\nLOSER", "SHUT\nTHE\nFUCK\nUP\nBITCHMADE\nLOSER", "LOL\nYOUR\nA\nSHITTY\nCOM\nREJECT\nLOSER",
"YOUR\nDYING\nTO\nME\nLMFAOO", "STOP\nSTEPPING\nU\nSLOW\nBRAINED\nMORON""EGOUL\nMEU\nE MAI\nMARE\nDECÂT\nPUIUL TĂU\nNEGRU", "NU POȚI\nPROGRAMA\nNU\nAI\nNICIO\nȘANSĂ\nÎMPOTRIVA\nMIEI\nPLÂNGE",
"MY\nMOM\nTYPES\nFASTER\nTHAN\nTHIS\nWHAT\nTHE\nFUCK\nLMFAOO"
]

wordlist = ["fuck up anitsocial faggot", "shitty low tier pedo", "lqbtq ultra supporter", "loser ass nigga snakes his friends for epussy", "unbalanced retarded fuck","ur a retard and what?",
"weak ass faggot", "Indian hindu bitch", "broke ass softie", "pathetic fucking cuck ", "shut the fuck up ", "dumb faggot", "sweet ass nigga", "bitch ass nigga", "dogshit loser",
"scummy pedophile", "pedo nigga touches kids", "faggot likes little boys", "dorkus", "shiity slut", "slutty ass nigga","WATCH\nYOUR\nPUSSY\nASS\nMOUTH\nBITCH", 
"we\ndont\nfuck\nwit\nu\nnigga", "bitchmade nigga ", "ur a cyber bully victim", "u have a hairy pussy", "dirty curry eater", "nigga got beat up by a dyke",
"dumbass bitch ", "nobody likes u geek", "LOL your jus ass aint u?", "crack junk pedophile", "failed reject", "angered cuck", "whos this cuckable reject", "somalian freak fuck", "ur my daughter",
"shitty subhuman", "AND UR WEAK LMFAOAOOA", "hitler crossdresser", "nigga got his rights took", "superintendent whore", "broke his neck",
"shitcan mexican ", "ill murder ur bloodline pedo", "nigga begging for dada attention", "shut the fuck up slow ass dork","fuck up anitsocial faggot", "shitty low tier pedo", "lqbtq ultra supporter", "loser ass nigga snakes his friends for epussy", "unbalanced retarded fuck","ur a retard and what?",
"weak ass faggot", "Indian hindu bitch", "broke ass softie", "pathetic fucking cuck ", "shut the fuck up ", "dumb faggot", "sweet ass nigga", "bitch ass nigga", "dogshit loser",
"scummy pedophile", "pedo nigga touches kids", "faggot likes little boys", "dorkus", "trash bag", "pedo response btw", "faggot ass pedophile stay away from little boys", "stop sexualizing your mom weirdo",
"stinky ass clown", "disowned sperm", 
]

ping_messages = [
"why are you pinging me faggot", "what now nigga?", "dont ping me bitch"
]

message_index = 0  

prefix = ''
intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=prefix, self_bot=True, intents=discord.Intents.default())


def load_tokens(file_path='token.txt'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

tokens = load_tokens()
gc_tasks = {}
kill_tasks = {}
autoreply_tasks = {}
arm_tasks = {}
outlast_tasks = {}
protection_tasks = {}
reactm_running = {}
reactm_tasks = {}
autoreact_users = {}
afkcheck_tasks = {}

outlast_running = False
status_changing_task = None
bold_mode = False
cord_user = False
protection_running = False
antiafk_enabled = False
mping_running = False

current_song = None
is_pr_active = False
snipe_messages = {}
pl_task = None
pressure_task = None
current_prefix = prefix
mimic_users = {}
status_rotate_task = None
rpc = None
rpc_task = None
status_changing_task = None 
massdm_task = None
massgc_task = None
ar_task = None
status_messages = []  
rotate_task = None  
ldr_tasks = {}  
CLIENT_ID = "1309769248746246194"
ldr_task = None
ladder_mode = False
bold_mode = False
reacting = False
tokens_file_path = 'token.txt'
statuses = {}  
new_name = {}
outlast_active = False
outlast_task = None                                                         
react_targets = {}
autoreact_users = {}
dreact_users = {}
force_delete_users = defaultdict(bool) 
gcspam_protection_enabled = False
autogc_enabled = False
gc_whitelist = {}
typing_active = {}  
status_rotation_active = False
emoji_rotation_active = False
current_status = ""
current_emoji = ""
autoreply_tasks = {}
status_changing_task = None


@bot.event
async def on_ready():
    print(f"""logged in as this faggot {bot.user}                                    
                   """)
    

@bot.command()
async def multilast(ctx, user: discord.User):
    global outlast_running
    outlast_running = True
    await ctx.send("```multilast enabled```")
    await ctx.message.delete()
    class SharedCounter:
        def __init__(self):
            self.value = 1
            self.lock = asyncio.Lock()
        
        async def increment(self):
            async with self.lock:
                current = self.value
                self.value += 1
                return current
    
    shared_counter = SharedCounter()

    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        

        token_counter = 1
        
        while outlast_running:
            message = random.choice(outlast_messages)
            global_count = await shared_counter.increment()
            
            payload = {
                'content': f"{message}\n{user.mention}```{global_count}```"
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://discord.com/api/v9/channels/{ctx.channel.id}/messages', 
                                      headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        print(f"Message sent with token: {token}")
                        token_counter += 1
                    elif resp.status == 429:
                        print(f"Rate limited with token: {token}. Retrying...")
                        await asyncio.sleep(1)
                    else:
                        print(f"Failed to send message with token: {token}. Status code: {resp.status}")

            await asyncio.sleep(0.1)

    tasks = [send_message(token) for token in tokens]
    await asyncio.gather(*tasks)

@bot.command()
async def multilastoff(ctx):
    global outlast_running
    if outlast_running:
        outlast_running = False  
        await ctx.send("```multilast disabled```")
    else:
        await ctx.send("```multilast is off```")
    await ctx.message.delete()

@bot.command()
async def gcn(ctx, user: discord.User):
    global protection_running
    protection_running = True
    channel_id = ctx.channel.id
    await ctx.message.delete()
    class SharedCounter:
        def __init__(self):
            self.value = 1
            self.lock = asyncio.Lock()
        
        async def increment(self):
            async with self.lock:
                current = self.value
                self.value += 1
                return current

    shared_counter = SharedCounter()

    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        last_send_time = 0
        backoff_time = 0.1
        
        while protection_running:
            try:
                current_time = time.time()
                time_since_last = current_time - last_send_time
                
                if time_since_last < backoff_time:
                    await asyncio.sleep(backoff_time - time_since_last)
                
                message = random.choice(gcn_messages)
                count = await shared_counter.increment()
                
                payload = {
                    'content': f"{user.mention} {message}\n```{count}```"
                }

                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        f'https://discord.com/api/v9/channels/{ctx.channel.id}/messages', 
                        headers=headers, 
                        json=payload
                    ) as resp:
                        if resp.status == 200:
                            print(f"Protection message sent with token: {token[-4:]}")
                            backoff_time = max(0.1, backoff_time * 0.95)
                            last_send_time = time.time()
                        elif resp.status == 429:
                            retry_after = float((await resp.json()).get('retry_after', 1))
                            print(f"Rate limited with token: {token[-4:]}. Waiting {retry_after}s...")
                            backoff_time = min(2.0, backoff_time * 1.5)
                            await asyncio.sleep(retry_after)
                        else:
                            print(f"Failed to send message with token: {token[-4:]}. Status: {resp.status}")
                            await asyncio.sleep(1)

                await asyncio.sleep(random.uniform(0.1, 0.3))
                
            except Exception as e:
                print(f"Error in send_message for token {token[-4:]}: {str(e)}")
                await asyncio.sleep(1)

    async def change_name(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        last_change_time = 0
        backoff_time = 0.5
        
        while protection_running:
            try:
                current_time = time.time()
                time_since_last = current_time - last_change_time
                
                if time_since_last < backoff_time:
                    await asyncio.sleep(backoff_time - time_since_last)
                
                gc_name = random.choice(gcn_messages)
                count = await shared_counter.increment()
                
                payload = {
                    'name': f"{gc_name} {count}"
                }

                async with aiohttp.ClientSession() as session:
                    async with session.patch(
                        f'https://discord.com/api/v9/channels/{channel_id}', 
                        headers=headers, 
                        json=payload
                    ) as resp:
                        if resp.status == 200:
                            print(f"GC name changed with token: {token[-4:]}")
                            backoff_time = max(0.5, backoff_time * 0.95)
                            last_change_time = time.time()
                        elif resp.status == 429:
                            retry_after = float((await resp.json()).get('retry_after', 1))
                            print(f"Rate limited with token: {token[-4:]}. Waiting {retry_after}s...")
                            backoff_time = min(5.0, backoff_time * 1.5)
                            await asyncio.sleep(retry_after)
                        else:
                            print(f"Failed to change GC name with token: {token[-4:]}. Status: {resp.status}")
                            await asyncio.sleep(1)

                await asyncio.sleep(random.uniform(0.5, 1.0))
                
            except Exception as e:
                print(f"Error in change_name for token {token[-4:]}: {str(e)}")
                await asyncio.sleep(1)

    message_tasks = [send_message(token) for token in tokens]
    name_tasks = [change_name(token) for token in tokens]
    all_tasks = message_tasks + name_tasks
    
    combined_task = asyncio.gather(*all_tasks)
    protection_tasks[channel_id] = combined_task
    


@bot.command()
async def gcnoff(ctx):
    global protection_running
    channel_id = ctx.channel.id

    if channel_id in protection_tasks:
        protection_running = False
        task = protection_tasks.pop(channel_id)
        task.cancel()
        await ctx.send("```gcn disabled```")
    else:
        await ctx.send("```gcn is off```")
    await ctx.message.delete()



@bot.command()
async def fill(ctx):
    tokens_file_path = 'token.txt'
    tokens = load_tokens(tokens_file_path)
    group_channel = ctx.channel
    await ctx.message.delete()
    for token in tokens:
        user_client = discord.Client(intents=intents)

        @user_client.event
        async def on_ready():
            print(f'Logged in as {user_client.user} using token {token[-4:]}.')
            try:
                await group_channel.add_recipients(user_client.user)
                print(f'Added {user_client.user} to the group chat')
            except discord.errors .Forbidden:
                print("Bot doesn't have permission to add to the group chat.")
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    retry_after = int(e.response.headers.get('Retry-After', 1))
                    print(f"Token {token[-4:]} is being rate limited. Waiting for {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                elif e.status == 401:
                    print(f"Token {token[-4:]} is invalid. Skipping...") 
                else:
                    print(f"HTTP error occurred: {e}")
            await user_client.close()

        await user_client.start(token, bot=False)

def read_tokens(filename='token.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

async def update_presence1(token, details):
    if token.strip() == "":
        print("Skipping empty token")
        return

    client = discord.Client()

    @client.event
    async def on_ready():
        activity = discord.Streaming(
            name=details, 
            url='https://www.twitch.tv/ex'
        )
        await client.change_presence(activity=activity)

    try:
        await client.start(token, bot=False)  
    except discord.LoginFailure:
        print(f"Failed to login with token: {token} - Invalid token")
    except Exception as e:
        print(f"An error occurred with token: {token} - {e}")

async def streamall(ctx, messages):
    tokens = read_tokens('token.txt')  
    details = [random.choice(messages) for _ in range(len(tokens))]

    tasks = [update_presence1(token, detail) for token, detail in zip(tokens, details)]
    await asyncio.gather(*tasks)
    await ctx.send(f"Statuses updated for all tokens")


async def rename_display_name(token, new_name):

    try:
        user_client = discord.Client()

        @user_client.event
        async def on_ready():
            print(f'Logged in as {user_client.user} using token {token[-4:]}.')
            try:
                for guild in user_client.guilds:
                    member = guild.get_member(user_client.user.id)
                    if member:
                        await member.edit(nick=new_name)
                        print(f"Renamed display name to {new_name} in server {guild.name} for token {token[-4:]}")
                    else:
                        print(f"Member not found in server {guild.name} for token {token[-4:]}")
                
            except discord.errors.Forbidden:
                print(f"Token {token[-4:]} doesn't have permission to change the display name in some servers.")
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    retry_after = int(e.response.headers.get('Retry-After', 1))
                    print(f"Token {token[-4:]} is being rate limited. Waiting for {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                elif e.status == 401:
                    print(f"Token {token[-4:]} is invalid. Skipping...")
                else:
                    print(f"HTTP error occurred with token {token[-4:]}: {e}")
            except Exception as e:
                print(f"Error occurred with token {token[-4:]}: {e}")
            finally:
                await user_client.close()


        await user_client.start(token, bot=False)

    except Exception as e:
        print(f"Failed to process token {token[-4:]}: {str(e)}")


@bot.command()
async def kill(ctx, user_id: str):
    channel_id = ctx.channel.id
    await ctx.message.delete()
    async def send_message(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        random_sentence = random.choice(wordlist)
        payload = {
            'content': f"# {random_sentence}\n{user_id}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload) as resp:
                if resp.status == 200:
                    print(f"Message sent with token: {token}")
                elif resp.status == 429:
                    print(f"Rate limited with token: {token}. Retrying...")
                    await asyncio.sleep(0.1)
                else:
                    print(f"Failed to send message with token: {token}. Status code: {resp.status}")

    async def kill_loop():
        while True:
            tasks = [send_message(token) for token in tokens]
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1)

    task = bot.loop.create_task(kill_loop())
    kill_tasks[(user_id, channel_id)] = task

@bot.command()
async def killoff(ctx):
    channel_id = ctx.channel.id
    tasks_to_stop = [key for key in kill_tasks.keys() if key[1] == channel_id]
    
    if tasks_to_stop:
        for user_id in tasks_to_stop:
            task = kill_tasks.pop(user_id)
            task.cancel()
    await ctx.send("```kill disabled```")

    await ctx.send("```kill is off```")

    await ctx.message.delete()


@bot.command()
async def rpcall(ctx, *, message: str):  
    messages = message.split(',') 
    await ctx.message.delete() 
    await streamall(ctx, messages)

async def change_status():
    await bot.wait_until_ready()
    while True:
        for status in statuses:
            await bot.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/ex"))
            await asyncio.sleep(10) 
    await ctx.message.delete()

@bot.command()
async def token(ctx):
    tokens_list = load_tokens()
    if not tokens_list:
        await ctx.send("```no tokens found in token.txt```")
        return
        await ctx.message.delete()
    async def get_username(token):
        try:
            intents = discord.Intents.default()
            client = commands.Bot(command_prefix='.', self_bot=True, intents=intents)
            
            username = None
            
            @client.event
            async def on_ready():
                nonlocal username
                username = f"{client.user.name}#{client.user.discriminator}"
                await client.close()
            
            await client.start(token, bot=False)
            return username
            
        except discord.LoginFailure:
            return f"Invalid token ending in {token[-4:]}"
        except Exception as e:
            return f"Error with token {token[-4:]}: {str(e)}"

    message = await ctx.send("```fetching token usernames..```")
    
    usernames = []
    for i, token in enumerate(tokens_list, 1):
        username = await get_username(token)
        if username:
            usernames.append(f"{i}. {username}")
    
    formatted_message = "```\n TOKENS \n" + "\n".join(usernames) + "\n```"
    await message.edit(content=formatted_message)


    @bot.command()
    async def rename(ctx, *, new_name: str):

     tokens_file_path = 'token.txt'
    

    if not os.path.exists(tokens_file_path):

        return
    
    with open(tokens_file_path, 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    
    if not tokens:
        await ctx.send("```no tokens found in token.txt```")
        return

    for token in tokens:
        await rename_display_name(token, new_name)


async def pl_task_function(channel, target):
    """
    Continuously send flood_messages to the target in the given channel.
    """
    while True:
        try:
            batch = random.sample(flood_messages, 10)
            messages = [
                f"# _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n # _ _ \n  #  {flood_messages} \n {target.mention if hasattr(target, 'mention') else target}"
                for flood_messages in batch
            ]

            
            await asyncio.gather(*(channel.send(message) for message in messages))

           
            await asyncio.sleep(0.5)  

        except Exception as e:
            print(f"Error occurred during flood loop: {e}")
            await asyncio.sleep(0.01)  


@bot.command(name='flood')
async def pack(ctx, target: str = None):
    await ctx.message.delete()

    if target is None:
        await ctx.send('```mention a user to flood```')
        return

    global pl_task
    if pl_task and not pl_task.done():
        await ctx.send("```flood enabled```")
        return

    if isinstance(ctx.channel, discord.DMChannel): 

        member = ctx.author
        channel = ctx.channel  
    elif isinstance(ctx.channel, (discord.TextChannel, discord.GroupChannel)):  
        try:
            member = await commands.MemberConverter().convert(ctx, target)
            channel = ctx.channel  
        except commands.MemberNotFound:
            await ctx.send('could not find user')
            return
    else:
        await ctx.send('unsupported channel type')
        return

    pl_task = asyncio.create_task(pl_task_function(channel, member))
    await ctx.send(f"started flooding {member.mention if hasattr(member, 'mention') else member}")

@bot.command(name='floodoff')
async def sa(ctx):
    global pl_task

    if pl_task and not pl_task.done():
        pl_task.cancel()
        pl_task = None
        await ctx.send("```flood disabled```")



@bot.command()
async def ar(ctx, user: discord.User):
    channel_id = ctx.channel.id
    await ctx.message.delete()
    await ctx.send(f"```ar enabled for {user.name}```")

    async def send_autoreply(message):
        while True:  
            try:
                random_reply = random.choice(autoreplies)
                await message.reply(random_reply)
                print(f"Successfully replied to {user.name}")
                break  
            except discord.errors.HTTPException as e:
                if e.status == 429:  
                    try:
                        response_data = await e.response.json()
                        retry_after = response_data.get('retry_after', 1)
                    except:
                        retry_after = 1 
                    print(f"Rate limited, waiting {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                else:
                    print(f"HTTP Error: {e}, retrying...")
                    await asyncio.sleep(1)
            except Exception as e:
                print(f"Error sending message: {e}, retrying...")
                await asyncio.sleep(1)

    async def reply_loop():
        def check(m):
            return m.author == user and m.channel == ctx.channel

        while True:
            try:
                message = await bot.wait_for('message', check=check)
                asyncio.create_task(send_autoreply(message))
                await asyncio.sleep(0.1)  
            except Exception as e:
                print(f"Error in reply loop: {e}")
                await asyncio.sleep(1)
                continue


    task = bot.loop.create_task(reply_loop())
    autoreply_tasks[(user.id, channel_id)] = task

@bot.command()
async def aroff(ctx):
    channel_id = ctx.channel.id
    tasks_to_stop = [key for key in autoreply_tasks.keys() if key[1] == channel_id]
    
    if tasks_to_stop:
        for user_id in tasks_to_stop:
            task = autoreply_tasks.pop(user_id)
            task.cancel()
        await ctx.send("```ar disabled```")
    else:
        await ctx.send("```no ar in this channel```")
    await ctx.message.delete()

@bot.command(name='ladder')
async def ldr(ctx, member: discord.Member = None):
    global ldr_task


    target = member if member else ctx.author


    await ctx.message.delete()




    async def send_messages():
        while True:
            try:
                
                random.shuffle(ladder_messages)

                
                for line in ladder_messages:
                   
                    formatted_message = '\n'.join([f"# {word}" for word in line.split()]) + f"\n{target.mention}\n ```DONT FOLD```"

                    
                    if isinstance(ctx.channel, discord.DMChannel): 
                        await ctx.author.send(formatted_message)
                    else: 
                        await ctx.send(formatted_message)

                    
                    await asyncio.sleep(0.1)

               
                random.shuffle(ladder_messages)  

            except asyncio.CancelledError:
                
                print("Task has been canceled.")
                break
            except Exception as e:
                
                print(f"An error occurred: {e}")
                await asyncio.sleep(1)  


    ldr_task = bot.loop.create_task(send_messages())



@bot.command(name='ladderoff')
async def stop_ldr(ctx):
    global ldr_task

    if ldr_task and not ldr_task.done():

        ldr_task.cancel()
        await ctx.send("```ladder disabled```")
    else:
        await ctx.send("```ladder is off```")



@bot.command()
async def whore(ctx, *args):
    global outlast_active, outlast_task

    
    if not args:
        await ctx.send("```mention a user```")
        return

    
    user_mentioned = None

    if len(args) == 1:
        arg = args[0]
        
        
        if arg.startswith("<@") and arg.endswith(">"):
            user_mentioned = arg  
        else:
          
            user_mentioned = f"<@{arg}>"
    await ctx.message.delete()
    if not user_mentioned:
        await ctx.send("```user not mentioned```")
        return

 
    if outlast_active:
        await ctx.send("```whore already enabled```")
        return

    outlast_active = True

    async def outlast_messages():
        while outlast_active:
            try:
                response = random.choice(whore_wordlist)

        
                await ctx.send(f"{response}\n{user_mentioned}")

                await asyncio.sleep(0.1)

            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Error: {e}")

    
    outlast_task = asyncio.create_task(outlast_messages())

@bot.command()
async def whoreoff(ctx):
    global outlast_active, outlast_task

    if outlast_active:
        outlast_active = False
        if outlast_task:
            outlast_task.cancel()
            await ctx.send("```whore disabled```")
            await ctx.message.delete()



@bot.command(name='ping')
async def pr(ctx):
    global is_pr_active

    
    if is_pr_active:
        await ctx.send("")
        return

    is_pr_active = True
    await ctx.send("```ping enabled```")

    def check_interaction(message):
        
        return (
            (ctx.author.mentioned_in(message) or message.reference and message.reference.resolved.author == bot.user)
            and message.author != bot.user
        )

    while is_pr_active:
        try:
            message = await bot.wait_for('message', check=check_interaction)
            global message_index

            await message.channel.send(f"{ping_messages[message_index]} ")
            message_index = (message_index + 1) % len(ping_messages) 

        except asyncio.CancelledError:
            break


@bot.command(name='pingoff')
async def ps(ctx):
    global is_pr_active

    if is_pr_active:
        is_pr_active = False
        await ctx.send("```ping disabled```")
    else:
        await ctx.send("```ping is off```")



@bot.command(name='spam')
async def say(ctx, times: int=None, *, message=None):
    await ctx.message.delete()
    if times is None:
        await ctx.send(f'```{bot.command_prefix}spam <times> <message>```')
        return
        if message is None:
            await ctx.send(f'```{bot.command_prefix}spam <times> <message>```')
            return
    for _ in range(times):
        await ctx.send(message)  



@bot.command()
async def react(ctx, user: discord.User, emoji: str):
    autoreact_users[user.id] = emoji
    await ctx.send(f"```react enabled for {user.name}```")
    await ctx.message.delete()
@bot.command()
async def reactoff(ctx, user: discord.User):
    if user.id in autoreact_users:
        del autoreact_users[user.id]
        await ctx.send(f"```react disabled for {user.name}```")
    else:
        await ctx.send("```react is off```")    
    await ctx.message.delete()
@bot.event
async def on_message(message):

    if message.author.bot:
        return


    if message.author.id in react_targets:
        await message.add_reaction(react_targets[message.author.id])


    await bot.process_commands(message)



@bot.command()
async def dreact(ctx, user: discord.User, *emojis):
    if not emojis:
        await ctx.send("```no emoji or user provided```")
        return      
    dreact_users[user.id] = [list(emojis), 0]  
    await ctx.send(f"```dreact enabled for {user.name}```")
    await ctx.message.delete()
@bot.command()
async def dreactoff(ctx, user: discord.User):
    if user.id in dreact_users:
        del dreact_users[user.id]
        await ctx.send(f"```dreact disabled for {user.name}```")
    else:
        await ctx.send("```dreact is off```")   
    await ctx.message.delete()


@bot.event
async def on_message(message):
    if message.author == bot.user and message.content.startswith('.'):
        return

    for user_id, emoji in autoreact_users.items():
        if message.author.id == user_id:
            try:
                await message.add_reaction(emoji)
            except Exception as e:
                print(e)

    for user_id, data in dreact_users.items():
        if message.author.id == user_id:
            emojis = data[0]
            current_index = data[1]
            try:
                await message.add_reaction(emojis[current_index])
                data[1] = (current_index + 1) % len(emojis)
            except Exception as e:
                print(e)


    if force_delete_users[message.author.id]:
        try:
            await message.delete()
        except:
            pass

    await bot.process_commands(message)



@bot.command(name='prefix')
async def prefix(ctx, new_prefix=None):
    await ctx.message.delete()
    if new_prefix is None:
        await ctx.send(f'```its prefix <prefix>```')
        return
    bot.command_prefix = str(new_prefix)
    await ctx.send(f'```prefix is now {new_prefix}```')
    await ctx.message.delete()


@bot.command()
async def reload(ctx):
    await ctx.send("```reloading bot...```")
    os.execv(sys.executable, ['python'] + sys.argv)
    await ctx.message.delete()


@bot.command()
async def av(ctx, user: discord.User = None):
    
    try:
        user = user or ctx.author
        await ctx.send(user.avatar_url) 
    except Exception as e:
        await ctx.send(f"failed to get avatar: {e}")
    await ctx.message.delete() 


@bot.command()
async def python(ctx, *, script_name: str):
    
    try:

        if not script_name.endswith('.py'):
            await ctx.send("```add .py at the end```")
            return
       
        if not os.path.isfile(script_name):
            await ctx.send(f"```script {script_name} isnt in py```")
            return

        
        subprocess.Popen(["python", script_name])
        await ctx.send(f"```starting {script_name}```")

    except Exception as e:
        await ctx.send(f"failed to start script: {e}")
    await ctx.message.delete()


@bot.command()
async def purge(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("```purge 1-100 messages```")
        return

    await ctx.message.delete()


    if isinstance(ctx.channel, discord.TextChannel):
      
        messages = await ctx.channel.history(limit=amount + 1).flatten()

        
        await ctx.channel.bulk_delete(messages)

        confirmation_message = await ctx.send(f"```deleted {amount} messages```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()


    elif isinstance(ctx.channel, discord.DMChannel):
     
        messages = await ctx.channel.history(limit=amount).flatten()

        bot_messages = [msg for msg in messages if msg.author == bot.user]
        for msg in bot_messages:
            await msg.delete()

        confirmation_message = await ctx.send(f"```deleted {len(bot_messages)} messages```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()

    elif isinstance(ctx.channel, discord.GroupChannel):
  
        messages = await ctx.channel.history(limit=amount).flatten()

        deleted_count = 0
        for message in messages:
            if message.author == bot.user:
                await message.delete()
                deleted_count += 1

        confirmation_message = await ctx.send(f"```deleted {deleted_count} messages```")
        await asyncio.sleep(0.1)
        await confirmation_message.delete()


@bot.command(name="forcepurge")
async def forcepurge(ctx, action: str, member: discord.Member = None):
    if action.lower() == "toggle":
        if member is None:
            await ctx.send("```mention a user```")
            return
        force_delete_users[member.id] = not force_delete_users[member.id]
        status = "enabled" if force_delete_users[member.id] else "disabled"
        await ctx.send(f"```forcepurge for {member.display_name} has been {status}.```")

    elif action.lower() == "list":

        enabled_users = [f"```<@{user_id}>```" for user_id, enabled in force_delete_users.items() if enabled]
        if enabled_users:
            await ctx.send("```users with forcepurge enabled:\n```" + "\n".join(enabled_users))
        else:
            await ctx.send("```forcepurge is off```")

    elif action.lower() == "clear":
        force_delete_users.clear()
        await ctx.send("```disabled forcepurge```")

    else:
        await ctx.send("```use `toggle`, `list`, or `clear````")
        await ctx.message.delete()

@bot.command()
async def massdm(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'```massdm <message>```')
        return  
    for friend in bot.user.friends:
        try:
            await friend.send(message)
            print(f"message sent to {friend.name}#{friend.discriminator}")
        except discord.Forbidden:
            print(f"Failed to send message to {friend.name}#{friend.discriminator} (blocked or dms are off)")
        except Exception as e:
            print(f"Error sending message to {friend.name}#{friend.discriminator}: {e}")
        await asyncio.sleep(4.0)
        await ctx.message.delete()




@bot.command()
async def massgc(ctx, *, message: str):

    global massgc_task

    if massgc_task and not massgc_task.done():
        await ctx.send("```use stopmass to disable```")
        return

    async def dm_group_chats():
        try:
            group_chats = [gc for gc in bot.private_channels if isinstance(gc, discord.GroupChannel)]
            for gc in group_chats:
                try:
                    await gc.send(message)
                    await asyncio.sleep(0.50)  
                except Exception as e:
                    print(f"could not send message to gc{gc}: {e}")
            await ctx.send("mass gc finished")
        except Exception as e:
            await ctx.send(f"error while massgc {e}")

    massgc_task = asyncio.create_task(dm_group_chats())
    await ctx.send("```message sending to all groupchats.```")
    await ctx.message.delete()



@bot.command(name='massunadd')
async def massunadd(ctx):

    try:
        
        friends = bot.user.friends

        if not friends:
            await ctx.send("```you have no friends ```")
            return

        await ctx.send(f"```unfriending all {len(friends)} users```")

        
        for friend in friends:
            await friend.remove_friend() 
            await asyncio.sleep(1)  
        
        await ctx.send("```unfriended all users```")

    except Exception as e:
        await ctx.send(f"an error occurred: {str(e)}")   
    await ctx.message.delete()


@bot.command()
async def stopmass(ctx):

    global massdm_task, massgc_task

    if massdm_task and not massdm_task.done():
        massdm_task.cancel()
        await ctx.send("```mass disabled```")
    else:
        await ctx.send("```mass is stopped```")

    if massgc_task and not massgc_task.done():
        massgc_task.cancel() 
        await ctx.message.delete()



@bot.command()
async def antigc(ctx):
    global gcspam_protection_enabled
    gcspam_protection_enabled = not gcspam_protection_enabled

    if gcspam_protection_enabled:
        await ctx.send(f"```ansi\n antigc enabled```")
    else:
        await ctx.send(f"```ansi\n antigc disabled```")
    await ctx.message.delete()


@bot.event
async def on_private_channel_create(channel):
    if gcspam_protection_enabled and isinstance(channel, discord.GroupChannel):
        try:
            headers = {
                'Authorization': bot.http.token,
                'Content-Type': 'application/json'
            }
            params = {
                'silent': 'true'
            }
            async with aiohttp.ClientSession() as session:
                async with session.delete(f'https://discord.com/api/v9/channels/{channel.id}', headers=headers, params=params) as resp:
                    if resp.status == 200:
                        print(f"left group chat silently: {channel.id}")
                    elif resp.status == 429:
                        retry_after = int(resp.headers.get("Retry-After", 1))
                        print(f"Rate limited. Retrying after {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                    else:
                        print(f"Failed to leave group chat. Status code: {resp.status}")
        except Exception as e:
            print(f"Error leaving group DM: {e}")

    if not autogc_enabled:
        return

    try:
        async for msg in channel.history(limit=1):
            if msg.author.id in gc_whitelist:
                return
    except:
        pass


@bot.command()
async def typing(ctx, time: str, channel: discord.TextChannel = None):
    await ctx.message.delete()
    
    if channel is None:
        channel = ctx.channel

    total_seconds = 0


    try:
        if time.endswith('s'):
            total_seconds = int(time[:-1]) 
        elif time.endswith('m'):
            total_seconds = int(time[:-1]) * 60  
        elif time.endswith('h'):
            total_seconds = int(time[:-1]) * 3600  
        else:
            total_seconds = int(time)  
    except ValueError:
        await ctx.send("```provide time format (5s, 2m, 1h)```")
        return

   
    typing_active[channel.id] = True

    try:
        async with channel.typing():
            await ctx.send(f"```enabled typing for {total_seconds}```")
            await asyncio.sleep(total_seconds)  
    except Exception as e:
        await ctx.send("```error triggering typing```")
    finally:
        typing_active.pop(channel.id, None)
    await ctx.message.delete()

@bot.command()
async def typingoff(ctx, channel: discord.TextChannel = None):

    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel

    if channel.id in typing_active:
        typing_active.pop(channel.id)  
        await ctx.send(f"```disabled typing in {channel.name}```")
    else:
        await ctx.send(f"```typing is off```")
    


@bot.command()
async def rpc(ctx, *, statuses_list: str):
    global status_changing_task
    global statuses
    
    statuses = statuses_list.split(',')
    statuses = [status.strip() for status in statuses]
    
    if status_changing_task:
        status_changing_task.cancel()
    
    status_changing_task = bot.loop.create_task(change_status())
    await ctx.message.delete()


@bot.command()
async def rpcoff(ctx):
    global status_changing_task
    
    if status_changing_task:
        status_changing_task.cancel()
        status_changing_task = None
        await bot.change_presence(activity=None)  
        await ctx.send(f"```rpc disabled```")
    else:
        await ctx.send(f"```rpc is off```")
    await ctx.message.delete()



@bot.command()
async def stream(ctx, *, activity: str):
    
    try:
        
        await bot.change_presence(activity=discord.Streaming(name=activity, url="https://www.twitch.tv/aa"))
        await ctx.send(f"```stream enabled: {activity}```")
    except Exception as e:
        await ctx.send(f"failed to enable streaming: {e}")
    await ctx.message.delete()


@bot.command()
async def streamoff(ctx):

    try:
        await bot.change_presence(activity=None)  
        await ctx.send("```stream disabled```")
    except Exception as e:
        await ctx.send(f"failed to disable streaming: {e}")
    await ctx.message.delete()


@bot.command()
async def playing(ctx, *, activity: str):

    try:
        await bot.change_presence(activity=discord.Game(name=activity))
        await ctx.send(f":playing enabled {activity}")
    except Exception as e:
        await ctx.send(f"failed to enable playing: {e}")
    await ctx.message.delete()
    

async def set_streaming_status(message):

    formatted_message = "\n".join(message.split(",")[:10]) 
    await bot.change_presence(
        activity=discord.Streaming(name=formatted_message, url="https://twitch.tv/aa")
    )


@bot.command(name='rstatus')
async def rotate_status(ctx, *, statuses: str):
    global status_rotation_active, current_status, current_emoji
    await ctx.message.delete()
    
    status_list = [s.strip() for s in statuses.split(',')]
    
    if not status_list:
        await ctx.send("```separate statuses by commas```", delete_after=3)
        return
        await ctx.message.delete()

    current_index = 0
    status_rotation_active = True
    
    async def update_status_emoji():
        json_data = {
            'custom_status': {
                'text': current_status,
                'emoji_name': current_emoji
            }
        }

        custom_emoji_match = re.match(r'<a?:(\w+):(\d+)>', current_emoji)
        if custom_emoji_match:
            name, emoji_id = custom_emoji_match.groups()
            json_data['custom_status']['emoji_name'] = name
            json_data['custom_status']['emoji_id'] = emoji_id
        else:
            json_data['custom_status']['emoji_name'] = current_emoji

        async with aiohttp.ClientSession() as session:
            try:
                async with session.patch(
                    'https://discord.com/api/v9/users/@me/settings',
                    headers={'Authorization': bot.http.token, 'Content-Type': 'application/json'},
                    json=json_data
                ) as resp:
                    await resp.read()
            finally:
                await session.close()

    await ctx.send(f"```rstatus enabled```")
    
    try:
        while status_rotation_active:
            current_status = status_list[current_index]
            await update_status_emoji()
            await asyncio.sleep(8)
            current_index = (current_index + 1) % len(status_list)
                
    finally:
        current_status = ""
        await update_status_emoji()
        status_rotation_active = False


@bot.command(name='rstatusoff')
async def stop_rotate_status(ctx):
    global status_rotation_active
    status_rotation_active = False
    await ctx.send("```rstatus disabled```", delete_after=3)
    await ctx.message.delete()



@bot.command(name='remoji')
async def rotate_emoji(ctx, *, emojis: str):
    global emoji_rotation_active, current_emoji, status_rotation_active
    await ctx.message.delete()
    
    emoji_list = [e.strip() for e in emojis.split(',')]
    
    if not emoji_list:
        await ctx.send("```separate emojis by commas```", delete_after=3)
        return
        await ctx.message.delete()
    current_index = 0
    emoji_rotation_active = True
    
    async def update_status_emoji():
        json_data = {
            'custom_status': {
                'text': current_status,
                'emoji_name': current_emoji
            }
        }
        
        custom_emoji_match = re.match(r'<a?:(\w+):(\d+)>', current_emoji)
        if custom_emoji_match:
            name, emoji_id = custom_emoji_match.groups()
            json_data['custom_status']['emoji_name'] = name
            json_data['custom_status']['emoji_id'] = emoji_id
        else:
            json_data['custom_status']['emoji_name'] = current_emoji

        async with aiohttp.ClientSession() as session:
            try:
                async with session.patch(
                    'https://discord.com/api/v9/users/@me/settings',
                    headers={'Authorization': bot.http.token, 'Content-Type': 'application/json'},
                    json=json_data
                ) as resp:
                    await resp.read()
            finally:
                await session.close()

    await ctx.send(f"```remoji enabled```")
    await ctx.message.delete()
    try:
        while emoji_rotation_active:
            current_emoji = emoji_list[current_index]
            await update_status_emoji()
            await asyncio.sleep(8)
            current_index = (current_index + 1) % len(emoji_list)
                
    finally:
        current_emoji = ""
        await update_status_emoji()
        emoji_rotation_active = False


@bot.command(name='remojioff')
async def stop_rotate_emoji(ctx):
    global emoji_rotation_active
    emoji_rotation_active = False
    await ctx.send("```remoji disabled```", delete_after=3)
    await ctx.message.delete()

@bot.command()
async def swat(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    gender = ["Male", "Female", "Non-Binary", "Other"]
    age = str(random.randint(18, 50))
    height = ['5\'5\"', '5\'8\"', '6\'0\"', '6\'2\"']
    location = ["1305 Tarragon Dr Flower Mound, Texas(TX), 75028", "28261 W Thome Rd Rock Falls, Illinois(IL), 61071", "1508 2nd St NW Bowman, North Dakota(ND), 58623", "60 Gertrude Rd Dalton, Massachusetts(MA), 01226",]
    occupation = ["Software Engineer", "Artist", "Teacher", "Chef"]
    name = ['Alex Johnson', 'Jamie Lee', 'Taylor Smith', 'Jordan Brown', 'Alice Jordan', 'Kaylee Brown', 'Jesse Sowders']

    await ctx.send(f"swatting {user.mention}...\n")
    await asyncio.sleep(1)

    await ctx.send(f"```📞 *9-1-1: Hello, what is ur emergency*```")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} my name is {random.choice(name)} i am very scared my parents were fighting and then i heard a big band like a bomb. . . .")
    await asyncio.sleep(1)
    
    await ctx.send(f"📞 okay calm down and get somewhere safe were do you live?")
    await asyncio.sleep(1)

    await ctx.send(f"i- i live at {random.choice(location)} please hurrry ")
    await asyncio.sleep(1)

    await ctx.send(f"📞 SWAT is coming shortly remain safe we will arrive soon")
    await asyncio.sleep(1)


    await ctx.send(f"🚓 SWAT: starts breaking down {user.mention} door ")
    await asyncio.sleep(1)

    await ctx.send(f"https://media.discordapp.net/attachments/1310177406732075101/1312274470504890421/b9b7b37cb0cf5e495d6512d30c56a4fb.gif?ex=674be656&is=674a94d6&hm=139874281c9b4d402eab13afd0669cd07505a18147aea95fa75277706ca32da5&=")
    await asyncio.sleep(1)
                        
    await ctx.send(f"🚓 SWAT: YOUR UNDERARRESTRED {user.mention}  ")
    await asyncio.sleep(1)

    await ctx.send(f"🚓 SWAT: targets {user.mention}")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} I DIDN'T DO ANYTHING HELP \n")
    await asyncio.sleep(1)

    await ctx.send(f"🚓 SWAT: GET DOWN ON THE FLOOR {user.mention}")
    await asyncio.sleep(1)

    await ctx.send(f"{user.mention} I DIDNT DO ANYTHING HELP \n")
    await asyncio.sleep(1)


    await ctx.send(f"*🚓 SWAT: locks up {user.mention}*")
    await asyncio.sleep(1)

    await ctx.send(f"Successfully swatted {user.mention} \n")
    await asyncio.sleep(1)
    
    await ctx.send(f"```Details:```"
                   f"```Name: {random.choice(name)}\n"
                   f"Gender: {random.choice(gender)}\n"
                   f"Age: {age}\n"
                   f"Height: {random.choice(height)}\n"
                   f"Location: {random.choice(location)}\n"
                   f"Occupation: {random.choice(occupation)}\n```")
    


@bot.command()
async def hack(ctx, user: discord.Member=None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
    content=f"```Successfully hacked {user}\n"
            f"Name: {random.choice(name)}\n"
            f"Gender: {random.choice(gender)}\n"
            f"Age: {age}\n"
            f"Height: {random.choice(height)}\n"
            f"Weight: {weight}\n"
            f"Hair Color: {random.choice(hair_color)}\n"
            f"Skin Color: {random.choice(skin_color)}\n"
            f"DOB: {dob}\n"
            f"Location: {random.choice(location)}\n"
            f"Phone: {phone}\n"
            f"E-Mail: {user.name + random.choice(email)}\n"
            f"Passwords: {', '.join(random.choices(password, k=3))}\n"
            f"Occupation: {random.choice(occupation)}\n"
            f"Annual Salary: {random.choice(salary)}\n"
            f"Ethnicity: {random.choice(ethnicity)}\n"
            f"Religion: {random.choice(religion)}\n"
            f"Sexuality: {random.choice(sexuality)}\n"
            f"Education: {random.choice(education)}\n"
            "```"
)
        

@bot.command()
async def rape(ctx, user: discord.User = None):
    if not user:
        await ctx.send("```rape <@user>```")
        return

    methods = ["kidnap", "drive by"]
    cars = ["black van", "white van", "soccer moms mini van", "corrvet", "lambo"]
    locations = ["sex dugeon", "basement", "rape center", "rape penthouse", "kink house"]
    people = ["UZI"]

    method = random.choice(methods)
    car = random.choice(cars)
    location = random.choice(locations)
    person = random.choice(people)
    
    async def send_message(content):
        while True:
            try:
                await ctx.send(content)
                break
            except discord.errors.HTTPException as e:
                if e.status == 429:
                    retry_after = e.retry_after
                    await asyncio.sleep(retry_after)
                    continue
                else:
                    break
            except Exception:
                break

    await send_message(f"```I see my newest victim. >:D```")
    await asyncio.sleep(.5)
    await send_message(f"```I get into my {car} and {method} {user.display_name}, stuffing you in my car.```")
    await asyncio.sleep(.5)
    await send_message(f"```{user.display_name} tries their hardest to escape, but falls unconscious because of the gasses.```")
    await asyncio.sleep(1)
    await send_message(f"```📰🗞️ NEWS: BREAKING NEWS! {user.display_name} HAS BEEN MISSING FOR 24 HOURS, CONTACT POLICE IF YOU HAVE ANY INFORMATION. LAST SEEN WALKING TO SCHOOL```")
    await asyncio.sleep(.5)
    await send_message(f"```{user.display_name}, im glad you woke up. This is my secret {location}```")
    await asyncio.sleep(.5)
    await send_message(f"```your pussy is so tight, mind if i stick this in?```")
    await asyncio.sleep(.5)
    await send_message(f"```your pussy is so tight for me, your so...```")
    await asyncio.sleep(.5)
    await send_message(f"```your such a good slut, i cant keep my cum in```")
    await asyncio.sleep(1)
    await send_message(f"```😩💦💦💦💦💦💦💦```")
    await asyncio.sleep(.5)
    await send_message(f"```I pass out because im a weak minded cuck```")
    await asyncio.sleep(.5)
    await send_message(f"```{user.display_name} runs away and goes to the police revelaing who i am.```")
    await asyncio.sleep(1)
    await send_message(f"```📰🗞️ NEWS: MASS RAPIST {person} CAUGHT IN HIS {location}. As the story is beging to devolp the victim, {user.display_name} has came out to out his rapist. But due to his shitty twisted logic he liked it?```")


@bot.command()
async def z(ctx):
    await ctx.send(f"https://cdn.discordapp.com/attachments/1395225282490667072/1415540751990919299/da3663c176a175053a93bee0a91553e1.gif?ex=68c3948e&is=68c2430e&hm=c3edee1686f1482c42bad7eef2324f1592d21ebd6cb39890541577c6c24863a7&")
    await ctx.send(f"```this is my wife right here fuck nigga```")
    await ctx.message.delete()
    

@bot.command()
async def dick(ctx, member: discord.Member = None):
    member = member or ctx.author

    length = random.randint(1, 20)

    pp_string = "3" + "=" * length + "D"

    await ctx.send(f"```{pp_string} {member.mention}  {length} inches```")
    await ctx.message.delete()

@bot.command() 
async def gay(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("```mention a user```")
        return

    gay_percent = random.randint(1, 100) 
    response = f"`{member.mention} is {gay_percent}% gay`"
    await ctx.send(response)
    await ctx.message.delete()


# MENU

@bot.remove_command('help') 

@bot.command()
async def menu(ctx):
    await ctx.message.delete()
    menu_message = await ctx.send(f"""```ansi
        snowy selfbot                               
╔═════════════════════════════╗
║          COMMANDS           ║ 
╚═════════════════════════════╝ 
 {white}[{black}tab1{white}] ->  multi token       
 {white}[{black}tab2{white}] ->  single token       
 {white}[{black}tab3{white}] ->  utility            
 {white}[{black}tab4{white}] ->  profile            
 {white}[{black}tab5{white}] ->  misc                        
 {white}[{black}all{white}]  ->  all cmds           
                                 
 {black}Commands: 53{white}                    
 {black}Made By: Uzi{white}                    ```""")
    await ctx.send(f"""https://tenor.com/view/blizzard-snow-forest-dark-forest-dark-snowing-forest-gif-26760300""")


@bot.command()
async def tab1(ctx):
    await ctx.message.delete()
    await ctx.send(f"""

```╔═════════════════════════════╗
║         MULTI TOKEN         ║
╚═════════════════════════════╝
[1]  multilast
[2]  multilastoff
[3]  gcn
[4]  gcnoff
[5]  fill
[6]  kill
[7]  killoff
[8]  rpcall
[9]  token
[10] rename         ```""")


@bot.command()
async def tab2(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
```╔═════════════════════════════╗
║        SINGLE TOKEN         ║
╚═════════════════════════════╝
[1]  flood
[2]  floodoff        
[3]  ar                 
[4]  aroff
[5]  ladder                                   
[6]  ladderoff                  
[7]  whore                  
[8]  whoreoff               
[9]  ping
[10] pingoff
[11] spam       ```""")


@bot.command()
async def tab3(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
```╔═════════════════════════════╗
║           UTILITY           ║
╚═════════════════════════════╝
[1]  react
[2]  reactoff
[3]  dreact
[4]  dreactoff
[5]  prefix
[6]  reload                
[7]  av
[8]  python 
[9]  purge
[10] forcepurge
[11] massdm           
[12] massgc                 
[13] massunadd
[14] stopmass
[15] antigc
[16] typing 
[17] typingoff ```""")


@bot.command()
async def tab4(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
```╔═════════════════════════════╗
║          PROFILE            ║
╚═════════════════════════════╝
[1] rpc
[2] rpcoff
[3] stream
[4] streamoff
[5] playing  
[6] rstatus
[7] rstatusoff
[8] remoji
[9] remojioff                      ```""")


@bot.command()
async def tab5(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
```╔═════════════════════════════╗
║            MISC             ║
╚═════════════════════════════╝                 
[2]  swat                 
[3]  hack                
[4]  rape                                   
[5]  dick
[6]  gay 
[7]  z                        ```""")

@bot.command()
async def all(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
```╔═════════════════════════════╗
║         ALL COMMANDS        ║
╚═════════════════════════════╝

TAB1 - MULTI TOKEN                   
[1]   multilast
[2]   multilastoff
[3]   gcn
[4]   gcnoff
[5]   fill
[6]   kill
[7]   killoff
[8]   rpcall
[9]   token
[10]  rename     

TAB2 - SINGLE TOKEN              
[12]  flood
[13]  floodoff       
[14]  ar                 
[15]  aroff
[16]  ladder                                   
[17]  ladderoff                  
[18]  whore                 
[19]  whoreoff               
[20]  ping
[21]  pingoff
[22]  spam  

TAB3 - UTILITY
[23]  react
[24]  reactoff
[25]  dreact
[26]  dreactoff
[27]  prefix
[28]  reload                
[29]  av
[30]  purge
[31]  forcepurge
[32]  massdm           
[33]  massgc                 
[34]  massunadd  
[35]  stopmass
[36]  antigc
[37]  typing
[38]  typingoff
                    
TAB4 - PROFILE                      
[39]  rpc
[40]  rpcoff
[41]  stream
[42]  streamoff
[43]  playing
[44]  rstatus
[45]  rstatusoff
[46]  remoji
[47]  remojioff
                                      
TAB5 - MISC                
[48]  swat                   
[49]  hack                
[50]  rape   
[51]  dick      
[52]  gay
[53]  z  ```""")

@bot.command()
async def help(ctx):
    await ctx.send(f"""```dm @uzi.py for help if your looking for a menu just type {bot.command_prefix}menu ```""")
    await ctx.message.delete()

# MADE BY UZI BITCH 
# @uzi.py

bot.run('ur token here', bot=False) 

