
window.vm = new Vue({
    el: '#mcontent',
    data: {
        "docuemtn_path": document.location.pathname,
        "local_dict": [],
        "select_city": [],
        'area_list': {},
        "city_area_select_list": {},
        "job_list": ["家事", "清潔", "傢俱", "廚衛", "建材", "油漆", "室內設計", "裝潢", "造景", "水電", "維修", "抓漏", "搬家", "貨運", "信用卡", "貸款", "代償", "保險", "理財", "證券", "期貨開戶", "收藏品拍賣", "老酒收購", "交易", "造型", "美髮", "美甲", "美睫", "彩妝師", "保養", "美妝", "瘦身", "整形醫美", "按摩Spa", "租車", "接送", "行銷", "活動", "派對企劃", "接案", "設計", "攝影", "外包", "會計", "代書", "記帳", "法律", "徵信社", "快遞", "跑腿", "代購", "派對", "聯誼", "徵友找伴", "動物醫院", "美容", "水族", "占卜", "風水", "心靈諮商", "跳蚤市場", "二手拍賣", "婚禮", "禮服", "婚攝", "新秘", "月子", "婦嬰用品玩具", "保母", "托育", "安親班", "課輔班", "看護", "健身", "舞蹈", "瑜珈", "就業", "證照", "職場英語", "體驗", "成長", "激勵課程", "兒童才藝", "安親", "升學", "留學", "補習班", "汽車交易", "機車交易", "維修保養", "汽機車精品", "車貸", "車險", "模特兒", "演藝", "外拍", "家教", "代課", "餐飲業打工", "行政", "內勤", "業務", "外勤", "門市", "專櫃", "徵求夥伴", "團隊", "投資人", "店面頂讓", "網站", "網址拍賣", "加盟", "經銷", "批發採購", "辦公室分租", "借址登記", "生財器具", "辦公設備", "租屋", "售屋", "工廠", "倉庫", "辦公租售", "店面", "攤位", "土地", "車位租售", "按摩舒壓", "同志娛樂", "活動促銷宣傳", "男按摩", "男公關", "仕女店", "五花八門", "寶塔墓園", "禮儀公司", "喪葬用品"],

        "job_select": [],
        "use_adsl": false,
        "adsl": { "name": "", "username": "", "password": "" }

    },
    methods: {
        submit_search_keyword: function () {
            var city_origin = window.vm.city_area_select_list;
            var city_list = []
            let area_list = document.querySelectorAll('#area_select>option:checked')
            var i = 0;
            for (const key in city_origin) {
                if (city_origin.hasOwnProperty(key)) {
                    let element = area_list[i].value
                    var new_pack = { "city_name": key, "area_list": element }
                    city_list.push(new_pack);
                    i++;
                }
            }            
            var job_list = $("#job_select").val();
            var custom_keyword = $("#keyword_tag textarea").val().split("\n")
            var keyword_list = job_list.concat(custom_keyword)

            var send_pack = {};
            send_pack['city'] = city_list
            send_pack['keyword'] = keyword_list
            if (this.use_adsl) {
                for (const key in this.adsl) {
                    if (this.adsl.hasOwnProperty(key)) {
                        const element = this.adsl[key];
                        if (element == "") { alert("請填寫完畢所有adsl訊息"); return 0; }
                    }
                }
                send_pack['adsl'] = this.adsl;
            }
            // console.log(send_pack);
            Send_Order("Search",send_pack)
        },
        load_local_dict: function () {
            var url = "assets/Local.json";
            var self = this;
            $.get(url, function (rs) {
                var all = rs
                self.local_dict = all;
                for (var i = 0; i < self.local_dict.length; i++) {
                    var local = self.local_dict[i];
                    var city = local['CityName'];
                    self.area_list[city] = local['AreaList'];
                }
                $("#city_select").select2();

            })
        },
        add_area: function (city) {
            var self = this;

            var city_item = $(".area-select-item[city='" + city + "']");
            
            if (city_item.is(":visible") == false || city_item.attr('open_stat') == 1) {
                city_item.show();
                city_item.select2({
                    closeOnSelect: false,
                    placeholder: "請選擇區域",
                    allowHtml: true,
                    allowClear: true,
                    tags: true
                });
                city_item.parent().find(".select2-container").show()
                city_item.attr('open_stat', 0);
            } else {
                //關閉區域選擇
                city_item.parent().find(".select2-container").hide()
                city_item.attr('open_stat', 1);
                var city_select_area = city_item.parent().find(".area-select-item").val()
                self.city_area_select_list[city] = city_select_area;
            }


        },

        add_job: function () {
            var job = $('#job_select').val();
            if (city == null) { return 0; }
            var idx = this.job_list.indexOf(job);
            if (idx == -1) {
                this.job_list.push(job)
                $("#job_select option[value='" + city + "']").remove();

            }
        },
        add_city: function () {
            var city = $('#city_select').val();
            if (city == null) { return 0; }
            var idx = this.select_city.indexOf(city);
            if (idx == -1) {
                this.select_city.push(city)
                this.city_area_select_list[city] = []                
                $("#city_select option[value='" + city + "']").remove();

            }
        },
        remove_city: function (city) {

            var idx = this.select_city.indexOf(city);

            this.select_city.splice(idx);
            delete this.city_area_select_list[city];
            //清除清單
            var options = "<option value='" + city + "'>" + city + "</option>"
            $("#city_select").append(options);

        },
        login_line: function () {
            alert(1)
            let account = document.querySelector('#exampleInputEmail1').value
            let password = document.querySelector('#exampleInputPassword1').value
            let line_pack = {"account": account, "password": password}
            console.log(account, password);
            
            Send_Order("login",line_pack)
        }
    },
    mounted() {

        this.load_local_dict();

        $("#job_select").select2({
            closeOnSelect: false,
            placeholder: "請選擇區域",
            allowHtml: true,
            allowClear: true,
            tags: true
        });

        Websocket_init();



    },
})