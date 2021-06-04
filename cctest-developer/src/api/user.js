import request from '@/utils/request'

export function getInfo(params,data) {
    return request({
        url: '/program/get_info',
        method: 'get',
        params,
        data
    })
}
export function searchRecords(params,data) {
    return request({
        url: '/program/get_records',
        method: 'get',
        params,
        data
    })
}


export function getRecords(data) {
    return request({
        url: '/api/pdaq',     //自定义功能
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


