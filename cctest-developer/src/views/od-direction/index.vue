<template>

    <div class="od-distance">
        <div class="distance-top">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                </div>
                <div class="top-panel">
                     <div id="direction-total" class="suites"></div>
                </div>
            </el-card>
        </div>
        <div class="distance-center">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <cardTitle :cardTitle="distanceTitle2"></cardTitle>
                </div>
                <div class="distance-center-panel">
                    <div id="direction-suites" class="suites"></div>
                </div>
            </el-card>
             <el-card class="box-card right-card">
                <div slot="header" class="clearfix">
                    <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                </div>
                <div class="distance-center-panel">
                    <div id="direction-features" class="suites"></div>
                </div>
            </el-card>
        </div>
        <div class="distance-bottom">
             <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <cardTitle :cardTitle="distanceTitle4"></cardTitle>
                </div>
                <div class="tab-panel">
                    <el-tabs v-model="activeName" type="card" >
                        <template v-for="(item,index) in angleData.accuracy">
                            <el-tab-pane :label="item.class_name" :name="item.class_name" :key=index>
                             <el-table :data="item.data" stripe >
                                <el-table-column label="相对速度精度统计" align="center">
                                    <el-table-column label="检查项" align="left">
                                        <template slot-scope="scope">
                                            {{scope.row.title_name+ scope.row.threshold}}
                                        </template>

                                    </el-table-column>
                                    <el-table-column label="测试用例总数" prop="total" align="center"></el-table-column>
                                    <el-table-column label="Passed" prop="passed" align="center"></el-table-column>
                                    <el-table-column label="Failed" prop="failed" align="center"></el-table-column>
                                    <el-table-column label="备注" prop="remark" align="center">
                                        <template slot-scope="scope">
                                            {{"max_err:"+ scope.row.remark.max_err}}<br>
                                            {{"case_name:"+ scope.row.remark.case_name}}
                                        </template>
                                    </el-table-column>
                                  </el-table-column>
                            </el-table>
                        </el-tab-pane>
                        </template>
                    </el-tabs>
                </div>
            </el-card>
        </div>
    </div>
</template>
<script>
    import  cardTitle  from "@/components/cardTitle"
    var echarts = require('echarts');   
    import { mapGetters } from 'vuex'

export default {
    data(){
        return{
            distanceTitle1:'Test Case',
            distanceTitle2:'Suites',
            distanceTitle3:'Features by stories',
            distanceTitle4:'OD朝向精度统计',
            activeName:'',
             carData:[
                {
                    "title":"纵向测距误差均值小于30%",
                    "total":"118",
                    "passed":"100",
                    "failed":"18",
                    "remark":"NA",
                },{
                    "title":"横向测距误差均值小于2m",
                    "total":"118",
                    "passed":"110",
                    "failed":"8",
                    "remark":"NA",
                } ,{
                    "title":"纵向测距[-1.5,1.5]范围内最大误差小于1m",
                    "total":"118",
                    "passed":"80",
                    "failed":"38",
                    "remark":"该范围内最大误差为2m",
                },{
                    "title":"纵向测距[1.5,4.5]范围内最小误差小于1m",
                    "total":"100",
                    "passed":"80",
                    "failed":"10",
                    "remark":"该范围内最大误差为2.2m",
                },  
            ]
        }
    },
    computed:  {
         ...mapGetters(
           {'angleData':'angle'} 
        )
     },
    components:{cardTitle},
    mounted(){
        this.initTotal();
        this.initSuites();
        this.initFeatures();
        this.activeName = this.angleData.accuracy[0].class_name;

    },
    methods:{
                // this.passData.filter(item=>{
                    //     if(item.test_item=='od_distance_use_kl' || item.test_item=='od_distance_no_kl'){
                    //         this.$store.commit('user/SET_DISTANCE', item);
                    //         setDistance(JSON.stringify(item));
                    //     }else if(item.test_item=='od_angle'){
                    //         this.$store.commit('user/SET_ANGLE', item);
                    //         setAngle(JSON.stringify(item));
                    //     }else if(item.test_item=='od_speed'){
                    //         this.$store.commit('user/SET_SPEED', item);
                    //         setSpeed(JSON.stringify(item));                  
                    //     }
                    // })

                    
                // this.totalData =[];
                // var item ={};
                // item.test_platform  = countjson.test_platform;
                // item.test_code_version  = countjson.test_code_version;
                // item.test_date  = countjson.test_date;
                // item.program  = countjson.program;
                // item.program_version  = countjson.program_version;
                // this.totalData.push(item);
                // this.passData = countjson.test_items;
                // this.passData.filter(item=>{
                //     if(item.test_item=='od_distance_use_kl' || item.test_item=='od_distance'){
                //         this.$store.commit('user/SET_DISTANCE', item);
                //         setDistance(JSON.stringify(item));
                //     }else if(item.test_item=='od_angle'){
                //                console.log(item);
                //         this.$store.commit('user/SET_ANGLE', item);
                //         setAngle(JSON.stringify(item));
                //     }else if(item.test_item=='od_speed'){
                //         this.$store.commit('user/SET_SPEED', item);
                //         setSpeed(JSON.stringify(item));
                //     }
                // })
        initTotal(){
            var  colorList=['#47E389', '#FFD577', '#FF6E6E'];
            this.myChart = echarts.init(document.getElementById('distance-total'));
            this.optionmyChart = {
                 title: {
                    text: '80',
                    subtext: 'test cases',
                    x: 'center',
                    y: 'center',
                    textStyle: {
                        fontSize:30,
                        fontWeight:'normal',
                        color: ['#333']
                    },
                    subtextStyle: {
                        color: '#666',
                        fontSize: 16
                    },
                },
                grid: {
                    // bottom: 150,
                    left: 0,
                    // right: '10%'
                },
                legend: {
                    show:false,
                    orient: 'vertical',
                    top: "middle",
                    right: "5%",
                    textStyle: {
                        color: '#505050',
                        fontSize: 25,

                    },
                    icon: 'roundRect'
                },
                series: [
                    // 主要展示层的
                    {
                        radius: ['25%', '51%'],
                        center: ['50%', '50%'],
                        type: 'pie',
                        itemStyle: {
                            normal: {
                                color: function(params) {
                                    return colorList[params.dataIndex]
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: true,
                                length: 15,
                                length2: 120,
                                lineStyle: {
                                    color: '#d3d3d3'
                                },
                                align: 'right'
                            },
                            color: "#000",
                            emphasis: {
                                show: true
                            }
            },
            label:{
                normal:{
//                     formatter: function(params){
//                         var str = '';
//                         switch(params.name){
//                             case 'passed':str = '{a|}\n{nameStyle|体育技能 }'+'{rate|'+params.value+'%}';break;
//                             case '':str = '{b|}\n{nameStyle|体育行为 }'+'{rate|'+params.value+'%}';break;
//                             case '体质健康':str = '{c|}\n{nameStyle|体质健康 }'+'{rate|'+params.value+'%}';break;
// ;
//                         }
//                         return str
//                     },
                    padding: [0, -110],
                    height: 165,
                    rich: {
                      
                        b: {
                            width:29,
                            height:45,
                            lineHeight: 50,
                         
                            align: 'left'
                        },
                        c: {
                            width:34,
                            height:33,
                            lineHeight: 50,
                          
                            align: 'left'
                        },
                 
                        nameStyle: {
                            fontSize: 16,
                            color: "#555",
                            align: 'left'
                        },
                        rate: {
                            fontSize: 20,
                            color: "#1ab4b8",
                            align: 'left'
                        }
                    }
                }
            },
            data: [
                {
                    value:17,
                    name:'passed',
                },
                {value:23, name:'failed'},
                {value:27, name:'broken'},
            ],
                    },
                    // 边框的设置
                    {
                        radius: ['47%', '51%'],
                        center: ['50%', '50%'],
                        type: 'pie',
                        label: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: false
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: false
                            }
                        },
                        animation: false,
                        tooltip: {
                            show: false
                        },
                        itemStyle: {
                            normal: {
                                color:'rgba(250,250,250,0.5)'
                            }
                        },
                        data: [{
                            value: 1,
                        }],
                    }
                ]
            };
            this.myChart.setOption(this.optionmyChart);
        },
      initSuites(){
                this.myChart = echarts.init(document.getElementById('direction-suites'));
                var spNum = 5,_max=100;
                var y_data = ['car_distance_test', 'bus_distance_test', 'truck_distance_test', 'person_distance_test', 'cyclist_distance_test'];
                var _data1 = [10,15,10,13,15,11];
                var _data2 = [19,5,40,33,15,51];
                var  _data3 = [21,55,10,13,35,11];
                var fomatter_fn = function(v) {
                    return (v.value / _max * 100).toFixed(0) 
                }
                var _label = {
                    normal: {
                        show: true,
                        position: 'inside',
                        formatter: fomatter_fn,
                        textStyle: {
                            color: '#fff',
                            fontSize: 16
                        }
                    }
                };
                this.optionmyChart = {
                    // legend: {
                    //     data: legendData,
                    //     textStyle: {
                    //         color: '#ccc'
                    //     }
                    // },
                    grid: {
                        containLabel: true,
                        left: 20,
                        top:0,
                        // right: 15,
                        // bottom: 30
                    },
                    tooltip: {
                        show: true,
                        backgroundColor: '#fff',
                        borderColor: '#ddd',
                        borderWidth: 1,
                        textStyle: {
                            color: '#3c3c3c',
                            fontSize: 16
                        },
                        formatter: function(p) {
                            console.log(p);
                            // var _arr = p.seriesName.split('/');
                            // idx = p.seriesIndex;//1，2，3
                            return '名称：' + p.seriesName + '<br>' + '完成：' + p.value + '<br>' + '占比：' + (p.value / _max * 100).toFixed(0) + '%';
                        },
                        extraCssText: 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.1)'
            },
            xAxis: {
                splitNumber: spNum,
                interval: _max / spNum,
                max: _max,
                axisLabel: {
                    show: false,
                    formatter: function(v) {
                        var _v = (v / _max * 100).toFixed(0);
                        return _v == 0 ? _v : _v + '%';
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }

            },
            yAxis: [{
                data: y_data,
                axisLabel: {
                    fontSize: 16,
                    color: '#646464'

                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            }, {
                show: false,
                data: y_data,
                axisLine: {
                    show: false
                }
            }],
            series: [{
                type: 'bar',
                name: 'passed',
                stack: '2',
                label: _label,
                legendHoverLink: false,
                barWidth: 27,
                itemStyle: {
                    normal: {
                        color: '#47E389'
                    },
                    emphasis: {
                        color: '#47E389'
                    }
                },
                data: _data1
            }, {
                type: 'bar',
                name: 'failed',
                stack: '2',
                legendHoverLink: false,
                barWidth: 27,
                label: _label,
                itemStyle: {
                    normal: {
                        color: '#FF6E6E'
                    },
                    emphasis: {
                        color: '#FF6E6E'
                    }
                },
                data: _data2
            }, {
                type: 'bar',
                stack: '2',
                name: 'broken',
                legendHoverLink: false,
                barWidth: 27,
                label: _label,
                itemStyle: {
                    normal: {
                        color: '#FFD577'
                    },
                    emphasis: {
                        color: '#FFD577'
                    }
                },
                data: _data3
            }]
                };
                this.myChart.setOption(this.optionmyChart);
        },
        initFeatures(){
                this.myChart = echarts.init(document.getElementById('direction-features'));
                var spNum = 5,_max=100;
                var y_data = ['car_distance_test', 'bus_distance_test', 'truck_distance_test', 'person_distance_test', 'cyclist_distance_test'];
                var _data1 = [10,15,10,13,15,11];
                var _data2 = [19,5,40,33,15,51];
                var  _data3 = [21,55,10,13,35,11];
                var fomatter_fn = function(v) {
                    return (v.value / _max * 100).toFixed(0) 
                }
                var _label = {
                    normal: {
                        show: true,
                        position: 'inside',
                        formatter: fomatter_fn,
                        textStyle: {
                            color: '#fff',
                            fontSize: 16
                        }
                    }
                };
                this.optionmyChart = {
                    // legend: {
                    //     data: legendData,
                    //     textStyle: {
                    //         color: '#ccc'
                    //     }
                    // },
                    grid: {
                        containLabel: true,
                        left: 20,
                        top:0,
                        // right: 15,
                        // bottom: 30
                    },
                    tooltip: {
                        show: true,
                        backgroundColor: '#fff',
                        borderColor: '#ddd',
                        borderWidth: 1,
                        textStyle: {
                            color: '#3c3c3c',
                            fontSize: 16
                        },
                        formatter: function(p) {
                            console.log(p);
                            // var _arr = p.seriesName.split('/');
                            // idx = p.seriesIndex;//1，2，3
                            return '名称：' + p.seriesName + '<br>' + '完成：' + p.value + '<br>' + '占比：' + (p.value / _max * 100).toFixed(0) + '%';
                        },
                        extraCssText: 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.1)'
            },
            xAxis: {
                splitNumber: spNum,
                interval: _max / spNum,
                max: _max,
                axisLabel: {
                    show: false,
                    formatter: function(v) {
                        var _v = (v / _max * 100).toFixed(0);
                        return _v == 0 ? _v : _v + '%';
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }

            },
            yAxis: [{
                data: y_data,
                axisLabel: {
                    fontSize: 16,
                    color: '#646464'

                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            }, {
                show: false,
                data: y_data,
                axisLine: {
                    show: false
                }
            }],
                series: [{
                type: 'bar',
                name: 'passed',
                stack: '2',
                label: _label,
                legendHoverLink: false,
                barWidth: 27,
                itemStyle: {
                    normal: {
                        color: '#47E389'
                    },
                    emphasis: {
                        color: '#47E389'
                    }
                },
                data: _data1
            }, {
                type: 'bar',
                name: 'failed',
                stack: '2',
                legendHoverLink: false,
                barWidth: 27,
                label: _label,
                itemStyle: {
                    normal: {
                        color: '#FF6E6E'
                    },
                    emphasis: {
                        color: '#FF6E6E'
                    }
                },
                data: _data2
            }, {
                type: 'bar',
                stack: '2',
                name: 'broken',
                legendHoverLink: false,
                barWidth: 27,
                label: _label,
                itemStyle: {
                    normal: {
                        color: '#FFD577'
                    },
                    emphasis: {
                        color: '#FFD577'
                    }
                },
                data: _data3
            }]
                };
                this.myChart.setOption(this.optionmyChart);
        }
    },

}
</script>
<style lang="less">
@import "../../assets/styles/dash.less";





</style>