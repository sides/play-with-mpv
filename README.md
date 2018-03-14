This is a web extension using [native messaging](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_messaging) to launch mpv with a link's url as the only argument. It tries to do as little as possible in code to achieve this simple task.

The extension needs to be installed manually, including editing the source files and setting up config files/editing registry on windows to allow for a python script to execute in the background. See the [native messaging](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_messaging) docs for more on that. Change "YOUR PATH HERE" in the source files to full paths to the relevant files. Needless to say it also requires python installed on your system.