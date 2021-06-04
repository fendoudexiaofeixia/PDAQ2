<template>
    <div class="contrast-right">
        <div class="contrast-content">
            <div class="contrast-top-content">
                 <Collapse v-model="test1" class="history-collapse">
                    <Panel name="1">
                        <h3>历史版本通过率对比</h3>
                        <el-card class="box-card history-card" slot="content"  shadow="hover">
                            <div id="history" class="history"></div>
                        </el-card>
                    </Panel>
                </Collapse>
            </div>
            <div class="contrast-bottom-content">
                <el-card class="constrast-card">
                    <div slot="header" class="clearfix">
                        <h3>版本对比</h3>
                    </div>
                    <div class="search-content search-top">
                        <el-form :inline="true" :model="contrastForm" ref="contrastForm" label-width="100px" :rules="rules" class="demo-form-inline">
                            <div class="form-case" >                       
                                <el-form-item  label="测试项："  prop="case">
                                    <el-cascader
                                            collapse-tags
                                            filterable
                                            v-model="contrastForm.case"
                                            placeholder="请选择测试项"
                                            :options="modelOptions"
                                            :props="{ multiple: true }"
                                            clearable
                                            class="case_select">
                                    </el-cascader>
                                </el-form-item>
                                <el-form-item label="版本："   prop="versions">
                                    <el-select 
                                        collapse-tags
                                        v-model="contrastForm.versions" placeholder="请选择版本" multiple class="version_select" clearable >
                                        <el-option
                                            v-for="(item,index) in versionOptions"
                                            :key="item.name+index"
                                            :label="item.name"
                                            :value="item.name">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                                <el-form-item label="测试用例："  prop="stage" >
                                    <el-select v-model="contrastForm.stage" placeholder="请选择用例等级"  class="" clearable >
                                        <el-option
                                            v-for="item in caseOptions"
                                            :key="item.value"
                                            :label="item.level"
                                            :value="item.value">
                                        </el-option> 
                                    </el-select>
                                </el-form-item>
                                <el-form-item >
                                    <el-button class="contrast-btn" @click="startContrast('contrastForm')" >开始对比</el-button>
                                </el-form-item>
                            </div>   
                        </el-form>
                    </div>
                    <el-card class="box-card case-card" v-for="(caseItem,caseIndex) in caseArr" :key="caseIndex+'case'">
                        <div slot="header" class="clearfix">
                            <span>{{caseItem.name}}</span>
                        </div>
                        <el-tabs v-if="caseItem.data.length>0" class="obj_tabs" @tab-click="handleClick(caseItem)"   v-model="caseItem.activeName">
                            <el-tab-pane v-for="(detailItem,detailIndex) in caseItem.data" :label="detailItem.name" :name="detailItem.name"  :key="detailItem.name+detailIndex">
                                <div class="suitesContent">
                                    <el-card class="box-card suite-card">
                                        <div slot="header" class="clearfix">
                                            <span>目标类型对比</span>
                                        </div>
                                        <div :id="caseItem.name+detailItem.name+'d'"  class="suite_chart"></div>
                                    </el-card>
                                </div>
                                <div class="featureContent"> 
                                    <el-card class="box-card suite-card">
                                        <div slot="header" class="clearfix">
                                            <span>场景对比</span>
                                        </div>
                                        <div :id="caseItem.name+detailItem.name+'f'" class="feature_chart"></div>
                                    </el-card>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </el-card>
                </el-card>
            </div>
        </div>
    </div>
</template>
<script>
    import { get_history , get_case_items ,get_constract_result } from  "@/api/user";
    var echarts = require('echarts');
    export default {
        activated: function() {
            this.init();
        },
        data(){
            return{
                rules: {
                    case: [
                        { required: true, message: '请选择测试项', trigger: 'blur' },
                    ],
                    versions: [
                        { required: true, message: '请选择版本', trigger: 'blur' },
                    ],     
                    stage: [
                        { required: true, message: '请选择测试用例', trigger: 'blur' },
                    ],
                },
                caseArr:[],
                activeName:'0',
                caseList:[],
                contrastForm:{
                    case:[],
                    versions:[],
                    stage:null,
                    items:[],
                },
                versionTest:'1',
                caseLevel:null,
                caseOptions:[
                    {
                        level:'all',
                        value:0
                    },{
                        level:'1',
                        value:1
                    },{
                        level:'2',
                        value:2
                    }
                ],
                versionOptions:null,
                version:null,
                modelOptions:[],
                versionArr:null,
                historyData:null,
                test1:'1',
                test:null,
                nameArr :[],
                testArr:[],
                caseItems:[],
                features:[],
                caseSuites:[],
                arr:[],
                suite_items:[],
                versionDataArr:[],
            }
        },
        mounted(){
            this.init();
        },
        methods:{
            handleClick(activeItem){
                this.drawSuites(activeItem ,this.caseArr);
                this.drawFeatures(activeItem ,this.caseArr);
            },
            sliceSearchOptions(item){
                var index = this.contrastForm.searchConditions.indexOf(item) 
                if (index !== -1) {
                    this.contrastForm.searchConditions.splice(index, 1)
                }
            },
            testpromise(value){
                return new Promise((resolve)=>{
                    resolve(
                        get_constract_result(value)
                        .then(res=>{
                            if(res.data){
                                return res.data
                            }
                        })
                    );
                });
            },
            startContrast(formName){
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.caseItems = [];
                        this.versionDataArr = [];
                        this.contrastForm.case.forEach(item=>{
                            this.caseItems.push(item)
                        });
                        var that  =  this;
                        that.caseArr=[];
                        // 获取对比接口 
                        // 参数：program(当前程序ysg,calmcar),versions(选择版本号),stage(选择测试用例等级),items(选择测试项)
                        that.testpromise({
                            program:(this.$route.params.program).toLowerCase(),
                            versions:(this.contrastForm.versions).toString(),
                            stage:this.contrastForm.stage=='all'?'0':this.contrastForm.stage,
                            items:this.caseItems})
                            .then(function (res) {
                                that.versionDataArr = res.versions;
                                for(var i=0;i<res.data.length;i++){
                                    res.data[i].activeName = res.data[i].data[0].name;
                                    that.caseArr.push(res.data[i])
                                }
                            })
                    }else{
                         this.$message({
                            message: '请选择对比内容',
                            type: 'error'
                         })
                    }
                })
            },
            drawFeatures(activeItem,caseArr){
                this.myChart = echarts.init(document.getElementById(activeItem.name+activeItem.activeName+'f')); 
                var featureName = [];                
                var series=[];
                var featureDatas = []
                for(var i = 0;i< caseArr.length;i++){
                    for(var j=0;j<caseArr[i].data.length;j++){
                        if(caseArr[i].data[j].name== activeItem.activeName && caseArr[i].name ==activeItem.name ){
                            featureName=caseArr[i].data[j].features;
                            for(var k=0;k<caseArr[i].data[j].data.length;k++){
                                if(caseArr[i].data[j].data[k].name =="features"){
                                    for(var v=0;v<this.versionDataArr.length;v++){
                                        var featureData = [];
                                        for(var m =0;m<caseArr[i].data[j].data[k].data.length;m++){
                                            featureData.push(caseArr[i].data[j].data[k].data[m].data[v])
                                        }
                                        featureDatas.push(featureData)
                                    }
                                }
                            }
                        }
                    } 
                }
                var color = ['#7DC4FC','#43D64D','#FFCC00','#FF8307','#FF3E3E','#9243D6','#6AB4FF', '#FF9A22'];
                for(var ss=0;ss<featureDatas.length;ss++){
                    series.push( {
                        name: this.versionDataArr[ss],
                        type: 'bar',
                        barWidth: '10%',
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: color[ss]
                                }, {
                                    offset: 1,
                                    color: color[ss]
                                }]),
                                barBorderRadius: 4,
                            },
                        },
                        data: featureDatas[ss]
                    })
                }

    
                this.optionmyChart = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: { // 坐标轴指示器，坐标轴触发有效 
                            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    grid: {
                        top:'8%',
                        left: '22%',
                        right: '0%',
                        bottom: '2%',
                        containLabel: true
                    },
                    legend: {
                        orient:  'vertical',
                        top:'2%',
                        left:'1%',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                            "padding": [3, 6],

                        },
                        data:this.versionDataArr,
                    },
                    xAxis: {
                        type: 'category',
                        data: featureName,
                        axisLine: {
                            lineStyle: {
                                color: "#999"
                            }
                        }, 
                        axisLabel: {
                            textStyle: {
                                color:'#333'
                            },
                            interval:0,//横轴信息全部显示  
                            rotate:20,
                        },
                    },
                    yAxis: {
                        type: 'value',
                        splitNumber: 4,
                        splitLine: {
                            lineStyle: {
                                type: 'dashed',
                                color: '#DDD'
                            }
                        },
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: "#333"
                            },
                        },
                        nameTextStyle: {
                            color: "#333"
                        },
                        splitArea: {
                            show: false
                        }
                    },
                    // dataZoom: [{
                    //     show: true,
                    //     height: 12,
                    //     xAxisIndex: [0],
                    //     bottom:'4%',
                    //     start: 10,
                    //     end: 90,
                    //     handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
                    //     handleSize: '110%',
                    //     handleStyle:{
                    //         color:"#d3dee5",
                    //     },
                    //     textStyle:{
                    //         color:"#333"
                    //     },
                    //     borderColor:"#90979c"
                    // }, {
                    //     type: "inside",
                    //     show: true,
                    //     height: 40,
                    //     start: 1,
                    //     end: 35
                    // }],
                    series: series,
                }
                this.myChart.setOption(this.optionmyChart);
                     
            },
            drawSuites(activeItem,caseArr){
                this.myChart = echarts.init(document.getElementById(activeItem.name+activeItem.activeName+'d')); 
                var series=[];
                var color = ['#27A9FF','#43D64D','#FFCC00','#FF8307','#FF3E3E','#9243D6'];
                for(var i = 0;i< caseArr.length;i++){
                    for(var j=0;j<caseArr[i].data.length;j++){
                        if(caseArr[i].data[j].name== activeItem.activeName && caseArr[i].name ==activeItem.name ){
                            for(var k=0;k<caseArr[i].data[j].data.length;k++){
                                if(caseArr[i].data[j].data[k].name =="suites"){
                                    for(var m =0;m<caseArr[i].data[j].data[k].data.length;m++){
                                        series.push({
                                            name: caseArr[i].data[j].data[k].data[m].name,
                                            type: 'line',
                                            data: caseArr[i].data[j].data[k].data[m].data,
                                            itemStyle: {
                                                normal: {
                                                    color:color[m],
                                                    borderWidth: 1,
                                                }
                                            },
                                            // smooth: true
                                        });         
                                        this.optionmyChart = {
                                            tooltip: {
                                                trigger: 'axis'
                                            },
                                            legend: {
                                                orient:  'vertical',
                                                top:'2%',
                                                left:'1%',
                                                itemWidth: 12,
                                                itemHeight: 12,
                                                textStyle: {
                                                    color: '#505050',
                                                    "padding": [3, 6],

                                                },
                                                data:caseArr[i].data[j].classes
                                            },
                                            grid: {
                                                top:'6%',
                                                left: '22%',
                                                right: '0%',
                                                bottom: '2%',
                                                containLabel: true
                                            },
                                            xAxis: [{
                                                type: 'category',
                                                data: this.versionDataArr,
                                                axisLine: {
                                                    lineStyle: {
                                                        color: "#999"
                                                    }
                                                }, 
                                                axisLabel: {
                                                    textStyle: {
                                                        color:'#333'
                                                    },
                                                    interval:0,//横轴信息全部显示  
                                                    rotate:10,
                                                },
                                            }],
                                            yAxis: [{
                                                type: 'value',
                                                splitNumber: 4,
                                                splitLine: {
                                                    lineStyle: {
                                                        type: 'dashed',
                                                        color: '#DDD'
                                                    }
                                                },
                                                axisLine: {
                                                    show: false,
                                                    lineStyle: {
                                                        color: "#333"
                                                    },
                                                },
                                                nameTextStyle: {
                                                    color: "#333"
                                                },
                                                splitArea: {
                                                    show: false
                                                }
                                            }],
                                            series:series,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                this.myChart.setOption(this.optionmyChart);
            },
            init(){
                get_case_items()
                 .then(res=>{
                     this.modelOptions = [];
                     res.data.forEach(item=>{
                        const caseData = {};
                        caseData.label = item.name;
                        caseData.value = item.name;
                        caseData.children = [];
                        item.children.forEach(child=>{
                            const childData= {};
                            childData.label = child.name;
                            childData.value = child.name;
                            childData.children = [];
                            child.children.forEach(son=>{
                                const sonData = {};
                                sonData.label = son.name ; 
                                sonData.value = son.name ; 
                                childData.children.push(sonData)
                            })
                            caseData.children.push(childData)
                         })
                        this.modelOptions.push(caseData);
                     })
                 })
                get_history({program:this.$route.params.program.toLowerCase()})
                .then(res=>{
                    this.versionArr =[];
                    this.nameArr = [];
                    this.historyData = [];
                    this.versionOptions = [];
                    this.nameArr= res.data.test_items;
                    this.historyCaseArr  = res.data.data;
                    this.versionArr  = res.data.versions;
                    res.data.versions.forEach(item=>{
                        const tableData ={};
                        tableData.name = item;
                        this.versionOptions.push(tableData);
                    })
                    // res.data.forEach(item => {
                        
                        // const tableData ={};
                        // tableData.name = item.name;
                        // tableData.value = item.name;
                        // var nameData = null;
                        // this.versionArr.push(tableData.value);
                        // this.versionOptions.push(tableData);
                        // item.data.forEach(child=>{
                        //     // console.log(child)
                        //     child.children.forEach(son=>{
                        //         nameData = son.name == 'performance'||son.name == 'report_functional'? child.name:child.name +'_'+son.name;
                        //         // lineData = son.passed/son.total.toFixed(2);
                                
                        //         this.nameArr.push (nameData);
                        //         // if(a==0){

                        //             // this.testArr[a].name = son.name == 'performance'? child.name:child.name +'_'+son.name
                        //         // }    
                        //         // var passPercent1 =  (son.passed/son.total).toFixed(2);
                        //         // this.testArr[a].data.push(passPercent1);
                        //     })

                        // })
                    // });
                    // this.nameArr =Array.from( new Set(this.nameArr));
                    // this.historyCaseArr = [];
                    // for(var i=0;i<this.nameArr.length;i++){
                    //     const caseData = {"name":this.nameArr[i], "data":[]};
                    //     caseData.data=['22','333']
                    //     this.historyCaseArr.push(caseData)
                    // }
                    this.drawAllHistory();
                    
                })
                                       
            },

            drawAllHistory(){
                this.myChart = echarts.init(document.getElementById('history')); 
                var series=[];
                var color = ['#9E87FF','#7DC4FC','#73DD54','#FFCC00','#46D4C7','#FF8307',  ];
                for(var i = 0;i<this.historyCaseArr.length;i++){
                    series.push({
                        name: this.historyCaseArr[i].name,
                        type: 'line',
                        smooth: true,
                        data: this.historyCaseArr[i].data,
                        itemStyle: {
                            normal: {
                                color:color[i],
                                borderWidth: 1,
                            }
                        },
                        
                        // smooth: true
                    });
                }
                this.optionmyChart = {
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        orient:  'vertical',
                        top:'2%',
                        left:'1%',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                                "padding": [3, 6],

                        },
                        data:this.nameArr
                    },
                    grid: {
                        top:'6%',
                        left: '20%',
                        right: '0%',
                        bottom: '2%',
                        containLabel: true
                    },
                    xAxis: [{
                        type: 'category',
                        data: this.versionArr,
                        splitLine: {
                            show:false
                        },
                        axisLine: {
                            lineStyle: {
                                color: "#999"
                            }
                        },
                        axisTick:{
                            show:false,
                        },
                        axisLabel: {
                            textStyle: {
                                color:'#333'
                            },
                            interval:0,//横轴信息全部显示  
                            rotate:10,
                        },
                    }],
                    yAxis: [{
                        type: 'value',
                        splitNumber: 4,
                        splitLine: {
                            lineStyle: {
                                type: 'dashed',
                                color: '#DDD'
                            }
                        },
                        axisLine: {
                            show: false,
                            // lineStyle: {
                            //     color: "#333"
                            // },
                        },
                        nameTextStyle: {
                            color: "#333"
                        },
                        splitArea: {
                            show: false
                        }
                    }],
                    series:series,
                }
                this.myChart.setOption(this.optionmyChart);
            }
        },
        updated(){
            for(var e = 0;e<this.caseArr.length;e++){
                this.drawSuites(this.caseArr[e],this.caseArr);
                this.drawFeatures(this.caseArr[e],this.caseArr)
            }
           
        },
        watch: {
            '$route' (to, from) { //监听路由是否变化
                if(to.params.program != from.params.program){
                    this.init();//重新加载数据
                }
            }
        },

    }
</script>
<style lang="less">
    .suite_chart{
        width: 66vw;
        height: 14vw;
    }
    .feature_chart{
        width: 66vw;
        height: 14vw; 
    }
    #conSuites{
        width: 100%;
        height: 100%;    
    }
    .suitesContent,.featureContent{
        width: 100%;
        height: 20vw;
        margin: 1vw 1vw ;   
        .suite-card{
            width: 100%;
            height: 20vw;
        }
        .el-card__body{
            width: 100%;
            height: 20vw;
        }
        .el-card__header{
            width: 100%;
        }
        .el-card__header .clearfix::before{
            content: '  ';
            width: 4px;
            height: 20px;
            background-color: #5673FF;
            position: absolute;   
        }
        .el-card__header span{
            margin-left: 14px;
        }

        // .shu{
        //     color:#29A2FF;
        //     margin-top: -4px;
        // }
    }

    .contrast-right{
        width: 100%;
        height: 100%;
        padding: 2vw 3vw;
        background-color: #F8FAFD;

    }
    .contrast-content{
        height: 100%;
        width: 100%;
        .contrast-bottom-content{
            margin: 1vw 0 0;

        }
        .history{
            width: 100%;
            height: 16vw;
        }
    }
    .search-top{
        width: 100%;
        margin: 1vw 0 0.4vw;
    }
    .search-content{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .contrast-btn{
        float:right;
        background-color: #5673FF;
        border: 1px solid #5673FF;
        box-shadow: 0 2px 6px 0 rgba(114,124,245,.5);
        color: #ffffff;
        line-height: 1;
            height: 100%;

        // padding: 0.4vw 1vw;
        font-size: 0.6vw;
    }
    .right-panel{
        float: right;
        height: 100%;
        line-height: 1;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        .contrast-add-btn{
            float:right;
            background-color: #fff;
            border: 1px solid #2980FF;
            color: #2980FF;
            padding: 0.4vw 1vw;
            font-size: 0.6vw;
        }
        .contrast-btn{
            float:right;
            background-color: #2980FF;
            border: 0px;
            color: #ffffff;
            padding: 0.4vw 1vw;
            font-size: 0.6vw;
        }
    }

    .history-collapse{
        box-shadow: rgba(154, 161, 171, 0.15) 0px 0px 35px 0px;
        border: 1px solid #EBEEF5;
        background-color: #FFF;
        border-radius:8px ;
        .ivu-collapse-header{
            height: auto !important;
            line-height: 1 !important;
            padding: 1.8rem 2rem 0.8rem;
            border-bottom: 0px solid #EBEEF5 !important;
            .ivu-icon{
                float: left;
            }
            h3{
                float: left;
                color: #0F1010
            }
        }
    }

    .form-case{
        width: 100%;
    }
    .case_select{
        width: 321px;
    }
    .version_select{
        min-width: 300px;
        .el-select__tags{
            max-width: auto !important;
        }
    }
    .el-cascader-menu__wrap{
        min-height: 104px;
        height: auto;
    }
    .constrast-card{
        border-radius: 8px;
        box-shadow: rgba(154, 161, 171, 0.15) 0px 0px 35px 0px !important;
        .el-card__header{
            border-bottom: 0px;
            padding: 1.5rem 3rem 0rem;
        }
        .el-card__body{
            width: 100%;
            height: 81%;
        }
    }
    .history-card{
        border: 0px;
      
    }

    .case-card{
        width: 100%;
        .el-card__body {
            width: 100%;
            padding: 1vw 2vw;
        }
        .el-card__header{
            width: 100%;
        }
        .el-card__header span{
            margin-left: 14px;
        }
        .el-tabs__active-bar{
            background-color: #5673FF;
        }
        .el-tabs__item.is-active{
            color: #5673FF;
        }
        // .el-card__header .clearfix::before{
        //     content: '  ';
        //     width: 4px;
        //     height: 20px;
        //     background-color: #29A2FF;
        //     position: absolute;   
        // }
    }
</style>