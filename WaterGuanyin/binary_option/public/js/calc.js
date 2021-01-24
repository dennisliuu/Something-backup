var ctx = document.getElementById("myChart");
ctx.height = document.height*0.8;
ctx.width = document.width*0.2;
var current_price = 0;
window.buy_team = []

var sun = new Image();
sun.src = '/asset/head.png';
Chart.pluginService.register({
    afterUpdate: function(chart) {
        try {
            for (let index = 0; index < buy_team.length; index++) {
                var c = buy_team[index];
                chart.config.data.datasets[0]._meta[0].data[c]._model.pointStyle = sun;
                
            }
           
        } catch (err) {
            
        }
        
    }
});
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: "line",
    scaleOverride: true,
    scaleSteps: 10,
    // The data for our dataset
    data: {
        labels: [],
        datasets: [{
            label: "BTC price",
            backgroundColor: "rgba(34,148,230,.1)",
            borderColor: "#4B6F9E",
            data: [],

        }]
    },
    draw:function(){
        console.log("draw")
    },
    // Configuration options go here
    options: {
        responsive: true,

    }
});

window.ctx = chart;


window.vm = new Vue({
    el: '#infomation',
    data: {
       now_price:0,
       work_unit:30,//比賽頻率
       work_hash:"",
       now_time:0,
       af_time:0,
       buyer_list:[],
       balance:1000,
       pofit:0,
       now_num:0


    },
    methods: {
    
    add_bet:function(btype,money){
        //下注
        var tt = get_time()
        var pack = {'type':btype,'money':money,'hash':this.work_hash,'time':tt['fmt'],'buy_price':this.now_price}
        this.buyer_list.push(pack)
        this.balance -= money;
        this.pofit -= money
        window.buy_team.push(this.now_num-1)
    },
    calc_result:function(){
        //計算結果
        var now_price = this.now_price;
        for(var i=0; i<this.buyer_list.length; i++){
            var bet = this.buyer_list[i];
           var is_win = this.judgment_win_or_fail(bet,now_price);
           if(is_win) {
               this.balance += (bet['money']*2);
               this.pofit += bet['money']*2;
        }
           console.log(bet)
           console.log(is_win)
        }
        this.buyer_list = [];
    },
    judgment_win_or_fail:function(buy_item,asset_price){
        if(buy_item['type'] == 'buy'){
            if(buy_item['buy_price'] < asset_price){
                return 1;
            }
        }

        if(buy_item['type'] == 'sell'){
            if(buy_item['buy_price'] > asset_price){
                return 1;
            }
        }

        return 0;
    },
    race_animate:function(){
        for(var i=0; i<this.buyer_list.length; i++){
            var bet = this.buyer_list[i];
           var is_win = this.judgment_win_or_fail(bet,this.now_price);
        //    if(is_win) {
        //
        //     var element = $(".buy_tr tr").eq(i)[0];
        //     animateCSS(element,"bounce")
        //    }
        //
        }
    },
      update_race:function(time_pack){
        var hash = time_pack['fmt']
        var time_obj = time_pack['obj'];
        var sec = time_obj.getSeconds();
        sec = parseFloat(sec)
        // console.log(sec)
        // console.log(this.work_hash)
        this.race_animate()
        if ( sec== 0 || sec == 30 || this.work_hash == "") {
           this.renew_work_race(hash)//更新賽局
        }
        var af = 0;
        if (sec < 30){
            af = 30 - sec;
        }
        if (sec >= 30){
            af = 60 - sec ;
        }
        this.af_time =af
      },
      renew_work_race:function(new_work_hash){
          this.calc_result()
          this.work_hash = new_work_hash
      }

    }
})
function animateCSS(node, animationName, callback) {
    // const node = document.querySelector(element)
    console.log(node)
    node.classList.add('animated', animationName)

    function handleAnimationEnd() {
        node.classList.remove('animated', animationName)
        node.removeEventListener('animationend', handleAnimationEnd)

        if (typeof callback === 'function') callback()
    }

    node.addEventListener('animationend', handleAnimationEnd)
}


var cloud = new Image();
cloud.src = 'https://i.imgur.com/DIbr9q1.png';
var p1 = new Image();
p1.src = 'https://i.imgur.com/DIbr9q1.png';
var p2 = new Image();
p2.src = 'https://i.imgur.com/DIbr9q1.png';


var add_times = 0;

function addData(chart, time_pack, data) {
    var label = time_pack['fmt']
    add_times += 1; // 這邊想要改成5次或者10次才加上時間label 
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    window.vm.now_price = data;
    window.vm.now_num = window.chart.data.labels.length
    // window.vm.now_time = time_pack['obj']
    window.vm.update_race(time_pack);
    chart.update();
}

function get_time() {
    var currentdate = new Date();
    var datetime =
        currentdate.getHours() + ":" +
        currentdate.getMinutes() + ":" +
        currentdate.getSeconds();
    var pack = {'obj':currentdate,"fmt":datetime}
    return pack;
}

setInterval(() => {
        addData(chart, get_time(), current_price);
    }, 1500

)