import Vue from 'vue'
import App from './App.vue'
import router from './router'
import "babel-polyfill";
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';

import htmlToPdf from "./utils/htmlTopdf"
Vue.use(htmlToPdf)


import transformTime from "./utils/transformTime"
Vue.prototype.transformTime = transformTime;



Vue.use(ViewUI);
Vue.use(ElementUI);
Vue.config.productionTip = false
import axios from 'axios'
Vue.prototype.$axios = axios;
import $ from 'jquery';
Vue.prototype.$ = $;
import echarts from 'echarts';
Vue.prototype.$echarts = echarts;
Vue.use(echarts);
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed' //自己添加
// import moment from 'moment';
// Vue.use(moment);
// axios.defaults.timeout = 5000 // 请求超时
// axios.defaults.baseURL = '/api'
// axios.defaults.baseURL = 'http://192.168.199.56:8089'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
