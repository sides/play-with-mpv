browser.contextMenus.create({
    id: 'play-with-mpv',
    title: 'Play with mpv',
    contexts: ['link', 'tab'],
});

browser.contextMenus.onClicked.addListener(info => {
    if (info.menuItemId !== 'play-with-mpv') {
        return;
    }

    const target = info.linkUrl || info.pageUrl || null;

    if (target) {
        browser.runtime.sendNativeMessage('play_with_mpv', [target]);
    }
});
