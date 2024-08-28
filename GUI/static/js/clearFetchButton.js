const clearFetchButton = document.getElementById('clearFetchButton');

clearFetchButton.addEventListener('click', () => {
    var videoStream = document.getElementById('videoStream');
    if (videoStream) {
        var container = document.getElementById("imageContainer");
        container.removeChild(videoStream);
        console.log('Video stream cleared.');
        window.location.href = clearFetchButton.dataset.redirectUrl;
    }
});

function checkStreamingData() {
    fetch('../static/json/streaming_data.json')
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.stopped);
            if (json.stopped) {
                var container = document.getElementById("imageContainer");
                container.removeChild(videoStream);
                clearInterval(intervalID);
                console.log('Video stream cleared.');
                window.location.href = clearFetchButton.dataset.redirectUrl;
            }
        });
}

let intervalID = setInterval(checkStreamingData, 1000);
