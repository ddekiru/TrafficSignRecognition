import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  const [imageUrl, setImageUrl] = useState("Question_mark.png");

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();

      reader.onload = (e) => {

        const formData = new FormData();
        formData.append('image', file);
        console.log(file);
        
        // Make a POST request using the Fetch API
        fetch('http://127.0.0.1:5000/detect_traffic_sign', {
          method: 'POST',
          body: formData
        })
        .then(response => {
          if (response.ok) {
            return response.blob();
          } else {
            throw new Error('Failed to fetch');
          }
        })
        .then(blob => {
          // Create a URL for the blob data
          const url = window.URL.createObjectURL(blob);
      
          // You can use the URL to set the source of an image element
          const imageElement = document.getElementById('imageId');
          console.log(imageElement)
          imageElement.src = url;
        })
          .catch(error => {
            console.error('Error:', error);
          });

        setImageUrl(e.target.result);
      };

      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="App">
      <div className="box d-flex align-items-center justify-content-center">
        <div className="imageBox d-flex align-items-center justify-content-evenly">
          <label className="btn btn-lg btn-primary" htmlFor="img">Image Upload</label>
          <input id="img" className="d-none" type="file" accept="image/*" onChange={handleImageChange} />

          <img className="traffic-sign-image" id="imageId" src={imageUrl} alt="Image" />
        </div>
      </div>
    </div>
  );
}

export default App;

