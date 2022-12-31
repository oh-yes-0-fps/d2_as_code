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
###Author: Oh-yes-10-FPS
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
class ReloadModifierResponse:
    reloadStatAdd: float
    reloadTimeScale: float

@dataclass()
class HandlingModifierResponse:
    handlingStatAdd: float
    handlingTimeScale: float

@dataclass()
class DamageModifierResponse:
    #i.e. focused fury
    damageScale: float #value of 1.0 does nothing
    #i.e. whisper catalyst
    critScale: float #value of 1.0 does nothing

#this is how kill clip, rampage, harmony, etc. work. cascade/desperado is same thing but use firing function.
def durationPerks(_input: FunctionInputData, _perkValue: int) -> DamageModifierResponse:
    if _perkValue == 1:
        return DamageModifierResponse(1.15, 1.0)
    elif _perkValue == 0:
        if _input._timeTotal > 12:
            return DamageModifierResponse(1.15, 1.0)
    return DamageModifierResponse(1.0, 1.0)

#called right before the reload
def reloadModifier(_input: FunctionInputData, _perkValue: int) -> ReloadModifierResponse:
    if _perkValue == 1:
        return ReloadModifierResponse(50, 1.0)
    elif _perkValue == 0:
        if _input._timeTotal > 12:
            return ReloadModifierResponse(50, 1.0)
    return ReloadModifierResponse(0, 1.0)

#is only used in static handling equations for now but later could do math for weapon combos
def handlingModifier(_input: FunctionInputData, _perkValue: int) -> HandlingModifierResponse:
    if _perkValue == 1:
        return HandlingModifierResponse(50, 1.0)
    elif _perkValue == 0:
        if _input._timeTotal > 12:
            return HandlingModifierResponse(50, 1.0)
    return HandlingModifierResponse(0, 1.0)

#called for weapon inspection
def statModifier(_input: FunctionInputData, _perkValue: int) -> dict[str, int]:
    if _perkValue == 1:
        return {"reload": 50, "handling": 50}
    return {}

if __name__ == "__main__":
    inputData = FunctionInputData(
        #default is a 120 rpm hc cuz why not
        _currFiringData=FiringConfig(0.5, 0, 1),
        _baseDamage=50,
        _baseCritMult=1.6,
        _shotsHitThisMag=55,
        _totalShotsHit=15,
        _baseMag=55,
        _currMag=5,
        _reservesLeft=10,
        _timeTotal=8.5,#assumes reload is 2s
        _timeThisMag=2,
        _stats = {},#if u need stats add them
        _weaponType="Hand Cannon",
        _weaponSlot="Primary"
    )
    perkValue = 1
    yourFunc = durationPerks

    pprint.pprint(yourFunc(inputData, perkValue).__dict__)
