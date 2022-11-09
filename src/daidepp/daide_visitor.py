from parsimonious.nodes import Node, NodeVisitor

from daidepp.keywords import *


class DAIDEVisitor(NodeVisitor):
    def visit_message(self, node, visited_children):
        return visited_children[0]

    def visit_press_message(self, node, visited_children):
        return visited_children[0]

    def visit_prp(self, node, visited_children):
        msg_type, _, arrangement, _ = visited_children
        return (msg_type.text, arrangement)

    def visit_ccl(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return ("CCL", press_message)

    def visit_fct(self, node, visited_children):
        _, _, arrangement, *_ = visited_children[0]

        if isinstance(arrangement, Node) and arrangement.text == "NOT":
            _, _, _, _, qry, _, _ = visited_children[0]
            output = ("FCT", ("NOT", qry))
        else:
            _, _, msg, _ = visited_children[0]
            output = ("FCT", msg)
        return output

    def visit_thk(self, node, visited_children):
        _, _, arrangement, *_ = visited_children[0]

        if isinstance(arrangement, Node) and arrangement.text == "NOT":
            _, _, _, _, qry, _, _ = visited_children[0]
            output = ("THK", ("NOT", qry))
        else:
            _, _, msg, _ = visited_children[0]
            output = ("THK", msg)
        return output

    def visit_try(self, node, visited_children):
        _, _, try_token, ws_try_tokens, _ = visited_children

        try_token_list = [try_token]
        for ws_try_token in ws_try_tokens:
            _, try_token = ws_try_token
            try_token_list.append(try_token)
        return ("TRY", try_token_list)

    def visit_ins(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return ("INS", arrangement)

    def visit_qry(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return ("QRY", arrangement)

    def visit_sug(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return ("SUG", arrangement)

    def visit_wht(self, node, visited_children):
        _, _, unit, _ = visited_children
        return ("WHT", unit)

    def visit_how(self, node, visited_children):
        _, _, province, _ = visited_children
        return ("HOW", province)

    def visit_exp(self, node, visited_children):
        _, _, turn, _, _, message, _ = visited_children
        return ("EXP", turn, message)

    def visit_iff(self, node, visited_children):
        _, _, arrangement, _, _, _, press_message, _, els = visited_children

        if isinstance(els, Node) and not els.text:
            output = ("IFF", arrangement, press_message)
        else:
            _, _, els_press, _ = els[0]
            output = ("IFF", arrangement, press_message, els_press)

        return output

    def visit_frm(self, node, visited_children):
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

        recv_power_list = [recv_power]
        for ws_recv_power in ws_recv_powers:
            _, recv_power = ws_recv_power
            recv_power_list.append(recv_power)

        return ("FRM", power, recv_power_list, message)

    def visit_reply(self, node, visited_children):
        return visited_children[0]

    def visit_yes(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return ("YES", press_message)

    def visit_rej(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return ("REJ", press_message)

    def visit_bwx(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return ("BWX", press_message)

    def visit_huh(self, node, visited_children):
        _, _, press_message, _ = visited_children
        return ("HUH", press_message)

    def visit_qry_wht_prp_ins(self, node, visited_children):
        return visited_children[0]

    def visit_idk(self, node, visited_children):
        _, _, message, _ = visited_children

        return ("IDK", message[0]) if isinstance(message, list) else ("IDK", message)

    def visit_sry(self, node, visited_children):
        _, _, exp, _ = visited_children
        return ("SRY", exp)

    def visit_fct_thk_prp_ins(self, node, visited_children):
        return visited_children[0]

    def visit_why(self, node, visited_children):
        _, _, message, _ = visited_children
        return ("WHY", message)

    def visit_pob(self, node, visited_children):
        _, _, why, _ = visited_children
        return ("POB", why)

    def visit_arrangement(self, node, visited_children):
        return visited_children[0]

    def visit_pce(self, node, visited_children):
        _, _, power, ws_powers, _ = visited_children

        pow_list = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            pow_list.append(pow)
        return ("PCE", pow_list)

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

        aly_list = [aly_power]
        for ws_aly_power in ws_aly_powers:
            _, aly_power = ws_aly_power
            aly_list.append(aly_power)

        vss_list = [vss_power]
        for ws_vss_power in ws_vss_powers:
            _, vss_power = ws_vss_power
            vss_list.append(vss_power)
        return ("ALY_VSS", (aly_list, vss_list))

    def visit_drw(self, node, visited_children):
        _, par_powers = visited_children

        if isinstance(par_powers, Node) and not par_powers.text:
            return "DRW"

        # For Partial draws are allowed (PDA) variant game
        _, power, ws_powers, _ = par_powers[0]
        pow_list = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            pow_list.append(pow)

        return ("DRW", pow_list)

    def visit_slo(self, node, visited_children):
        _, _, power, _ = visited_children
        return ("SLO", power)

    def visit_not(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return ("NOT", arrangement)

    def visit_nar(self, node, visited_children):
        _, _, arrangement, _ = visited_children
        return ("NAR", arrangement)

    def visit_xdo(self, node, visited_children):
        _, _, order, _ = visited_children
        return ("XDO", order)

    def visit_and(self, node, visited_children):
        _, _, arrangement, _, par_arrangements = visited_children

        arr_list = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arr_list.append(arr)
        return ("AND", arr_list)

    def visit_orr(self, node, visited_children):
        _, _, arrangement, _, par_arrangements = visited_children

        arr_list = [arrangement]
        for par_arr in par_arrangements:
            _, arr, _ = par_arr
            arr_list.append(arr)

        return ("ORR", arr_list)

    def visit_dmz(self, node, visited_children):
        _, _, power, ws_powers, _, _, province, ws_provinces, _ = visited_children

        pow_list = [power]
        for ws_pow in ws_powers:
            _, pow = ws_pow
            pow_list.append(pow)

        prov_list = [province]
        for ws_prov in ws_provinces:
            _, prov = ws_prov
            prov_list.append(prov)
        return ("DMZ", pow_list, prov_list)

    def visit_scd(self, node, visited_children):
        _, scd_statements = visited_children

        scd_list = []
        for scd_statment in scd_statements:
            _, power, _, supply_center, ws_supply_centers, _ = scd_statment

            sc_list = [supply_center]
            for ws_sc in ws_supply_centers:
                _, sc = ws_sc
                sc_list.append(sc)
            scd_list.append((power, sc_list))
        return ("SCD", scd_list)

    def visit_occ(self, node, visited_children):
        _, par_units = visited_children

        unit_list = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            unit_list.append(unit)
        return ("OCC", unit_list)

    def visit_cho(self, node, visited_children):
        _, _, range, _, par_arrangements = visited_children

        range = tuple([int(x) for x in range.text.split()])
        arr_list = []
        for par_arrangement in par_arrangements:
            _, arrangement, _ = par_arrangement
            arr_list.append(arrangement)
        return ("CHO", range, arr_list)

    def visit_for(self, node, visited_children):
        _, _, turn, _, _, arrangement, _ = visited_children[0]

        if isinstance(turn, list):
            _, start_turn, _, _, end_turn, _ = turn
            output = ("FOR", start_turn, end_turn, arrangement)
        else:
            output = ("FOR", turn, arrangement)
        return output

    def visit_xoy(self, node, visited_children):
        _, _, power_x, _, _, power_y, _ = visited_children
        return ("XOY", power_x, power_y)

    def visit_ydo(self, node, visited_children):
        _, _, power, _, par_units = visited_children

        unit_list = []
        for par_unit in par_units:
            _, unit, _ = par_unit
            unit_list.append(unit)
        return ("YDO", power, unit_list)

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

        recv_power_list = [recv_power]
        for ws_recv_power in ws_recv_powers:
            _, recv_power = ws_recv_power
            recv_power_list.append(recv_power)
        return ("SND", power, recv_power_list, message)

    def visit_fwd(self, node, visited_children):
        _, _, power1, ws_powers1, _, _, power2, _, _, power3, _ = visited_children

        power1_list = [power1]
        for ws_power1 in ws_powers1:
            _, power1 = ws_power1
            power1_list.append(power1)
        return ("FWD", power1_list, power2, power3)

    def visit_bcc(self, node, visited_children):
        _, _, power1, _, _, power2, ws_powers2, _, _, power3, _ = visited_children

        power2_list = [power2]
        for ws_power2 in ws_powers2:
            _, power2 = ws_power2
            power2_list.append(power2)
        return ("BCC", power1, power2_list, power3)

    def visit_order(self, node, visited_children):
        return visited_children[0]

    def visit_hld(self, node, visited_children):
        _, unit, _, _ = visited_children
        return ("HLD", unit)

    def visit_mto(self, node, visited_children):
        _, unit, _, _, _, province = visited_children
        return ("MTO", unit, province)

    def visit_sup(self, node, visited_children):
        _, supporting_unit, _, _, _, supported_unit, _, ws_mto_prov = visited_children

        if isinstance(ws_mto_prov, Node) and not ws_mto_prov.text:
            output = ("SUP", supporting_unit, supported_unit)
        else:
            _, _, mto_prov = ws_mto_prov = ws_mto_prov[0]
            output = ("SUP", supporting_unit, supported_unit, mto_prov)
        return output

    def visit_cvy(self, node, visited_children):
        _, convoying_unit, _, _, _, convoyed_unit, _, _, _, province = visited_children
        return ("CVY", convoying_unit, convoyed_unit, province)

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
            prov_sea,
            ws_prov_seas,
            _,
        ) = visited_children

        prov_sea_list = [prov_sea]
        for ws_prov_sea in ws_prov_seas:
            _, prov_sea = ws_prov_sea
            prov_sea_list.append(prov_sea)
        return ("CVY", unit, province, prov_sea_list)

    def visit_retreat(self, node, visited_children):
        return visited_children[0]

    def visit_rto(self, node, visited_children):
        _, unit, _, _, _, province = visited_children
        return ("RTO", unit, province)

    def visit_dsb(self, node, visited_children):
        _, unit, _, _ = visited_children
        return ("DSB", unit)

    def visit_build(self, node, visited_children):
        return visited_children[0]

    def visit_bld(self, node, visited_children):
        _, unit, _, _ = visited_children
        return ("BLD", unit)

    def visit_rem(self, node, visited_children):
        _, unit, _, _ = visited_children
        return ("REM", unit)

    def visit_wve(self, node, visited_children):
        power, _, _ = visited_children
        return ("WVE", power)

    def visit_power(self, node, visited_children):
        return node.text

    def visit_prov_coast(self, node, visited_children):
        return node.text

    def visit_prov_no_coast(self, node, visited_children):
        return node.text

    def visit_prov_sea(self, node, visited_children):
        return node.text

    def visit_supply_center(self, node, visited_children):
        return node.text

    def visit_unit(self, node, visited_children):
        power, _, unit_type, _, province = visited_children
        return power, unit_type, province

    def visit_unit_type(self, node, visited_children):
        return node.text

    def visit_province(self, node, visited_children):
        if isinstance(visited_children, str):
            return node.text
        return visited_children[0]

    def visit_prov_landlock(self, node, visited_children):
        return node.text

    def visit_prov_land_sea(self, node, visited_children):
        return node.text

    def visit_prov_coast(self, node, visited_children):
        _, province, _, coast, _ = visited_children[0]
        return province.text + " " + coast.text

    def visit_coast(self, node, visited_children):
        return node.text

    def visit_turn(self, node, visited_children):
        season, _, year = visited_children
        return season + " " + year.text

    def visit_season(self, node, visited_children):
        return node.text

    def visit_try_tokens(self, node, visited_children):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node


daide_visitor = DAIDEVisitor()
