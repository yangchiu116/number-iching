class DigitalYiJingCalculator:
    """
    數字易經磁場分析器 - 專業強弱等級版
    包含：英文字母轉換、0/5 同化處理、八星能量四級判定 (最強/次強/次弱/最弱)
    """
    magnetic_field_map = {}

    # 補回前端 index.html 預期讀取的 優點、缺點 與 特性 欄位
    FIELD_DETAILS = {
        "天醫": {"特性": "財富、聰明、婚姻", "優點": "天生聰明、正財運佳、可成大事", "缺點": "過於單純、容易被騙、缺乏主見",
                 "能量符號": "⭐⭐⭐⭐⭐"},
        "生氣": {"特性": "貴人、人緣、轉機", "優點": "隨緣、看得開、有貴人相助", "缺點": "企圖心不足、容易妥協、懶散",
                 "能量符號": "⭐⭐⭐⭐"},
        "延年": {"特性": "事業、領導、專業", "優點": "大將之風、意志堅定、領袖特質",
                 "缺點": "壓力大、勞碌、固執、大男人/女人主義", "能量符號": "⭐⭐⭐⭐"},
        "伏位": {"特性": "等待、延續、被動", "優點": "耐心、做事謹慎、善於思考", "缺點": "缺乏安全感、猶豫不決、容易錯失良機",
                 "能量符號": "⭐⭐⭐"},
        "絕命": {"特性": "衝動、極端、冒險", "優點": "反應快、企圖心強、判斷力敏銳", "缺點": "容易走極端、脾氣暴躁、官司是非",
                 "能量符號": "💀💀💀💀"},
        "五鬼": {"特性": "才華、變動、點子", "優點": "才華橫溢、點子多、學習能力強",
                 "缺點": "沒安全感、感情易有第三者、突發災禍", "能量符號": "💀💀💀💀"},
        "禍害": {"特性": "口才、口舌、健康", "優點": "口才極佳、辯才無礙、能言道",
                 "缺點": "口舌是非、脾氣差、愛面子、免疫力弱", "能量符號": "💀💀💀"},
        "六煞": {"特性": "桃花、人際、情感", "優點": "社交力強、心思細膩、異性緣佳",
                 "缺點": "多愁善感、感情猶豫、容易有地下情", "能量符號": "💀💀💀"}
    }

    @classmethod
    def _add_level_data(cls, star_name, levels):
        """輔助方法：根據圖片表格將數字與等級配對"""
        labels = ["最強", "次強", "次弱", "最弱"]
        for i, pair_list in enumerate(levels):
            for pair in pair_list:
                cls.magnetic_field_map[pair] = (star_name, labels[i])

    @classmethod
    def initialize_data(cls):
        """依照圖片表格初始化 64 組數值與強弱等級"""
        # 四吉星
        cls._add_level_data("生氣", [["14", "41"], ["67", "76"], ["39", "93"], ["28", "82"]])
        cls._add_level_data("天醫", [["13", "31"], ["68", "86"], ["49", "94"], ["27", "72"]])
        cls._add_level_data("延年", [["19", "91"], ["78", "87"], ["34", "43"], ["26", "62"]])
        cls._add_level_data("伏位", [["11", "22"], ["99", "88"], ["66", "77"], ["33", "44"]])

        # 四凶星
        cls._add_level_data("六煞", [["16", "61"], ["47", "74"], ["38", "83"], ["29", "92"]])
        cls._add_level_data("禍害", [["17", "71"], ["89", "98"], ["46", "64"], ["23", "32"]])
        cls._add_level_data("五鬼", [["18", "81"], ["79", "97"], ["36", "63"], ["24", "42"]])
        cls._add_level_data("絕命", [["12", "21"], ["69", "96"], ["48", "84"], ["37", "73"]])

    @classmethod
    def _convert_letters(cls, text):
        """英文字母轉換 A=1, B=2...Z=26"""
        converted = ""
        for char in text.upper():
            if 'A' <= char <= 'Z':
                converted += str(ord(char) - 64)
            elif char.isdigit():
                converted += char
        return converted

    @classmethod
    def _process_0_5(cls, digits):
        """處理 0 與 5 的延續邏輯"""
        if not digits: return ""
        res = []
        for i, char in enumerate(digits):
            if char in '05':
                if i > 0:
                    res.append(res[-1])
                elif i + 1 < len(digits):
                    target = next((d for d in digits[i + 1:] if d not in '05'), char)
                    res.append(target)
                else:
                    res.append(char)
            else:
                res.append(char)
        return "".join(res)

    @classmethod
    def analyze_number(cls, number):
        """執行分析並回傳包含強弱等級的結構化資料"""
        numeric_str = cls._convert_letters(number)
        processed = cls._process_0_5(numeric_str)

        sequence = []
        summary = {}

        for i in range(len(processed) - 1):
            pair = processed[i:i + 2]
            if pair in cls.magnetic_field_map:
                star, level = cls.magnetic_field_map[pair]
                base_detail = cls.FIELD_DETAILS[star]

                # 整合強弱等級資訊到 details 中，確保前端 index.html 能讀取到
                full_detail = base_detail.copy()
                full_detail["能量"] = f"{level} {base_detail['能量符號']}"

                sequence.append({
                    "pair": f"{pair}({level})",  # 在顯示數字時標註強弱
                    "star": star,
                    "details": full_detail
                })
                summary[star] = summary.get(star, 0) + 1

        return {"sequence": sequence, "summary": summary}


# 初始化資料
DigitalYiJingCalculator.initialize_data()