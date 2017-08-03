'use strict';

/**
 * 使用指定的环境变量来加载文件
 *
 * @author 老雷<leizongmin@gmail.com>
 */

var fs = require('fs');
var path = require('path');
var vm = require('vm');
var Module = require('module');

/**
 * 载入程序文件，并删除其缓存
 *
 * @param {string} filename 文件名
 * @param {object} context 环境变量
 * @param {object} parent 父模块
 * @return {object}
 */
module.exports = function (filename, context, parent) {
  var self = this;
  filename = path.resolve(filename);
  
  // 如果没有指定环境变量和父模块，则清除缓存模块并加载
  if (!context && !parent) {
    /*debug debug('require no cache file: ' + filename); */
    
    delete require.cache[filename];
    var m = require(filename);
    delete require.cache[filename];
    
    return m;
  }
  // 否则，使用指定的环境变量和父模块来载入文件
  else {
    /*debug debug('require specified context file: ' + filename); */
    
    if (typeof context !== 'object')
      context = {}
    
    // 复制全局变量
    var sandbox = merge(global, context);
    
    return requireWithContext(filename, sandbox, parent);
  }
}

/**
 * 使用指定的沙箱环境来载入模块文件
 *
 * @param {string} filename 文件名
 * @param {object} sandbox 沙箱
 * @param {object} parent 父对象
 * @return {object}
 */
var requireWithContext = function (filename, sandbox, parent) {
  try {
    if (!parent)
      parent = {require: require}
    if (!sandbox)
      sandbox = {}
    
    // 读取代码
    var code = fs.readFileSync(filename, 'utf8');
    
    // 模拟require()环境
    sandbox.module = new Module(filename, parent);
    sandbox.exports = sandbox.module.exports;
    sandbox.__dirname = path.dirname(filename);
    sandbox.__filename = filename;
    sandbox.module.filename = filename;
    sandbox.module.paths = Module._nodeModulePaths(sandbox.__dirname);
    sandbox.global = sandbox;
    sandbox.root = root;
    sandbox.require = function (path) {
      var f = sandbox.require.resolve(path);
      return parent.require(f);
    }
    sandbox.require.resolve = function(request) {
      return Module._resolveFilename(request, sandbox.module);
    }
    sandbox.require.main = process.mainModule;
    sandbox.require.extensions = Module._extensions;
    sandbox.require.cache = Module._cache;
    
    // 运行代码
    vm.runInNewContext(code, sandbox, filename);
      
    // 返回模块输出
    return sandbox.module.exports;
  }
  catch (err) {
    // 如果是语法错误，则尝试输出更详细的信息，比如出错的位置
    if (isSyntaxError(err)) {
      process.stdout.write('--------------------------------------------------------------------------------\n');
      process.stdout.write(err.toString() + '\n');
      try {
        require(filename);
      }
      catch (e) { }
      process.stdout.write('--------------------------------------------------------------------------------\n');
    }
    throw new Error(err.toString() + '\n    at ' + filename);
  }
}


/**
 * 判断异常是否为语法错误
 *
 * @param {Error} e
 * @return {bool}
 */
var isSyntaxError = function (e) {
  // Convert error to string
  e = e && (e.stack || e.toString());
  return e && e.match(/^SyntaxError/) &&
           !(e.match(/^SyntaxError: Unexpected token .*\n/) &&
           e.match(/\n    at Object.parse \(native\)\n/));
};

/**
 * 合并多个对象
 *
 * @param {object} obja
 * @param {object} objb
 * @return {object}
 */
var merge = function () {
  var ret = {};
  for (var i in arguments) {
    var obj = arguments[i];
    for (var j in obj) {
      ret[j] = obj[j];
    }
  }
  
  return ret;
};