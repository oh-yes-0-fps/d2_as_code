from dataclasses import dataclass, field
import pprint


@dataclass()
class FiringConfig:
    """for full auto set size to 1 and duration to 0"""
    burstDelay: float
    burstDuration: float
    burstSize: int
    oneAmmoBurst: bool = field(default=False)
    isCharge: bool = field(default=False)
    isExplosive: bool = field(default=False)

#ignore this for now
@dataclass()
class RefundData:
    crit: bool
    requirement: int
    refund: int


###
###You can delete whatever you don't use
###
###Test the function
###
###Author: Your Name
###Date_last_updated: 12/30/2020 :: US

#import this here to prevent recursive import, its fine cuz duck typed
@dataclass()
class FunctionInputData:
    """This is to help with verbosity of function params"""
    _currFiringData:FiringConfig
    _baseDamage:float
    _baseCritMult:float
    _shotsHitThisMag:int
    _totalShotsHit:int
    _baseMag:int
    _currMag:int
    _reservesLeft:int
    _timeTotal:float
    _timeThisMag:float
    #for testing have this function has a dict with name of stat
    #   as key and value as the value of the stat
    #   in production will be a dict with enum as key and value as value of stat
    _stats:dict
    _weaponType:str #in production will be enum
    _weaponSlot:str #in production will be enum


@dataclass()
class DamageModifierResponse:
    #i.e. focused fury
    damageScale: float #value of 1.0 does nothing
    #i.e. whisper catalyst
    critScale: float #value of 1.0 does nothing

@dataclass()
class ExtraDamageResponse:
    #for example grand overture, you would have additive dmg of all the rockets,
    #  time for all the rockets to shoot, and number of rockets
    additiveDamage: float
    timeForAdditiveDamage: float
    #number of hits for the additive damage, doesn't mult dmg just spreads it out
    additiveDamageHits: int
    #damage scales for weapon buffs
    weaponScale: bool
    #damage scales for crits
    critScale: bool

@dataclass()
class ReloadModifierResponse:
    reloadStatAdd: float
    reloadTimeScale: float

@dataclass()
class FiringModifierResponse:
    burstDelayScale: float #lower is faster
    burstSizeAdd: int #additive
    burstDurationScale: float #lower is faster

@dataclass()
class HandlingModifierResponse:
    handlingStatAdd: float
    handlingTimeScale: float

#Perk Value is the amount of stacks of the perk and/or if its active
#toggle perks like surrounded will use it as a bool, 0 is false, 1 is true
#dynamic perks like rampage will use it as the current stack
#static perks like focused fury will ignore this value

#replace function name with name of perk

#called b4 the bullet is shot
def damageModifier(_input: FunctionInputData, _perkValue: int) -> DamageModifierResponse:
    pass


#called after the bullet is shot
def extraDamage(_input: FunctionInputData, _perkValue: int) -> ExtraDamageResponse:
    pass


#called right before the reload
def reloadModifier(_input: FunctionInputData, _perkValue: int) -> ReloadModifierResponse:
    pass


#called after every shot
def firingModifier(_input: FunctionInputData, _perkValue: int) -> FiringModifierResponse:
    pass


#is only used in static handling equations for now but later could do math for weapon combos
def handlingModifier(_input: FunctionInputData, _perkValue: int) -> HandlingModifierResponse:
    pass

#is only used in static range equations for now
def rangeModifier(_input: FunctionInputData, _perkValue: int) -> float:
    pass

#called for weapon inspection
def statModifier(_input: FunctionInputData, _perkValue: int) -> dict[str, int]:
    pass


if __name__ == "__main__":
    inputData = FunctionInputData(
        #default is a 120 rpm hc cuz why not
        _currFiringData=FiringConfig(0.5, 0, 1),
        _baseDamage=50,
        _baseCritMult=1.6,
        _shotsHitThisMag=5,
        _totalShotsHit=15,
        _baseMag=10,
        _currMag=5,
        _reservesLeft=10,
        _timeTotal=8.5,#assumes reload is 2s
        _timeThisMag=2,
        _stats = {},#if u need stats add them
        _weaponType="Hand Cannon",
        _weaponSlot="Primary"
    )
    perkValue = 1
    yourFunc = damageModifier

    pprint.pprint(yourFunc(inputData, perkValue).__dict__)
