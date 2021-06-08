<template>
    <div class="dash-index-wrapper" >
        <!-- <div class="dash-index-right"> -->
            <div class="index-bottom">
                <div class="dash-index-top">
                    <h3>硬件测试信息</h3>
                    <div class="index-top-right">
<!--                        <el-select v-model="selectProgram" class="select-program"   placeholder="请选择查询结果" clearable >-->
<!--                            <el-option v-for="(item,index) in programList" :key="index+'program'" :label="item.name" :value="item.value"></el-option>-->
<!--                        </el-select>-->
<!--                        <el-select v-model="selectStage" class="select-program"   placeholder="请选择PDAQ系列" clearable >-->
<!--                            <el-option v-for="(item,index) in stageList" :key="index+'program'" :label="item.name" :value="item.value"></el-option>-->
<!--                        </el-select>-->
                        <el-input v-model="IP_address" class="select-program"   placeholder="请输入IP地址" clearable >
                          <el-option name="input" autofocus="true"></el-option>
                        </el-input>
                        <Button   class="search-btn"  @click="searchProgram">搜索</Button>
                    </div>
                </div>
                <el-table
                 class="index_table"
                    :data="testRecords.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                    style="width: 100%"
                    stripe>
                    <el-table-column prop="IP_address" label="IP地址" align="center"></el-table-column>
                    <el-table-column prop="PCB版本" label="PCB版本" align="center" min-width="140"></el-table-column>
                    <el-table-column prop="ICCID"  label="ICCID" align="center"></el-table-column>
                    <el-table-column prop="添加时间" label="测试时间" align="center" sortable  min-width="140"></el-table-column>
                    <el-table-column prop="Activation_time" label="激活时间" align="center" sortable  min-width="140"> </el-table-column>
<!--                    <el-table-column prop="test_duration" label="时长" align="center" > </el-table-column>-->
                    <el-table-column prop="test_result" label="测试结果" align="center"></el-table-column>
                    <el-table-column label="操作" align="center"> 
                        <template slot-scope="scope">
                            <el-button @click="showDetail(scope.row)"  class="detail-btn">查看</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <div class="pagination index_page">
                    <el-pagination
                        @size-change="sizeChange"
                        @current-change="currentChange"
                        :current-page="currentPage"
                        :page-sizes="[10, 20, 30, 40]"
                        :page-size="pagesize"
                        layout="total, sizes, prev, pager, next, jumper"
                        :total="testRecords.length">
                    </el-pagination>
                </div>
            <!-- </div> -->
        </div>
    </div>
</template>


<script>
    import { getRecords ,search_pdaq } from "@/api/user";
    export default {
        data(){
            return{
                stageList:[
                     {
                        name:"all",
                        value:"0"
                    },
                    {
                        name:"PDAQ-5",
                        value:"5",
                    },
                    {
                        name:"TDA4",
                        value:"1"
                    },
                  {
                    name:"PDAQ-6",
                    value: "6"
                  }

                ],
                programList:[
                    {
                        name:"合格",
                        value:"合格"
                    },
                    {
                        name:"不合格",
                        value:"不合格"
                    }
                ],
                pagesize:10,
                currentPage: 1,
                selectProgram:null,
                selectStage:null,
                selectProgram_version:null,
                testRecords:[],
                IP_address : null,
                ICCID :null,
            }
        },
        mounted(){
            this.init();
        },
        methods:{
          
            searchProgram(){
              // let _search = this.IP_address.toLowerCase();
                this.currentPage = 1;
                // searchRecords({test_result:this.selectProgram,PCB版本:this.selectStage})
                //     .then(res=>{
                //     this.testRecords = [];
                //     res.data.forEach(item => {
                //         const testData = {};
                //         testData.IP_address = item.IP_address;
                //         testData.PCB版本 = item.PCB版本;
                //         testData.ICCID = item.ICCID;
                //         // testData.test_duration = this.transformTime.transformSecond(item.test_duration);
                //         testData.添加时间 = item.添加时间;
                //         testData.Activation_time = item.Activation_time;
                //         testData.test_result = item.test_result;
                //         testData.test_program_version = item.test_program_version;
                //         if(item.stage ==='0'){
                //             testData.stage = 'all';
                //         }else{
                //             testData.stage =  item.stage;
                //         }
                //         this.testRecords.push(testData);
                //     });
                // });
                search_pdaq({IP_address:this.IP_address})
                .then(res => {
                  this.testRecords = [];
                  // this.IP_address = null;
                  res.data.filter(item => {//增加多项搜索功能
                    const DATA = {};
                    DATA.IP_address = item.IP_address;
                    DATA.PCB版本 = item.PCB版本;
                    DATA.ICCID = item.ICCID;
                    // testData.test_duration = this.transformTime.transformSecond(item.test_duration);
                    DATA.添加时间 = item.添加时间;
                    DATA.Activation_time = item.Activation_time;
                    DATA.test_result = item.test_result;
                    DATA.test_program_version = item.test_program_version;
                    // console.log(DATA);
                    if(item.stage ==='0'){
                        DATA.stage = 'all';
                    }else{
                        DATA.stage =  item.stage;
                    }
                    this.testRecords.push(DATA);
                  });
                });
            },
            init(){
                getRecords()
                .then(res=>{
                    this.testRecords = [];
                    res.data.forEach(item => {
                        const testData = {};
                        testData.IP_address = item.IP_address; //此处已更改  原始数据为programe
                        // console.log(item)
                        testData.PCB版本 = item.PCB版本;
                        // testData.test_duration = this.transformTime.transformSecond(item.test_duration);
                        testData.添加时间 = item.添加时间;
                        testData.Activation_time = item.Activation_time;
                        testData.ICCID = item.ICCID;
                        testData.test_result = item.test_result;
                        if(item.stage ==='0'){
                            testData.stage = 'all';
                        }else{
                            testData.stage =  item.stage;
                        }
                        this.testRecords.push(testData);
                        // console.log(item)
                    });
                })
            },
            sizeChange(val){
                this.pagesize =val;
                this.init()
            },
            currentChange(val){
                this.currentPage = val;
                this.init()
            },
            showDetail(row){
                const {href} = this.$router.resolve({
                    name: 'dashboard',
                    params: {"program":row.program,"version":row.version,"stage":row.stage},
                    
                });
                window.open(href, '_blank')
            },
        }
    }
    </script>

<style lang="less">
    @import "../assets/styles/dash.less";
</style>