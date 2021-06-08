import request from '@/utils/request'

export function search_pdaq(params,data) {
    return request({
        url: '/api/search',    //实现后台检索功能
        method: 'get',
        params,
        data
    })
}
export function searchRecords(params,data) {
    return request({
        url: '/api/filter/',    //检索后端符合要求的PDAQ数据,此功能放弃，因目前实力不够，无法完成开发，等下一版本
        method: 'get',
        params,
        data
    })
}


export function getRecords(data) {
    return request({
        url: '/api/pdaq',     //自定义功能   获取全部的 pdaq 列表信息
        method: 'get',
        data
    })
}

export function getBase(params,data) {
    return request({
        url: '/program/get_base_info',
        method: 'get',
        params,
        data
    })
}

export function getItems(params,data) {
    return request({
        url: '/program/get_items',
        method: 'get',
        params,
        data
    })
}

export function getSuites(params,data) {
    return request({
        url: '/program/get_suites',
        method: 'get',
        params,
        data
    })
}
export function getFeatures(params,data) {
    return request({
        url: '/program/get_features',
        method: 'get',
        params,
        data
    })
}
export function getAccuracy(params,data) {
    return request({
        url: '/program/get_accuracy',
        method: 'get',
        params,
        data
    })
}
export function getPerformanceItems(params,data) {
    return request({
        url: '/program/performance',
        method: 'get',
        params,
        data
    })
}

export function getMenuItems(data) {
    return request({
        url: '/model/get_nav',
        method: 'get',
        data
    })
}


export function get_platform(params,data) {
    return request({
        url: '/model/get_platforms',
        method: 'get',
        params,
        data
    })
}


export function get_Folder(params,data) {
    return request({
        url: '/model/get_type',
        method: 'get',
        params,
        data
    })
}


export function get_Model_detail(params,data) {
    return request({
        url: '/model/get_result',
        method: 'get',
        params,
        data
    })
}

export function get_py(params,data) {
    return request({
        url: '/model/get_python',
        method: 'get',
        params,
        data
    })
}


export function get_history(params,data) {
    return request({
        url: '/program/history/trend',
        method: 'get',
        params,
        data
    })
}


export function get_constract_result(params,data) {
    return request({
        url: '/program/compare',
        method: 'get',
        params,
        data
    })
}



export function get_case_items(data) {
    return request({
        url: '/program/search/items',
        method: 'get',
        data
    })
}


