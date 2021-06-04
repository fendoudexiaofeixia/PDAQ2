<template>
    <div class="bread-panel">
        <el-breadcrumb separator-class="el-icon-d-arrow-right">
            <template v-for="(item,index)  in routeList">
                <el-breadcrumb-item  :key="item.path+index" v-if="item.meta.name">
                    <span v-if="item.redirect==='noredirect'||index==routeList.length-1" class="no-redirect">{{item.meta.name}}</span>
                    <router-link v-else :to="item.redirect||item.path">{{item.meta.name}}</router-link>
                </el-breadcrumb-item>
            </template>
        </el-breadcrumb>
    </div>
</template>

<script>
    export default {
        name: "bread",
        data(){
            return{
                routeList:null
            }
        },
        created() {
            this.getBreadcrumb()
        },
        watch: {
            $route() {
                this.getBreadcrumb()
            }
        },
        methods: {
            getBreadcrumb() {
                let matched = this.$route.matched.filter(item => item.name);
                const first = matched[1];
                if (first && first.name !== 'dashboard') {
                    matched = [{ path: '/dash-board', meta: { name: '首页' }}].concat(matched)
                }
                this.routeList = matched;
            }
        }
    }
</script>

<style lang="less">
    .el-breadcrumb{
        font-size: 12px
    }
    .bread-panel{
        margin: 1vw 0  1.5vw;
        // height: 40px;
    }
    .el-breadcrumb__item:last-child .el-breadcrumb__inner, .el-breadcrumb__item:last-child .el-breadcrumb__inner a, .el-breadcrumb__item:last-child .el-breadcrumb__inner a:hover, .el-breadcrumb__item:last-child .el-breadcrumb__inner:hover{
        color: #00FFFF;
        font-size: 10px;
    }
    .el-breadcrumb__inner a, .el-breadcrumb__inner.is-link{
        color: rgba(166,185,197,0.8);
        font-size: 10px;
    }
</style>
