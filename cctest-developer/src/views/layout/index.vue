<template>
    <div class="layout-wrapper">
        <div class="layout-top">
            <div class="side-top">
                <img src="../../assets/images/logo/whiteshort1.png">
                <h4>
                    测试管理信息平台
                </h4>
            </div>
        </div>
        <div class="layout-left">
            <side-bar></side-bar>
            <!-- <nav-bar></nav-bar> -->
        </div>
        <div class="layout-right">
            <!-- <div class="layout-left" :style="{'width':sideWidth}"> -->
<!-- 
           <div class="layout-left" v-show="menuside.length!=0"  :style="{'width':sideWidth}">
                <sideBar @width="width"></sideBar>
            </div> -->
            <!-- <div> -->
            <!-- <div :class="menuside.length==0?'layout-right-wrapper':'layout-right'"  > -->
                <keep-alive>
                    <transition name="roter-view" mode="in-out">
                        <router-view></router-view>
                    </transition>
                </keep-alive>
                <!-- </div> -->
        </div>
    </div> 
</template>

<script>
    import sideBar  from "./components/sideBar"
    export default {
        name: "index",
        data(){
            return{
                sideWidth:'15vw',
                otherWidth:null
            }
        },
        components: {sideBar},
        methods:{
            width(val){
                this.sideWidth = val;
            }
        },
        watch:{
            width(val){
                this.sideWidth = val;
            }
        },
        computed:{
            menuside(){
                return this.$store.getters.menuside;
            },
    
        },
    }
</script>

<style lang="less">

</style>
