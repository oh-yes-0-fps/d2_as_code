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


#called right before the reload
def rapidHit(_input: FunctionInputData, _perkValue: int) -> ReloadModifierResponse:
    values = [(0,1),(5,0.99),(30,0.97),(35,0.96),(45,0.94),(60,0.93)]
    if _input._shotsHitThisMag > 5:
        value = values[-1]
    else:
        value = values[_input._shotsHitThisMag]
    return ReloadModifierResponse(value[0], value[1])


#called for weapon inspection
def rapidHitStat(_input: FunctionInputData, _perkValue: int) -> dict[str, int]:
    values = [(0,0),(5,2),(30,12),(35,14),(45,18),(60,25)]
    value = values[_perkValue]
    return {"reload": value[0], "stability": value[1]}


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
    perkValue = 0
    yourFunc = rapidHit

    pprint.pprint(yourFunc(inputData, perkValue).__dict__)
