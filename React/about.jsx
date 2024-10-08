import React from 'react';

const AboutUs = () => {
    return (
    <div className = "bg-gradient-to-b from-gray-100 to-gray-300 min-h-screen flex flex-col items-center">
        <div className="navbar bg-gray-800 text-white p-4 flex items-center w-full">
        <div className="text-3xl font-permanent-marker flex-shrink-0">
            FRS
        </div>
        <div className="flex-grow flex justify-center">
            <a href="index.html" className="hover:text-gray-300 mx-4">Home</a>
            <a href="about.html" className="hover:text-gray-300 mx-4">About Us</a>
            <a href="terms.html" className="hover:text-gray-300 mx-4">Terms and Conditions</a>
        </div>
    </div>
    <div className="container mx-auto mt-8 flex-grow flex flex-col items-center">
        <section className="bg-white p-6 shadow-md rounded-lg mb-8 w-full max-w-2xl text-center">
            <h2 className="text-3xl font-bold mb-4 text-gray-800 underline">Our Story</h2>
            <p className="text-gray-700">
                We are developing a face recognition system for our senior design project. 
                This software product aims to identify and recognize individuals, particularly students, 
                based on specific facial characteristics such as eyes and mouth. 
                The primary users targeted are colleges and universities. 
                The general architecture of our software product comprises five key components: 
                data collection, image processing, face detection, face recognition, and database management.
            </p>
        </section>
        <section className="bg-white p-6 shadow-md rounded-lg mb-8 w-full max-w-2xl text-center">
            <h2 className="text-3xl font-bold mb-4 text-gray-800 underline">Our Team</h2>
            <ul className="space-y-8">
                <li className="text-center">
                    <h3 className="text-xl font-semibold text-gray-800">Kai Chun Goh</h3>
                    <img src="/images/kai.png" alt="Kai Chun Goh" className="w-24 h-24 rounded-full mx-auto mb-4" />
                    <p className="text-gray-700">
                        Kai Chun Goh has cultivated his expertise in the C++ language through various self-initiated projects.
                        His curiosity now leads him towards exploring programming languages associated with frontend development,
                        aiming to broaden his skill set and enhance his career prospects.
                    </p>
                </li>
                <li className="text-center">
                    <h3 className="text-xl font-semibold text-gray-800">Khang Huynh Bao Duong</h3>
                    <img src="/images/khang.png" alt="Khang Huynh Bao Duong" className="w-24 h-24 rounded-full mx-auto mb-4" />
                    <p className="text-gray-700">
                        Khang Huynh Bao Duong, an employee at NetApp, boasts proficiency in an array of programming languages 
                        including C++, Python, HTML, CSS, JS, and SQL. With a thirst for knowledge, Duong is keen on diving deeper 
                        into AI-related programming languages, driven by a passion for emerging technologies.
                    </p>
                </li>
                <li className="text-center">
                    <h3 className="text-xl font-semibold text-gray-800">Wei Jin Gnoh</h3>
                    <img src="/images/wei.png" alt="Wei Jin Gnoh" className="w-24 h-24 rounded-full mx-auto mb-4" />
                    <p className="text-gray-700">
                        Wei Jin Gnoh's journey in programming has been marked by independent projects, where he has mastered C++ and Python. 
                        Eager to stay ahead in the dynamic tech landscape, Gnoh sets his sights on learning AI-related programming languages, 
                        recognizing their significance in shaping future innovations.
                    </p>
                </li>
                <li className="text-center">
                    <h3 className="text-xl font-semibold text-gray-800">Yu Qing Leong</h3>
                    <img src="/images/yu.png" alt="Yu Qing Leong" className="w-24 h-24 rounded-full mx-auto mb-4" />
                    <p className="text-gray-700">
                        Yu Qing Leong, currently employed as a Software Tester at NetApp, possesses a versatile skill set encompassing C, HTML, 
                        and Python, along with proficiency across multiple operating systems. Leong's career aspirations revolve around mastering 
                        backend-related programming languages, a step towards achieving a more holistic understanding of software development.
                    </p>
                </li>
            </ul>
        </section>
        <section className="bg-white p-6 shadow-md rounded-lg mb-8 w-full max-w-2xl text-center">
            <h2 className="text-3xl font-bold mb-4 text-gray-800">Our Mission</h2>
            <p className="text-gray-700">
                Successfully implementing a face recognition system that can
                accurately identify and recognize individuals based on specific facial characteristics.
            </p>
        </section>
    </div>
    <div>
    <footer className="text-center p-4 bg-gray-800 text-white w-full">
        <p><i>&copy;2024 FRS. All rights reserved.</i></p>
    </footer>
    </div>
    </div>
    );
};

export default AboutUs;
