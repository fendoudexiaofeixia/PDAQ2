export default {
    transformSecond:function(value){
        var theTime = parseInt(value);
        var theTime1 = 0;// 分 
        var theTime2 = 0;// 小时 
        var theTime3 = 0;// 天
        if(theTime > 60) { 
            theTime1 = parseInt(theTime/60); 
            theTime = parseInt(theTime%60); 
            if(theTime1 > 60) { 
                theTime2 = parseInt(theTime1/60); 
                theTime1 = parseInt(theTime1%60); 
                if(theTime2 > 24){
                    //大于24小时
                    theTime3 = parseInt(theTime2/24);
                    theTime2 = parseInt(theTime2%24);
                }
            } 
        } 
        var result = '';
        if(theTime > 0){
        result = ""+parseInt(theTime)+"秒";
        }
        if(theTime1 > 0) { 
        result = ""+parseInt(theTime1)+"分"+result; 
        } 
        if(theTime2 > 0) { 
        result = ""+parseInt(theTime2)+"小时"+result; 
        } 
        if(theTime3 > 0) { 
        result = ""+parseInt(theTime3)+"天"+result; 
        }
        return result; 
    },
    transformDate:function(value){
        var date = new Date(value*1000)
        var year = date.getFullYear();
        var month = (date.getMonth() + 1 )<10 ? "0" +(date.getMonth() + 1) : (date.getMonth() + 1);
        var day = date.getDate()<10?"0"+date.getDate():date.getDate();
        var hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
        var minute = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
        var second = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
        var currentTime = year + "-" + month + "-" + day + "  " + hour + ":" + minute + ":" + second;
        return currentTime
    }

}
