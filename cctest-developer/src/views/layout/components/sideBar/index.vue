<template>
    <div class="side-card">
  
        <div class="side-bottom">
             <el-menu
                :default-active="$route.path"
                class="test_menu el-menu-vertical-demo"
                router
                unique-opened
             >
                <template v-for="(item,index) in menu">
                    <template v-if="item.children.length<1">
                        <el-menu-item :index="item.url" :key="index+'item'">
                            <!-- <img :src="item.unselected" class="na_unselected">
                            <img :src="item.selected" class="na_selected"> -->
                            <img src="../../../../assets/images/icon/nav_icon_01.png" class="na_unselected">
                            <img src="../../../../assets/images/icon/nav_icon_01_selected.png" class="na_selected">
                            <!-- <Icon :type="item.icon" class="menu-icon" size="16"></Icon>  -->
                            <span  slot="title">{{item.name}}</span>
                        </el-menu-item>
                    </template>
                    <template v-else>
                          <el-submenu :index="item.name" :key="index+'url'">
                            <template slot="title">
                                <!-- <img :src="item.unselected" class="na_unselected">
                                <img :src="item.selected" class="na_selected"> -->
                                <img src="../../../../assets/images/icon/nav_icon_02.png" class="na_unselected">
                                <img src="../../../../assets/images/icon/nav_icon_02_selected.png" class="na_selected">
                                <!-- <Icon :type="item.icon" class="menu-icon" size="16"></Icon> -->
                                <span  slot="title">{{item.name}}</span>
                            </template> 
                            <template v-for="(child,childIndex) in item.children" >
                                <template v-if="child.children.length<1">
                                    <el-menu-item :index="item.url+'-'+child.name" :key="childIndex+'child'">
                                        <span  slot="title">{{child.name}}</span>
                                    </el-menu-item>
                                </template>
                                <template v-else>
                                    <el-submenu :index="child.name" :key="childIndex+'child'" class="child_sub">
                                        <span  slot="title">{{child.name}}</span>
                                        <template v-for="(kid,kidIndex) in child.children" >
                                            <el-menu-item :index="item.url+'_'+child.name+'_'+kid.name" :key="kidIndex+'kid'">
                                                <span  slot="title">{{kid.name}}</span>
                                            </el-menu-item>
                                        </template>
                                    </el-submenu>
                                </template>  
                            </template> 
                        </el-submenu>
                    </template>
                </template>
            </el-menu>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    import { getMenuItems } from  "@/api/user";
    import { setMenu } from '@/utils/auth'
    export default {
        name: "index",
        data(){
            return{
                isCollapse: false,
                sideWidth:null,
                child:[],
                permission_routers:[
                    {
                        name:'硬件测试',
                        path:'/dashboard',
                        icon:'ios-apps',
                        children:[],
                        url:'/',
                        unselected:"@/assets/images/icon/nav_icon_01.png",
                        selected:"@/assets/images/icon/nav_icon_01_selected.png",
                    },{
                        name:'模型',
                        path:'/ModelRelease',
                        icon:'logo-buffer',
                        children:[],
                        url:'/ModelRelease',
                        unselected:"../../../../../assets/images/icon/nav_icon_02.png",
                        selected:"../../../../../assets/images/icon/nav_icon_02_selected.png",
                    },{
                        name:'对比图表',
                        path:'/contrast',
                        icon:'md-copy',
                        url:'/contrast',
                        children:[
                            {
                                name:'YSG',
                                path:'/contrast-YSG',
                                icon:'',
                                children:[],
                                url:'/YSG',
                            },{
                                name:'CalmCar',
                                path:'/contrast-CalmCar',
                                icon:'',
                                children:[],
                                url:'/CalmCar',
                            }
                        ],
                    }
                ],              
            }
        },
        mounted(){
            this.getMenu()
        },
        methods:{
            getMenu(){
                getMenuItems({})
                .then(res=>{
                    res.data.forEach(dataItem => {
                      console.log(res.data)
                        this.permission_routers.forEach(item=>{
                          // console.log(item.name)
                            if (item.name==='模型'){
                                item.children = [];
                                item.children.push(dataItem);
                                // console.log(item.name)
                            }
                        })
                        this.$store.commit("user/SET_MENU",this.permission_routers);
                        setMenu(JSON.stringify(this.permission_routers));
                    });
                })
            },
            handleOpen() {
                // console.log(key, keyPath);
            },
            handleClose() {
                // console.log(key, keyPath);
            },
        },
        computed:  {
            ...mapGetters(
                {menu:'menu'},
            )
        }
    }
</script>

<style lang="less">
   @import "../../../../assets/styles/dash.less";
</style>
