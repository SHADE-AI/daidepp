from parsimonious.grammar import Grammar

grammar = Grammar(
    """
    message = press_message / reply
    press_message = prp / ccl / fct / thk / try / ins / qry / sug / wht / how / exp / iff / frm
    prp = "PRP" lpar arrangement rpar 
    ins = "INS" lpar arrangement rpar
    qry = "QRY" lpar arrangement rpar
    sug = "SUG" lpar arrangement rpar
    ccl = "CCL" lpar press_message rpar
    fct = ("FCT" lpar qry rpar) / ("FCT" lpar "NOT" lpar qry rpar rpar) / ("FCT" lpar arrangement rpar)
    thk = ("THK" lpar qry rpar) / ("THK" lpar "NOT" lpar qry rpar rpar) / ("THK" lpar arrangement rpar)
    try = "TRY" lpar try_tokens (ws try_tokens)* rpar
    wht = "WHT" lpar unit rpar
    how = "HOW" lpar province rpar
    exp = "EXP" lpar turn rpar lpar message rpar
    iff = "IFF" lpar arrangement rpar "THN" lpar press_message rpar ("ELS" lpar press_message rpar)?
    frm = "FRM" lpar power rpar lpar power (ws power)* rpar lpar message rpar

    reply = yes / rej / bwx / huh / fct / thk / idk / sry / why / pob
    yes = "YES" lpar press_message rpar
    rej = "REJ" lpar press_message rpar
    bwx = "BWX" lpar press_message rpar
    huh = "HUH" lpar press_message rpar
    idk = "IDK" lpar qry_wht_prp_ins rpar
    sry = "SRY" lpar exp rpar
    why = "WHY" lpar fct_thk_prp_ins rpar
    pob = "POB" lpar why rpar

    arrangement = pce / aly_vss / drw / slo / not / nar / xdo / dmz / and / orr / scd / occ / cho / for / xoy / ydo / snd / fwd / bcc
    pce = "PCE" lpar power (ws power)* rpar
    aly_vss = "ALY" lpar power (ws power)* rpar "VSS" lpar power (ws power)* rpar
    drw = "DRW" (lpar power (ws power)+ rpar)?
    slo = "SLO" lpar power rpar
    not = "NOT" lpar arrangement rpar
    nar = "NAR" lpar arrangement rpar
    xdo = "XDO" lpar order rpar
    and = "AND" lpar arrangement rpar (lpar arrangement rpar)+
    orr = "ORR" lpar arrangement rpar (lpar arrangement rpar)+
    dmz = "DMZ" lpar power (ws power)* rpar lpar province (ws province)* rpar
    scd = "SCD" (lpar power ws supply_center (ws supply_center)* rpar)+
    occ = "OCC" (lpar unit rpar)+
    cho = "CHO" lpar (~"\d+ \d+") rpar (lpar arrangement rpar)+
    for = ("FOR" lpar turn rpar lpar arrangement rpar) / ("FOR" lpar (lpar turn rpar lpar turn rpar) rpar lpar arrangement rpar)
    xoy = "XOY" lpar power rpar lpar power rpar
    ydo = "YDO" lpar power rpar (lpar unit rpar)+
    snd = "SND" lpar power rpar lpar power (ws power)* rpar lpar message rpar
    fwd = "FWD" lpar power (ws power)* rpar lpar power rpar lpar power rpar
    bcc = "BCC" lpar power rpar lpar power (ws power)* rpar lpar power rpar
    
    order = hld / mto / sup/ cvy / move_by_cvy / retreat / build
    hld = lpar unit rpar "HLD"
    mto = lpar unit rpar "MTO" ws province
    sup = lpar unit rpar "SUP" lpar unit rpar ("MTO" ws province)?
    cvy = lpar unit rpar "CVY" lpar unit rpar "CTO" ws province
    move_by_cvy = lpar unit rpar "CTO" ws province ws "VIA" lpar prov_sea (ws prov_sea)* rpar
    retreat = rto / dsb
    rto = lpar unit rpar "RTO" ws province
    dsb = lpar unit rpar "DSB"
    build = bld / rem / wve
    bld = lpar unit rpar "BLD"
    rem = lpar unit rpar "REM"
    wve = power ws "WVE"

    unit_type = "AMY" / "FLT"
    unit = power ws unit_type ws province
    power = "AUS" / "ENG" / "FRA" / "GER" / "ITA" / "RUS" / "TUR"
    province = prov_coast / prov_no_coast / prov_sea / (lpar prov_coast ws coast rpar)
    coast = "NCS" / "ECS" / "SCS" / "WCS"
    prov_coast = "ALB" / "ANK" / "APU" / "ARM" / "BEL" / "BER" / "BRE" / "BUL" / "CLY" / "CON" / "DEN" / "EDI" / "FIN" / "GAS" / "GRE" / "HOL" / "KIE" / "LON" / "LVN" / "LVP" / "MAR" / "NAF" / "NAP" / "NWY" / "PIC" / "PIE" / "POR" / "PRU" / "ROM" / "RUM" / "SEV" / "SMY" / "SPA" / "STP" / "SWE" / "SYR" / "TRI" / "TUN" / "TUS" / "VEN" / "YOR" / "WAL" 
    prov_no_coast = "BOH" / "BUD" / "BUR" / "MOS" / "MUN" / "GAL" / "PAR" / "RUH" / "SER" / "SIL" / "TYR" / "UKR" / "VIE" / "WAR" 
    prov_sea = "ADR" / "AEG" / "BAL" / "BAR" / "BLA" / "BOT" / "EAS" / "ENG" / "HEL" / "ION" / "IRI" / "LYO" / "MAO" / "NAO" / "NTH" / "NWG" / "SKA" / "TYS" / "WES"  
    supply_center = "ANK" / "BEL" / "BER" / "BRE" / "BUD" / "BUL" / "CON" / "DEN" / "EDI" / "GRE" / "HOL" / "KIE" / "LON" / "LVP" / "MAR" / "MOS" / "MUN" / "NAP" / "NWY" / "PAR" / "POR" / "ROM" / "RUM" / "SER" / "SEV" / "SMY" / "SPA" / "STP" / "SWE" / "TRI" / "TUN" / "VEN" / "VIE" / "WAR"
    turn = season ws ~"\d{4}"
    season = "SPR" / "SUM" / "FAL" / "AUT" / "WIN"
    try_tokens = "PRP" / "PCE" / "ALY" / "VSS" / "DRW" / "SLO" / "NOT" / "NAR" / "YES" / "REJ" / "BWX" / "XDO" / "DMZ" / "AND" / "ORR" / "SCD" / "OCC" / "INS" / "QRY" / "THK" / "FCT" / "IDK" / "SUG" / "WHT" / "HOW" / "EXP" / "SRY" / "FOR" / "IFF" / "THN" / "ELS" / "XOY" / "YDO" / "FRM" / "FWD" / "SND"

    lpar = ~"\s*\(\s*"
    rpar = ~"\s*\)\s*"
    ws = ~"\s+"
    qry_wht_prp_ins = qry / wht/ prp /ins
    fct_thk_prp_ins = fct / thk / prp / ins
    """
)
