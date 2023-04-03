
<h1>Face Preprocessing for Facial Recognition</h1>

<p>This repository contains a Python script that preprocesses images containing faces to make them suitable for facial recognition. The preprocessing includes converting the images to grayscale, cropping the faces, and resizing them to a fixed size. The script uses OpenCV and Matplotlib for image processing and display.</p>

<h2>Dependencies</h2>

<ul>
    <li>Python 3.x</li>
    <li>OpenCV (cv2)</li>
    <li>Matplotlib</li>
</ul>

<p>You can install the required libraries using pip:</p>

<pre><code>pip install opencv-python
pip install matplotlib
</code></pre>

<h2>Usage</h2>

<ol>
    <li>Clone this repository or download the <code>image_preprocessing.py</code> file.</li>
    <li>Update the file paths for the face and eye cascade files, as well as the input image paths, in the <code>main()</code> function in the <code>image_preprocessing.py</code> file:
        <pre><code>face_cascade_path = "path/to/haarcascade_frontalface_default.xml"
image1_path = "path/to/mugshot1.jpg"
image2_path = "path/to/mugshot2.jpg"
</code></pre>
    </li>
    <li>Run the <code>image_preprocessing.py</code> script:
        <pre><code>python image_preprocessing.py
</code></pre>
    </li>
    <li>
        <p>The script will process the input images, extract and preprocess the faces, and display the processed images using Matplotlib. Press any key to close the displayed image and show the next one.</p>
    </li>
    <li>Processed images will be saved in the working directory with the format <code>processed_&lt;input_image_name&gt;_&lt;face_index&gt;.jpg</code>.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

