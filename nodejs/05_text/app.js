/**
 * 主模块
 */

var requireWithContext = require('./require_with_context');

var random = Math.random();
console.log('main: random=' + random);

var file = requireWithContext('./file.js', {
  random:     random      // 此为要传给该文件的变量，在该文件内可以直接使用
});