const webpack = require('webpack');
module.exports = {
    publicPath: '',
    assetsDir: 'static',
    devServer: { // 所有 webpack-dev-server 的选项都支持
        proxy: {
            '/api': {
                // target:'http://192.168.196.114:8000',
                // target:'http://192.168.199.56:8000',
                target:'http://127.0.0.1:8000',
                changeOrigin: true,
                pathRewrite:{
                    '^/api':''
                }
            }
        }, // 跨域代理
    },
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $:"jquery",
                jQuery:"jquery",
                "windows.jQuery":"jquery"
            })
        ]
    }
}
