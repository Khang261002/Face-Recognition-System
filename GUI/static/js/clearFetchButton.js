const clearFetchButton = document.getElementById('clearFetchButton');
let intervalID;

clearFetchButton.addEventListener('click', () => {
    clearVideoStream();
    window.location.href = clearFetchButton.dataset.redirectUrl;
});

function clearVideoStream() {
    const videoStream = document.getElementById('videoStream');
    if (videoStream) {
        const container = document.getElementById("imageContainer");
        container.removeChild(videoStream);
        console.log('Video stream cleared.');
        updateStoppedStatus(true); // Update the status to stopped
    }
}

function checkStreamingData() {
    fetch('../static/json/streaming_data.json')
        .then((response) => response.json())
        .then((json) => {
            if (json.stopped) {
                clearVideoStream();
                clearInterval(intervalID);
            }
        });
}

// Update the stopped status in streaming_data.json
function updateStoppedStatus(isStopped) {
    fetch('/update_streaming_status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ stopped: isStopped }),
    })
    .then(response => response.json())
    .then(data => console.log('Streaming status updated:', data))
    .catch(error => console.error('Error updating streaming status:', error));
}

// Set the interval to check streaming data every second
intervalID = setInterval(checkStreamingData, 1000);

// Add an event listener to handle page unload
window.addEventListener('beforeunload', () => {
    clearInterval(intervalID);
    updateStoppedStatus(true); // Set stopped to true on page unload
});
