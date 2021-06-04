<template>
    <div :class="test_class== 'wide'? 'wide-width':'origin-width'">
        <p class="head-htitle">{{title}}</p>
        <!-- <hr class="head-hr"> -->
    </div>
</template>

<script>
export default {
    data(){
        return{
            
        }
    },
    name:'headTitle',
    props:['title','test_class'],
}
</script>
<style lang="less">
   
    .head-hr{
        color: #538DFF;
        width: 40px;
        margin-top: 5px;
        border: 1px solid #538DFF;
    }
</style>