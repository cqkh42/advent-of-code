input_ = """
Al => ThF
Ca => SiTh
F => CaF
F => PMg
F => SiAl
B => BCa
B => TiB
Ca => CaCa
Ca => PB
N => HSi
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg
O => HP
O => OTi
P => CaP
P => PTi
H => NTh
H => OB
Mg => BF
Mg => TiMg
Al => ThZaa
Al => ThRnFAr
H => CZha
H => CZhc
H => CZhi
H => CZhm
H => NZhq
H => OZhw
H => NZhu
B => TiZba
Ca => PZca
Ca => SiZcc
Ca => SiZcg
Zaa => RnZab
Zab => FAr
Zba => RnZbb
Zbb => FAr
Zca => RnZcb
Zcb => FAr
Zcc => RnZcd
Zcd => FZce
Zce => YZcf
Zcf => FAr
Zcg => RnZch
Zch => MgAr
Zha => RnZhb
Zhb => AlAr
Zhc => RnZhd
Zhd => FZhe
Zhe => YZhf
Zhf => FZhg
Zhg => YZhh
Zhh => FAr
Zhi => RnZhj
Zhj => FZhk
Zhk => YZhl
Zhl => MgAr
Zhm => RnZhn
Zhn => MgZho
Zho => YZhp
Zhp => FAr
Zhq => RnZhr
Zhr => FZhs
Zhs => YZht
Zht => FAr
Zhu => RnZhv
Zhv => MgAr
Zhw => RnZhx
Zhx => FAr
N => CZna
Zna => RnZnb
Znb => FAr
O => CZoa
Zoa => RnZob
Zob => FZoc
Zoc => YZod
Zod => FAr
O => CZoe
Zoe => RnZof
Zof => MgAr
O => NZog
Zog => RnZoh
Zoh => FAr
P => SiZpa
Zpa => RnZpb
Zpb => FAr
"""

molecule = [
    "C", "Rn", "Ca", "Si", "Rn", "B", "Si", "Rn", "F", "Ar", "Ti", "B", "P",
    "Ti", "Ti", "B", "F", "Ar", "P", "B", "Ca", "Si", "Th", "Si", "Rn", "Ti",
    "B", "P", "B", "P", "Mg", "Ar", "Ca", "Si", "Rn", "Ti", "Mg", "Ar", "Ca",
    "Si", "Th", "Ca", "Si", "Rn", "F", "Ar", "Rn", "Si", "Rn", "F", "Ar", "Ti",
    "Ti", "B", "F", "Ar", "Ca", "Ca", "Si", "Rn", "Si", "Th", "Ca", "Ca", "Si",
    "Rn", "Mg", "Ar", "F", "Y", "Si", "Rn", "F", "Y", "Ca", "F", "Ar", "Si",
    "Th", "Ca", "Si", "Th", "P", "B", "P", "Ti", "Mg", "Ar", "Ca", "P", "Rn",
    "Si", "Al", "Ar", "P", "B", "Ca", "Ca", "Si", "Rn", "F", "Y", "Si", "Th",
    "Ca", "Rn", "F", "Ar", "Ar", "Ca", "Ca", "Si", "Rn", "P", "B", "Si", "Rn",
    "F", "Ar", "Mg", "Y", "Ca", "Ca", "Ca", "Ca", "Si", "Th", "Ca", "Ca", "Si",
    "Al", "Ar", "Ca", "Ca", "Si", "Rn", "P", "B", "Si", "Al", "Ar", "B", "Ca",
    "Ca", "Ca", "Ca", "Si", "Th", "Ca", "P", "B", "Si", "Th", "P", "B", "P",
    "B", "Ca", "Si", "Rn", "F", "Y", "F", "Ar", "Si", "Th", "Ca", "Si", "Rn",
    "F", "Ar", "B", "Ca", "Ca", "Si", "Rn", "F", "Y", "F", "Ar", "Si", "Th",
    "Ca", "P", "B", "Si", "Th", "Ca", "Si", "Rn", "P", "Mg", "Ar", "Rn", "F",
    "Ar", "P", "Ti", "B", "Ca", "P", "Rn", "F", "Ar", "Ca", "Ca", "Ca", "Ca",
    "Si", "Rn", "Ca", "Ca", "Si", "Rn", "F", "Y", "F", "Ar", "F", "Ar", "B",
    "Ca", "Si", "Th", "F", "Ar", "Th", "Si", "Th", "Si", "Rn", "Ti", "Rn", "P",
    "Mg", "Ar", "F", "Ar", "Ca", "Si", "Th", "Ca", "P", "B", "Ca", "Si", "Rn",
    "B", "F", "Ar", "Ca", "Ca", "P", "Rn", "Ca", "Ca", "P", "Mg", "Ar", "Si",
    "Rn", "F", "Y", "F", "Ar", "Ca", "Si", "Th", "Rn", "P", "B", "P", "Mg",
    "Ar"
]
