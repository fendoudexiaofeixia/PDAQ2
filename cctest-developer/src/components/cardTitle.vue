<template>
    <div class="card-left-line">
        <p class="card-head-title">{{cardTitle}}</p>
    </div>
</template>

<script>
export default {
    data(){
        return{

        }
    },
    props:['cardTitle'],
}
</script>
<style lang="less">
    .card-head-title{
        // position: relative;
        margin: 0 0rem;
        font-size: 1.1rem;
        color: #343434;
        font-weight: 500;
    }
    .card-left-line{
        position: relative;
        margin: 0.6rem 0.6rem 1rem;
    }
    // .card-left-line::after{
    //     content: " ";
    //     position: absolute;
    //     left: 0;
    //     top: 0.3vw;
    //     width: 4px;
    //     background-color: #5673FF;
    //     height: 66%;
    //     margin-right: 1vw;
    // }
</style>