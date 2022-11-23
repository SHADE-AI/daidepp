from parsimonious.nodes import Node, NodeVisitor

from daidepp.keywords import *


class DAIDEVisitor(NodeVisitor):
    def visit_message(self, node, visited_children):
        return visited_children[0]

    def visit_press_message(self, node, visited_children):
        return visited_children[0]

    def visit_prp(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return PRP(arrangement)

    def visit_ccl(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return CCL(press_message)

    def visit_fct(self, node, visited_children):
        _, _, arrangement_qry_not, _ = visited_children[0]
        return FCT(arrangement_qry_not)

    def visit_thk(self, node, visited_children):
        _, _, arrangement_qry_not, _ = visited_children[0]
        return THK(arrangement_qry_not)

    def visit_try(self, node, visited_children):
        _, _, try_token, ws_try_tokens, _ = visited_children

        try_tokens = [try_token]
        for ws_try_token in ws_try_tokens:
            _, try_token = ws_try_token
            try_tokens.append(try_token)
        return TRY(*try_tokens)

    def visit_ins(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return INS(arrangement)

    def visit_qry(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return QRY(arrangement)

    def visit_sug(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return SUG(arrangement)

    def visit_wht(self, node, visited_children):
        _, _, unit, _ = visited_children
        return WHT(unit)

    def visit_how(self, node, visited_children):
        _, _, province_power, _ = visited_children
        return HOW(province_power)

    def visit_exp(self, node, visited_children):
        _, _, turn, _, _, message, _ = visited_children
        return EXP(turn, message)

    def visit_iff(self, node, visited_children):
        _, _, arrangement, _, _, _, press_message, _, els = visited_children

        if isinstance(els, Node) and not els.text:
            return IFF(arrangement, press_message)

        else:
            _, _, els_press_message, _ = els[0]
            return IFF(arrangement, press_message, els_press_message)

    def visit_frm(self, node, visited_children):
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

    def visit_reply(self, node, visited_children):
        return visited_children[0]

    def visit_yes(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return YES(press_message)

    def visit_rej(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return REJ(press_message)

    def visit_bwx(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return BWX(press_message)

    def visit_huh(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return HUH(press_message)

    def visit_qry_wht_prp_ins(self, node, visited_children):
        return visited_children[0]

    def visit_idk(self, node, visited_children):
        _, _, qry_exp_wht_prp_ins_sug, _ = visited_children

        return (
            IDK(qry_exp_wht_prp_ins_sug[0])
            if isinstance(qry_exp_wht_prp_ins_sug, list)
            else IDK(qry_exp_wht_prp_ins_sug)
        )

    def visit_sry(self, node, visited_children):
        _, _, exp, _ = visited_children
        return SRY(exp)

    def visit_fct_thk_prp_ins(self, node, visited_children):
        return visited_children[0]

    def visit_why(self, node, visited_children):
        _, _, fct_thk_prp_ins, _ = visited_children
        return WHY(fct_thk_prp_ins)

    def visit_pob(self, node, visited_children):
        _, _, why, _ = visited_children
        return POB(why)

    def visit_arrangement(self, node, visited_children):
        return visited_children[0]

    def visit_pce(self, node, visited_children):
        _, _, power, ws_powers, _ = visited_children

        powers = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            powers.append(pow)
        return PCE(*powers)

    def visit_aly_vss(self, node, visited_children):
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

    def visit_drw(self, node, visited_children):
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

    def visit_slo(self, node, visited_children):
        _, _, power, _ = visited_children
        return SLO(power)

    def visit_not(self, node, visited_children):
        _, _, arrangement_qry, _ = visited_children[0]
        return NOT(arrangement_qry)

    def visit_nar(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return NAR(arrangement)

    def visit_xdo(self, node, visited_children):
        _, _, order, _ = visited_children
        return XDO(order)

    def visit_and(self, node, visited_children):
        _, _, arrangement, _, par_arrangements = visited_children[0]

        arrangements = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arrangements.append(arr)
        return AND(*arrangements)

    def visit_orr(self, node, visited_children):
        _, _, arrangement, _, par_arrangements = visited_children[0]

        arrangements = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arrangements.append(arr)
        return ORR(arrangements)

    def visit_dmz(self, node, visited_children):
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

    def visit_scd(self, node, visited_children):
        _, scd_statements = visited_children

        power_and_supply_centers = []
        for scd_statment in scd_statements:
            _, power, _, supply_center, ws_supply_centers, _ = scd_statment

            supply_centers = [supply_center]
            for ws_sc in ws_supply_centers:
                _, sc = ws_sc
                supply_centers.append(sc)
            power_and_supply_centers.append(
                PowerAndSupplyCenters(power, supply_centers)
            )
        return SCD(*power_and_supply_centers)

    def visit_occ(self, node, visited_children):
        _, par_units = visited_children

        units = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            units.append(unit)
        return OCC(*units)

    def visit_cho(self, node, visited_children):
        _, _, range, _, par_arrangements = visited_children

        minimum, maximum = tuple([int(x) for x in range.text.split()])
        arrangements = []
        for par_arrangement in par_arrangements:
            _, arrangement, _ = par_arrangement
            arrangements.append(arrangement)
        return CHO(minimum, maximum, *arrangements)

    def visit_for(self, node, visited_children):
        _, _, turn, _, _, arrangement, _ = visited_children[0]

        if isinstance(turn, list):
            _, start_turn, _, _, end_turn, _ = turn
            return FOR(start_turn, end_turn, arrangement)
        else:
            return FOR(start_turn, None, arrangement)

    def visit_xoy(self, node, visited_children):
        _, _, power_x, _, _, power_y, _ = visited_children
        return XOY(power_x, power_y)

    def visit_ydo(self, node, visited_children):
        _, _, power, _, par_units = visited_children

        units = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            units.append(unit)
        return YDO(power, *units)

    def visit_snd(self, node, visited_children):
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

    def visit_fwd(self, node, visited_children):
        _, _, power, ws_powers, _, _, power_1, _, _, power_2, _ = visited_children

        powers = [power]
        for ws_power in ws_powers:
            _, power = ws_power
            powers.append(power)
        return FWD(powers, power_1, power_2)

    def visit_bcc(self, node, visited_children):
        _, _, power_1, _, _, power, ws_powers, _, _, power_2, _ = visited_children

        powers = [power]
        for ws_power in ws_powers:
            _, power = ws_power
            powers.append(power)
        return BCC(power_1, powers, power_2)

    def visit_order(self, node, visited_children):
        return visited_children[0]

    def visit_hld(self, node, visited_children):
        _, unit, _, _ = visited_children
        return HLD(unit)

    def visit_mto(self, node, visited_children):
        _, unit, _, _, _, province = visited_children
        return MTO(unit, province)

    def visit_sup(self, node, visited_children):
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

    def visit_cvy(self, node, visited_children):
        _, convoying_unit, _, _, _, convoyed_unit, _, _, _, province = visited_children
        return CVY(convoying_unit, convoyed_unit, province)

    def visit_move_by_cvy(self, node, visited_children):
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

    def visit_retreat(self, node, visited_children):
        return visited_children[0]

    def visit_rto(self, node, visited_children):
        _, unit, _, _, _, province = visited_children
        return RTO(unit, province)

    def visit_dsb(self, node, visited_children):
        _, unit, _, _ = visited_children
        return DSB(unit)

    def visit_build(self, node, visited_children):
        return visited_children[0]

    def visit_bld(self, node, visited_children):
        _, unit, _, _ = visited_children
        return BLD(unit)

    def visit_rem(self, node, visited_children):
        _, unit, _, _ = visited_children
        return REM(unit)

    def visit_wve(self, node, visited_children):
        power, _, _ = visited_children
        return WVE(power)

    def visit_power(self, node, visited_children):
        return node.text

    def visit_prov_coast(self, node, visited_children):
        return node.text

    def visit_prov_no_coast(self, node, visited_children):
        return Location(province=node.text)
        return node.text

    def visit_prov_sea(self, node, visited_children):
        return node.text

    def visit_supply_center(self, node, visited_children):
        return node.text

    def visit_unit(self, node, visited_children):
        power, _, unit_type, _, location = visited_children
        return Unit(power, unit_type, location=location)

    def visit_unit_type(self, node, visited_children):
        return node.text

    def visit_province(self, node, visited_children) -> Location:
        # if isinstance(visited_children, str):
        #     return node.text
        return visited_children[0]

    def visit_prov_landlock(self, node, visited_children):
        return Location(province=node.text)
        return node.text

    def visit_prov_land_sea(self, node, visited_children):
        return Location(province=node.text)
        return node.text

    def visit_prov_coast(self, node, visited_children):
        _, province, _, coast, _ = visited_children[0]
        return Location(province=province.text, coast=coast.text)
        return province.text + " " + coast.text

    def visit_coast(self, node, visited_children):
        return node.text

    def visit_turn(self, node, visited_children):
        season, _, year = visited_children
        return Turn(season, int(year.text))

    def visit_season(self, node, visited_children):
        return node.text

    def visit_try_tokens(self, node, visited_children):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node

    def visit_daide_string(self, node, visited_children):
        return visited_children[0]


daide_visitor = DAIDEVisitor()
