<template>
    <div class="dash-wrapper"  >
        <div class="dash-btn-right">
             <div class="btn-right">
                 <el-button class="view-btn" icon="el-icon-picture"  @click="ExportSavePdf(photoTitle,'jpg')">导出图片</el-button>
                <el-button class="export-btn" icon="el-icon-document" @click="ExportSavePdf(htmlTitle,nowTime)">导出pdf</el-button>
            </div>
        </div>
    <div  class="dash-test-wrapper" id="pdfCentent">
      <div class="dash-first" id="head-top1">
            <div class="head-title-card" id="head-card1">
                <div class="left"> 
                    <p class="head-htitle"> {{firstTitle}}</p>
                </div>
            </div>
            <div class="total-panel">
                <div class="total-top">
                    <el-card class="box-card first-card" shadow="hover">
                    <el-table :data="totalData" >
                            <el-table-column prop="program" label="程序"  min-width="80" align="center"></el-table-column>
                            <el-table-column prop="version" label="版本号" min-width="150" align="center"></el-table-column>
                            <el-table-column prop="test_platform" label="测试平台" min-width="100" align="center" ></el-table-column>
                            <el-table-column prop="test_start_time" label="开始时间" align="center" min-width="100"></el-table-column>
                            <el-table-column prop="test_end_time" label="结束时间" align="center" min-width="100"> </el-table-column>
                            <el-table-column prop="test_duration" label="时长" align="center" min-width="100"> </el-table-column>
                        </el-table>
                    </el-card>
                </div>
                 <div class="total-center">
                    <el-card class="box-card center-card" shadow="hover">
                        <div slot="header" class="clearfix">
                            <cardTitle :cardTitle="totalTitle1"></cardTitle>
                        </div>
                        <div class="center-pass-table">
                            <el-table :data="testCaseData" class="pass-table" :span-method="objectSpanMethod">
                                <el-table-column  label="功能" align="left" class-name="type" min-width="100">
                                    <template slot-scope="scope">
                                        {{scope.row.name}}
                                        <!-- <span v-if="scope.row.test_item == 'od_distance_use_kl'||scope.row.test_item == 'od_distance_no_kl'"> </span>
                                        <span v-else-if="scope.row.test_item == 'od_angle'">{{'OD朝向'}} </span>
                                        <span v-else-if="scope.row.test_item == 'od_speed_use_kl'">{{'OD相对速度'}} </span> -->
                                    </template>
                                </el-table-column>
                                <el-table-column  label="测试项" align="left" class-name="type" min-width="150" >
                                    <template slot-scope="scope" >
                                        {{scope.row.child_item}}
                                    </template>
                                </el-table-column>
                                <el-table-column prop="passed" label="passed" align="center" class-name="pass"></el-table-column>
                                <el-table-column prop="failed" label="failed" align="center" class-name="fail"></el-table-column>
                                <el-table-column prop="broken" label="broken" align="center" class-name="broken"></el-table-column>
                            </el-table>
                        </div>
                    </el-card>
                    <el-card class="box-card center-card pass-e" shadow="hover">
                        <div slot="header" class="clearfix">
                            <cardTitle :cardTitle="totalTitle2"></cardTitle>
                        </div>
                        <div class="center-pass-table " id="pass-right">
                            <div id="passEcharts" class="passEcharts"></div>
                        </div>
                    </el-card>
                </div>
            </div>
        </div>     
        <template v-for="(item,index) in caseData" >
             <div :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"   :key="index+'pass'" id="test_item">
                    <!-- <headTitle  :title="item.test_item"></headTitle> -->
                    <el-card    :id="item.test_item" class="test_item">
                        <div slot="header" class="clearfix">
                            <h3 class="child_header">{{item.test_item}}</h3>
                        </div>
                      <div class="od-distance">
                        <div class="method_panel">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="test_title"></cardTitle>
                                </div>
                                <div class="top-panel">
                                    <ul v-if="item.test_item.indexOf('distance')!=-1" class="method_ul">
                                        <li >
                                            {{distance.Intro}}
                                        </li>
                                        <li>
                                            {{distance.title}}
                                            <div class="error_panel">
                                                <p>纵向相对误差：</p>
                                                <img src="../assets/images/dis_1.png">
                                            </div>
                                            <div class="error_panel">
                                                <p> 纵向相对误差：</p>
                                                <img src="../assets/images/dis_2.png">
                                            </div>
                                        </li>
                                        
                                    </ul>
                                    <ul v-if="item.test_item.indexOf('angle')!=-1" class="method_ul">
                                        <li >
                                            {{angle.Intro}}
                                        </li>
                                        <li>
                                            {{angle.title}}
                                            <div class="error_panel">

                                            <img src="../assets/images/angle_1.png" class="angle_img">
                                                </div>
                                        </li>
                                    </ul> 
                                    <ul v-if="item.test_item.indexOf('relative')!=-1" class="method_ul">
                                            <li >
                                            {{relative_velocity.Intro}}
                                        </li>
                                        <li>
                                            {{relative_velocity.title}}
                                                <div class="error_panel">
                                                <p>纵向误差：</p>
                                                <img src="../assets/images/re_1.png" class="rel_img">
                                            </div>
                                            <div class="error_panel">
                                                <p> 纵向误差：</p>
                                                <img src="../assets/images/re_2.png" class="rel_img">
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-top">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                </div>
                                <div class="top-panel">
                                    <div :id="'_d'+index" class="suites"></div>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-center">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle2"></cardTitle>
                                </div>
                                <div class="distance-center-panel">
                                    <div :id="'_s'+index" class="suites"></div>
                                </div>
                            </el-card>
                            <el-card class="box-card right-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                </div>
                                <div class="distance-center-panel">
                                    <div :id="'_f'+index" class="suites"></div>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-bottom" v-if="item.accuracy.length!=0">
                            <el-card class="box-card" shadow="hover">
                                <div class="tab-panel">
                                    <!-- <el-tabs type="card" > -->
                                        
                                        <template v-for="(accuracyItem,accuracyIndex) in item.accuracy">
                                            <!-- <el-tab-pane :label="accuracyItem.class_name" :key="accuracyIndex"> -->
                                            <div class="accuracy_div"  :key="accuracyIndex">
                                            <el-table :data="accuracyItem.data" stripe class="accTable" id="accTable">
                                                <el-table-column :label="accuracyItem.class_name==null||accuracyItem.class_name==undefined?'':accuracyItem.class_name" align="center">
                                                    <el-table-column label="检查项" align="left" min-width="265">
                                                        <template slot-scope="scope">
                                                            {{scope.row.title_name}}
                                                        </template>
                                                    </el-table-column>
                                                    <el-table-column label="测试用例总数" prop="total" align="center"></el-table-column>
                                                    <el-table-column label="Passed" prop="passed" align="center"></el-table-column>
                                                    <el-table-column label="Failed" prop="failed" align="center"></el-table-column>
                                                             <el-table-column label="max_err" prop="max_err" align="center" min-width="80">
                                                                <template slot-scope="scope">
                                                                        <template v-if="scope.row.max_err==0">
                                                                            {{'NA'}}
                                                                        </template> 
                                                                        <template v-else>
                                                                            <template v-if="scope.row.max_err==undefined||scope.row.max_err==null"> 
                                                                                  {{scope.row.max_err}}
                                                                                </template>
                                                                                <template v-else>
                                                                                    {{(scope.row.max_err).toFixed(2)}}
                                                                                </template>
                                                                        </template>
                                                                    </template>
                                                             </el-table-column>
                                                        <el-table-column label="case_name" align="center" min-width="140">
                                                            <template slot-scope="scope">
                                                                <template v-if="scope.row.max_err==0">
                                                                    {{'NA'}}
                                                                </template> 
                                                                <template v-else>
                                                                       <el-button class="showcasebtn" @click="showCase(scope.row)">{{ scope.row.case_name}} </el-button> 
                                                                </template>
                                                            </template>
                                                        </el-table-column>
                                                </el-table-column>
                                            </el-table>
                                            <div class="accuracy-center" v-if=" item.test_item.indexOf('distance') !=-1 " :key="accuracyIndex">
                                                <el-card class="box-card accuracy-card" shadow="hover">
                                                    <div slot="header" class="clearfix">
                                                        <cardTitle :cardTitle="broad"></cardTitle>
                                                    </div>
                                                    <div class="accuracy-pass-table" style="position:relative">
                                                        <div :id="'accuracy-broad'+accuracyIndex+item.test_item" class="passEcharts"></div>
                                                        <img src="../assets/images/car.png" style="height:60px;position:absolute;bottom:-20px;left:46%;transform:rotate(180deg);" >
                                                    </div>
                                                </el-card>
                                                <el-card class="box-card accuracy-card" shadow="hover">
                                                    <div slot="header" class="clearfix">
                                                        <cardTitle :cardTitle="vertical"></cardTitle>
                                                    </div>
                                                    <div class="accuracy-pass-table" style="position:relative">
                                                        <div :id="'accuracy-vertical'+accuracyIndex+item.test_item"  class="passEcharts"></div>
                                                        <img src="../assets/images/car.png" style="height:60px;position:absolute;left:20px;top:30%;transform:rotate(-90deg);" >
                                                    </div>
                                                </el-card>
                                            </div>

                                              </div>
                                            <!-- </el-tab-pane> -->
                                        </template>
                                    <!-- </el-tabs> -->
                                </div>
                            </el-card>
                        </div>
                    </div>
                </el-card>
            </div>  
        </template>  
        </div>   
    </div>
</template>

<script>
    import {setTestData} from '@/utils/auth'
    import { mapGetters } from 'vuex'
    import { getInfo,getItems  } from "@/api/user";
    // import  headTitle  from "@/components/headTitle" 
    import  cardTitle  from "@/components/cardTitle"

    // import odDirection from "@/views/od-direction/index";
    // import odDistance from "@/views/od-distance/index";
    // import odSpeed from "@/views/od-speed/index";
    var echarts = require('echarts');
    
    export default {
        name: "dashBoard",
        data(){
            return{
                distance:{
                    Intro:'测试使用rtk作为真值，通过本车以及目标高精度GPS定位数据，转换成本车坐标系下的测距结果。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其测距误差',
                    title:'测试指标:',
                },
                angle:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据可获得目标相对本车运动朝向数据，作为本测试项真值，通过时间戳将真值与相机检测数据进行匹配。对比量化目标朝向检测检测效果。',
                    title:'测试指标:',
                },
                relative_velocity:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据,转换成本车坐标系下的测距结果。根据距离随时间变化计算基于本车坐标系下的横纵向相对速度作为真值。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其相对速度误差。',
                    title:'测试指标:',
                },
                test_title:"测试方法",
                activeName:null,
                labelPosition:'top',
                totalData:[],
                testCaseData:[],
                passData:[],
                firstTitle:'概况',
                secondTitle:'OD测距',
                thirdTitle:'OD朝向',
                forthTitle:'OD相对速度',
                totalTitle1:'测试用例通过率总览',
                totalTitle2:'通过率总览',
                totalTitle3:'版本通过率对比',  
                accuracyData:null,
                distanceTitle1:'测试用例',
                distanceTitle2:'测试车型分组',
                distanceTitle3:'特性场景分组',
                distanceTitle4:'精度统计',
                addData:'1',
                broad:'横向测距',
                vertical:'纵向测距',
                program:null,
                program_version:null,
                caseData:[],
                htmlTitle:'PDF',
                nowTime:'',
                photoTitle:'jpg',
                position:null,
                spanArr:[],
                endflag:false,
                testChartData:[]
            }
        },
        components: {cardTitle},
        mounted(){
            this.initData();   
            this.initTitle();
        },
        methods:{
            initData(){
                getInfo({program:this.$route.query.program,version:this.$route.query.version})
                .then(res=>{
                    this.caseData =[];
                    res.data.test_items.forEach(item=>{
                        if(item.test_item!='performance'){
                            this.caseData.push(item)
                        }
                    })
                    this.passData = res.data.test_items; 
                    this.$store.commit('user/SET_TESTDATA', res.data);                            
                    setTestData(JSON.stringify(res.data));
                    this.totalData =[];
                    var item = {};
                    item.test_platform  = res.data.test_platform;
                    item.test_code_version  = res.data.test_code_version;
                    item.test_start_time  =this.transformTime.transformDate(res.data.test_start_time);
                    item.test_end_time  = this.transformTime.transformDate(res.data.test_end_time);
                    item.test_duration =  this.transformTime.transformSecond(res.data.test_duration);
                    item.program  = res.data.program;
                    this.program  = res.data.program;
                    item.version  = res.data.version;
                    this.program_version =  res.data.version;
                    this.htmlTitle = res.data.program +'_'+ res.data.version;
                    this.photoTitle = res.data.program+'_'+res.data.version;
                    this.totalData.push(item);
                })
            },
            initTitle(){
                getItems({program:this.$route.query.program,version:this.$route.query.version})
                    .then(res=>{
                        res.data.forEach(item => {
                        item.children.forEach(child=>{
                            const tableData={};
                            tableData.name = item.name;
                            tableData.broken= child.broken;
                            tableData.failed= child.failed;
                            tableData.passed= child.passed;
                            tableData.total= child.total;
                            tableData.child_item= child.name;
                            this.testCaseData.push(tableData)
                            const chartData={};
                            if(item.name=='performance'){
                                chartData.test_item = child.name;
                            }else{
                                chartData.test_item = item.name+'_'+ child.name;
                            }
                            chartData.broken= child.broken;
                            chartData.failed= child.failed;
                            chartData.passed= child.passed;
                            chartData.total= child.total;
                            this.testChartData.push(chartData)
                            this.rowspan()                    
                            this.initChart()
                        })
                    })
                })
            },
            rowspan() {
                this.spanArr = [];
                this.position = 0; 
                this.testCaseData.forEach((item,index) => {
                if( index === 0){
                    this.spanArr.push(1);
                    this.position = 0;
                }else{
                    if(this.testCaseData[index].name === this.testCaseData[index-1].name ){
                    this.spanArr[this.position] += 1;//连续有几行项目名名称相同
                    this.spanArr.push(0); // 名称相同后往数组里面加一项0
                    }else{
                    this.spanArr.push(1);
                    this.position = index;
                    }
                }
                })
            },
            objectSpanMethod({ rowIndex, columnIndex }) {  //表格合并行
                if(columnIndex === 0){  //序号列也进行合并(第一列)
                //this.spanArr这个数组里面存的是table里面连续的有几条数据相同
                //例如:[1,1,2,0,2,0]
                //1  代表的没有连续的相同的
                //2  代表连续的两个相同
                //0  代表是和上一条内容相同
                const _row = this.spanArr[rowIndex];
                const _col = _row>0 ? 1 : 0;
                return {
                    rowspan: _row, //行
                    colspan: _col  //列
                }

                }
            },
          initLeftCuracy(item,accuracy_item,index){
                var passed = [];
                var name =[];
                // var test=[];
                var accuracy_data = accuracy_item.data;
                for(var j =0;j < accuracy_data.length;j++){
                    if(accuracy_data[j].title_name.indexOf('横向测距') !=-1&&(accuracy_data[j].title_name.indexOf('范围内') !=-1)){
                        passed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                        // test.push(accuracy_data[j])
                        name.push(accuracy_data[j].range)
                    }
                }
                // if(test.length == 1){
                //      var range = ((test[0].range).substr(1)).substr(0,(test[0].range).substr(1).length-1);

                //     range.split(',')
                //     console.log(range)
                // }else{
                    // for(var k=0;k<test.length;k++){
                    //  var r2 = ((test[k].range).substr(1)).substr(0,(test[k].range).substr(1).length-1);
                    //     name.push(r2.substring(r2.indexOf(','),r2))
                    //     if(k== test.length-1){
                    //          name.push(r2.substring(r2.indexOf(',')+1,r2.length))
                    //     }
                    // }
                    // console.log(name)
                // }
                this.myChart = echarts.init(document.getElementById('accuracy-broad'+index+item.test_item)); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                        grid: {
                            top:'3%',
                            left: '4%',
                            right: '4%',
                            bottom: '12%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: name,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                    // align: 'right',

                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }, 
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {

                                    textStyle: {
                                    },
                                    color:'#333',

                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                "barMaxWidth": '42%',
                                 barGap:'-100%',
                                    "itemStyle": {
                                        "normal": {

                                            'borderColor':'#B2E4FA',
                                            "color": "#DEF5FF",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#333",                                
                                                    "fontSize":"80%",

                                                },
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                             
                        ]
                };
                this.myChart.setOption(this.optionmyChart);
            },
            initRightCuracy(item,accuracy_item,index){
            var passed = [];
            var name =[]; 
                var accuracy_data = accuracy_item.data;
                for(var j =0;j < accuracy_data.length;j++){
                    if(accuracy_data[j].title_name.indexOf('纵向测距') !=-1&&(accuracy_data[j].title_name.indexOf('阈值') !=-1)){
                        passed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                        // var range = ((accuracy_data[j].range).substr(1)).substr(0,(accuracy_data[j].range).substr(1).length-1);
                            name.push(accuracy_data[j].range)
                        // name.push(range.substring(range.indexOf(','),range))
                        // if(range.indexOf('+oo') != -1){
                        //     name.push('+oo')
                        // }
                    }
                }
                
                this.myChart = echarts.init(document.getElementById('accuracy-vertical'+index+item.test_item)); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                    //    legend: {
                    //         // y: '4%',
                    //         top: '0%',
                    //         right:'0%',
                    //         itemWidth: 12,
                    //         itemHeight: 12,
                    //         textStyle: {
                    //             color: '#505050',
                    //                 fontSize:14,
                    //                 "padding": [3, 6],

                    //         },
                    //         // padding:[0,10],
                    //         data: [ 'passed', 'failed', 'broken', ]
                    //     },
                        grid: {
                            top:'3%',
                            left: '12%',
                            right: '2%',
                            bottom: '0%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: name,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                        // offset:[0,30],
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }, 
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    },
                                    color:'#333',

                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                "barMaxWidth": '42%',
                                    "itemStyle": {
                                        "normal": {

                                            'borderColor':'#B2E4FA',
                                            "color": "#DEF5FF",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#333",                                
                                                    "fontSize":"80%",
                                                    // "fontWeight":'bold',

                                                },
                                                // "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                             
                        ]
                };
                this.myChart.setOption(this.optionmyChart);

            },
            initChart(){
                var yName =[];
                var passed = [];
                var failed =[];
                var broken = [];
                var total;
                for(var i =0;i< this.testChartData.length;i++){
                    yName.push( this.testChartData[i].test_item);
                    total =  this.testChartData[i].passed+ this.testChartData[i].failed+ this.testChartData[i].broken;
                    passed.push(( this.testChartData[i].passed/total).toFixed(2));
                    failed.push(( this.testChartData[i].failed/total).toFixed(2)) ;                   
                    broken.push(( this.testChartData[i].broken/total).toFixed(2));
                }
                this.myChart = echarts.init(document.getElementById('passEcharts')); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                       legend: {
                            top: '0%',
                            right:'3.5%',
                            itemWidth: 12,
                            itemHeight: 12,
                            textStyle: {
                                color: '#505050',
                                    fontSize:14,
                                    "padding": [3, 6],

                            },
                            data: [ 'passed', 'failed', 'broken', ]
                        },
                        grid: {
                            left: '4%',
                            right: '4%',
                            bottom: '1%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: yName,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    },
                                     interval:0,//横轴信息全部显示  
                                    rotate:30,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }
                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                    "itemStyle": {
                                        "normal": {
                                            "color": "#47E389",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#fff",                                
                                                    "fontSize":"80%",
                                                    "fontWeight":'bold',

                                                },
                                                // "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                              {
                                name:"failed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                "itemStyle": {
                                "normal": {
                                    "color": "#FF6E6E",
                                    "label": {
                                        "show": true,
                                        "textStyle": {
                                            "color": "#fff",
                                                    "fontSize":"80%",
                                            "fontWeight":'bold',
                                        },

                                        "position": "inside",
                                        formatter: function(p) {
                                            return p.value > 0 ? (p.value) : '';
                                        }
                                    }
                                }
                            },
                                data: failed
                            }, {
                                name: "broken",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                    "itemStyle": {
                                        "normal": {
                                            "color": "#FFD577",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#fff",
                                                    "fontSize":"80%",
                                                    "fontWeight":'bold',

                                                },
                                                "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: broken
                            },
                        ]
                };
                this.myChart.setOption(this.optionmyChart);
            },

            initCaseChart(item,index){
                this.myChart = echarts.init(document.getElementById("_d"+index)); 
                this.optionmyChart = {
                    title: {
                        text: item.total,
                        subtext: 'test cases',
                        x: 'center',
                        y: 'center',
                        textStyle: {
                            fontSize:40,
                            fontWeight:'bold',
                            color: ['#505050'],
                            align: 'center',

                        },
                        subtextStyle: {
                            color: '#505050',
                            // fontSize: 22
                        },
                    },
                    // grid: {
                    //     top: '40%',
                    //     left: '50%',
                    //     right: '10%'
                    // },
                    legend: {
                        orient: 'vertical',
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                             "padding": [0, 0],

                            fontSize:14
                        },
                            // padding:[0,10],
                    },
                    series: [
                        {
                            name: '',
                            type: 'pie',
                            radius: ['48%', '58%'],
                            color: ["#47E389", "#FF6E6E", "#FFD577"],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {
                                        "formatter": "{per|{c}\n} {b|{b}} ",
                                        "borderColor": "transparent",
                                        "borderRadius": 4,
                                        "rich": {
                                            "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                            },
                                            "hr": {
                                                "borderColor": "#aaa",
                                                "width": "100%",
                                                "borderWidth": 1,
                                                "height": 0
                                            },
                                            "b": {
                                                "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                                
                                            },
                                            "c": {
                                                "fontSize": 14,
                                                "color": "#b3e5ff"
                                            },
                                            "per": {
                                                "color": "#505050",
                                                "fontSize": 22,
                                                "padding": [3, 2],
                                                "fontWeight":'bold',
                                                "borderRadius": 2
                                            }
                                        },
                                        "textStyle": {
                                            "color": "#fff",
                                            "fontSize": 16
                                        }
                                    },
                                },
                                emphasis: {
                                    "label": {
                                    "show": true,
                                    "formatter": "{per|{c}\n} {b|{b}}",
                                    "backgroundColor": "rgba(255, 147, 38, 0)",
                                    "borderColor": "transparent",
                                    "borderRadius": 4,
                                    "rich": {
                                          "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                        },
                                        "hr": {
                                            "borderColor": "#aaa",
                                            "width": "100%",
                                            "borderWidth": 1,
                                            "height": 0
                                        },
                                        "b": {
                                            "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                            
                                        },
                                        "c": {
                                            "fontSize": 14,
                                            "color": "#b3e5ff"
                                            },
                                        "per": {
                                            "color": "#505050",
                                            "fontSize": 22,
                                            "fontWeight":'bold',
                                            "padding": [3, 2],
                                            "borderRadius": 2
                                        }
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    length: 28,
                                    length2: 36

                                }
                            },
                            data: [
                                {value:item.passed, name: 'passed'},
                                {value:item.failed, name: 'failed'},
                                {value:item.broken, name: 'broken'},
                           
                            ]
                        }
                    ]};
                    this.myChart.setOption(this.optionmyChart);
                },
            initSuiteChart(item,index){
                var suite = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<item.suites.length;i++){
                    suite.push(item.suites[i].suite);
                    passed.push(item.suites[i].passed);
                    failed.push(item.suites[i].failed);
                    broken.push(item.suites[i].broken);
                }
                this.myChart = echarts.init(document.getElementById('_s'+index)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                            fontSize:14,
                         "padding": [3, 6],

                        },
                    },
                    grid: {
                        left: '3%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {

                        // type: 'value',
                        axisLabel: {
                            show: false,

                            },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },
                        splitLine: {
                            show: false
                        },
                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        splitLine: {
                            show: false
                        },
                        type: 'category',
                        data: suite,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 45,
                            textStyle: {
                                // fontSize: '16'
                            }
                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                               "color": "#47E389",
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                    "fontWeight":'bold',


                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FF6E6E',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                                    "fontSize":"85%",
                                    "fontWeight":'bold',

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FFD577',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                                    "fontSize":"85%",
                                    "fontWeight":'bold',

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                     
                     
                    ]
                };
                this.myChart.setOption(this.optionmyChart);
                // this.$nextTick(() => {
                //     this.$refs.test;
                // })
            },
            initFeatureChart(item,index){
                var feature = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<item.features.length;i++){
                    feature.push(item.features[i].feature);
                    passed.push(item.features[i].passed);
                    failed.push(item.features[i].failed);
                    broken.push(item.features[i].broken);
                }
                this.myChart = echarts.init(document.getElementById('_f'+index)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                                                     "padding": [3, 6],
                            fontSize:14,

                            // fontSize:16
                        },
                    },
                    grid: {
                        left: '4%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        // type: 'value',
                        axisLabel: {
                            show: false,

                            },
                        splitLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },

                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        splitLine: {
                            show: false
                        },
                          axisTick:{
                            show:false
                        },
                        type: 'category',
                        data: feature,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 40,
                            // textStyle: {
                            //     fontSize: '16',
                            // },
                            interval:0,//横轴信息全部显示  

                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            "color": "#47E389",
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FF6E6E',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FFD577',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                     "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                     
                     
                    ]
                };
                this.myChart.setOption(this.optionmyChart);
            }
        },
        updated(){
                for(var i=0;i< this.caseData.length;i++){    
                    this.initCaseChart(this.caseData[i],i);
                    this.initSuiteChart(this.caseData[i],i);
                    this.initFeatureChart(this.caseData[i],i);
                    if( this.caseData[i].test_item.indexOf('distance')!=-1){
                        var accuracy = this.caseData[i].accuracy
                        for(var k=0;k < accuracy.length; k++){
                            this.initLeftCuracy(this.caseData[i],accuracy[k],k);
                            this.initRightCuracy(this.caseData[i],accuracy[k],k);
                        }
                    }
                }            
        },
        computed:  {
            ...mapGetters(
                {testData:'testData'}
   
            )
        }
    }
</script>

<style lang="less">
@import "../assets/styles/dash.less";
</style>
