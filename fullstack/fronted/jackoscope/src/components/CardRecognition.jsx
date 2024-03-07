import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';

function CardRecognition() {
    const [cameraStream, setCameraStream] = useState(null);
    const [recognizedCard, setRecognizedCard] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        const initializeCamera = async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                setCameraStream(stream);
            } catch (error) {
                console.error('Error accessing camera:', error);
                setError('Could not access camera. Please check your device settings.');
            }
        };

        initializeCamera();

        return () => {
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
            }
        };
    }, [cameraStream]);

    const handleRecognizeCard = async () => {
        try {
            const response = await axios.get('/recognize-card');
            setRecognizedCard(response.data);
        } catch (error) {
            console.error('Error recognizing card:', error);
            setError('Error recognizing card. Please try again later.');
        }
    };

    return (
        <div>
            {error && <p>{error}</p>}
            <div>
                <h2>Camera Feed</h2>
                {cameraStream && <VideoPlayer stream={cameraStream} />}
            </div>
            <div>
                <h2>Recognized Card</h2>
                <button onClick={handleRecognizeCard} disabled={!cameraStream}>
                    Recognize Card
                </button>
                {recognizedCard && <p>Recognized Card: {recognizedCard}</p>}
            </div>
        </div>
    );
}

const VideoPlayer = ({ stream }) => {
    const videoRef = useRef();

    useEffect(() => {
        videoRef.current.srcObject = stream;
    }, [stream]);

    return <video autoPlay ref={videoRef} />;
};

export default CardRecognition;
