





<template>
    <div class="dash-wrapper"  >
        <div class="layout-top">
            <div class="side-top">
                <img src="../../assets/images/logo/whiteshort1.png">
                <h4>
                    测试管理平台
                </h4>
            </div>
            <div class="dash-btn-right">
                <div class="btn-right">
                    <Button class="view-btn"  @click="seeMore()"><Icon type="md-eye" size="15"  style="color:rgba(255,255,255,0.6)"/><span style="margin-left:6px">查看</span></Button>
                    <el-button class="export-btn"  @click="openExport()"> <i class="el-icon-upload2" ></i>导出</el-button> 
                </div>
            </div>
        </div>
  
        <div class="anchor-panel">
            <Anchor show-ink>    
                <AnchorLink href="#head-top" active title="概况"/>
                <template v-for="(item,index) in testData" >
                    <AnchorLink  
                            :href="'#'+item.name"
                            :title="item.name"
                            :key="'anchor'+index"
                        >
                        <template v-if="item.name!='performance'&&item.name!='functional'&&item.name!='lane'">
                            <AnchorLink  v-for="(child,childIndex) in item.children" 
                                :href="'#'+item.name+'_'+child.name"
                                :title="child.name"
                                :key="'anchor'+childIndex" />
                        </template>
                    </AnchorLink>
                </template>
            </Anchor>
        </div>
    <div class="dash-test-wrapper" >
        <div class="dash-first" id="head-top">
            <div class="head-title-card">
                <div class="left">
                    <p class="head-htitle"> {{firstTitle}}</p>
                </div>
            </div>
            <div class="total-panel">
                <div class="total-top">
                    <div class="total-top-left">
                        <el-card class="box-card top-card" > 
                            <div slot="header" class="clearfix">
                                <cardTitle :cardTitle="totalTitle"></cardTitle>
                            </div>
                            <el-card class="box-card inset-card" v-for="item in infoData" :key="item.title" > 
                                <div class="info-bottom">
                                    <div class="info-bottom-left">
                                        <img :src="item.src">
                                    </div>
                                    <div class="info-bottom-right">
                                        <p>{{item.data}}</p>
                                        <p class="title">{{item.title}}</p>
                                    </div>
                                </div>
                            </el-card>
                        </el-card>  
                    </div>
                    <div class="total-top-right">
                        <el-card class="box-card top-card" >
                            <div slot="header" class="clearfix">
                                <cardTitle :cardTitle="totalTitle1"></cardTitle>
                            </div>
                            <div class="center-pass-table">
                                <el-table :data="testCaseData" class="pass-table" :span-method="objectSpanMethod">
                                    <el-table-column  label="功能" align="left" class-name="type" min-width="100">
                                        <template slot-scope="scope">
                                            {{scope.row.name}}
                                        </template>
                                    </el-table-column>
                                    <el-table-column  label="测试项" align="center" class-name="type" min-width="150" >
                                        <template slot-scope="scope" >
                                            {{scope.row.child_item}}
                                        </template>
                                    </el-table-column>
                                    <el-table-column prop="passed" label="passed" align="center" class-name="pass"></el-table-column>
                                    <el-table-column prop="failed" label="failed" align="center" class-name="fail"></el-table-column>
                                    <el-table-column prop="broken" label="broken" align="center" class-name="broken"></el-table-column>
                                </el-table>
                            </div>
                        </el-card>
                    </div>
                </div>
                <div class="total-bottom">
                       <div class="card-left-line">
                            <p class="card-head-title">{{totalTitle2}}</p>
                        </div>
                    <el-card class="box-card top-pass-card pass-e" >
                        <div slot="header" class="clearfix">
                        </div>
                        <div class="center-pass-table " id="pass-right">
                            <div id="passEcharts" class="passEcharts"></div>
                        </div>
                    </el-card>
                </div>
            </div>
        </div>   
        <template v-for="(item,index) in passData" >
             <div v-if="item.name!='performance'&& item.name !='functional'&&item.name !='lane'" :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"  :key="index+'pass'" :id="item.name">
                <headTitle  :title="item.name"></headTitle>
                    <el-card v-for="(child,childIndex) in item.children"  :key="childIndex" :id="item.name+'_'+child.name" class="test_item" shadow="never">
                        <div slot="header" class="clearfix">
                            <h3 class="child_header" v-if="child.name=='angle'">{{'目标朝向'}}</h3>
                            <h3 class="child_header" v-else-if="child.name=='distance_use_kl'">{{'测距方法0'}}</h3>
                            <h3 class="child_header" v-else-if="child.name=='distance_no_kl'">{{'测距方法1'}}</h3>
                            <h3 class="child_header" v-else-if="child.name=='relative_velocity'">{{'相对速度'}}</h3>
                        </div>
                        <div class=" box-wrapper od-distance">
                            <div class="box-inset info-set">
                                <el-card class="box-card" shadow="never">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="test_title"></cardTitle>
                                    </div>
                                    <div class="top-panel">
                                        <ul v-if="child.name.indexOf('distance')!=-1" class="method_ul">
                                            <li >
                                                {{distance.Intro}}
                                            </li>
                                            <li>
                                                {{distance.title}}
                                                <div class="error_panel">
                                                    <p>纵向相对误差：</p>
                                                    <img src="../../assets/images/dis_1.png">
                                                </div>
                                                <div class="error_panel">
                                                    <p> 横向相对误差：</p>
                                                    <img src="../../assets/images/dis_2.png">
                                                </div>
                                            </li>
                                        </ul> 
                                        <ul v-if="child.name.indexOf('angle')!=-1" class="method_ul">
                                            <li >
                                                {{angle.Intro}}
                                            </li>
                                            <li>
                                                {{angle.title}}
                                                <div class="error_panel">
                                                    <img src="../../assets/images/angle_1.png" class="angle_img">
                                                 </div>
                                            </li>
                                        </ul> 
                                        <ul v-if="child.name.indexOf('relative')!=-1" class="method_ul">
                                                <li >
                                                {{relative_velocity.Intro}}
                                            </li>
                                            <li>
                                                {{relative_velocity.title}}
                                                    <div class="error_panel">
                                                    <p>纵向误差：</p>
                                                    <img src="../../assets/images/re_1.png" class="rel_img">
                                                </div>
                                                <div class="error_panel">
                                                    <p> 横向误差：</p>
                                                    <img src="../../assets/images/re_2.png" class="rel_img">
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </el-card>
                            </div>
                            <div class="box-inset long-set">
                                <el-card class="box-card" shadow="never">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                    </div>
                                    <div class="distance-center-panel">
                                        <div :id="'_f'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                    </div>
                                </el-card>
                            </div>
                            <div class="box-inset short-set">
                                <el-card class="box-card" shadow="never">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                    </div>
                                    <div class="top-panel">
                                        <div :id="'_d'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                    </div>
                                </el-card>
                            </div>
                            <div class="box-inset short-set">
                                <el-card class="box-card" shadow="never">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="distanceTitle2"></cardTitle>
                                    </div>
                                    <div class="distance-center-panel">
                                        <div :id="'_s'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                    </div>
                                </el-card>
                            </div>
                        </div>
                        <div class="distance-bottom" v-if="child.accuracy.length>0">
                            <el-card class="box-card" shadow="never">
                                <div slot="header" class="clearfix">
                                </div>
                                <div class="tab-panel">
                                    <el-tabs type="card"  v-model="activeName">
                                        <template v-for="(accuracyItem,accuracyIndex) in child.accuracy" >
                                            <el-tab-pane :label="accuracyItem.class_name" :key="accuracyIndex" >
                                                <div class="table_panel">
                                                    <el-table :data="accuracyItem.data" stripe class="accTable" id="accTable">
                                                        <el-table-column  label="检查项" align="left" min-width="265">
                                                            <template slot-scope="scope">
                                                                {{scope.row.title_name}}
                                                            </template>
                                                        </el-table-column>
                                                        <el-table-column label="测试用例总数" prop="total" align="center"></el-table-column>
                                                        <el-table-column label="Passed" prop="passed" align="center" class-name="pass"></el-table-column>
                                                        <el-table-column label="Failed" prop="failed" align="center"  class-name="fail"></el-table-column>
                                                        <el-table-column label="max_err" prop="max_err" align="center" min-width="80"  class-name="broken">
                                                                <template slot-scope="scope">
                                                                        <template v-if="scope.row.max_err==0"> 
                                                                            {{'NA'}}
                                                                        </template> 
                                                                        <template v-else>
                                                                            <template v-if="scope.row.max_err==undefined||scope.row.max_err==null"> 
                                                                                    {{scope.row.max_err}}
                                                                                </template>
                                                                                <template v-else>
                                                                                    {{(scope.row.max_err).toFixed(2)}}
                                                                                </template>
                                                                        </template>
                                                                    </template>
                                                                </el-table-column>
                                                                <el-table-column label="case_name" prop="case_name" align="center" min-width="140">
                                                                    <template slot-scope="scope">
                                                                        <template v-if="scope.row.max_err==0">
                                                                    {{'NA'}}
                                                                </template> 
                                                                <template v-else>
                                                                    <el-button class="showcasebtn" @click="showCase(scope.row)">{{ scope.row.case_name}} </el-button> 
                                                                </template>
                                                            </template>
                                                        </el-table-column>
                                                    </el-table>
                                                </div>
                                            <div class="accuracy-center" v-if="child.name!='angle'&&child.name!='relative_velocity'">
                                                <div class="accuracy_left">
                                                    <div class="card-left-line">
                                                        <p class="card-head-title">{{broad}}</p>
                                                    </div>
                                                    <el-card class="box-card accuracy-card" shadow="never">
                                                        <div slot="header" class="clearfix">
                                                        </div>
                                                        <div class="accuracy-name-table" style="position:relative">
                                                            <div :id="'accuracy-broad'+accuracyIndex+'_'+item.name+'_'+child.name" class="leftnameEcharts" :ref="'left_chart_'+activeName"></div>
                                                            <img src="../../assets/images/car_mode1.png" style="height:60px;position:absolute;bottom:-30px;left:46%;" >
                                                        </div>
                                                    </el-card>
                                                </div>
                                                <div class="accuracy_right">
                                                    <div class="card-left-line">
                                                        <p class="card-head-title">{{vertical}}</p>
                                                    </div>
                                                    <el-card class="box-card accuracy-card" shadow="never">
                                                        <div slot="header" class="clearfix">
                                                        </div>
                                                        <div class="accuracy-name-table" style="position:relative">
                                                            <div :id="'accuracy-vertical'+accuracyIndex+'_'+item.name+'_'+child.name"  class="rightnameEcharts" :ref="'right_chart_'+activeName"></div>
                                                            <img src="../../assets/images/car_mode2.png" style="position:absolute;left:10px;top:42%" >
                                                        </div>
                                                    </el-card>
                                                </div>
                                                </div>
                                            </el-tab-pane>
                                        </template>
                                    </el-tabs>
                                </div>
                            </el-card>   
                        </div>
                    </el-card>
                </div>  


                <!-- 性能测试 -->
                <div v-if="item.name=='performance'" :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"  :key="index+'pass'" :id="item.name">
                    <headTitle  :title="item.name"></headTitle>
                        <el-card v-for="(child,childIndex) in item.children"  :key="childIndex" :id="item.name+'_'+child.name" class="test_item"  shadow="never">
                            <div slot="header" class="clearfix">
                                <h3 class="child_header">
                                    {{'性能测试'}}
                                </h3>
                            </div>
                            <div class="od-distance">
                                <div class="method_panel">
                                    <el-card class="box-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="test_title"></cardTitle>
                                        </div>
                                        <div class="top-panel">
                                            <ul  class="per_ul">
                                                <li v-for="(per_item,per_index) in performance_Intro" :key="per_item+per_index">
                                                    {{per_item.title}}
                                                    <ul class="per_li">
                                                        <li v-for="(child_per_item,child_per_index) in per_item.Intro" :key="child_per_index">
                                                            {{child_per_item.name}}
                                                        </li>
                                                    </ul>
                                                </li>
                                            </ul> 
                                        </div>
                                    </el-card>
                                </div>
                                <div class="distance-center">
                                    <el-card class="box-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_d'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card>
                                    <el-card class="box-card right-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_f'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card>
                                </div>
                            </div>
                            <div class="distance-bottom" >
                                <el-card class="box-card" shadow="never" v-if="fpsShow">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="fpsTitle"></cardTitle>
                                    </div>
                                    <div class="tab-panel" >
                                        <el-table :data="fpsData"  class="accTable" stripe >
                                            <el-table-column label="相机数" align="center" prop="camera_num"></el-table-column>
                                            <el-table-column label="模块" align="center" prop="name"></el-table-column>
                                            <el-table-column label="平均" align="center">
                                                <el-table-column label="开启录制" align="center" prop="mean.open"></el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="mean.close"></el-table-column>
                                            </el-table-column>
                                            <el-table-column label="Percentile(99)" align="center">
                                                <el-table-column label="开启录制" align="center" prop="99%percentile.open"> </el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="99%percentile.close"></el-table-column>
                                            </el-table-column>
                                        </el-table>
                                    </div>
                                </el-card>  
                                <el-card class="box-card fps-card" shadow="never" v-if="timeShow">
                                    <div slot="header" class="clearfix"> 
                                        <cardTitle :cardTitle="timeTitle"></cardTitle>
                                    </div>
                                    <div class="tab-panel">
                                        <el-table :data="timeData"  class="accTable"   :span-method="timeSpanMethod">
                                            <el-table-column label="相机数" align="center" prop="camera_num"></el-table-column>
                                            <el-table-column label="模块" align="center" prop="name"></el-table-column>
                                            <el-table-column label="平均" align="center" prop="mean">
                                                <el-table-column label="开启录制" align="center" prop="mean.open"></el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="mean.close"></el-table-column>
                                            </el-table-column>
                                            <el-table-column label="Percentile(99)" align="center" >
                                                <el-table-column label="开启录制" align="center" prop="99%percentile.open"> </el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="99%percentile.close"></el-table-column>
                                            </el-table-column>
                                        </el-table>
                                    </div>
                                </el-card>
                                <el-card class="box-card fps-card" shadow="never"  v-if="resourceShow">
                                    <div slot="header" class="clearfix">
                                        <cardTitle :cardTitle="sourceTitle"></cardTitle>
                                    </div>
                                    <div class="tab-panel" >
                                        <el-table :data="resourceData"  class="accTable" :span-method="sourceSpanMethod">
                                            <el-table-column label="相机数" align="center" prop="camera_num"></el-table-column>
                                            <el-table-column label="模块" align="center" prop="name"></el-table-column>
                                            <el-table-column label="平均" align="center">
                                                <el-table-column label="开启录制" align="center" prop="mean.open"> </el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="mean.close"></el-table-column>
                                            </el-table-column>
                                            <el-table-column label="Percentile(99)" align="center" >
                                                <el-table-column label="开启录制" align="center" prop="99%percentile.open"></el-table-column>
                                                <el-table-column label="关闭录制" align="center" prop="99%percentile.close"></el-table-column>
                                            </el-table-column>
                                        </el-table>
                                    </div> 
                                </el-card>
                            </div>
                        </el-card>
                    </div>  

                    <!-- lane -->
                <div v-if="item.name=='lane'" :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"  :key="index+'pass'" :id="item.name">
                    <headTitle  :title="item.name"></headTitle>
                        <el-card v-for="(child,childIndex) in item.children"  :key="childIndex" :id="item.name+'_'+child.name" class="test_item"  shadow="never">
                            <div slot="header" class="clearfix">
                                <h3 class="child_header">
                                </h3>
                            </div>
                            <div class="lane-od-distance">
                                <div class="method_panel">
                                    <el-card class="box-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="test_title"></cardTitle>
                                        </div>
                                        <div class="top-panel">
                                            <ul  class="method_ul">
                                                <li  >{{lane_Intro.name}}</li>
                                                <li  >{{lane_Intro.title}}</li>   
                                                <p class="lane_p">{{'图一，检测有效区间内以1m为区间，在该场景内统计平均横向误差。'}} </p>
                                                <img src="../../assets/images/lane/01.png" class="per_fir">
                                                <p  class="lane_p">{{'图二，分别对每帧数据进行精度统计，共统计六组指标：'}} </p>
                                                <ul class="lane_ul">
                                                    <li>
                                                        <p>{{'分别统计在有效范围内每条车道线平均横向误差（err_x_inner）'}}</p>
                                                        <img src="../../assets/images/lane/02.png">
                                                    </li>
                                                    <li>
                                                        <p>{{'[0-60]m范围内每条车道线平均横向误差（err_x_（0-60m））'}}</p>
                                                        <img src="../../assets/images/lane/03.png">
                                                    </li>
                                                    <li>
                                                        <p>  {{'每条车道线检测起始点横向误差（err_x_start）'}}</p>
                                                        <img src="../../assets/images/lane/04.png" class="fir_05">
                                                    </li>
                                                    <li>
                                                        <p>  {{'每条车道线检测0m横向误差（err_x_0m）'}}</p>
                                                        <img src="../../assets/images/lane/05.png" class="fir_05">
                                                    </li>
                                                    <li>
                                                        <p> {{'有效范围内每条车道线平均相对横向误差（relative_err_inner）'}}</p>
                                                        <img src="../../assets/images/lane/06.png">
                                                    </li>
                                                    <li>
                                                        <p>  {{'有[1-60]m范围内每条车道线平均相对横向误差（relative_err_（1-60m））'}}</p>
                                                        <img src="../../assets/images/lane/07.png">
                                                    </li>
                                                </ul>
                                                <p  class="lane_p">{{'图三，场景轨迹图。'}}</p>
                                            </ul>
                                        </div>
                                    </el-card>
                                </div>
                                <div class="distance-center">
                                    <el-card class="box-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_d'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card>
                                    <el-card class="box-card right-card" shadow="never">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_f'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card>
                                </div>
                            </div>
                            <div class="distance-bottom" v-if="child.accuracy.length>0">
                                <el-card class="box-card" shadow="never">
                                    <div slot="header" class="clearfix">
                                    </div>
                                    <div class="tab-panel"> 
                                        <el-tabs type="card" >
                                            <template v-for="(accuracyItem,accuracyIndex) in child.accuracy">
                                                <el-tab-pane :label="accuracyItem.class_name" :key="accuracyIndex">
                                                    <div class="table_panel">

                                                <el-table :data="accuracyItem.data" stripe class="accTable" id="accTable">
                                                    <el-table-column    class-name="pass" :label="accuracyItem.class_name==null||accuracyItem.class_name==undefined?'':accuracyItem.class_name" align="center">
                                                        <el-table-column label="检查项" align="left" min-width="265">
                                                            <template slot-scope="scope">
                                                                {{scope.row.title_name}}
                                                            </template>
                                                        </el-table-column>
                                                        <el-table-column label="测试用例总数" prop="total" align="center"></el-table-column>
                                                        <el-table-column label="Passed" prop="passed" align="center"   class-name="pass"></el-table-column>
                                                        <el-table-column label="Failed" prop="failed" align="center"  class-name="fail"></el-table-column>
                                                                <el-table-column label="max_err" prop="max_err" align="center" min-width="80"  class-name="broken">
                                                                <template slot-scope="scope">
                                                                        <template v-if="scope.row.max_err==0"> 
                                                                            {{'NA'}}
                                                                        </template> 
                                                                        <template v-else>
                                                                            <template v-if="scope.row.max_err==undefined||scope.row.max_err==null"> 
                                                                                    {{scope.row.max_err}}
                                                                                </template>
                                                                                <template v-else>
                                                                                    {{(scope.row.max_err).toFixed(2)}}
                                                                                </template>
                                                                        </template>
                                                                    </template>
                                                                </el-table-column>
                                                            <el-table-column label="case_name" prop="case_name" align="center" min-width="140">
                                                                <template slot-scope="scope">
                                                                    <template v-if="scope.row.max_err==0">
                                                                        {{'NA'}}
                                                                    </template> 
                                                                    <template v-else>
                                                                        <el-button class="showcasebtn" @click="showCase(scope.row)">{{ scope.row.case_name}} </el-button> 
                                                                    </template>
                                                                </template>
                                                            </el-table-column>
                                                    </el-table-column>
                                                </el-table>
                                                    </div>
                                                <!-- <div class="accuracy-center" v-if="child.name!='angle'&&child.name!='relative_velocity'">
                                                    <el-card class="box-card accuracy-card" shadow="hover">
                                                        <div slot="header" class="clearfix">
                                                            <cardTitle :cardTitle="broad"></cardTitle>
                                                        </div>
                                                        <div class="accuracy-name-table" style="position:relative">
                                                            <div :id="'accuracy-broad'+accuracyIndex+'_'+item.name+'_'+child.name" class="leftnameEcharts"></div>
                                                            <img src="../../assets/images/car.png" style="height:60px;position:absolute;bottom:-20px;left:46%;transform:rotate(180deg);" >
                                                        </div>
                                                    </el-card>
                                                    <el-card class="box-card accuracy-card" shadow="hover">
                                                        <div slot="header" class="clearfix">
                                                            <cardTitle :cardTitle="vertical"></cardTitle>
                                                        </div>
                                                        <div class="accuracy-name-table" style="position:relative">
                                                            <div :id="'accuracy-vertical'+accuracyIndex+'_'+item.name+'_'+child.name"  class="rightnameEcharts"></div>
                                                            <img src="../../assets/images/car.png" style="height:60px;position:absolute;left:20px;top:30%;transform:rotate(-90deg);" >
                                                        </div>
                                                    </el-card>
                                                </div> -->
                                                </el-tab-pane>
                                            </template>
                                        </el-tabs>
                                    </div>
                                </el-card>   
                            </div>
                        </el-card>
                    </div>
                    <div v-if="item.name=='functional'" :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"  :key="index+'pass'" :id="item.name">
                    <headTitle  :title="item.name"></headTitle>
                        <el-card v-for="(child,childIndex) in item.children"  :key="childIndex" :id="item.name+'_'+child.name" class="test_item"   shadow="never">
                            <div slot="header" class="clearfix">
                                <h3 class="child_header">
                                    <!-- {{'report_functional'}} -->
                                </h3>
                            </div>
                            <div class="od-distance funtional_panel">
                                <!-- <div class="method_panel">
                                    <el-card class="box-card" shadow="hover">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="test_title"></cardTitle>
                                        </div>
                                        <div class="top-panel">
                                            <ul  class="per_ul">
                                                <li v-for="(per_item,per_index) in performance_Intro" :key="per_item+per_index">
                                                    {{per_item.title}}
                                                    <ul class="per_li">
                                                        <li v-for="(child_per_item,child_per_index) in per_item.Intro" :key="child_per_index">
                                                            {{child_per_item.name}}
                                                        </li>
                                                    </ul>
                                                </li>
                                            </ul> 
                                        </div>
                                    </el-card>
                                </div> -->
                                <div class="distance-top">
                                    <el-card class="box-card" shadow="hover">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                        </div>
                                        <div class="top-panel">
                                            <div :id="'_d'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card>
                                </div>
                                <!-- <div class="distance-top">
                                    <el-card class="box-card" shadow="hover">
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_d'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card> -->
                                    <!-- <el-card class="box-card right-card" shadow="hover"> 
                                        <div slot="header" class="clearfix">
                                            <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                        </div>
                                        <div class="distance-center-panel">
                                            <div :id="'_f'+'_'+item.name+'_'+child.name+'_'+childIndex" class="suites"></div>
                                        </div>
                                    </el-card> -->
                                <!-- </div> -->
                            </div>
                        </el-card>
                    </div>
                </template>  
            <BackTop></BackTop>
        </div>   
    </div>
</template>

<script>
    import {setTestData ,setName} from '@/utils/auth'
    import { mapGetters } from 'vuex'
    import { getBase ,  getItems,getSuites,getAccuracy,getFeatures , getPerformanceItems} from "@/api/user";
    import  headTitle  from "@/components/headTitle" 
    import  cardTitle  from "@/components/cardTitle"
    var echarts = require('echarts');
    
    export default {
        name: "dashBoard",
        data(){
            return{
                sourceTitle:'资源占用统计',
                timeTitle:'模块耗时统计',
                fpsTitle:'帧率统计',
                fpsData:[{
                    "name": "perception_fps",
                    "camera_num": 7,
                    "max": {
                        "2": 5.75,
                        "1": 6.84
                    },
                    "min": {
                        "2": 0.93,
                        "1": 2.96
                    },
                    "mean": {
                        "open": 5.14,
                        "close": 6.01
                    },
                    "99%percentile": {
                        "open": 5.64,
                        "close": 6.62
                        }
                    }
                ],
                timeData:[],
                resourceData:[],
                passed:[],
                distance:{
                    Intro:'测试使用rtk作为真值，通过本车以及目标高精度GPS定位数据，转换成本车坐标系下的测距结果。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其测距误差',
                    title:'测试指标:',
                },
                angle:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据可获得目标相对本车运动朝向数据，作为本测试项真值，通过时间戳将真值与相机检测数据进行匹配。对比量化目标朝向检测检测效果。',
                    title:'测试指标:',
                },
                relative_velocity:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据,转换成本车坐标系下的测距结果。根据距离随时间变化计算基于本车坐标系下的横纵向相对速度作为真值。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其相对速度误差。',
                    title:'测试指标:',
                },
                performance_Intro:[
                    {
                        title:'一、日志分析:',
                        Intro:[{
                           name:'应用程序将内部各模块每帧图像处理耗时记录在日志文件中，测试过程分析每次测试log文件即可获得每模块每帧耗时占用。同时日志文件中也记录了实时帧率计算结果。测试程序将每帧数据解析并分析。',
                        }]
                    },
                    {
                        title:'二、系统工具以及命令:',
                        Intro:[{
                           name:'应用程序运行在LINUX操作系统上，其资源占用部分可通过系统命令查看，如top命令可参考应用程序占用的CPU和内存情况。同时NVIDIA平台提供tegrastatus工具可查看设备当前GPU占用。测试程序在跑视频之前开启线程运行监控程序, 实时抓取CPU, 内存和GPU等信息。',
                        }]
                    },
                    {
                        title:'三、数据统计说明:',
                        Intro:[{
                                name:'基于每帧的模块耗时T=[t0,t1...tn]以及实时帧率F=[f0,f1...fn]等数据。计算各项参数的最大, 最小和平均值以及%p位数。',
                            },
                            {
                                name:'其中%p分位数含义为：统计学术语，如果将一组数据从小到大排序，并计算相应的累计百分位，则某一百分位所对应数据的值就称为这一百分位的百分位数。可表示为：一组n个观测值按数值大小排列。如，处于p%位置的值称第p百分位数。',
                            }
                        ]
                    }
                ],
                lane_Intro:{
                    name:'测试使用RTK构建高精度地图作为真值，通过本车GPS定位数据，转换成本车坐标系下的车道线测距结果。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其测距误差。',
                    title:'评测指标：',
                },
                test_title:"测试方法",
                activeName:0,
                labelPosition:'top',
                totalData:[],
                infoData:[
                    {
                        index:1,
                        src:require("../../assets/images/icon/information_icon_1.png"),
                        title:'程序',
                    }, {
                        index:2,
                        src:require("../../assets/images/icon/information_icon_2.png"),
                        title:'版本号',
                    },{
                        index:3,
                        src:require("../../assets/images/icon/information_icon_3.png"),
                        title:'测试平台',
                    },{
                        index:4,
                        src:require("../../assets/images/icon/information_icon_4.png"),
                        title:'开始时间',
                    },{
                        index:5,
                        src:require("../../assets/images/icon/information_icon_5.png"),
                        title:'结束时间',
                    },{
                        index:6,
                        src:require("../../assets/images/icon/information_icon_6.png") ,
                        title:'时长',
                    }
                ],
                testCaseData:[],
                test_Data:[],
                passData:[],
                firstTitle:'概况',
                secondTitle:'OD测距',
                thirdTitle:'OD朝向',
                forthTitle:'OD相对速度',
                totalTitle:'基本信息',
                totalTitle1:'测试用例通过率总览',
                totalTitle2:'通过率总览',
                totalTitle3:'版本通过率对比',  
                accuracyData:null,
                distanceTitle1:'测试用例',
                distanceTitle2:'目标类型分组',
                distanceTitle3:'场景分组',
                distanceTitle4:'精度统计',
                addData:'1',
                broad:'横向测距',
                vertical:'纵向测距',
                program:null,
                program_version:null,
                caseData:[],
                position:null,
                fpsPosition:null,
                cameraPosition:null,
                modePosition:null,
                sourceCameraPosition:null,
                sourceModePosition:null,
                timeCameraPosition:null,
                spanArr:[],
                fpsSpanArr:[],
                cameraArr:[],
                timeCameraArr:[],
                sourceCameraArr:[],
                modeArr:[],
                sourceModeArr:[],
                endflag:false,
                fpsShow:false,
                timeShow:false,
                resourceShow:false,
                testChartData:[],
                tes:[
                    {
                        "99%percentile": 10.0974, 
                        "max": 10.8833, 
                        "mean": 9.998678971962617, 
                        "min": 7.9869, 
                        "name": "７相机",
                        "run_mode": '1(说明：开启或关闭录制)',
                    }
                ]
            }
        },
        components: {headTitle,cardTitle},
        mounted(){
            if(this.$route.params.stage=='all'){
                    this.$route.params.stage=0
                }
            this.initData();
            this.getTestItem();
            this.getFps();
            this.getTime();
            this.getResource();
        },

        methods:{
            initData(){
                getBase({program:this.$route.params.program,version:this.$route.params.version,stage:this.$route.params.stage=='all'?'0':this.$route.params.stage})
                .then(res=>{
                        // <el-table-column prop="program" label="程序"  min-width="80" align="center"></el-table-column>
                        //     <el-table-column prop="version" label="版本号" min-width="150" align="center"></el-table-column>
                        //     <el-table-column prop="test_platform" label="测试平台" min-width="100" align="center" ></el-table-column>
                        //     <el-table-column prop="test_start_time" label="开始时间" align="center" min-width="100"></el-table-column>
                        //     <el-table-column prop="test_end_time" label="结束时间" align="center" min-width="100"> </el-table-column>
                        //     <el-table-column prop="test_duration" label="时长" align="center" min-width="100"> </el-table-column>
                    this.infoData[0].data =  res.data.program;
                    this.infoData[1].data =  res.data.version;
                    this.infoData[2].data =  this.transformTime.transformDate(res.data.test_start_time);
                    this.infoData[3].data =  this.transformTime.transformDate(res.data.test_end_time);
                    this.infoData[4].data =  this.transformTime.transformDate(res.data.test_end_time);
                    this.infoData[5].data =  this.transformTime.transformSecond(res.data.test_duration);

                    this.totalData =[];
                    var item = {};
                    item.test_platform  = res.data.test_platform;
                    item.test_code_version  = res.data.test_code_version;
                    item.test_start_time  =this.transformTime.transformDate(res.data.test_start_time);
                    item.test_end_time  = this.transformTime.transformDate(res.data.test_end_time);
                    item.test_duration =  this.transformTime.transformSecond(res.data.test_duration);
                    item.program  = res.data.program;
                    this.program  = res.data.program;
                    item.version  = res.data.version;
                    this.program_version =  res.data.version;
                    this.totalData.push(item);
                })
            },
           async getTime(){
               await getPerformanceItems({program:this.$route.params.program,version:this.$route.params.version,stage:this.$route.params.stage=='all'?'0':this.$route.params.stage,item:'run_time'})
                  .then(res=>{
                    this.timeData = [];
                    res.data.forEach(item=>{
                        this.timeData.push(item);
                        this.timeShow = true;
                    })
                   this.timeRowspan(this.timeData)
                })
            },
            async  getFps(){
                await getPerformanceItems({program:this.$route.params.program,version:this.$route.params.version,stage:this.$route.params.stage=='all'?'0':this.$route.params.stage,item:'fps'})
                .then(res=>{
                    this.fpsData = [];
                    res.data.forEach(item=>{
                        this.fpsData.push(item);
                        this.fpsShow = true;
                    })
                   this.perRowSpan(this.fpsData)
                })
            },
            async  getResource(){ 
                getPerformanceItems({program:this.$route.params.program,version:this.$route.params.version,stage:this.$route.params.stage=='all'?'0':this.$route.params.stage,item:'resource_usage'})
                    .then(res=>{
                        this.resourceData = [];
                        res.data.forEach(item=>{
                            this.resourceData.push(item);
                            this.resourceShow = true;

                        })
                    this.sourceRowSpan(this.resourceData)
                    })
            },
            sourceSpanMethod({ rowIndex, columnIndex }){
                if(columnIndex === 0){ 
                    const _row = this.sourceCameraArr[rowIndex];
                    const _col = _row>0 ? 1 : 0;
                    return {
                        rowspan: _row, //行
                        colspan: _col  //列
                    }
                }
            },
            sourceRowSpan(data){
                this.sourceCameraArr = [];
                this.sourceCameraPosition=0;  
                // this.sourceModeArr=[];
                // this.sourceModePosition = 0;
                data.forEach((item,index) => {
                    if( index === 0){
                        this.sourceCameraArr.push(1);
                        this.sourceCameraPosition=0;
                        // this.sourceModeArr.push(1);
                        // this.sourceModePosition=0;
                    }else{
                        if(data[index].camera_num ===data[index-1].camera_num ){
                            this.sourceCameraArr[this.sourceCameraPosition] += 1;
                            this.sourceCameraArr.push(0); 
                        }else{
                            this.sourceCameraArr.push(1);
                            this.sourceCameraPosition = index;
                        }
                        // if(data[index].name ===data[index-1].name ){
                        //     this.sourceModeArr[this.sourceModePosition] += 1;
                        //     this.sourceModeArr.push(0); 
                        // }else{
                        //     this.sourceModeArr.push(1);
                        //     this.sourceModePosition = index;
                        // }
                    }
                })
                
            },
            timeRowspan(data){
                this.timeCameraArr = [];
                this.timeCameraPosition=0;  
                // this.modeArr=[];
                // this.modePosition = 0;
                data.forEach((item,index) => {
                    if( index === 0){
                        this.timeCameraArr.push(1);
                        this.timeCameraPosition=0;
                        // this.modeArr.push(1);
                        // this.modePosition=0;
                    }else{
                        if(data[index].camera_num ===data[index-1].camera_num ){
                            this.timeCameraArr[this.timeCameraPosition] += 1;
                            this.timeCameraArr.push(0); 
                        }else{
                            this.timeCameraArr.push(1);
                            this.timeCameraPosition = index;
                        }
                        // if(data[index].name ===data[index-1].name ){
                        //     this.modeArr[this.modePosition] += 1;
                        //     this.modeArr.push(0); 
                        // }else{
                        //     this.modeArr.push(1);
                        //     this.modePosition = index;
                        // }
                    }
                })
            },
            timeSpanMethod({ rowIndex, columnIndex }){
                if(columnIndex === 0){ 
                    const _row = this.timeCameraArr[rowIndex];
                    const _col = _row>0 ? 1 : 0;
                    return {
                        rowspan: _row, //行
                        colspan: _col  //列
                    }
                }
            },
            perRowSpan(data){
                this.fpsSpanArr = [];
                this.fpsPosition = 0;
                this.cameraArr = [];
                this.cameraPosition=0; 
                data.forEach((item,index) => {
                    if( index === 0){
                        this.fpsSpanArr.push(1);
                        this.fpsPosition = 0;
                        this.cameraArr.push(1);
                        this.cameraPosition=0;
                    }else{
                        if(data[index].name === data[index-1].name ){
                            this.fpsSpanArr[this.fpsPosition] += 1;//连续有几行项目名名称相同
                            this.fpsSpanArr.push(0); // 名称相同后往数组里面加一项0
                        }else{
                            this.fpsSpanArr.push(1);
                            this.fpsPosition = index;
                        }
                        if(data[index].camera_num ===data[index-1].camera_num ){
                            this.cameraArr[this.cameraPosition] += 1;//连续有几行项目名名称相同
                            this.cameraArr.push(0); //
                        }else{
                            this.cameraArr.push(1);
                            this.cameraPosition = index;
                        }
                        // if(data[index].run_mode ===data[index-1].run_mode ){
                        //     this.modeArr[this.modePosition] += 1;//连续有几行项目名名称相同
                        //     this.modeArr.push(0); //
                        // }else{
                        //     this.modeArr.push(1);
                        //     this.modePosition = index;
                        // }
                    }
                })
            },
            perSpanMethod({ rowIndex, columnIndex }){
                if(columnIndex === 0){  //序号列也进行合并(第一列)
                    //this.spanArr这个数组里面存的是table里面连续的有几条数据相同
                    //例如:[1,1,2,0,2,0]
                    //1  代表的没有连续的相同的
                    //2  代表连续的两个相同
                    //0  代表是和上一条内容相同
                    const _row = this.fpsSpanArr[rowIndex];
                    const _col = _row>0 ? 1 : 0;
                    return {
                        rowspan: _row, //行
                        colspan: _col  //列
                    }

                }else if(columnIndex ===1 ){
                    const _row = this.cameraArr[rowIndex];
                    const _col = _row>0 ? 1 : 0;
                    return {
                        rowspan: _row, //行
                        colspan: _col  //列
                    }
                }
            },
            rowspan() {
                this.spanArr = [];
                this.position = 0; 
                this.testCaseData.forEach((item,index) => {
                if( index === 0){
                    this.spanArr.push(1);
                    this.position = 0;
                }else{
                    if(this.testCaseData[index].name === this.testCaseData[index-1].name ){
                        this.spanArr[this.position] += 1;//连续有几行项目名名称相同
                        this.spanArr.push(0); // 名称相同后往数组里面加一项0
                    }else{
                        this.spanArr.push(1);
                        this.position = index;
                    }
                }
                })
            },
            objectSpanMethod({ rowIndex, columnIndex }) {  //表格合并行
                if(columnIndex === 0){  //序号列也进行合并(第一列)
                //this.spanArr这个数组里面存的是table里面连续的有几条数据相同
                //例如:[1,1,2,0,2,0]
                //1  代表的没有连续的相同的
                //2  代表连续的两个相同
                //0  代表是和上一条内容相同
                const _row = this.spanArr[rowIndex];
                const _col = _row>0 ? 1 : 0;
                return {
                    rowspan: _row, //行
                    colspan: _col  //列
                }

                }
            },
            openExport(){
                const {href} = this.$router.resolve({
                    name: 'report',
                    query:{"program":this.$route.params.program,"version":this.$route.params.version,"stage":this.$route.params.stage=='0'?'all':this.$route.params.stage},
                    
                });
                window.open(href, '_blank')
            },
            showCase(row){
                var url ="http://192.168.199.195/vision-test/allure/" + this.program +'/'+ this.program_version +'/'+ (this.$route.params.stage=='all'?'0':this.$route.params.stage) +'/allure-report/#behaviors' + row.case_url;
                window.open(url,'_blank');
            },
            seeMore(){
                var url = 'http://192.168.199.195/vision-test/allure/'+this.program + '/'+ this.program_version +'/'+ (this.$route.params.stage=='all'?'0':this.$route.params.stage) +'/allure-report/';
                window.open(url,'_blank');
            } ,  
            
            testpromise(value){
                return new Promise((resolve)=>{
                     resolve(
                        getAccuracy(value)
                            .then(res=>{
                                if(res.data){
                                    return res.data
                                }
                            })
                        );
                });
            },
    
            getTestItem(){
                this.endflag = false;
                var that = this;
                     getItems({program:that.$route.params.program,version:that.$route.params.version,stage:that.$route.params.stage=='all'?'0':that.$route.params.stage})
                        .then(res=>{
                            that.passData=[];
                            res.data.forEach(item => {
                                item.children.forEach(child=>{
                                this.testpromise({program:that.$route.params.program,version:that.$route.params.version,stage:that.$route.params.stage=='all'?'0':that.$route.params.stage,item:item.name=='performance'?item.name:item.name+'_'+child.name&&item.name=='lane'?item.name:item.name+'_'+child.name&&item.name=='functional'?item.name:item.name+'_'+child.name})
                                    .then(function (obj) {
                                        child.accuracy = obj;
                                        that.endflag = true;
                                        that.passData=res.data             
                                        that.$store.commit('user/SET_TESTDATA',res.data);                            
                                        setTestData(JSON.stringify(res.data));
                                            getSuites({program:that.$route.params.program,version:that.$route.params.version,stage:that.$route.params.stage=='all'?'0':that.$route.params.stage,item:item.name=='performance'?item.name:item.name+'_'+child.name&&item.name=='lane'?item.name:item.name+'_'+child.name&&item.name=='functional'?item.name:item.name+'_'+child.name})
                                                .then(res=>{
                                                    var j = item.children.indexOf(child);
                                                    if(res.data){
                                                        that.initCaseChart(item,child,j);
                                                        if(item.name!='performance'){
                                                            that.initSuiteChart(item,child,j,res.data);
                                                        }
                                                    }
                                                })
                                                if(item.name!='performance' && item.name!='functional'){
                                                     getFeatures({program:that.$route.params.program,version:that.$route.params.version,stage:that.$route.params.stage=='all'?'0':that.$route.params.stage,item:item.name=='lane'?item.name:item.name+'_'+child.name})
                                                        .then(res=>{
                                                            var childIndex = item.children.indexOf(child);
                                                            if(res.data){
                                                                that.initFeatureChart(item,child,childIndex,res.data);
                                                            }   
                                                            var accuracy = child.accuracy;
                                                            for(var k=0;k < accuracy.length; k++){
                                                                var passed = [];
                                                                var rightPassed = [];
                                                                var rightName = [];
                                                                var name =[];
                                                                var accuracy_data = accuracy[k].data;
                                                                for(var j =0;j < accuracy_data.length;j++){
                                                                    if(accuracy_data[j].title_name.indexOf('横向测距') !=-1&&(accuracy_data[j].title_name.indexOf('范围内') !=-1)){
                                                                        passed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                                                                        name.push(accuracy_data[j].range)
                                                                        that.$store.commit('user/SET_NAME',name);                            
                                                                        setName(JSON.stringify(name));
                                                                        that.initLeftCuracy(item,child,accuracy[k],k,passed,name);
                                                                    }
                                                                    if(accuracy_data[j].title_name.indexOf('纵向测距') !=-1&&(accuracy_data[j].title_name.indexOf('阈值') !=-1)){
                                                                        rightPassed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                                                                        rightName.push(accuracy_data[j].range)
                                                                        that.initRightCuracy(item,child,accuracy[k],k,rightPassed,rightName);
                                                                    }
                                                                }
                                                            }  
                                                        }) 
                                                }else{
                                                    getFeatures({program:that.$route.params.program,version:that.$route.params.version,stage:that.$route.params.stage=='all'?'0':that.$route.params.stage,item:item.name})
                                                        .then(res=>{
                                                            var childIndex = item.children.indexOf(child);
                                                            if(res.data){
                                                                that.initFeatureChart(item,child,childIndex,res.data);
                                                            }       
                                                        }) 
                                                }
                                    })
                                    child.accuracy=[];
                                    const tableData={};
                                    tableData.name = item.name;
                                    tableData.broken= child.broken;
                                    tableData.failed= child.failed;
                                    tableData.passed= child.passed;
                                    tableData.total= child.total;
                                    if(item.name == 'performance' || item.name =='functional' || item.name =='lane'){
                                        tableData.child_item= ''
                                    }else{
                                        tableData.child_item= child.name;
                                    }
                                    that.testCaseData.push(tableData)
                                    const chartData={};
                                    if(item.name=='performance'){
                                        chartData.test_item = child.name;
                                    }else if(item.name=='functional' ||item.name=='lane'){
                                        chartData.test_item = item.name;
                                    }else{
                                        chartData.test_item = item.name+'_'+ child.name;
                                    }
                                    chartData.broken= child.broken;
                                    chartData.failed= child.failed;
                                    chartData.passed= child.passed;
                                    chartData.total= child.total;
                                    that.testChartData.push(chartData)
                            })
                    this.rowspan()                    
                    this.initChart();
             
                    })
                })

            },

            deepClone(obj) {
                let newObj = Array.isArray(obj) ? [] : {};
                if (obj && typeof obj === "object") {
                    for (let key in obj) {
                        if (obj.hasOwnProperty(key)) {
                            newObj[key] = (obj && typeof obj[key] === 'object') ? this.deepClone(obj[key]) : obj[key];
                        }
                    }
                }
                return newObj
            },
            initChart(){
                var yName =[];
                var passed = [];
                var failed =[];
                var broken = [];
                var total;
                for(var i =0;i< this.testChartData.length;i++){
                    yName.push( this.testChartData[i].test_item);
                    total =  this.testChartData[i].passed+ this.testChartData[i].failed+ this.testChartData[i].broken;
                    passed.push(( this.testChartData[i].passed/total).toFixed(2));
                    failed.push(( this.testChartData[i].failed/total).toFixed(2)) ;                   
                    broken.push(( this.testChartData[i].broken/total).toFixed(2));
                }
                this.myChart = echarts.init(document.getElementById('passEcharts')); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                       legend: {
                            top: '6%',
                            right:'3.5%',
                            itemWidth: 12,
                            itemHeight: 12,
                            textStyle: {
                                color: '#505050',
                                    fontSize:14,
                                    "padding": [3, 6],

                            },
                            data: [ 'passed', 'failed', 'broken', ]
                        },
                        grid: {
                            left: '5%',
                            right: '4%',
                            bottom: '0%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: yName,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    },
                                    interval:0,//横轴信息全部显示  
                                    rotate:10,

                                },
                                splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }
                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                        color:'rgba(220,224,232,0.8)',
                                    }
                                   
                                }
                            }
                        ],
                        series: [  
                            {
                                name: "passed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '26%',
                                "itemStyle": {

                                    "normal": {
                                       color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                            offset: 0,
                                            color: '#2AC26A'
                                        }, {
                                            offset: 1,
                                            color: '#56EE97'
                                        }]),
                                        shadowColor: '#56EE97',
                                        shadowBlur: 4,
                                        "label": {
                                            "show": true,
                                            "textStyle": {
                                                "color": "#fff",                                
                                                "fontSize":"80%",
                                                "fontWeight":'bold',
                                            },
                                            // "position": "inside",
                                            formatter: function(p) {
                                                return p.value > 0 ? (p.value) : '';
                                            }
                                        }
                                    }
                                },

                                data: passed
                            },
                              {
                                name:"failed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '26%',
                                "itemStyle": {
                                "normal": {
                                    color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                        offset: 0,
                                        color: '#FF7B80'
                                    }, {
                                        offset: 1,
                                        color: '#EB5151'
                                    }]),
                                    shadowColor: '#EB5151',
                                    shadowBlur: 4,
                                    "label": {
                                        "show": true,
                                        "textStyle": {
                                            "color": "#fff",
                                            "fontSize":"80%",
                                            "fontWeight":'bold',
                                        },
                                        "position": "inside",
                                        formatter: function(p) {
                                            return p.value > 0 ? (p.value) : '';
                                        }
                                    }
                                }
                            },
                                data: failed
                            }, {
                                name: "broken",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '26%',
                                "itemStyle": {
                                    "normal": {
                                        shadowColor: '#FFA100',
                                        shadowBlur: 4,
                                        color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                            offset: 0,
                                            color: '#FFDB77'
                                        }, {
                                            offset: 1,
                                            color: '#FFA100'
                                        }]),
                                        "label": {
                                            "show": true,
                                            "textStyle": {
                                                "color": "#fff",
                                                "fontSize":"80%",
                                                "fontWeight":'bold',

                                            },
                                            "position": "inside",
                                            formatter: function(p) {
                                                return p.value > 0 ? (p.value) : '';
                                            }
                                        }
                                    }
                                },
                                data: broken
                            },
                        ]
                };
                this.myChart.setOption(this.optionmyChart);
            },

            initCaseChart(item,childItem,childIndex){
                this.myChart = echarts.init(document.getElementById("_d"+'_'+item.name+'_'+childItem.name+'_'+childIndex)); 
                this.optionmyChart = {
                    title: {
                        text: childItem.total,
                        subtext: 'test cases',
                        x: 'center',
                        y: 'center',
                        textStyle: {
                            fontSize:40,
                            fontWeight:'bold',
                            color: ['#505050'],
                            align: 'center',

                        },
                        subtextStyle: {
                            color: '#505050',
                            // fontSize: 22
                        },
                    },
                    // grid: {
                    //     top: '40%',
                    //     left: '50%',
                    //     right: '10%'
                    // },
                    legend: {
                        orient: 'vertical',
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                             "padding": [0, 0],

                            fontSize:14
                        },
                            // padding:[0,10],
                    },
                    series: [
                        {
                            name: '',
                            type: 'pie',
                            radius: ['48%', '58%'],
                            // color: ["#47E389", "#FF6E6E", "#FFD577"],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {

                                        "formatter": "{per|{c}\n} {b|{b}} ",
                                        "borderColor": "transparent",
                                        "borderRadius": 4,
                                        "rich": {
                                            "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                            },
                                            "hr": {
                                                "borderColor": "#aaa",
                                                "width": "100%",
                                                "borderWidth": 1,
                                                "height": 0
                                            },
                                            "b": {
                                                "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                                
                                            },
                                            "c": {
                                                "fontSize": 14,
                                                "color": "#b3e5ff"
                                            },
                                            "per": {
                                                "color": "#505050",
                                                "fontSize": 22,
                                                "padding": [3, 2],
                                                "fontWeight":'bold',
                                                "borderRadius": 2
                                            }
                                        },
                                        "textStyle": {
                                            "color": "#fff",
                                            "fontSize": 16
                                        }
                                    },
                                },
                                emphasis: {
                                    "label": {
                                    "show": true,
                                    "formatter": "{per|{c}\n} {b|{b}}",
                                    "backgroundColor": "rgba(255, 147, 38, 0)",
                                    "borderColor": "transparent",
                                    "borderRadius": 4,
                                    "rich": {
                                          "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                        },
                                        "hr": {
                                            "borderColor": "#aaa",
                                            "width": "100%",
                                            "borderWidth": 1,
                                            "height": 0
                                        },
                                        "b": {
                                            "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                            
                                        },
                                        "c": {
                                            "fontSize": 14,
                                            "color": "#b3e5ff"
                                            },
                                        "per": {
                                            "color": "#505050",
                                            "fontSize": 22,
                                            "fontWeight":'bold',
                                            "padding": [3, 2],
                                            "borderRadius": 2
                                        }
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    length: 28,
                                    length2: 36

                                }
                            },
                            data: [
                                {   
                                    value:childItem.passed, 
                                    name: 'passed',
                                     itemStyle: {
                                        shadowColor: '#56EE97',
                                        shadowBlur: 4,
                                        color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                            offset: 0,
                                            color: '#2AC26A'
                                        }, {
                                            offset: 1,
                                            color: '#56EE97'
                                        }])
                                    },
                                },
                                {
                                    value:childItem.failed, 
                                    name: 'failed',
                                          itemStyle: {
                                        shadowColor: '#EB5151',
                                        shadowBlur: 4,
                                        color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                            offset: 0,
                                            color: '#FF7B80'
                                        }, {
                                            offset: 1,
                                            color: '#EB5151'
                                        }])
                                    },
                                },
                                {   value:childItem.broken, 
                                    name: 'broken',
                                          itemStyle: {
                                        shadowColor: '#FFA100',
                                        shadowBlur: 4,
                                        color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                            offset: 0,
                                            color: '#FFDB77'
                                        }, {
                                            offset: 1,
                                            color: '#FFA100'
                                        }])
                                    },
                                },
                           
                            ]
                        }
                    ]};
                    this.myChart.setOption(this.optionmyChart);
                },

            initSuiteChart(item,childItem,childIndex,data){
                var suite = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<data.suites.length;i++){
                    suite.push(data.suites[i].suite);
                    passed.push(data.suites[i].passed);
                    failed.push(data.suites[i].failed);
                    broken.push(data.suites[i].broken);
                } 
                this.myChart = echarts.init(document.getElementById('_s'+'_'+item.name+'_'+childItem.name+'_'+childIndex)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                            fontSize:14,
                            "padding": [3, 6],
                        },
                    },
                    grid: {
                        left: '3%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        axisLabel: {
                            show: false,
                        },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },
                        splitLine: {
                            show: false
                        },
                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        splitLine: {
                            show: false
                        },
                        type: 'category',
                        data: suite,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 45,
                            textStyle: {
                                // fontSize: '16'
                            }
                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            shadowColor: '#56EE97',
                            shadowBlur: 4,
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: '#2AC26A'
                            }, {
                                offset: 1,
                                color: '#56EE97'
                            }]),
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                    "fontWeight":'bold',
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            shadowColor: '#EB5151',
                            shadowBlur: 4,
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: '#FF7B80'
                            }, {
                                offset: 1,
                                color: '#EB5151'
                            }]),
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                    "fontWeight":'bold',
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            shadowColor: '#FFA100',
                            shadowBlur: 4,
                             color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: '#FFDB77'
                            }, {
                                offset: 1,
                                color: '#FFA100'
                            }]),
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                    "fontWeight":'bold',
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                    ]
                };
                this.myChart.setOption(this.optionmyChart);
         
            },
            initFeatureChart(item,childItem,childIndex,data){
                var feature = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<data.features.length;i++){
                    feature.push(data.features[i].feature);
                    passed.push(data.features[i].passed);
                    failed.push(data.features[i].failed);
                    broken.push(data.features[i].broken);
                }
                this.myChart = echarts.init(document.getElementById('_f'+'_'+item.name+'_'+childItem.name+'_'+childIndex)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                            "padding": [3, 6],
                            fontSize:14,
                        },
                    },
                    grid: {
                        // top:'13%',
                        left: '4%',
                        right: '1%',
                        bottom: '1%',
                        containLabel: true
                    },
                    xAxis: {
                        axisLabel: {
                            show: false,
                        },
                        splitLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },
                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        splitLine: {
                            show: false
                        },
                          axisTick:{
                            show:false
                        },
                        type: 'category',
                        data: feature,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 40,
                            // textStyle: {
                            //     fontSize: '16',
                            // },
                            interval:0,//横轴信息全部显示  

                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: '#2AC26A'
                            }, {
                                offset: 1,
                                color: '#56EE97'
                            }]),
                            shadowColor: '#56EE97',
                            shadowBlur: 4,
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                    offset: 0,
                                    color: '#FF7B80'
                                }, {
                                    offset: 1,
                                    color: '#EB5151'
                                }]),
                            shadowColor: '#EB5151',
                            shadowBlur: 4,
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: '#FFDB77'
                            }, {
                                offset: 1,
                                color: '#FFA100'
                            }]),
                            shadowColor: '#FFA100',
                            shadowBlur: 4,
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                     "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                    ],
                };
                this.myChart.setOption(this.optionmyChart);
            },
            initLeftCuracy(item,child,accuracy_item,index,passed,name){
                const CubeLeft = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const xAxisPoint = shape.xAxisPoint
                        const c0 = [shape.x, shape.y]
                        const c1 = [shape.x - 9, shape.y - 9]
                        const c2 = [xAxisPoint[0] - 9, xAxisPoint[1] - 9]
                        const c3 = [xAxisPoint[0], xAxisPoint[1]]
                        ctx.moveTo(c0[0], c0[1]).lineTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).closePath()
                    }
                })
                const CubeRight = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const xAxisPoint = shape.xAxisPoint
                        const c1 = [shape.x, shape.y]
                        const c2 = [xAxisPoint[0], xAxisPoint[1]]
                        const c3 = [xAxisPoint[0] + 18, xAxisPoint[1] - 9]
                        const c4 = [shape.x + 18, shape.y - 9]
                        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
                    }
                })
                const CubeTop = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const c1 = [shape.x, shape.y]
                        const c2 = [shape.x + 18, shape.y - 9]
                        const c3 = [shape.x + 9, shape.y - 18]
                        const c4 = [shape.x - 9, shape.y - 9]
                        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
                    }
                })
                echarts.graphic.registerShape('CubeLeft', CubeLeft)
                echarts.graphic.registerShape('CubeRight', CubeRight)
                echarts.graphic.registerShape('CubeTop', CubeTop)
                            // if(test.length == 1){
                //      var range = ((test[0].range).substr(1)).substr(0,(test[0].range).substr(1).length-1);

                //     range.split(',')
                //     console.log(range)
                // }else{
                    // for(var k=0;k<test.length;k++){
                    //  var r2 = ((test[k].range).substr(1)).substr(0,(test[k].range).substr(1).length-1);
                    //     name.push(r2.substring(r2.indexOf(','),r2))
                    //     if(k== test.length-1){
                    //          name.push(r2.substring(r2.indexOf(',')+1,r2.length))
                    //     }
                    // }
                    // console.log(name)
                // }
                this.myChart = echarts.init(document.getElementById('accuracy-broad'+index+'_'+item.name+'_'+child.name)); 
                this.optionmyChart = {
                            "grid": {
                                "top": "2%",
                                "left": "1%",
                                "bottom": "13%",
                                "right": "0%",
                                "containLabel": true
                            },
                            tooltip: {
                                trigger: 'axis',
                                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                    type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                                },  
                                textStyle: {
                                    color: "#fff"
                                }
                            },
                            // tooltip:{
                            //     show:true 
                            // },
                            animation: true,
                            xAxis: {
                                type: 'category',
                                data:name,
                                axisLine: {
                                    show:false
                                },
                                offset: 20,
                                axisTick: {
                                    show: false,
                                },
                                axisLabel: {
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,
                                }
                            },
                            yAxis: {
                                type: 'value',
                                axisLine: {
                                    show: true,
                                    lineStyle: {
                                        color: 'white'
                                    }
                                },
                                splitLine: {
                                  lineStyle:{
                                        color:'rgba(220,224,232,0.8)',
                                        type:'dashed',
                                    }
                                },
                                axisTick: {
                                    show: false
                                },
                                axisLabel: {
                                    color:'#333'
                                },
                                boundaryGap: ['20%', '20%']
                            },
                            series: [{
                                type: 'custom',
                                name: "passed",
                           
                                renderItem: (params, api) => {
                                    const location = api.coord([api.value(0), api.value(1)])
                                    return {
                                        type: 'group',
                                        children: [{
                                            type: 'CubeLeft',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                       color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            }
                                        }, {
                                            type: 'CubeRight',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                        color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            }
                                        }, {
                                            type: 'CubeTop',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                                    {
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                        color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            }
                                        }]
                                    }
                                },
                                data: passed
                            },{
                                type: 'bar',
                                label: {
                                    normal: {
                                        show: true,
                                        position: 'top',
                                        color: 'rgba(86,115,255,1)',
                                        offset: [4, -14]
                                    }
                                },
                                itemStyle: {
                                    color: 'transparent'
                                },
                                tooltip: {
                                        show: false,

                                },
                                data: passed
                            }
                            ]
                        // tooltip: {
                        //     trigger: 'axis',
                        //     axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        //         type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        //     },  
                        //     textStyle: {
                        //         color: "#fff"
                        //     }
                        // },
                        // grid: {
                        //     top:'3%',
                        //     left: '4%',
                        //     right: '4%',
                        //     bottom: '12%',
                        //     containLabel: true
                        // },
                        // xAxis: [
                        //     {
                        //         type: 'category',
                        //         data: name,
                        //          axisTick:{
                        //             show:false
                        //         },
                        //         axisLine:{
                        //             show:false
                        //         },
                        //         axisLabel: {
                        //             // align: 'right',

                        //             // interval: 0,
                        //             // rotate: 40,
                        //             textStyle: {
                        //                 // fontSize: '14'
                        //             }, 
                        //             color:'#333',
                        //             interval:0,//横轴信息全部显示  
                        //             rotate:0,

                        //         },
                        //            splitLine: {
                        //             show: false
                        //         },
                        //     }
                        // ],
                        // yAxis: [
                        //     {
                        //         type: 'value',
                        //         axisLabel: {

                        //             textStyle: {
                        //             },
                        //             color:'#333',

                        //         },
                              
                        //         axisLine:{
                        //             show:false
                        //         },
                        //         axisTick:{
                        //             show:false
                        //         },
                        //         splitLine:{
                        //             lineStyle:{
                        //                 type:'dashed',
                        //             }
                                   
                        //         }
                        //     }
                        // ],
                        // series: [
                            
                        //     {
                        //         name: "passed",
                        //         type: 'bar',
                        //         "barMaxWidth": '42%',
                        //          barGap:'-100%',
                        //             "itemStyle": {
                        //                 "normal": {

                        //                     'borderColor':'#B2E4FA',
                        //                     "color": "#DEF5FF",
                        //                     "label": {
                        //                         "show": true,
                        //                         "textStyle": {
                        //                             "color": "#333",                                
                        //                             "fontSize":"80%",

                        //                         },
                        //                         formatter: function(p) {
                        //                             return p.value > 0 ? (p.value) : '';
                        //                         }
                        //                     }
                        //                 }
                        //             },
                        //         data: passed
                        //     },
                             
                        // ]
                };
                this.myChart.setOption(this.optionmyChart);
            },
            initRightCuracy(item,child,accuracy_item,index,passed,name){
                const CubeLeft = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const xAxisPoint = shape.xAxisPoint
                        const c0 = [shape.x, shape.y]
                        const c1 = [shape.x - 9, shape.y - 9]
                        const c2 = [xAxisPoint[0] - 9, xAxisPoint[1] - 9]
                        const c3 = [xAxisPoint[0], xAxisPoint[1]]
                        ctx.moveTo(c0[0], c0[1]).lineTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).closePath()
                    }
                })
                const CubeRight = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const xAxisPoint = shape.xAxisPoint
                        const c1 = [shape.x, shape.y]
                        const c2 = [xAxisPoint[0], xAxisPoint[1]]
                        const c3 = [xAxisPoint[0] + 18, xAxisPoint[1] - 9]
                        const c4 = [shape.x + 18, shape.y - 9]
                        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
                    }
                })
                const CubeTop = echarts.graphic.extendShape({
                    shape: {
                        x: 0,
                        y: 0
                    },
                    buildPath: function(ctx, shape) {
                        const c1 = [shape.x, shape.y]
                        const c2 = [shape.x + 18, shape.y - 9]
                        const c3 = [shape.x + 9, shape.y - 18]
                        const c4 = [shape.x - 9, shape.y - 9]
                        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
                    }
                })
                echarts.graphic.registerShape('CubeLeft', CubeLeft)
                echarts.graphic.registerShape('CubeRight', CubeRight)
                echarts.graphic.registerShape('CubeTop', CubeTop)
                this.myChart = echarts.init(document.getElementById('accuracy-vertical'+index+'_'+item.name+'_'+child.name)); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                    //    legend: {
                    //         // y: '4%',
                    //         top: '0%',
                    //         right:'0%',
                    //         itemWidth: 12,
                    //         itemHeight: 12,
                    //         textStyle: {
                    //             color: '#505050',
                    //                 fontSize:14,
                    //                 "padding": [3, 6],

                    //         },
                    //         // padding:[0,10],
                    //         data: [ 'passed', 'failed', 'broken', ]
                    //     },
                            "grid": {
                                top:'3%',
                                left: '10%',
                                right: '2%',
                                bottom: '10%',
                                containLabel: true
                            },
                            animation: true,
                            xAxis: {
                                type: 'category',
                                data:name,
                                axisLine: {
                                    show:false
                                },
                                offset: 20,
                                axisTick: {
                                    show: false,
                                },
                                axisLabel: {
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,
                                }
                            },
                            yAxis: {
                                type: 'value',
                                axisLine: {
                                    show: true,
                                    lineStyle: {
                                        color: 'white'
                                    }
                                },
                                splitLine: {
                                  lineStyle:{
                                        type:'dashed',
                                        color:'rgba(220,224,232,0.8)',
                                    }
                                },
                                axisTick: {
                                    show: false
                                },
                                axisLabel: {
                                    color:'#333'
                                },
                                boundaryGap: ['20%', '20%']
                            },
                            series: [{
                                type: 'custom',
                                name: "passed",
                                renderItem: (params, api) => {
                                    const location = api.coord([api.value(0), api.value(1)])
                                    return {
                                        type: 'group',
                                        children: [{
                                            type: 'CubeLeft',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                       color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            },
                            
                                        }, {
                                            type: 'CubeRight',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                        color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            }
                                        }, {
                                            type: 'CubeTop',
                                            shape: {
                                                api,
                                                xValue: api.value(0),
                                                yValue: api.value(1),
                                                x: location[0],
                                                y: location[1],
                                                xAxisPoint: api.coord([api.value(0), 0])
                                            },
                                            style: {
                                                fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                                    {
                                                        offset: 0,
                                                        color: 'rgba(86,115,255,0.8)'
                                                    },
                                                    {
                                                        offset: 1,
                                                        color: 'rgba(86,115,255,0.1)'
                                                    }
                                                ])
                                            }
                                        }]
                                    }
                                },
                                data: passed
                            },{
                                type: 'bar',
                                label: {
                                    normal: {
                                        show: true,
                                        position: 'top',
                                        color: 'rgba(86,115,255,1)',
                                        offset: [4, -14]
                                    }
                                },
                                itemStyle: {
                                    color: 'transparent'
                                },
                                tooltip: {
                                    show: false,
                                },
                                data: passed
                            }
                        ]
                        // grid: {
                        //     top:'3%',
                        //     left: '12%',
                        //     right: '2%',
                        //     bottom: '0%',
                        //     containLabel: true
                        // },
                        // xAxis: [
                        //     {
                        //         type: 'category',
                        //         data: name,
                        //          axisTick:{
                        //             show:false
                        //         },
                        //         axisLine:{
                        //             show:false
                        //         },
                        //         axisLabel: {
                        //                 // offset:[0,30],
                        //             // interval: 0,
                        //             // rotate: 40,
                        //             textStyle: {
                        //                 // fontSize: '14'
                        //             }, 
                        //             color:'#333',
                        //             interval:0,//横轴信息全部显示  
                        //             rotate:0,

                        //         },
                        //            splitLine: {
                        //             show: false
                        //         },
                        //     }
                        // ],
                        // yAxis: [
                        //     {
                        //         type: 'value',
                        //         axisLabel: {
                        //             // interval: 0,
                        //             // rotate: 40,
                        //             textStyle: {
                        //                 // fontSize: '14'
                        //             },
                        //             color:'#333',

                        //         },
                              
                        //         axisLine:{
                        //             show:false
                        //         },
                        //         axisTick:{
                        //             show:false
                        //         },
                        //         splitLine:{
                        //             lineStyle:{
                        //                 type:'dashed',
                        //             }
                                   
                        //         }
                        //     }
                        // ],
                        // series: [
                            
                        //     {
                        //         name: "passed",
                        //         type: 'bar',
                        //         "barMaxWidth": '42%',
                        //             "itemStyle": {
                        //                 "normal": {

                        //                     'borderColor':'#B2E4FA',
                        //                     "color": "#DEF5FF",
                        //                     "label": {
                        //                         "show": true,
                        //                         "textStyle": {
                        //                             "color": "#333",                                
                        //                             "fontSize":"80%",
                        //                             // "fontWeight":'bold',

                        //                         },
                        //                         // "position": "inside",
                        //                         formatter: function(p) {
                        //                             return p.value > 0 ? (p.value) : '';
                        //                         }
                        //                     }
                        //                 }
                        //             },
                        //         data: passed
                        //     },
                             
                        // ]
                };
                this.myChart.setOption(this.optionmyChart);

            },
        },
   
    computed:  {
        ...mapGetters(
            {testData:'testData'},
            {testName:'name'}
        )
    },
    watch:{
        // activeName(value){
            // this.$nextTick(()=> {
                // function resizeEcharts(){
                //     this.$refs[`left_chart_${value}`].forEach(item=>{
                //         var element = item[0];
                //         console.log(element)
                //         echarts. getInstanceByDom(element).resize();
                //     })
                // }
             
                // window.addEventListener("resize",resizeEcharts);

                // this.$refs[`left_chart_${value}`].resize();
                // this.$refs[`right_chart_${value}`].resize()
            // })
        // }
    }
}
  
</script>

<style lang="less">
    @import "../../assets/styles/dash.less";

</style>
























<template>
    <div class="dash-wrapper"  >
        <div class="dash-btn-right">
             <div class="btn-right">
                 <el-button class="view-btn" icon="el-icon-picture"  @click="ExportSavePdf(photoTitle,'jpg')">导出图片</el-button>
                <el-button class="export-btn" icon="el-icon-document" @click="ExportSavePdf(htmlTitle,nowTime)">导出pdf</el-button>
            </div>
        </div>
    <div  class="dash-test-wrapper" id="pdfCentent">
      <div class="dash-first" id="head-top1">
            <div class="head-title-card" id="head-card1">
                <div class="left"> 
                    <p class="head-htitle"> {{firstTitle}}</p>
                </div>
            </div>
            <div class="total-panel">
                <div class="total-top">
                    <el-card class="box-card first-card" shadow="hover">
                    <el-table :data="totalData" >
                            <el-table-column prop="program" label="程序"  min-width="80" align="center"></el-table-column>
                            <el-table-column prop="version" label="版本号" min-width="150" align="center"></el-table-column>
                            <el-table-column prop="test_platform" label="测试平台" min-width="100" align="center" ></el-table-column>
                            <el-table-column prop="test_start_time" label="开始时间" align="center" min-width="100"></el-table-column>
                            <el-table-column prop="test_end_time" label="结束时间" align="center" min-width="100"> </el-table-column>
                            <el-table-column prop="test_duration" label="时长" align="center" min-width="100"> </el-table-column>
                        </el-table>
                    </el-card>
                </div>
                <div class="total-center">
                    <el-card class="box-card center-card" shadow="hover">
                        <div slot="header" class="clearfix">
                            <cardTitle :cardTitle="totalTitle1"></cardTitle>
                        </div>
                        <div class="center-pass-table">
                            <el-table :data="passData" class="pass-table" >
                                <el-table-column  label="测试项" align="left" class-name="type" min-width="150">
                                    <template slot-scope="scope">
                                        {{scope.row.test_item}}
                                        <!-- <span v-if="scope.row.test_item == 'od_distance_use_kl'||scope.row.test_item == 'od_distance_no_kl'"> </span>
                                        <span v-else-if="scope.row.test_item == 'od_angle'">{{'OD朝向'}} </span>
                                        <span v-else-if="scope.row.test_item == 'od_speed_use_kl'">{{'OD相对速度'}} </span> -->
                                    </template>
                                </el-table-column>
                                <el-table-column prop="passed" label="passed" align="center" class-name="pass"></el-table-column>
                                <el-table-column prop="failed" label="failed" align="center" class-name="fail"></el-table-column>
                                <el-table-column prop="broken" label="broken" align="center" class-name="broken"></el-table-column>
                            </el-table>
                        </div>
                    </el-card>
                    <el-card class="box-card center-card pass-e" shadow="hover">
                        <div slot="header" class="clearfix">
                            <cardTitle :cardTitle="totalTitle2"></cardTitle>
                        </div>
                        <div class="center-pass-table " id="pass-right">
                            <div id="passEcharts" class="passEcharts"></div>
                        </div>
                    </el-card>
                </div>
            </div>
        </div>     
        <template v-for="(item,index) in caseData" >
             <div :class="index%2==0 ?'even-dashwrapper':'odd-dashwrapper'"   :key="index+'pass'" id="test_item">
                    <!-- <headTitle  :title="item.test_item"></headTitle> -->
                    <el-card    :id="item.test_item" class="test_item">
                        <div slot="header" class="clearfix">
                            <h3 class="child_header">{{item.test_item}}</h3>
                        </div>
                      <div class="od-distance">
                        <div class="method_panel">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="test_title"></cardTitle>
                                </div>
                                <div class="top-panel">
                                    <ul v-if="item.test_item.indexOf('distance')!=-1" class="method_ul">
                                        <li >
                                            {{distance.Intro}}
                                        </li>
                                        <li>
                                            {{distance.title}}
                                            <div class="error_panel">
                                                <p>纵向相对误差：</p>
                                                <img src="../assets/images/dis_1.png">
                                            </div>
                                            <div class="error_panel">
                                                <p> 纵向相对误差：</p>
                                                <img src="../assets/images/dis_2.png">
                                            </div>
                                        </li>
                                        
                                    </ul>
                                    <ul v-if="item.test_item.indexOf('angle')!=-1" class="method_ul">
                                        <li >
                                            {{angle.Intro}}
                                        </li>
                                        <li>
                                            {{angle.title}}
                                            <div class="error_panel">

                                            <img src="../assets/images/angle_1.png" class="angle_img">
                                                </div>
                                        </li>
                                    </ul> 
                                    <ul v-if="item.test_item.indexOf('relative')!=-1" class="method_ul">
                                            <li >
                                            {{relative_velocity.Intro}}
                                        </li>
                                        <li>
                                            {{relative_velocity.title}}
                                                <div class="error_panel">
                                                <p>纵向误差：</p>
                                                <img src="../assets/images/re_1.png" class="rel_img">
                                            </div>
                                            <div class="error_panel">
                                                <p> 纵向误差：</p>
                                                <img src="../assets/images/re_2.png" class="rel_img">
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-top">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle1"></cardTitle>
                                </div>
                                <div class="top-panel">
                                    <div :id="'_d'+index" class="suites"></div>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-center">
                            <el-card class="box-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle2"></cardTitle>
                                </div>
                                <div class="distance-center-panel">
                                    <div :id="'_s'+index" class="suites"></div>
                                </div>
                            </el-card>
                            <el-card class="box-card right-card" shadow="hover">
                                <div slot="header" class="clearfix">
                                    <cardTitle :cardTitle="distanceTitle3"></cardTitle>
                                </div>
                                <div class="distance-center-panel">
                                    <div :id="'_f'+index" class="suites"></div>
                                </div>
                            </el-card>
                        </div>
                        <div class="distance-bottom" v-if="item.accuracy.length!=0">
                            <el-card class="box-card" shadow="hover">
                                <div class="tab-panel">
                                    <!-- <el-tabs type="card" > -->
                                        
                                        <template v-for="(accuracyItem,accuracyIndex) in item.accuracy">
                                            <!-- <el-tab-pane :label="accuracyItem.class_name" :key="accuracyIndex"> -->
                                            <div class="accuracy_div"  :key="accuracyIndex">
                                            <el-table :data="accuracyItem.data" stripe class="accTable" id="accTable">
                                                <el-table-column :label="accuracyItem.class_name==null||accuracyItem.class_name==undefined?'':accuracyItem.class_name" align="center">
                                                    <el-table-column label="检查项" align="left" min-width="265">
                                                        <template slot-scope="scope">
                                                            {{scope.row.title_name}}
                                                        </template>
                                                    </el-table-column>
                                                    <el-table-column label="测试用例总数" prop="total" align="center"></el-table-column>
                                                    <el-table-column label="Passed" prop="passed" align="center"></el-table-column>
                                                    <el-table-column label="Failed" prop="failed" align="center"></el-table-column>
                                                             <el-table-column label="max_err" prop="max_err" align="center" min-width="80">
                                                                <template slot-scope="scope">
                                                                        <template v-if="scope.row.max_err==0">
                                                                            {{'NA'}}
                                                                        </template> 
                                                                        <template v-else>
                                                                            <template v-if="scope.row.max_err==undefined||scope.row.max_err==null"> 
                                                                                  {{scope.row.max_err}}
                                                                                </template>
                                                                                <template v-else>
                                                                                    {{(scope.row.max_err).toFixed(2)}}
                                                                                </template>
                                                                        </template>
                                                                    </template>
                                                             </el-table-column>
                                                        <el-table-column label="case_name" align="center" min-width="140">
                                                            <template slot-scope="scope">
                                                                <template v-if="scope.row.max_err==0">
                                                                    {{'NA'}}
                                                                </template> 
                                                                <template v-else>
                                                                       <el-button class="showcasebtn" @click="showCase(scope.row)">{{ scope.row.case_name}} </el-button> 
                                                                </template>
                                                            </template>
                                                        </el-table-column>
                                                </el-table-column>
                                            </el-table>
                                            <div class="accuracy-center" v-if=" item.test_item.indexOf('distance') !=-1 " :key="accuracyIndex">
                                                <el-card class="box-card accuracy-card" shadow="hover">
                                                    <div slot="header" class="clearfix">
                                                        <cardTitle :cardTitle="broad"></cardTitle>
                                                    </div>
                                                    <div class="accuracy-pass-table" style="position:relative">
                                                        <div :id="'accuracy-broad'+accuracyIndex+item.test_item" class="passEcharts"></div>
                                                        <img src="../assets/images/car.png" style="height:60px;position:absolute;bottom:-20px;left:46%;transform:rotate(180deg);" >
                                                    </div>
                                                </el-card>
                                                <el-card class="box-card accuracy-card" shadow="hover">
                                                    <div slot="header" class="clearfix">
                                                        <cardTitle :cardTitle="vertical"></cardTitle>
                                                    </div>
                                                    <div class="accuracy-pass-table" style="position:relative">
                                                        <div :id="'accuracy-vertical'+accuracyIndex+item.test_item"  class="passEcharts"></div>
                                                        <img src="../assets/images/car.png" style="height:60px;position:absolute;left:20px;top:30%;transform:rotate(-90deg);" >
                                                    </div>
                                                </el-card>
                                            </div>

                                              </div>
                                            <!-- </el-tab-pane> -->
                                        </template>
                                    <!-- </el-tabs> -->
                                </div>
                            </el-card>
                        </div>
                    </div>
                </el-card>
            </div>  
        </template>  
        </div>   
    </div>
</template>

<script>
    import {setTestData} from '@/utils/auth'
    import { mapGetters } from 'vuex'
    import { getInfo } from "@/api/user";
    // import  headTitle  from "@/components/headTitle" 
    import  cardTitle  from "@/components/cardTitle"

    // import odDirection from "@/views/od-direction/index";
    // import odDistance from "@/views/od-distance/index";
    // import odSpeed from "@/views/od-speed/index";
    var echarts = require('echarts');
    
    export default {
        name: "dashBoard",
        data(){
            return{
                distance:{
                    Intro:'测试使用rtk作为真值，通过本车以及目标高精度GPS定位数据，转换成本车坐标系下的测距结果。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其测距误差',
                    title:'测试指标:',
                },
                angle:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据可获得目标相对本车运动朝向数据，作为本测试项真值，通过时间戳将真值与相机检测数据进行匹配。对比量化目标朝向检测检测效果。',
                    title:'测试指标:',
                },
                relative_velocity:{
                    Intro:'测试使用rtk作为真值，通过计算本车以及目标之间的高精度GPS定位数据,转换成本车坐标系下的测距结果。根据距离随时间变化计算基于本车坐标系下的横纵向相对速度作为真值。rtk数据以及相机检测结果通过时间戳作为匹配。对比真值以及检测结果量化其相对速度误差。',
                    title:'测试指标:',
                },
                test_title:"测试方法",
                activeName:null,
                labelPosition:'top',
                totalData:[],
                passData:[],
                firstTitle:'概况',
                secondTitle:'OD测距',
                thirdTitle:'OD朝向',
                forthTitle:'OD相对速度',
                totalTitle1:'测试用例通过率总览',
                totalTitle2:'通过率总览',
                totalTitle3:'版本通过率对比',  
                accuracyData:null,
                distanceTitle1:'测试用例',
                distanceTitle2:'测试车型分组',
                distanceTitle3:'特性场景分组',
                distanceTitle4:'精度统计',
                addData:'1',
                broad:'横向测距',
                vertical:'纵向测距',
                program:null,
                program_version:null,
                caseData:[],
                htmlTitle:'PDF',
                nowTime:'',
                photoTitle:'jpg',
            }
        },
        components: {cardTitle},
        mounted(){
            this.initData();    
        },
        methods:{
            initData(){
                getInfo({program:this.$route.query.program,version:this.$route.query.version})
                .then(res=>{
                    this.caseData =[];
                    res.data.test_items.forEach(item=>{
                        if(item.test_item!=='performance'){
                            this.caseData.push(item)
                        }
                    })
                    this.passData = res.data.test_items; 
                    this.$store.commit('user/SET_TESTDATA', res.data);                            
                    setTestData(JSON.stringify(res.data));
                    this.totalData =[];
                    var item = {};
                    item.test_platform  = res.data.test_platform;
                    item.test_code_version  = res.data.test_code_version;
                    item.test_start_time  =this.transformTime.transformDate(res.data.test_start_time);
                    item.test_end_time  = this.transformTime.transformDate(res.data.test_end_time);
                    item.test_duration =  this.transformTime.transformSecond(res.data.test_duration);
                    item.program  = res.data.program;
                    this.program  = res.data.program;
                    item.version  = res.data.version;
                    this.program_version =  res.data.version;
                    this.htmlTitle = res.data.program +'_'+ res.data.version;
                    this.photoTitle = res.data.program+'_'+res.data.version;
                    this.totalData.push(item);
                    this.initChart();
                })
            },
          initLeftCuracy(item,accuracy_item,index){
                var passed = [];
                var name =[];
                // var test=[];
                var accuracy_data = accuracy_item.data;
                for(var j =0;j < accuracy_data.length;j++){
                    if(accuracy_data[j].title_name.indexOf('横向测距') !=-1&&(accuracy_data[j].title_name.indexOf('范围内') !=-1)){
                        passed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                        // test.push(accuracy_data[j])
                        name.push(accuracy_data[j].range)
                    }
                }
                // if(test.length == 1){
                //      var range = ((test[0].range).substr(1)).substr(0,(test[0].range).substr(1).length-1);

                //     range.split(',')
                //     console.log(range)
                // }else{
                    // for(var k=0;k<test.length;k++){
                    //  var r2 = ((test[k].range).substr(1)).substr(0,(test[k].range).substr(1).length-1);
                    //     name.push(r2.substring(r2.indexOf(','),r2))
                    //     if(k== test.length-1){
                    //          name.push(r2.substring(r2.indexOf(',')+1,r2.length))
                    //     }
                    // }
                    // console.log(name)
                // }
                this.myChart = echarts.init(document.getElementById('accuracy-broad'+index+item.test_item)); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                        grid: {
                            top:'3%',
                            left: '4%',
                            right: '4%',
                            bottom: '12%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: name,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                    // align: 'right',

                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }, 
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {

                                    textStyle: {
                                    },
                                    color:'#333',

                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                "barMaxWidth": '42%',
                                 barGap:'-100%',
                                    "itemStyle": {
                                        "normal": {

                                            'borderColor':'#B2E4FA',
                                            "color": "#DEF5FF",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#333",                                
                                                    "fontSize":"80%",

                                                },
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                             
                        ]
                };
                this.myChart.setOption(this.optionmyChart);
            },
            initRightCuracy(item,accuracy_item,index){
            var passed = [];
            var name =[]; 
                var accuracy_data = accuracy_item.data;
                for(var j =0;j < accuracy_data.length;j++){
                    if(accuracy_data[j].title_name.indexOf('纵向测距') !=-1&&(accuracy_data[j].title_name.indexOf('阈值') !=-1)){
                        passed.push((accuracy_data[j].passed/accuracy_data[j].total).toFixed(2));
                        // var range = ((accuracy_data[j].range).substr(1)).substr(0,(accuracy_data[j].range).substr(1).length-1);
                            name.push(accuracy_data[j].range)
                        // name.push(range.substring(range.indexOf(','),range))
                        // if(range.indexOf('+oo') != -1){
                        //     name.push('+oo')
                        // }
                    }
                }
                
                this.myChart = echarts.init(document.getElementById('accuracy-vertical'+index+item.test_item)); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                    //    legend: {
                    //         // y: '4%',
                    //         top: '0%',
                    //         right:'0%',
                    //         itemWidth: 12,
                    //         itemHeight: 12,
                    //         textStyle: {
                    //             color: '#505050',
                    //                 fontSize:14,
                    //                 "padding": [3, 6],

                    //         },
                    //         // padding:[0,10],
                    //         data: [ 'passed', 'failed', 'broken', ]
                    //     },
                        grid: {
                            top:'3%',
                            left: '12%',
                            right: '2%',
                            bottom: '0%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: name,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                        // offset:[0,30],
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }, 
                                    color:'#333',
                                    interval:0,//横轴信息全部显示  
                                    rotate:0,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    },
                                    color:'#333',

                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                "barMaxWidth": '42%',
                                    "itemStyle": {
                                        "normal": {

                                            'borderColor':'#B2E4FA',
                                            "color": "#DEF5FF",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#333",                                
                                                    "fontSize":"80%",
                                                    // "fontWeight":'bold',

                                                },
                                                // "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                             
                        ]
                };
                this.myChart.setOption(this.optionmyChart);

            },
            initChart(){
                var testData = this.$store.getters.testData;
                var testItems = testData.test_items;
                var yName =[];
                var passed = [];
                var failed =[];
                var broken = [];
                var total;
                for(var i =0;i< testItems.length;i++){
                    yName.push(testItems[i].test_item);
                    total = testItems[i].passed+testItems[i].failed+testItems[i].broken;
                    passed.push((testItems[i].passed/total).toFixed(2));
                    failed.push((testItems[i].failed/total).toFixed(2)) ;                   
                    broken.push((testItems[i].broken/total).toFixed(2));
                }
                this.myChart = echarts.init(document.getElementById('passEcharts')); 
                this.optionmyChart = {
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            },  
                            textStyle: {
                                color: "#fff"
                            }
                        },
                       legend: {
                            top: '0%',
                            right:'3.5%',
                            itemWidth: 12,
                            itemHeight: 12,
                            textStyle: {
                                color: '#505050',
                                    fontSize:14,
                                    "padding": [3, 6],

                            },
                            data: [ 'passed', 'failed', 'broken', ]
                        },
                        grid: {
                            left: '4%',
                            right: '4%',
                            bottom: '1%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: yName,
                                 axisTick:{
                                    show:false
                                },
                                axisLine:{
                                    show:false
                                },
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    },
                                     interval:0,//横轴信息全部显示  
                                    rotate:30,

                                },
                                   splitLine: {
                                    show: false
                                },
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    // interval: 0,
                                    // rotate: 40,
                                    textStyle: {
                                        // fontSize: '14'
                                    }
                                },
                              
                                axisLine:{
                                    show:false
                                },
                                axisTick:{
                                    show:false
                                },
                                splitLine:{
                                    lineStyle:{
                                        type:'dashed',
                                    }
                                   
                                }
                            }
                        ],
                        series: [
                            
                            {
                                name: "passed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                    "itemStyle": {
                                        "normal": {
                                            "color": "#47E389",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#fff",                                
                                                    "fontSize":"80%",
                                                    "fontWeight":'bold',

                                                },
                                                // "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: passed
                            },
                              {
                                name:"failed",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                "itemStyle": {
                                "normal": {
                                    "color": "#FF6E6E",
                                    "label": {
                                        "show": true,
                                        "textStyle": {
                                            "color": "#fff",
                                                    "fontSize":"80%",
                                            "fontWeight":'bold',
                                        },

                                        "position": "inside",
                                        formatter: function(p) {
                                            return p.value > 0 ? (p.value) : '';
                                        }
                                    }
                                }
                            },
                                data: failed
                            }, {
                                name: "broken",
                                type: 'bar',
                                stack: '广告',
                                "barMaxWidth": '40%',
                                    "itemStyle": {
                                        "normal": {
                                            "color": "#FFD577",
                                            "label": {
                                                "show": true,
                                                "textStyle": {
                                                    "color": "#fff",
                                                    "fontSize":"80%",
                                                    "fontWeight":'bold',

                                                },
                                                "position": "inside",
                                                formatter: function(p) {
                                                    return p.value > 0 ? (p.value) : '';
                                                }
                                            }
                                        }
                                    },
                                data: broken
                            },
                        ]
                };
                this.myChart.setOption(this.optionmyChart);
            },

            initCaseChart(item,index){
                this.myChart = echarts.init(document.getElementById("_d"+index)); 
                this.optionmyChart = {
                    title: {
                        text: item.total,
                        subtext: 'test cases',
                        x: 'center',
                        y: 'center',
                        textStyle: {
                            fontSize:40,
                            fontWeight:'bold',
                            color: ['#505050'],
                            align: 'center',

                        },
                        subtextStyle: {
                            color: '#505050',
                            // fontSize: 22
                        },
                    },
                    // grid: {
                    //     top: '40%',
                    //     left: '50%',
                    //     right: '10%'
                    // },
                    legend: {
                        orient: 'vertical',
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                             "padding": [0, 0],

                            fontSize:14
                        },
                            // padding:[0,10],
                    },
                    series: [
                        {
                            name: '',
                            type: 'pie',
                            radius: ['48%', '58%'],
                            color: ["#47E389", "#FF6E6E", "#FFD577"],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {
                                        "formatter": "{per|{c}\n} {b|{b}} ",
                                        "borderColor": "transparent",
                                        "borderRadius": 4,
                                        "rich": {
                                            "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                            },
                                            "hr": {
                                                "borderColor": "#aaa",
                                                "width": "100%",
                                                "borderWidth": 1,
                                                "height": 0
                                            },
                                            "b": {
                                                "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                                
                                            },
                                            "c": {
                                                "fontSize": 14,
                                                "color": "#b3e5ff"
                                            },
                                            "per": {
                                                "color": "#505050",
                                                "fontSize": 22,
                                                "padding": [3, 2],
                                                "fontWeight":'bold',
                                                "borderRadius": 2
                                            }
                                        },
                                        "textStyle": {
                                            "color": "#fff",
                                            "fontSize": 16
                                        }
                                    },
                                },
                                emphasis: {
                                    "label": {
                                    "show": true,
                                    "formatter": "{per|{c}\n} {b|{b}}",
                                    "backgroundColor": "rgba(255, 147, 38, 0)",
                                    "borderColor": "transparent",
                                    "borderRadius": 4,
                                    "rich": {
                                          "a": {
                                                "color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"
                                        },
                                        "hr": {
                                            "borderColor": "#aaa",
                                            "width": "100%",
                                            "borderWidth": 1,
                                            "height": 0
                                        },
                                        "b": {
                                            "color": "#505050",
                                                "fontSize": 14,
                                                "lineHeight": 16,
                                            
                                        },
                                        "c": {
                                            "fontSize": 14,
                                            "color": "#b3e5ff"
                                            },
                                        "per": {
                                            "color": "#505050",
                                            "fontSize": 22,
                                            "fontWeight":'bold',
                                            "padding": [3, 2],
                                            "borderRadius": 2
                                        }
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    length: 28,
                                    length2: 36

                                }
                            },
                            data: [
                                {value:item.passed, name: 'passed'},
                                {value:item.failed, name: 'failed'},
                                {value:item.broken, name: 'broken'},
                           
                            ]
                        }
                    ]};
                    this.myChart.setOption(this.optionmyChart);
                },
            initSuiteChart(item,index){
                var suite = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<item.suites.length;i++){
                    suite.push(item.suites[i].suite);
                    passed.push(item.suites[i].passed);
                    failed.push(item.suites[i].failed);
                    broken.push(item.suites[i].broken);
                }
                this.myChart = echarts.init(document.getElementById('_s'+index)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                            fontSize:14,
                         "padding": [3, 6],

                        },
                    },
                    grid: {
                        left: '3%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {

                        // type: 'value',
                        axisLabel: {
                            show: false,

                            },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },
                        splitLine: {
                            show: false
                        },
                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        splitLine: {
                            show: false
                        },
                        type: 'category',
                        data: suite,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 45,
                            textStyle: {
                                // fontSize: '16'
                            }
                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                               "color": "#47E389",
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                    "fontWeight":'bold',


                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FF6E6E',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                                    "fontSize":"85%",
                                    "fontWeight":'bold',

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FFD577',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                                    "fontSize":"85%",
                                    "fontWeight":'bold',

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                     
                     
                    ]
                };
                this.myChart.setOption(this.optionmyChart);
                // this.$nextTick(() => {
                //     this.$refs.test;
                // })
            },
            initFeatureChart(item,index){
                var feature = [];
                var passed = [];
                var failed = [];
                var broken = [];
                for(var i=0;i<item.features.length;i++){
                    feature.push(item.features[i].feature);
                    passed.push(item.features[i].passed);
                    failed.push(item.features[i].failed);
                    broken.push(item.features[i].broken);
                }
                this.myChart = echarts.init(document.getElementById('_f'+index)); 
                this.optionmyChart = {
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: [ 'passed', 'failed', 'broken' ],
                        top: '0%',
                        right:'0',
                        itemWidth: 12,
                        itemHeight: 12,
                        textStyle: {
                            color: '#505050',
                                                     "padding": [3, 6],
                            fontSize:14,

                            // fontSize:16
                        },
                    },
                    grid: {
                        left: '4%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        // type: 'value',
                        axisLabel: {
                            show: false,

                            },
                        splitLine: {
                            show: false
                        },
                        axisTick:{
                            show:false
                        },
                        axisLine: {
                            show: false 
                        },

                    },
                    yAxis: {
                        axisLine: {
                            show: false
                        },
                        splitLine: {
                            show: false
                        },
                          axisTick:{
                            show:false
                        },
                        type: 'category',
                        data: feature,
                        axisLabel: {
                            // interval: 0,
                            // rotate: 40,
                            // textStyle: {
                            //     fontSize: '16',
                            // },
                            interval:0,//横轴信息全部显示  

                        },
                    },
                    series: [
                        {
                            name: 'passed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            "color": "#47E389",
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: passed
                        },
                        {
                            name: 'failed',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FF6E6E',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                    "fontSize":"85%",
                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: failed
                        },
                        {
                            name: 'broken',
                            type: 'bar',
                            stack: '总量',
                            "barMaxWidth": 25,
                            color:'#FFD577',
                            label: {
                                show: true,
                                position: 'inside',
                                "textStyle": {
                                    "color": "#fff",                                
                                     "fontSize":"85%",

                                },
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            },
                            data: broken
                        },
                     
                     
                    ]
                };
                this.myChart.setOption(this.optionmyChart);
            }
        },
        updated(){
                for(var i=0;i< this.caseData.length;i++){    
                    this.initCaseChart(this.caseData[i],i);
                    this.initSuiteChart(this.caseData[i],i);
                    this.initFeatureChart(this.caseData[i],i);
                    if( this.caseData[i].test_item.indexOf('distance')!=-1){
                        var accuracy = this.caseData[i].accuracy
                        for(var k=0;k < accuracy.length; k++){
                            this.initLeftCuracy(this.caseData[i],accuracy[k],k);
                            this.initRightCuracy(this.caseData[i],accuracy[k],k);
                        }
                    }
                }            
        },
        computed:  {
            ...mapGetters(
                {testData:'testData'}
   
            )
        }
    }
</script>

<style lang="less">
@import "../assets/styles/dash.less";
</style>
