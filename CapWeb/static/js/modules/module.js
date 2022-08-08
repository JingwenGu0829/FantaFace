src="static/js/jquery-3.2.1.min.js"

var beginButton = document.querySelector('button#begin');
var recordButton = document.querySelector('button#record');
var playButton = document.querySelector('button#play');
var downloadButton = document.querySelector('button#download');
var reStartButton = document.querySelector('button#reStart');
var postButton =doocument.querySelector('button#post')

var gumVideo = document.querySelector('#gumVideo');
var gumVideo2 = document.querySelector('#gumVideo2');

var mediaRecorder;
var recordedBlobs;
var sourceBuffer;

function getUserMediaStream(constraints, cb) {
    navigator.mediaDevices.getUserMedia(constraints)
                .then(handleSuccess)
                .catch(err => { cb(err, null); });
}

        function handleSuccess(stream) {
            console.log(stream)
            recordButton.disabled = false;
            console.log('getUserMedia() got stream: ', stream);
            window.stream = stream;
            if (window.URL) {

                gumVideo.srcObject = stream;

                console.log(gumVideo.srcObject)
            } else {
                gumVideo.src = stream;
                console.log(gumVideo)
            }

            var c = document.getElementById("myCanvas");
            c.width = 400;
            c.height = 300;
            var i;
            gumVideo.addEventListener('play', function () {
                var p = document.createElement('p');
                p.innerText = 'hello';

            }, false);
            gumVideo.addEventListener('pause', function () { if (i) { window.clearInterval(i); } }, false);
            gumVideo.addEventListener('ended', function () { if (i) { clearInterval(i); } }, false);
        }

        function startRecording() {
            recordedBlobs = [];
            var options = { mimeType: 'video/webm;codecs=vp9' };
            if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                console.log(options.mimeType + ' is not Supported');
                options = { mimeType: 'video/webm;codecs=vp8' };
                if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                    console.log(options.mimeType + ' is not Supported');
                    options = { mimeType: 'video/webm' };
                    if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                        console.log(options.mimeType + ' is not Supported');
                        options = { mimeType: '' };
                    }
                }
            }
            try {
                mediaRecorder = new MediaRecorder(window.stream, options);
            } catch (e) {
                console.error('Exception while creating MediaRecorder: ' + e);
                alert('Exception while creating MediaRecorder: '
                    + e + '. mimeType: ' + options.mimeType);
                return;
            }
            console.log('Created MediaRecorder', mediaRecorder, 'with options', options);
            recordButton.textContent = '停止';
            playButton.disabled = true;
            downloadButton.disabled = true;
            reStartButton.disabled = true;
            mediaRecorder.onstop = handleStop;
            mediaRecorder.ondataavailable = handleDataAvailable;
            mediaRecorder.start(10);
            console.log('MediaRecorder started', mediaRecorder);
        }
        function handleStop(event) {
            console.log('Recorder stopped: ', event);
        }
        function handleDataAvailable(event) {
            if (event.data && event.data.size > 0) {
                recordedBlobs.push(event.data);
            }
        }
        function toggleRecording() {
            if (recordButton.textContent === '录制' || recordButton.textContent === '重录') {
                startRecording();
                setTimeout(() => {
                    stopRecording();
                    recordButton.textContent = '重录';
                    playButton.disabled = false;
                    downloadButton.disabled = false;
                    reStartButton.disabled = false;
                    postButton.disabled=false;
                }, 5000);
            } else {
                stopRecording();
                recordButton.textContent = '重录';
                playButton.disabled = false;
                downloadButton.disabled = false;
                reStartButton.disabled = false;
                postButton.disabled=false;
            }
        }
        function stopRecording() {
            mediaRecorder.stop();
            bufferToDataUrl()
            console.log('Recorded Blobs: ', recordedBlobs);
        }
        function play() {
            var superBuffer = new Blob(recordedBlobs, { type: 'video/mp4' });
            gumVideo2.src = window.URL.createObjectURL(superBuffer);
            gumVideo2.play()
        }
        
        function post(){
            var superBuffer=new Blob(recordedBlobs, { type: 'video/mp4' })
            gumVideo2.src = window.URL.createObjectURL(superBuffer);
            $.ajax({
                url: 'video',
                type: "POST",
                data: {
                    'video': gumVideo,
                    'csrfmiddlewaretoken': '{{ csrf_token }}',
                },
                success: function (data) {
                    alert ("Congrats! You sent some data: " + tagID);}
                ,
                error: function() {
                     alert ("Something went wrong");
                 }
                    })};

        
        function upload() {
            var blob = new Blob(recordedBlobs, { type: 'video/mp4' });
        }
        function bufferToDataUrl() {
            let blob = new Blob(recordedBlobs, { type: "video/webm" });
            let reader = new FileReader();
            reader.onload = function () {
                var a = document.createElement('a');
                a.style.display = 'none';
                a.href = reader.result;
                a.download = 'record.mp4';
                document.body.appendChild(a);
                a.click();
                setTimeout(function () {
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(reader.result);
                }, 100);
            };
            reader.readAsDataURL(blob);
        }
        function restartRecord() {
            recordButton.textContent = '录制';
            playButton.disabled = true;
            downloadButton.disabled = true;
            reStartButton.disabled = true;
            navigator.mediaDevices.getUserMedia({ audio: true, video: { facingMode: 'user' } }).
                then(handleSuccess).catch(handleError);
        }
        function dataUrlToFile(dataUrl) {
            let binary = atob(dataUrl.split(",")[1]);
            let data = [];
            for (var i = 0; i < binary.length; i++)
                data.push(binary.charCodeAt(i));
            return new File([new Uint8Array(data)], "recorded-video.webm", {
                type: "video/webm"
            });
        }
        function getDisplayMediaStream(cb) {
            navigator.mediaDevices.getDisplayMedia()
                .then(stream => { cb(null, stream); })
                .catch(err => { cb(err, null); })
        }
        		function takePicture() {
			let ctx = canvas.getContext('2d');
			ctx.drawImage(video, 0, 0, config.video.width, config.video.height);
		}

        function takePicture() {
			let ctx = canvas.getContext('2d');
			ctx.drawImage(video, 0, 0, config.video.width, config.video.height);
		}
        function downPhoto() {
			const MIME_TYPE = "image/png";
			const dlLink = document.createElement('a');
			dlLink.download = '测试照片';
			dlLink.href = canvas.toDataURL(MIME_TYPE);
			dlLink.dataset.downloadurl = [MIME_TYPE, dlLink.download, dlLink.href].join(':');
			document.body.appendChild(dlLink);
			dlLink.click();
			document.body.removeChild(dlLink);
		}
        
        setTimeout(function(){
            document.getElementById('take').onclick = () => {
            let ctx = document.getElementById("canvas").getContext('2d')
            ctx.drawImage(document.getElementById("video"), 0, 0, 300, 300)
            }
        },1000); 
