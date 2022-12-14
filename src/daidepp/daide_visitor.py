import logging
from typing import Any

from parsimonious.nodes import Node, NodeVisitor

from daidepp.keywords import *

logger = logging.getLogger(__file__)
logger.addHandler(logging.StreamHandler())


class DAIDEVisitor(NodeVisitor):
    def visit_message(self, node, visited_children) -> Message:
        return visited_children[0]

    def visit_press_message(self, node, visited_children) -> PressMessage:
        return visited_children[0]

    def visit_prp(self, node, visited_children) -> PRP:
        _, _, arrangement, _ = visited_children
        return PRP(arrangement)

    def visit_ccl(self, node, visited_children) -> CCL:
        _, _, press_message, _ = visited_children
        return CCL(press_message)

    def visit_fct(self, node, visited_children) -> FCT:
        _, _, arrangement_qry_not, _ = visited_children[0]
        return FCT(arrangement_qry_not)

    def visit_thk(self, node, visited_children):
        _, _, arrangement_qry_not, _ = visited_children[0]
        return THK(arrangement_qry_not)

    def visit_try(self, node, visited_children) -> TRY:
        _, _, try_token, ws_try_tokens, _ = visited_children

        try_tokens = [try_token]
        for ws_try_token in ws_try_tokens:
            _, try_token = ws_try_token
            try_tokens.append(try_token)
        return TRY(*try_tokens)

    def visit_ins(self, node, visited_children) -> INS:
        _, _, arrangement, _ = visited_children
        return INS(arrangement)

    def visit_qry(self, node, visited_children) -> QRY:
        _, _, arrangement, _ = visited_children
        return QRY(arrangement)

    def visit_sug(self, node, visited_children) -> SUG:
        _, _, arrangement, _ = visited_children
        return SUG(arrangement)

    def visit_wht(self, node, visited_children) -> WHT:
        _, _, unit, _ = visited_children
        return WHT(unit)

    def visit_how(self, node, visited_children) -> HOW:
        _, _, province_power, _ = visited_children
        return HOW(province_power)

    def visit_exp(self, node, visited_children) -> EXP:
        _, _, turn, _, _, message, _ = visited_children
        return EXP(turn, message)

    def visit_iff(self, node, visited_children) -> IFF:
        _, _, arrangement, _, _, _, press_message, _, els = visited_children

        if isinstance(els, Node) and not els.text:
            return IFF(arrangement, press_message)

        else:
            _, _, els_press_message, _ = els[0]
            return IFF(arrangement, press_message, els_press_message)

    def visit_frm(self, node, visited_children) -> FRM:
        (
            _,
            _,
            frm_power,
            _,
            _,
            recv_power,
            ws_recv_powers,
            _,
            _,
            message,
            _,
        ) = visited_children

        recv_powers = [recv_power]
        for ws_recv_power in ws_recv_powers:
            _, recv_power = ws_recv_power
            recv_powers.append(recv_power)
        return FRM(frm_power, recv_powers, message)

    def visit_reply(self, node, visited_children) -> Reply:
        return visited_children[0]

    def visit_yes(self, node, visited_children) -> YES:
        _, _, press_message, _ = visited_children
        return YES(press_message)

    def visit_rej(self, node, visited_children) -> REJ:
        _, _, press_message, _ = visited_children
        return REJ(press_message)

    def visit_bwx(self, node, visited_children) -> BWX:
        _, _, press_message, _ = visited_children
        return BWX(press_message)

    def visit_huh(self, node, visited_children) -> HUH:
        _, _, press_message, _ = visited_children
        return HUH(press_message)

    def idk_param(self, node, visited_children) -> Union[QRY, WHT, PRP, INS]:
        return visited_children[0]

    def visit_idk(self, node, visited_children) -> IDK:
        _, _, idk_param, _ = visited_children

        return IDK(idk_param[0]) if isinstance(idk_param, list) else IDK(idk_param)

    def visit_sry(self, node, visited_children) -> SRY:
        _, _, exp, _ = visited_children
        return SRY(exp)

    def why_param(self, node, visited_children) -> Union[FCT, THK, PRP, INS]:
        return visited_children[0]

    def visit_why(self, node, visited_children) -> WHY:
        _, _, why_param, _ = visited_children
        return WHY(why_param)

    def visit_pob(self, node, visited_children) -> POB:
        _, _, why, _ = visited_children
        return POB(why)

    def visit_arrangement(self, node, visited_children) -> Arrangement:
        return visited_children[0]

    def visit_pce(self, node, visited_children) -> PCE:
        _, _, power, ws_powers, _ = visited_children

        powers = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            powers.append(pow)
        return PCE(*powers)

    def visit_aly_vss(self, node, visited_children) -> ALYVSS:
        (
            aly,
            _,
            aly_power,
            ws_aly_powers,
            _,
            vss,
            _,
            vss_power,
            ws_vss_powers,
            _,
        ) = visited_children

        aly_powers = [aly_power]
        for ws_aly_power in ws_aly_powers:
            _, aly_power = ws_aly_power
            aly_powers.append(aly_power)

        vss_powers = [vss_power]
        for ws_vss_power in ws_vss_powers:
            _, vss_power = ws_vss_power
            vss_powers.append(vss_power)
        return ALYVSS(aly_powers, vss_powers)

    def visit_drw(self, node, visited_children) -> DRW:
        _, par_powers = visited_children

        if isinstance(par_powers, Node) and not par_powers.text:
            return DRW()

        # For Partial draws are allowed (PDA) variant game
        _, power, ws_powers, _ = par_powers[0]
        powers = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            powers.append(pow)

        return DRW(*powers)

    def visit_slo(self, node, visited_children) -> SLO:
        _, _, power, _ = visited_children
        return SLO(power)

    def visit_not(self, node, visited_children) -> NOT:
        _, _, arrangement_qry, _ = visited_children[0]
        return NOT(arrangement_qry)

    def visit_nar(self, node, visited_children) -> NAR:
        _, _, arrangement, _ = visited_children
        return NAR(arrangement)

    def visit_xdo(self, node, visited_children) -> XDO:
        _, _, order, _ = visited_children
        return XDO(order)

    def visit_and(self, node, visited_children) -> AND:
        _, _, arrangement, _, par_arrangements = visited_children[0]

        arrangements = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arrangements.append(arr)
        return AND(*arrangements)

    def visit_orr(self, node, visited_children) -> ORR:
        _, _, arrangement, _, par_arrangements = visited_children[0]

        arrangements = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arrangements.append(arr)
        return ORR(arrangements)

    def visit_dmz(self, node, visited_children) -> DMZ:
        _, _, power, ws_powers, _, _, province, ws_provinces, _ = visited_children

        powers = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            powers.append(pow)

        provinces = [province]
        for ws_prov in ws_provinces:
            _, prov = ws_prov
            provinces.append(prov)
        return DMZ(powers, provinces)

    def visit_scd(self, node, visited_children) -> SCD:
        _, scd_statements = visited_children

        power_and_supply_centers = []
        for scd_statment in scd_statements:
            _, power, _, supply_center, ws_supply_centers, _ = scd_statment

            supply_centers = [Location(supply_center)]
            for ws_sc in ws_supply_centers:
                _, sc = ws_sc
                supply_centers.append(Location(sc))
            power_and_supply_centers.append(
                PowerAndSupplyCenters(power, *supply_centers)
            )
        return SCD(*power_and_supply_centers)

    def visit_occ(self, node, visited_children) -> OCC:
        _, par_units = visited_children

        units = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            units.append(unit)
        return OCC(*units)

    def visit_cho(self, node, visited_children) -> CHO:
        _, _, range, _, par_arrangements = visited_children

        minimum, maximum = tuple([int(x) for x in range.text.split()])
        arrangements = []
        for par_arrangement in par_arrangements:
            _, arrangement, _ = par_arrangement
            arrangements.append(arrangement)
        return CHO(minimum, maximum, *arrangements)

    def visit_for(self, node, visited_children) -> FOR:
        _, _, turn, _, _, arrangement, _ = visited_children[0]

        if isinstance(turn, list):
            _, start_turn, _, _, end_turn, _ = turn
            return FOR(start_turn, end_turn, arrangement)
        else:
            return FOR(start_turn, None, arrangement)

    def visit_xoy(self, node, visited_children) -> XOY:
        _, _, power_x, _, _, power_y, _ = visited_children
        return XOY(power_x, power_y)

    def visit_ydo(self, node, visited_children) -> YDO:
        _, _, power, _, par_units = visited_children

        units = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            units.append(unit)
        return YDO(power, *units)

    def visit_snd(self, node, visited_children) -> SND:
        (
            _,
            _,
            power,
            _,
            _,
            recv_power,
            ws_recv_powers,
            _,
            _,
            message,
            _,
        ) = visited_children

        recv_power = [recv_power]
        for ws_recv_power in ws_recv_powers:
            _, recv_power = ws_recv_power
            recv_power.append(recv_power)
        return SND(power, recv_power, message)

    def visit_fwd(self, node, visited_children) -> FWD:
        _, _, power, ws_powers, _, _, power_1, _, _, power_2, _ = visited_children

        powers = [power]
        for ws_power in ws_powers:
            _, power = ws_power
            powers.append(power)
        return FWD(powers, power_1, power_2)

    def visit_bcc(self, node, visited_children) -> BCC:
        _, _, power_1, _, _, power, ws_powers, _, _, power_2, _ = visited_children

        powers = [power]
        for ws_power in ws_powers:
            _, power = ws_power
            powers.append(power)
        return BCC(power_1, powers, power_2)

    def visit_order(self, node, visited_children) -> Order:
        return visited_children[0]

    def visit_hld(self, node, visited_children) -> HLD:
        _, unit, _, _ = visited_children
        return HLD(unit)

    def visit_mto(self, node, visited_children) -> MTO:
        _, unit, _, _, _, province = visited_children
        return MTO(unit, province)

    def visit_sup(self, node, visited_children) -> SUP:
        (
            _,
            supporting_unit,
            _,
            _,
            _,
            supported_unit,
            _,
            ws_province_no_coast,
        ) = visited_children

        if isinstance(ws_province_no_coast, Node) and not ws_province_no_coast.text:
            return SUP(supporting_unit, supported_unit)
        else:
            _, _, province_no_coast = ws_mto_prov = ws_province_no_coast[0]
            return SUP(supporting_unit, supported_unit, province_no_coast)

    def visit_cvy(self, node, visited_children) -> CVY:
        _, convoying_unit, _, _, _, convoyed_unit, _, _, _, province = visited_children
        return CVY(convoying_unit, convoyed_unit, province)

    def visit_move_by_cvy(self, node, visited_children) -> MoveByCVY:
        (
            _,
            unit,
            _,
            _,
            _,
            province,
            _,
            _,
            _,
            province_sea,
            ws_province_seas,
            _,
        ) = visited_children

        province_seas = [province_sea]
        for ws_province_sea in ws_province_seas:
            _, province_sea = ws_province_sea
            province_seas.append(province_sea)
        return MoveByCVY(unit, province, *province_seas)

    def visit_retreat(self, node, visited_children) -> Retreat:
        return visited_children[0]

    def visit_rto(self, node, visited_children) -> RTO:
        _, unit, _, _, _, province = visited_children
        return RTO(unit, province)

    def visit_dsb(self, node, visited_children) -> DSB:
        _, unit, _, _ = visited_children
        return DSB(unit)

    def visit_build(self, node, visited_children) -> Build:
        return visited_children[0]

    def visit_bld(self, node, visited_children) -> BLD:
        _, unit, _, _ = visited_children
        return BLD(unit)

    def visit_rem(self, node, visited_children) -> REM:
        _, unit, _, _ = visited_children
        return REM(unit)

    def visit_wve(self, node, visited_children) -> WVE:
        power, _, _ = visited_children
        return WVE(power)

    def visit_power(self, node, visited_children) -> Power:
        return node.text

    def visit_prov_coast(self, node, visited_children) -> ProvinceCoast:
        return node.text

    def visit_prov_no_coast(self, node, visited_children) -> ProvinceNoCoast:
        return Location(province=node.text)

    def visit_prov_sea(self, node, visited_children) -> ProvinceSea:
        return node.text

    def visit_supply_center(self, node, visited_children) -> SupplyCenter:
        return node.text

    def visit_unit(self, node, visited_children) -> Unit:
        power, _, unit_type, _, location = visited_children
        return Unit(power, unit_type, location=location)

    def visit_unit_type(self, node, visited_children) -> UnitType:
        return node.text

    def visit_province(self, node, visited_children) -> Location:
        return visited_children[0]

    def visit_prov_landlock(self, node, visited_children) -> Location:
        return Location(province=node.text)

    def visit_prov_land_sea(self, node, visited_children) -> Location:
        return Location(province=node.text)

    def visit_prov_coast(self, node, visited_children) -> Location:
        _, province, _, coast, _ = visited_children[0]
        return Location(province=province.text, coast=coast.text)

    def visit_coast(self, node, visited_children) -> ProvinceCoast:
        return node.text

    def visit_turn(self, node, visited_children) -> Turn:
        season, _, year = visited_children
        return Turn(season, int(year.text))

    def visit_season(self, node, visited_children) -> Season:
        return node.text

    def visit_try_tokens(self, node, visited_children) -> TryTokens:
        return node.text

    def visit_sub_arrangement(self, node, visited_children) -> Arrangement:
        return visited_children[0]

    def generic_visit(self, node, visited_children) -> Any:
        return visited_children or node

    def visit_daide_string(self, node, visited_children) -> Any:
        return visited_children[0]

    def visit_uhy(self, node, visited_children) -> UHY:
        _, _, press_message, _ = visited_children
        return UHY(press_message)

    def visit_hpy(self, node, visited_children) -> HPY:
        _, _, press_message, _ = visited_children
        return HPY(press_message)

    def visit_ang(self, node, visited_children) -> ANG:
        _, _, press_message, _ = visited_children

        return ANG(press_message)

    def visit_rfo(self, node, visited_children) -> RFO:
        return RFO()


daide_visitor = DAIDEVisitor()
