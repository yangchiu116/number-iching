class DigitalYiJingCalculator:
    """
    數字易經磁場分析器 - 專業邏輯版
    包含：0/5 同化處理、八星詳細解釋、能量統計
    """
    magnetic_field_map = {}

    # 八星磁場詳細解釋資料庫
    FIELD_DETAILS = {
        "天醫": {"特性": "財富、聰明、婚姻", "優點": "天生聰明、正財運佳、可成大事", "缺點": "過於單純、容易被騙、缺乏主見",
                 "能量": "⭐⭐⭐⭐⭐"},
        "生氣": {"特性": "貴人、人緣、轉機", "優點": "隨緣、看得開、有貴人相助", "缺點": "企圖心不足、容易妥協、懶散",
                 "能量": "⭐⭐⭐⭐"},
        "延年": {"特性": "事業、領導、專業", "優點": "大將之風、意志堅定、領袖特質",
                 "缺點": "壓力大、勞碌、固執、大男人/女人主義", "能量": "⭐⭐⭐⭐"},
        "伏位": {"特性": "等待、延續、被動", "優點": "耐心、做事謹慎、善於思考", "缺點": "缺乏安全感、猶豫不決、容易錯失良機",
                 "能量": "⭐⭐⭐"},
        "絕命": {"特性": "衝動、極端、冒險", "優點": "反應快、企圖心強、判斷力敏銳", "缺點": "容易走極端、脾氣暴躁、官司是非",
                 "能量": "💀💀💀💀"},
        "五鬼": {"特性": "才華、變動、點子", "優點": "才華橫溢、點子多、學習能力強",
                 "缺點": "沒安全感、感情易有第三者、突發災禍", "能量": "💀💀💀💀"},
        "禍害": {"特性": "口才、口舌、健康", "優點": "口才極佳、辯才無礙、能言善道",
                 "缺點": "口舌是非、脾氣差、愛面子、免疫力弱", "能量": "💀💀💀"},
        "六煞": {"特性": "桃花、人際、情感", "優點": "社交力強、心思細膩、異性緣佳",
                 "缺點": "多愁善感、感情猶豫、容易有地下情", "能量": "💀💀💀"}
    }

    @classmethod
    def _add_field(cls, *params):
        """輔助方法：將多個數字組合加入到地圖中"""
        field_name = params[-1]
        for pair in params[:-1]:
            cls.magnetic_field_map[pair] = field_name

    @classmethod
    def initialize_data(cls):
        """初始化八星對應表"""
        # 四吉星
        cls._add_field("13", "31", "68", "86", "49", "94", "27", "72", "天醫")
        cls._add_field("14", "41", "67", "76", "39", "93", "28", "82", "生氣")
        cls._add_field("19", "91", "87", "78", "43", "34", "26", "62", "延年")
        cls._add_field("11", "22", "99", "88", "77", "66", "44", "33", "00", "55", "伏位")
        # 四凶星
        cls._add_field("12", "21", "69", "96", "84", "48", "37", "73", "絕命")
        cls._add_field("18", "81", "79", "97", "36", "63", "24", "42", "五鬼")
        cls._add_field("17", "71", "89", "98", "46", "64", "23", "32", "禍害")
        cls._add_field("16", "61", "47", "74", "38", "83", "29", "92", "六煞")

    @classmethod
    def _process_0_and_5(cls, digits):
        """
        處理 0 與 5 的特殊解碼規則（修正版）
        規則：0 代表隱藏/延續，5 代表凸顯/強化
        """
        processed = []  # 修正：確保初始化為列表，解決 Expression expected 錯誤
        for i in range(len(digits)):
            current = digits[i]
            if current in ['0', '5']:
                if i > 0:
                    # 延續前一位數字的能量
                    processed.append(processed[i - 1])
                elif i + 1 < len(digits):
                    # 若在首位則參考後一位
                    processed.append(digits[i + 1])
                else:
                    processed.append(current)
            else:
                processed.append(current)
        return "".join(processed)

    @classmethod
    def analyze_number(cls, number):
        """
        分析數字字串並回傳結構化資料
        :return: 包含詳細序列 (sequence) 與 統計摘要 (summary) 的字典
        """
        if not number or len(number) < 2:
            return {"sequence": [], "summary": {}}

        # 1. 執行 0 與 5 的專業預處理
        processed_num = cls._process_0_and_5(number)

        sequence = []
        summary = {}

        # 2. 兩兩拆解分析
        for i in range(len(processed_num) - 1):
            pair = processed_num[i:i + 2]
            original_pair = number[i:i + 2]  # 保留原始數字供前端對照
            star = cls.magnetic_field_map.get(pair)

            if star:
                detail = cls.FIELD_DETAILS.get(star, {})
                # 加入詳細序列
                sequence.append({
                    "pair": original_pair,
                    "processed_pair": pair,
                    "star": star,
                    "details": detail
                })
                # 加入統計摘要 (供圓餅圖使用)
                summary[star] = summary.get(star, 0) + 1

        return {"sequence": sequence, "summary": summary}


# 程式載入時自動執行初始化
DigitalYiJingCalculator.initialize_data()