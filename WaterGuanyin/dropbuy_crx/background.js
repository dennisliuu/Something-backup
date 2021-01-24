chrome.browserAction.onClicked.addListener(function (tab) {
  chrome.tabs.create({ 'url': "https://dropbuy.global/" }, function (tab) {
    // Tab opened.
  });
});

console.log(document.domain);// Outputs present active URL of tab
