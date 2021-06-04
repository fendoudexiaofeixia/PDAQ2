<template>
    <div class="wrapper">
        <div class="model-left-wrapper">
            <el-tabs tab-position="top" class="top-bar" @tab-click = "showIntType"  v-model="activeName">
                <el-tab-pane  v-for="(item,index) in folder"  :key="index" :label="item"  :name="item"  >
                    <span slot="label">  <img src="../../assets/images/folder.png"> <p> {{item}}</p> </span>
                    <div class="model-right-wrapper">
                         <template v-if="item == 'PY'">
                            <div class="content-right-wrapper">
                                  <Collapse v-model="value2" accordion>
                                    <Panel name="PY">
                                        PY
                                         <p slot="content">
                                           <pre> {{PYContent}}</pre>
                                         </p>
                                    </Panel>
                                  </Collapse>
                            </div>
                         </template>
                        <template v-else>
                            <el-tabs   @tab-click = "showDetail" type="card" class="int_tab"  v-model="IntActiveName">
                                <el-tab-pane  v-for="(intType,IntIndex) in IntList"  :key="IntIndex" :label="intType" :name="intType">
                                    <span slot="label">{{intType}} </span>
                                    <div class="content-right-wrapper">
                                         <Collapse   v-for="( child,childIndex ) in currentContent" v-model="value1" accordion :key="childIndex+'content'" >
                                             <Panel :name="child.name">
                                                 {{child.name}}
                                                <div slot="content">
                                                  <pre>  {{child.content}}</pre>
                                                </div>
                                            </Panel>
                                         </Collapse>
                                    </div>
                                </el-tab-pane>
                            </el-tabs>
                        </template>

                    </div>
                </el-tab-pane>
            </el-tabs>
        </div>
    </div>
</template>
<script>
    import { mapGetters } from 'vuex'
    import { get_platform , get_Folder , get_Model_detail , get_py} from  "@/api/user";
    export default {
        data(){
            return{
                activeName:'',
                folder:null,
                currentPlat:null,
                IntList:[],
                currentInt:null,
                currentContent:null,
                PYContent:null,
                value1:'',
                value2:'PY',
                IntActiveName:''
            }
        },
        mounted(){
            this.init()
        },
        methods:{
            showDetail(val){

                this.getContent(val.label)
            },
            getContent(val){
                get_Model_detail({path:this.$route.params.platform+'/'+this.$route.params.date+'/'+this.currentPlat,type:val})
                .then(res=>{
                    this.currentContent  = [];
                    this.currentContent  = res.data;
                })
            },
            showIntType(val){
                if(val == 'PY'){
                    this.currentPlat = val;
                }else{
                    this.currentPlat = val.label;
                }
                this.getType(this.activeName)
            },
            getType(val){
                if(val == 'PY'){
                    get_py({path:this.$route.params.platform+'/'+this.$route.params.date})
                    .then(res=>{
                        this.PYContent = res.data.content;
                    })
                }else{
                    get_Folder({path:this.$route.params.platform+'/'+this.$route.params.date+'/'+val})
                    .then(res=>{
                        this.IntList = [];
                        this.IntList = res.data;
                        this.IntActiveName = this.IntList[0];
                        this.getContent(this.IntActiveName)
                    })
                }
            },
            init(){
                get_platform({path:this.$route.params.platform+'/'+this.$route.params.date})
                .then(res=>{
                    this.folder = [];
                    res.data.forEach(item => {
                        if(item.indexOf('.py')!=-1){
                            item = 'PY';
                            this.folder[1] = this.folder [0];
                            this.folder[0] = 'PY';
                        }else{
                            this.folder.push(item);
                        }
                        this.activeName = this.folder[0];
                        this.showIntType(this.activeName )
                    });
                })
            }   
        },
        watch: {
            '$route' (to, from) { //监听路由是否变化
                if(to.params.date != from.params.date){
                    this.init();//重新加载数据
                }
            }
        },

        computed:{
            ...mapGetters(
                { menu:'menu'}, 
            )
        }
    }
</script>
<style lang="less">
    .model-left-wrapper{
        .el-tabs {
            height: 100%;
        }
        height: 100%;
        background-color: #ffffff;
        box-shadow: rgba(0, 0, 0, 0.16) 0px  2px 4px;
        .el-tabs--left, .el-tabs--right{
            height: 100%;
        }
        .el-tabs__item.is-active{
            img{
                content: url('../../assets/images/icon_blue.png');
            }
        }
        .el-tabs__item{
            width: 125px;
            height: auto;
            padding: 0.4vw 20px 0vw;
        }
        .el-tabs__content{
            overflow: auto;
            height:  calc(100% - 48px);
            background-color: #F8FAFD;
        }
        .top-bar{
            .el-tabs__header{
                // box-shadow: rgba(86,115,255,0.1) 2px 2px 6px;
            }
        }
        .el-tabs__header{
            padding: 0 3vw;
            margin-bottom: 0px;
        }
         .el-tabs__item  span{
             display: flex;
             display: -ms-flex;
             align-items: center;
         }
        .el-tabs__item  span p{
            margin-left: 20px;
        }
        .el-tabs__nav-wrap::after{
            height: 0px;
        }
        .el-tab-pane{
            height: 100%;
        }
        .el-tabs--left .el-tabs__header.is-left{
            margin-right: 0;   
        }
        .el-tabs--left .el-tabs__item.is-left{
            display: flex;
            align-items: center;
            justify-content: center;
            span{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
        }
    }
    .model-right-wrapper{
        width: 100% ;
        height: 100%;
        // background-color: #F8FAFD;
        padding: 3vw;
        // overflow-y: scroll;
        .int_tab .el-tabs__header{
            padding: 0 ;
        }
    }
    .content-right-wrapper{
        .ivu-collapse{
            margin: 10px 0;
            // padding: 8px 0;
            border-radius: 8px;
            border: 1px solid #DCE0E8;
            background-color: #fff;
        }
        .ivu-collapse>.ivu-collapse-item.ivu-collapse-item-active>.ivu-collapse-header{
            background-image:linear-gradient(#91A9FF, #5275F5 ) ;
            border-bottom: 0px ;
            color: #fff;
        }
        .ivu-collapse-item>.ivu-collapse-header{
            color: #333;
            border-radius: 8px 8px 0px 0px ;
            height: 48px;
            line-height: 47px;
        }
        .ivu-collapse-content>.ivu-collapse-content-box p{
            font-size: 0.8vw;
            color:#333;
        }
        .ivu-collapse-content>.ivu-collapse-content-box pre{
            font-size: 0.8vw !important;
        }
        .ivu-collapse-content>.ivu-collapse-content-box{
            padding-top: 0;
            padding-bottom: 0;  
        }
        .ivu-collapse-content {
            color: #333;
            padding: 1vw 2.5vw;
            background-color: #fff;
            overflow-x: scroll;
        }
        .content_collapse{
            .ivu-collapse{
                background-color: #F2F2F2;
                .ivu-collapse-item>.ivu-collapse-header{
                    color: #333;
                }
            }
            .el-collapse-item__header{
                padding: 1vw;
                .ivu-icon{
                    color: #29A2FF;
                }
            }
            .el-collapse-item__content{
                padding: 1vw;
                overflow-x: scroll;
            }
        }
    }
    .folder-list{
        padding-top: 2vw;
    }
    .folder-list li{
        padding: 1vw 2vw;
        display: flex;
        align-items: center;
        flex-direction: column;
        color: #333;
    }
    .test{
        transition: all .2s ease-in-out;
        img{
            transition: all .2s ease-in-out;
        }
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .test:hover{
        cursor: pointer;
        img{
            content: url('../../assets/images/icon_blue.png');
        }
        p{
            color: #2986FF;
        }

    }
    .int_tab{
        .el-tabs__header{
                margin: 0 0 1vw !important;

            // box-shadow: rgba(0,0,0,0) 0px 0px 0px !important;
        }
        .el-tabs__header .el-tabs__item:last-child, .el-tabs--bottom .el-tabs--right>.el-tabs__header .el-tabs__item:last-child, .el-tabs--bottom.el-tabs--border-card>.el-tabs__header .el-tabs__item:last-child, .el-tabs--bottom.el-tabs--card>.el-tabs__header .el-tabs__item:last-child, .el-tabs--top .el-tabs--left>.el-tabs__header .el-tabs__item:last-child, .el-tabs--top .el-tabs--right>.el-tabs__header .el-tabs__item:last-child, .el-tabs--top.el-tabs--border-card>.el-tabs__header .el-tabs__item:last-child, .el-tabs--top.el-tabs--card>.el-tabs__header .el-tabs__item:last-child{
            padding-right: 2vw;
        }
        .el-tabs__header .el-tabs__item.is-active{
            background-color: #fff;
            border-radius: 20px;
            color: #5684FF;
            border:  1px solid rgba(86, 115, 255, 0.2);
            border-bottom: 1px solid rgba(86, 115, 255, 0.2);
            box-shadow: rgba(122, 139, 166, 0.2) 0px 2px 4px;
        }
        .el-tabs__item{
            font-size: 0.8vw;
            padding: 0vw 20px 0vw;
        }
        .el-tabs__header .el-tabs__item span{
            padding:  0  1.2vw;
            font-size: 0.8vw;
        }
        .el-tabs__header{
            border-bottom: 0px;
            margin: 0 0 2vw;
        }
        .el-tabs__header .el-tabs__item{
            border-bottom: 0px;
            border-left: 0px;
        }
        .el-tabs__header .el-tabs__nav{
            // border-bottom: auto;
            border-radius: 20px;
            background-color: #F4F5FA;
            border: 0px;
        }
    }

</style>