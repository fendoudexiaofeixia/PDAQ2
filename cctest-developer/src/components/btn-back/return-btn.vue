<template>
    <Button icon="md-arrow-back" class="return-btn" @click="returnRoute">返回</Button>
</template>

<script>
    export default {
        name: "return-btn",
        data(){
            return{

            }
        },
        methods:{
            returnRoute(){
                this.$router.go(-1);
            }
        }
    }
</script>

<style lang="less">
    .return-btn{
        background: rgba(0,0,0,0);
        color: #00FFFF;
        transition: color 0.2s;
        font-size: 12px;
        border: 0px;
        .ivu-icon{
            font-size: 17px;
            color: #00FFFF;
        }
    }
    .return-btn:hover{
        background: rgba(0,0,0,0);
        color: #ffffff;
    }
</style>
