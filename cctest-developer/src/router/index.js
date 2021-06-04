import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

const dashBoard = r => require.ensure([], () => r(require('@/views/dash-board/dashBoard')), 'dash-board');
const index = r => require.ensure([], () => r(require('@/views/index')), 'index');
const layout = r => require.ensure([], () => r(require('@/views/layout/index')), 'layout');
const report = r => require.ensure([], () => r(require('@/views/report')), 'report');
const modelList = r => require.ensure([], () => r(require('@/views/model-list/modelList')), 'modelList');
const modelDetail = r => require.ensure([], () => r(require('@/views/model-list/modelDetail')), 'modelDetail');
const contrast  = r => require.ensure([], () => r(require('@/views/contrast-list/index')), 'contrast');
const contrastDetail  = r => require.ensure([], () => r(require('@/views/contrast-list/contrastDetail')), 'contrastDetail');


const routes = [
    {
        path: '/',
        name: 'layout',
        component: layout, 
        redirect: '/',
        children:[ 
          {
            path:'/',
            name:'index',
            component:index,
              meta: {
                  requireAuth: true,
                  name: 'index',
              },
          },
          {
              path:'/ModelRelease',
              name:'模型列表',
              component:modelList,
                meta: {
                    requireAuth: true,
                    name: 'modelList',
                },
                children:[{
                    path:'/ModelRelease_:platform+_:date',
                    name:'modelDetail',
                    component:modelDetail,
                      meta: {
                          requireAuth: true,
                          name: 'modelDetail',
                      },
                }]
            },
            {
              path:'/contrast',
              name:'对比列表',
              component:contrast,
                meta: {
                    requireAuth: true,
                    name: 'contrast',
                },
                children:[
                  {
                      path:'/contrast-:program',
                      name:'contrastDetail',
                      component:contrastDetail,
                      meta: {
                          requireAuth: true,
                          name: 'contrastDetail',
                      },  
                  }
                  
            ]
          }
        ],
    },
    {
      path:'/:program+_:version+_:stage',
      name:'dashboard',
      component:dashBoard,
        meta: {
            requireAuth: true,
            name: 'dash',
        },
    },
    {
      path:'/report',
      name:'report',
      component:report,
        meta: {
            requireAuth: true,
            name: 'report',
        },
    },
        
]

const router = new Router({
  routes
})

// router.beforeEach((to, from, next) => {
//     let token = store.getters.token;
//     if(!token){
//         if(to.meta.requireAuth){
//             next({
//                 path: '/'
//             })
//         }else{
//             next();
//         }
//     }else{
//         next();
//     }
//   })



  export default router;
