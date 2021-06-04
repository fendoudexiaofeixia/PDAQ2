<template>
    <div class="nav-menu-panel">
          <el-menu  
                :default-active="$route.path"
                :unique-opened="true"
                mode= "horizontal"
                class="el-menu-vertical-demo"
                @select="selectmenu"
                router>
            <template v-for="(item,index) in menu">
                <el-menu-item :index="item.url" :key="index+'item'">
                    <!-- <Icon :type="item.icon" class="menu-icon" size="16"></Icon> -->
                    <span  slot="title">{{item.name}}</span>
                </el-menu-item>
            </template>
          </el-menu>
    </div>
</template>
<script>
import {setMenuItemInfo} from '../../../utils/auth'

export default {
    data(){
        return{
            theme1:'light',
        }
    },
    // mounted(){
    //     this.selectmenu(this.$route.path)
    // },
    methods:{
        selectmenu(index){
            this.$store.getters.menu.filter(item=> {
                if(item.url == index){
                    this.$store.commit('user/SET_MENU_SIDE', item.children);
                    setMenuItemInfo(JSON.stringify(item.children))
                }
            })
        }
    },
    computed:{
            menu(){
                return this.$store.getters.menu;
            },
          
        },
}
</script>
<style lang="less">
    .nav-menu-panel{
        width: 76%;
        height: 100%;
        z-index: 1;
        // position: absolute;
        // top: 0;
        // left: 0;
        .el-menu--horizontal>.el-menu-item.is-active{
            color: #00ffff;
            border-bottom: 0px;
            position: relative;
        }
        .el-menu--horizontal>.el-menu-item.is-active::after{
            position: absolute;
            bottom: 17%;
            content: " ";
            left: 50%;
            width: 2px;
            height: 2px;
            border-left: 3px solid transparent;
            border-right: 3px solid transparent;
            border-top: 4px solid #00D9FF;
        }
        .el-menu-item.is-active i{
            color: #00ffff
        }
        .el-menu--horizontal>.el-menu-item{
            color: #ffffff;
            background: url("../../../assets/images/sidebar/top.png");
            background-position: 100% 100%;
            background-size: 100% 100%;
            height: 100%;
            width: 180px;
            line-height: 50px!important;
            // padding: 0.3vw 20px;
            text-align: center;
             font-size: 1.05vw;
            font-weight: 500;
        }
    
        .el-menu{
            background-color: rgba(0, 0, 0, 0);
            border-bottom: 0px;
            height: 100%;
           
        }
        .el-menu-item i{
            color: #ffffff
        }  
        .el-menu-item i:hover{
            color: #00ffff
        }
        .el-menu-item:focus, .el-menu-item:hover{
            background-color: rgba(0, 0, 0, 0) !important;
            color: #00ffff !important;
            .el-menu-item i{
                color: #ffffff
            }     
        }
        .el-menu--horizontal>.el-menu-item:nth-child(1){
            position: absolute;
            top: 4px;
            left: 0px;
        }
         .el-menu--horizontal>.el-menu-item:nth-child(2){
            position: absolute;
            top: 4px;
            left: 13.4%;
        }
         .el-menu--horizontal>.el-menu-item:nth-child(3){
            position: absolute;
            top: 6px;
            right: 10.8%;
        }
         .el-menu--horizontal>.el-menu-item:nth-child(4){
            position: absolute;
            top: 4px;
            right: -1.8%;
        }
    }
</style>