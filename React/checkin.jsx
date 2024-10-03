import React, { useState } from "react";
import "./App.css"; // If you need extra custom styles

const Popup = ({ message, show, onClose }) => {
  if (!show) return null;
  return (
    <div className="fixed z-50 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded shadow-lg text-center">
        <span
          className="absolute top-2 right-2 text-xl cursor-pointer"
          onClick={onClose}
        >
          &times;
        </span>
        <p>{message}</p>
      </div>
    </div>
  );
};

function App() {
  const [showPopup, setShowPopup] = useState(false);

  // Handler for check-in button click
  const handleCheckInClick = () => {
    setShowPopup(true);
  };

  const handleClosePopup = () => {
    setShowPopup(false);
  };

  return (
    <div className="bg-gradient-to-b from-gray-100 to-gray-300 min-h-screen flex flex-col items-center">
      <header className="navbar bg-gray-800 text-white p-4 flex items-center w-full">
        <div className="text-3xl font-permanent-marker flex-shrink-0">FRS</div>
        <div className="flex-grow flex justify-center">
          <a href="/" className="hover:text-gray-300 mx-4">
            Home
          </a>
          <a href="/about" className="hover:text-gray-300 mx-4">
            About Us
          </a>
          <a href="/terms" className="hover:text-gray-300 mx-4">
            Terms and Conditions
          </a>
        </div>
      </header>

      {/* Main Section */}
      <div id="imageContainer" className="col-lg-8 offset-lg-2 mt-5">
        <h3>Check-in</h3>
        <img
          id="videoStream"
          src="https://via.placeholder.com/600"
          alt="video stream"
          width="600px"
        />
        {/* Check-in button to trigger the pop-up */}
        <button
          onClick={handleCheckInClick}
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Check-In
        </button>
      </div>

      {/* Footer */}
      <footer className="text-center p-4 bg-gray-800 text-white w-full mt-auto">
        <p>
          <i>&copy;2024 FRS. All rights reserved.</i>
        </p>
      </footer>

      {/* Pop-up Modal */}
      <Popup
        message="You have successfully checked in!"
        show={showPopup}
        onClose={handleClosePopup}
      />
    </div>
  );
}

export default App;
