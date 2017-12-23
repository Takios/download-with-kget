function onResponse(response) {
  if (response){
    console.log(response);
  }
}

function onSentError(error) {
  console.log("Error at sending native message. Full error message: " + error);
  var sendNotification = browser.notifications.create({
    type: "basic",
    message: "Full error message: " + error,
    title: "Error at sending native message"
  });
}

function addDownloadToKget(info, tab) {

  if (info.menuItemId == "download-with-kget"){
    if (info.linkUrl) {
      downloadUrl = info.linkUrl;
      console.log("Found link URL");
    } else if (info.frameUrl) {
      downloadUrl = info.frameUrl;
      console.log("Found frame URL");
    } else if (info.pageUrl) {
      downloadUrl = info.pageUrl;
      console.log("Found page URL");
    } else {
      console.log("Cannot determine download URL");
    }

    var sendingToNativeApp = browser.runtime.sendNativeMessage(
      "download_with_kget",
      downloadUrl);

    sendingToNativeApp.then(onResponse, onSentError);
  }
}

browser.contextMenus.create({
  id: "download-with-kget",
  title: "Download with KGet",
  contexts: [ "audio", "image", "link", "page", "tab", "video" ]
});

browser.contextMenus.onClicked.addListener(addDownloadToKget);

