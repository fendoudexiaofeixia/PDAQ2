<template>
    <div class="contrast-right">
        <div class="contrast-content">
            <div class="contrast-top-content">
                 <Collapse v-model="test1">
                    <Panel name="1">
                        历史版本通过率对比
                        <el-card class="box-card" slot="content">
                            <div id="history" class="history"></div>
                        </el-card>
                    </Panel>
                </Collapse>
            </div>
            <div class="contrast-bottom-content">
                <el-card class="constast-card">
                    <div slot="header" class="clearfix">
                        <span>版本对比</span>
                    </div>
                    <div class="search-content">
                        <el-form :inline="true" :model="contrastForm" ref="contrastForm" label-width="100px" class="demo-form-inline">
                            <div class="form-case" >                       
                                <el-form-item  label="测试项："  >
                                    <el-cascader-panel
                                            v-model="contrastForm.case"
                                            placeholder="请选择测试项"
                                            :options="modelOptions"
                                            :props="{ multiple: true }"
                                            clearable>
                                    </el-cascader-panel>
                                </el-form-item>
                                <el-form-item label="版本：" >
                                    <el-select 
                                        v-model="contrastForm.versions" placeholder="请选择版本" multiple class="version_select">
                                        <el-option
                                            v-for="item in versionOptions"
                                            :key="item.name"
                                            :label="item.name"
                                            :value="item.value">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                                <el-form-item label="测试用例："  >
                                    <el-select v-model="contrastForm.stage" placeholder="请选择用例等级"  class="">
                                        <el-option
                                            v-for="item in caseOptions"
                                            :key="item.value"
                                            :label="item.level"
                                            :value="item.value">
                                        </el-option> 
                                    </el-select>
                                </el-form-item>
                                <el-form-item >
                                    <el-button class="contrast-btn" @click="startContrast" >开始对比</el-button>
                                </el-form-item>
                            </div>   
                        </el-form>
                    </div>
                    <el-card class="box-card case-card" v-for="(caseItem,caseIndex) in caseArr" :key="caseIndex+'case'">
                        <div slot="header" class="clearfix">
                            <span>{{caseItem.name}}</span>
                        </div>
                        <el-tabs v-if="caseItem.child.length>0" class="obj_tabs" @tab-click="handleClick"   v-model="caseItem.activeName">
                            <el-tab-pane v-for="(detailItem,detailIndex) in caseItem.child" :label="detailItem.test_item" :name="detailItem.test_item"  :key="detailItem.test_item+detailIndex">
                                <div class="suitesContent">
                                    <el-card class="box-card suite-card">
                                        <div slot="header" class="clearfix">
                                            <span>目标类型对比</span>
                                        </div>
                                        <div :id="detailItem.test_item+'d'"  class="feature_chart"></div>
                                    </el-card>
                                </div>
                                <div class="featureContent"> 
                                    <el-card class="box-card suite-card">
                                        <div slot="header" class="clearfix">
                                            <span>场景对比</span>
                                        </div>
                                        <div :id="detailItem.test_item+'f'" class="feature_chart"></div>
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
                suite_items:[]
            }
        },
        mounted(){
            this.init();
        },
        methods:{
            handleClick(){

            },
            sliceSearchOptions(item){
                var index = this.contrastForm.searchConditions.indexOf(item) 
                if (index !== -1) {
                    this.contrastForm.searchConditions.splice(index, 1)
                }
            },
            startContrast(){
                this.caseItems = [];
                this.caseArr=[];
                var flag=true;
                this.contrastForm.case.forEach((item,index)=>{
                    if(index+1 < this.contrastForm.case.length){
                        var tableData = {};
                        if(this.contrastForm.case[index][0] == this.contrastForm.case[index+1][0]){
                            if(flag){
                                tableData.name=this.contrastForm.case[index+1][0];  
                                tableData.child = [];   
                                this.contrastForm.case.forEach((child,childIndex)=>{
                                    if(child[0] == tableData.name){
                                        const childData={};
                                        if(childIndex+1==this.contrastForm.case.length){
                                            childData.test_item =  child[0]+'_'+child[1];
                                            tableData.child.push(childData); 
                                            tableData.activeName = tableData.child[0].test_item; 
                                        }else{
                                            if(childIndex+1 < this.contrastForm.case.length && this.contrastForm.case[childIndex][1] != this.contrastForm.case[childIndex+1][1]){
                                                childData.test_item =  child[0]+'_'+child[1];
                                                tableData.child.push(childData); 
                                                tableData.activeName = tableData.child[0].test_item; 
                                            }
                                        }
                                    }
                                })
                                flag =false;
                                this.caseArr.push(tableData)
                            }
                        }else{
                            tableData.name=this.contrastForm.case[index+1][0];
                            tableData.child = [];
                            this.contrastForm.case.forEach((child)=>{
                                if(child[0] == tableData.name){
                                    const childData={};
                                    childData.test_item =  child[0]+'_'+child[1];
                                    tableData.child.push(childData); 
                                    tableData.activeName =tableData.child[0].test_item; 
                                }
                            })
                            this.caseArr.push(tableData)
                        }
                        
                    }
                    this.caseItems.push(item)
                });
                // 获取对比接口 
                // 参数：program(当前程序ysg,calmcar),versions(选择版本号),stage(选择测试用例等级),items(选择测试项)
                get_constract_result({
                    program:(this.$route.params.program).toLowerCase(),
                    versions:(this.contrastForm.versions).toString(),
                    stage:this.contrastForm.stage=='all'?'0':this.contrastForm.stage,
                    items:this.caseItems})
                .then(res=>{
                    if(res.data){
                        res.data.suites.forEach(item=>{
                            // console.log(item)
                            item.data.forEach(child=>{
                                // console.log(child)
                                // this.drawSuites(child,res.data.suites);
                            })
                        })
                        res.data.features.forEach(item=>{
                            item.data.forEach(child=>{
                                this.drawFeatures(child,res.data.features);
                            })
                        })
                    }else{
                        this.$message({ 
                            type: 'error',
                            message: res.data.description
                        });
                    }
                })
            },
            drawFeatures(feature){
                // console.log(features)
                this.myChart = echarts.init(document.getElementById(feature.test_item+'f')); 
                this.optionmyChart = {
                    tooltip: {
                    trigger: 'axis',
                    axisPointer: { // 坐标轴指示器，坐标轴触发有效 
                        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    grid: {
                        left: '2%',
                        right: '4%',
                        bottom: '14%',
                        top:'16%',
                        containLabel: true
                    },
                    legend: {
                        data: ['1', '2', '3'],
                        right: 10,
                        top:12,
                        textStyle: {
                            color: "#fff"
                        },
                        itemWidth: 12,
                        itemHeight: 10,
                    },
                    xAxis: {
                        type: 'category',
                        data: ['2012','2013','2014','2015','2016','2017','2018','2019'],
                        axisLine: {
                            lineStyle: {
                            color: 'white'

                            }
                        },
                        axisLabel: {
                            textStyle: {
                            fontFamily: 'Microsoft YaHei'
                            }
                        },
                    },

                    yAxis: {
                        type: 'value',
                        max:'1200',
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: 'white'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: 'rgba(255,255,255,0.3)'
                            }
                        },
                        axisLabel: {}
                    },
                    "dataZoom": [{
                        "show": true,
                        "height": 12,
                        "xAxisIndex": [
                            0
                        ],
                        bottom:'8%',
                        "start": 10,
                        "end": 90,
                        handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
                        handleSize: '110%',
                        handleStyle:{
                            color:"#d3dee5",

                        },
                        textStyle:{
                            color:"#fff"
                        },
                        borderColor:"#90979c"
                    }, {
                        "type": "inside",
                        "show": true,
                        "height": 15,
                        "start": 1,
                        "end": 35
                    }],
                        series: [{
                            name: '1',
                            type: 'bar',
                            barWidth: '15%',
                            itemStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#fccb05'
                                    }, {
                                        offset: 1,
                                        color: '#f5804d'
                                    }]),
                                    barBorderRadius: 12,
                                },
                            },
                            data: [400, 400, 300, 300, 300, 400, 400, 400, 300]
                        },
                        {
                            name: '2',
                            type: 'bar',
                            barWidth: '15%',
                            itemStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#8bd46e'
                                    }, {
                                        offset: 1,
                                        color: '#09bcb7'
                                    }]),
                                    barBorderRadius: 11,
                                }
                                
                            },
                            data: [400, 500, 500, 500, 500, 400,400, 500, 500]
                        },
                        {
                            name: '3',
                            type: 'bar',
                            barWidth: '15%',
                            itemStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#248ff7'
                                    }, {
                                        offset: 1,
                                        color: '#6851f1'
                                    }]),
                                barBorderRadius: 11,
                                }
                            },
                            data: [400, 600, 700, 700, 1000, 400, 400, 600, 700]
                        }]
                }
                this.myChart.setOption(this.optionmyChart);
            },
            drawSuites(suite){
                // var legendSuite = [];
                // var aa=0;
                console.log(this.caseArr)
                // for(var c =0;c<this.caseArr.length;c++){
                //     if(suite.test_item==this.caseArr[c].activeName ){
                //         console.log(this.caseArr[c])
                //         // const tableData={};
                //         // tableData.name = [];
                //         // tableData.data = [];
                //         // console.log(suite)
                //         // for(var j=0;j< suite.children.length;j++){
                //         //     tableData.data.push(suite.children[j].suite)
                //         //     legendSuite.push(tableData)
                //         // }
                //     }
                // }
                // console.log(legendSuite)
                this.myChart = echarts.init(document.getElementById(suite.test_item+'d')); 
                var series=[];
                var color = ['#27A9FF','#43D64D','#FFCC00','#FF8307','#FF3E3E','#9243D6'];
                for(var i = 0;i< suite.length;i++){
                    series.push({
                        name: this.contrastForm.versions,
                        type: 'line',
                        data: ['100','200','222'],
                        itemStyle: {
                            normal: {
                                color:color[i],
                                borderWidth: 1,
                            }
                        },
                        smooth: true
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
                        data:['1','2']
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
                        data: this.contrastForm.versions,
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
                    var  a = 0;
                    res.data.forEach(item => {
                        this.versionArr.push(item.name);
                        const tableData ={};
                        tableData.name  = item.name;
                        // 版本
                        var str = item.name.substring(item.name.indexOf('-')+1,item.name.length) ;
                        tableData.value = str.substring(0,str.length-2);
                        this.versionOptions.push(tableData);
                        item.data.forEach(child=>{
                            child.children.forEach(son=>{
                                if(a==0){
                                    // nameArr
                                    this.nameArr.push (son.name == 'performance'?child.name:child.name +'_'+son.name);
                                    item = {"name":son.name == 'performance'?child.name:child.name +'_'+son.name,"data":[]}
                                    this.testArr.push(item)
                                }
                                var passPercent1 =  (son.passed/son.total).toFixed(2);
                                this.testArr[a].data.push(passPercent1);
                            })
                        })
                        a++;
                        this.historyData.push(item)
                    });
                    this.drawAllHistory( this.historyData);
                })
            },

            drawAllHistory(){
                this.myChart = echarts.init(document.getElementById('history')); 
                var series=[];
                var color = ['#27A9FF','#43D64D','#FFCC00','#FF8307','#FF3E3E','#9243D6'];
                for(var i = 0;i<this.testArr.length;i++){
                    series.push({
                        name: this.testArr[i].name,
                        type: 'line',
                        data: this.testArr[i].data,
                        itemStyle: {
                            normal: {
                                color:color[i],
                                borderWidth: 1,
                            }
                        },
                        smooth: true
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
                            left: '22%',
                            right: '0%',
                            bottom: '2%',
                            containLabel: true
                        },
                       xAxis: [{
                            type: 'category',
                            data: this.versionArr,
                            axisLine: {
                                lineStyle: {
                                    color: "#999"
                                }
                            },
                            axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
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
                


                        // series: [
                        //     {
                        //     name: this.nameArr[0],
                        //     type: 'line',
                        //     data: [23,60,20,36,23,85],
                        //     lineStyle: {
                        //         normal: {
                        //             width: 8,
                        //             color: {
                        //                 type: 'linear',

                        //                 colorStops: [{
                        //                     offset: 0,
                        //                     color: '#A9F387' // 0% 处的颜色
                        //                 }, {
                        //                     offset: 1,
                        //                     color: '#48D8BF' // 100% 处的颜色
                        //                 }],
                        //                 globalCoord: false // 缺省为 false
                        //             },
                        //             shadowColor: 'rgba(72,216,191, 0.3)',
                        //             shadowBlur: 10,
                        //             shadowOffsetY: 20
                        //         }
                        //     },
                        //     itemStyle: {
                        //         normal: {
                        //             color: '#fff',
                        //             borderWidth: 10,
                        //             /*shadowColor: 'rgba(72,216,191, 0.3)',
                        //             shadowBlur: 100,*/
                        //             borderColor: "#A9F387"
                        //         }
                        //     },
                        //     smooth: true
                        // },
                        
                        
                        // ]
                }
                this.myChart.setOption(this.optionmyChart);
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
    .feature_chart{
        width: 100%;
        height: 100%;    
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
            background-color: #29A2FF;
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
    }
    .contrast-content{
        height: 100%;
        width: 100%;
        .contrast-bottom-content{
            margin: 4vw 0 0;

        }
        .history{
            width: 100%;
            height: 16vw;
        }
    }
    .search-content{
        display: flex;
        align-items: center;
        justify-content: space-between;
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
    .form-case{
        width: 100%;
    }
    .version_select{
        min-width: 366px;
        .el-select__tags{
            max-width: auto !important;
        }
    }
    .el-cascader-menu__wrap{
        min-height: 104px;
        height: auto;
    }
    .constast-card{
        .el-card__body{
            width: 100%;
            height: 81%;
        }
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
        // .el-card__header .clearfix::before{
        //     content: '  ';
        //     width: 4px;
        //     height: 20px;
        //     background-color: #29A2FF;
        //     position: absolute;   
        // }
    }
</style>