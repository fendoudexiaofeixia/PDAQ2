<template>
    <div class="head-panel">
            <div class="head-logo">
                <!-- <img src="../../../assets/images/logo/login_logo.png"> -->
                <h3>CalmCar测试管理平台</h3>
            </div>
            <div class="head-avator">
                <!-- <Dropdown transfer trigger="hover" @on-click="changeUser" class="userDropDown">
                    <a href="javascript:void(0)" class="dropdown-panel">
                        <el-avatar :size="size" src="../../../assets/images/logo/nav_logo.png" ></el-avatar>
                            {{user.loginName}}     
                        <Icon type="ios-arrow-down"></Icon>
                    </a>
                    <DropdownMenu  slot="list">
                        <DropdownItem   name="sign-out">
                        退出登录
                        </DropdownItem>
                    </DropdownMenu >
                </Dropdown> -->
        </div>   
    </div>
</template>

<script>
export default {
    name: 'headBar',
    data(){
        return{
            size:'small',
            user:{loginName:'calmcar'}
        }
    },
    mounted() {
    },

    methods:{
        changeUser(name){
            if(name == 'own-space'){
                this.$router.push('/change-pwd')
            }else if(name == 'own-avatar'){
                this.$router.push('/avatar')
            }else if(name == 'sign-out'){
                this.$router.push('/')
            }
        }
    },
    computed:{
        // user(){
        //     return this.$store.getters.user;
        // },
        // url(){
            // return config.ta+this.$store.getters.user.imgUrl;
        // }
    },
}
</script>

<style lang="less">
    .head-panel{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2vw;
        box-shadow:0 0 4px rgba(45,84,221,.2);
    }
    .head-logo{
        width: 16rem;
        display: flex;
        justify-content: center;
        align-items: center;    
        img{
            height: 36px;
            margin-top: 3px;
        }
        h3{
            color: #007fff;
            margin: 0 8px;
            line-height: 32px;
            font-size: 1.5rem;
            font-weight: 600;
        }
    }
    .head-avator{
        width: 240px;
        display: flex;
        justify-content: center;
        .el-avatar--small{
            margin-right: 5px;
        }
        .dropdown-panel{
            display: flex;
            align-items: center;
            justify-content: center;
        }
    }

    .ivu-select-dropdown{
        background-color: #070F30;
        border: 1px solid rgba(17,153,238,.4);
        color: #070F30;
        box-shadow: rgba(17,153,238,.16) 0 2px 4px;
        .ivu-dropdown-item-divided{
            border-top:0px; 
        }
        .ivu-dropdown-item{
            color: rgba(17,153,238,.8);
            font-size: 12px !important;
        }
        .ivu-dropdown-item:nth-child(2){
            border-top:  1px solid rgba(17,153,238,.4);
        }      
        .ivu-dropdown-menu {
            min-width: 88px;
        }
        .ivu-dropdown-item:hover{
            background-color: rgba(17,153,238,.7);
            color: #FFFFFF;
        }
    }
    .dropdown-panel{
        color: #D8E0E5;
        .ivu-avatar-image{
            margin: 0 6px;
        }
        .ivu-icon{
            margin: 0 4px;
        }
    }
</style>
