const { app, BrowserWindow, autoUpdater } = require('electron')
const child_process = require('child_process');
// const {autoUpdater} = require('electron-updater');
const os = require('os');
// var remote = require('remote');
// const {dialog} = require('electron').remote

// const ps = require('ps-node');
// const autoUpdater = require('electron-updater');
// const {autoUpdater} = require('electron')
let win = null;

// const path = require('path');

// 检测更新，在你想要检查更新的时候执行，renderer事件触发后的操作自行编写
function updateHandle() {

    const os = require('os');

    //JavaScript
    const server = 'https://coderlife.me/fblives'
    const feed = `${server}`
    console.log(feed)
    autoUpdater.setFeedURL(feed)
    autoUpdater.addListener("error", function(error) { 
        // console.log(error)
        // sendUpdateMessage("error")

    }); 
 
    autoUpdater.on('checking-for-update', function (event) {
    
        // sendUpdateMessage(event)   
    });
    autoUpdater.on('update-available', function (event) {
        // sendUpdateMessage("找到新的版本，開始進行更新…")
        sendUpdateMessage('下載中新的版本…請稍候');
    });
    autoUpdater.on('update-not-available', function (info) {
        // sendUpdateMessage(info)

    });

    // 更新下载进度事件
    autoUpdater.on('download-progress', function (progressObj) {
        // sendUpdateMessage('下載中新的版本…請稍候');
    })
    autoUpdater.on('update-downloaded', (event, releaseNotes, releaseName) => {
        const dialogOpts = {
            type: 'info',
            buttons: ['立即重開程式', '稍候再說'],
            title: 'Application Update',
            message: process.platform === 'win32' ? releaseNotes : releaseName,
            detail: '新版本已經準備完成，請問您要?'
        }

        dialog.showMessageBox(dialogOpts, (response) => {
            if (response === 0) autoUpdater.quitAndInstall()
        })
    })

    //执行自动更新检查
    // console.log("run_auto_update")

    autoUpdater.checkForUpdates();
}

//生成和刪除應用快捷方式，用於安裝和解除安裝，直接在app.on('ready',() => {startupEventHandle()})的時候執行；
function startupEventHandle() {
    // if (require('electron-squirrel-startup')) return;
    var handleStartupEvent = function () {
        if (process.platform !== 'win32') {
            return false;
        }
        var squirrelCommand = process.argv[1];
        switch (squirrelCommand) {
            case '--squirrel-install':
            case '--squirrel-updated':
                install();
                return true;
            case '--squirrel-uninstall':
                uninstall();
                app.quit();
                return true;
            case '--squirrel-obsolete':
                app.quit();
                return true;
        }
        // 安裝
        function install() {
            var cp = require('child_process');
            var updateDotExe = path.resolve(path.dirname(process.execPath), '..', 'update.exe');
            var target = path.basename(process.execPath);
            var child = cp.spawn(updateDotExe, ["--createShortcut", target], { detached: true });
            child.on('close', function (code) {
                app.quit();
            });
        }

        // 解除安裝
        function uninstall() {
            var cp = require('child_process');
            var updateDotExe = path.resolve(path.dirname(process.execPath), '..', 'update.exe');
            var target = path.basename(process.execPath);
            var child = cp.spawn(updateDotExe, ["--removeShortcut", target], { detached: true });
            child.on('close', function (code) {
                app.quit();
            });
        }
    };


    if (handleStartupEvent()) {
        return;
    }
}


// 通过main进程发送事件给renderer进程，提示更新信息
// mainWindow = new BrowserWindow()
function sendUpdateMessage(text) {
    console.log(text)
    //win.webContents.send('message', text)
    const dialogOpts = {
        type: 'info',
        buttons: ['OK'],
        title: 'Application Update',
        message: "info",
        detail: text
    }

    // dialog.showMessageBox(dialogOpts, (response) => {
    //     if (response === 0) autoUpdater.quitAndInstall()
    // })

}
const path = require('path');


const find = require('find-process');
function Check_Core_Is_Runing(){
  
    find('name', 'FB_Services_Master', true)
  .then(function (list) {
    console.log('there are %s Core process(es)', list.length);
    if (list.length == 0) {
        
    setTimeout(function () {

        var mc = path.dirname(app.getPath('exe')) + '\\resources\\FB_Services_Master.exe';

        var mc_stat = fs.existsSync(mc)
        if (!mc_stat) {
            mc = 'resources\\FB_Services_Master.exe';
            win.webContents.openDevTools()
        }
        // console.log(mc)
        var newProcess = child_process.exec(mc);
        processes.push(newProcess);
        setTimeout(function(){

            Check_Core_Is_Runing();
        },1500)
    }, 100)
    }
  });
}

// console.log(process.versions);
const fs = require('fs')
const processes = [];
function createWindow() {


    win = new BrowserWindow({
        width: 1280,
        height: 720,
        webPreferences: {
            nodeIntegration: false, // for jQuery
        },
        autoHideMenuBar: true,
        show: true
    })


    win.loadFile('html/index.html')


    win.on("closed", function () {
    });

    updateHandle();
}
app.on('window-all-closed', function () {
    if (process.platform != 'darwin') {
        processes.forEach(function (proc) {
            proc.kill();
        });

        app.quit();
    }
});
app.on('ready', createWindow)

