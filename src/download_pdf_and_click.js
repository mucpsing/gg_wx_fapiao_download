/*!
 * @Author: CPS
 * @email: 373704015@qq.com
 * @Date: 2025-04-10 20:24:27.728475
 * @Last Modified by: CPS
 * @Last Modified time: 2025-04-10 20:24:27.728475
 * @Projectname
 * @file_path "D:\CPS\MyProject\Projects_Personal\GG_wx_fapiao_download\src"
 * @Filename "自动下载脚本.js"
 * @Description: 原理是劫持open，每次打开url时对url进行修改，将ReadDownload修改未Download, open修改为0， Dj_ifr修改未false，作用未知
 * url形式： http://zszjoa.prpsdc.com:8099/sys/attachment/sys_att_main/sysAttMain.do?method=readDownload&fdId=19610d2caeabfe395ab847a4df1854e2&useBrowserOpen=true&isSupportDirect=null&dj_ifr=true&open=1
 */

var old_open = window.open;

if (!window.__cps)
  window.__cps = {
    readEl: document.getElementsByClassName('upload_opt_icon')[0],
  };

// 当前文件名是在： upload_list_filename_title
// 当前后缀名是在： upload_list_filename_ext
window.__cps.getHtmlContent = className => {
  const tar = document.getElementsByClassName(className);

  if (tar.length != 1) {
    console.log('发生错误了，元素获取数量不对: ', tar);
    return '';
  }

  return tar[0].innerHTML;
};

// window.__cps.readDownloadIcon = () => {
//   if (document.getElementsByClassName('upload_opt_icon').length > 2) return;

//   const parentEl = document.getElementsByClassName('upload_list_operation')[0];
//   const readEl = document.getElementsByClassName('upload_opt_icon')[0]; // 要复制的元素

//   // 2. 克隆元素（true 表示深拷贝）
//   const downloadEl = readEl.cloneNode(true);
//   const innerEl = downloadEl.querySelector('.upload_opt_tip_inner');
//   innerEl.innerHTML = '下载';

//   window.__cps.downloadEl = downloadEl;
//   parentEl.insertBefore(downloadEl, readEl);
// };

/**
 *  劫持open解释url
 */
window.open = function (old_url) {
  const targetURL = new URL(old_url);
  targetURL.searchParams.set('dj_ifr', 'false'); //
  targetURL.searchParams.set('open', '0'); //
  targetURL.searchParams.set('method', 'download'); // 默认是 readDownload,我是猜的download，猜对了
  console.log('fdId: ', targetURL.searchParams.get('fdId'));

  // 发起 Fetch 请求
  fetch(targetURL, {
    method: 'GET',
    credentials: 'include', // 携带 Cookie（如果需要登录态）
  })
    .then(response => {
      // 检查响应状态
      if (!response.ok) {
        throw new Error(`HTTP 错误，状态码：${response.status}`);
      }

      // 获取响应内容类型
      const contentType = response.headers.get('content-type');

      // 根据内容类型处理数据
      if (contentType.includes('application/json')) {
        return response.json(); // 解析 JSON
      } else if (contentType.includes('text/')) {
        return response.text(); // 解析文本
      } else {
        return response.blob(); // 处理二进制文件（如 PDF、图片）
      }
    })
    .then(data => {
      // 打印结果，这是一个Blob对象
      // console.log('请求成功，响应内容：', data);

      const save_name = __cps.getHtmlContent('upload_list_filename_title') + __cps.getHtmlContent('upload_list_filename_ext');

      const reader = new FileReader();
      reader.onload = function (e) {
        const base64Data = e.target.result;
        const link = document.createElement('a');
        link.href = base64Data;
        link.download = save_name;
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      };
      reader.readAsDataURL(data); // 将 Blob 转为 Base64
    })
    .catch(error => {
      console.error('请求失败：', error);
    });
};

const readEl = document.getElementsByClassName('upload_opt_icon')[0];
const innerEl = readEl.querySelector('.upload_opt_tip_inner');
innerEl.innerHTML = '下载';
readEl.click();
