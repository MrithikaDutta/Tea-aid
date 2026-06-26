import { useState } from "react";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handleAnalyze = async () => {
    if (!image) {
      alert("Please upload an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      setResult({
        disease: data.disease,
        confidence: data.confidence,
        severity: data.severity_percentage,
        grade: data.severity_grade,
        advice: data.advice,
      });
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong. Please check backend server.");
    }
  };

  return (
    <div className="app">
      <header className="navbar">
        <h2>TeaAid</h2>
        <nav>
          <a href="#home">Home</a>
          <a href="#analysis">Analysis</a>
          <a href="#about">About</a>
        </nav>
      </header>

      <section className="hero" id="home">
        <div>
          <p className="tagline">AI-Based Tea Leaf Disease Advisory System</p>
          <h1>Tea Leaf Disease Detection and Severity Estimation</h1>
          <p>
            Upload a tea leaf image to detect the disease, estimate severity,
            view segmentation output, and receive RAG-based treatment advice.
          </p>
          <a href="#analysis" className="start-btn">
            Start Analysis
          </a>
        </div>

        <div className="class-card">
          <h3>Supported Classes</h3>
          <p>Healthy</p>
          <p>Algal Leaf Spot</p>
          <p>Brown Blight</p>
          <p>Gray Blight</p>
          <p>Helopeltis</p>
        </div>
      </section>

      <section className="analysis" id="analysis">
        <h2>Disease Analysis</h2>
        <p className="section-subtitle">
          Upload a tea leaf image and run the system.
        </p>

        <div className="analysis-grid">
          <div className="card">
            <h3>Upload Image</h3>

            <label className="upload-box">
              <input type="file" accept="image/*" onChange={handleImageUpload} />

              {preview ? (
                <img src={preview} alt="Uploaded tea leaf" />
              ) : (
                <div>
                  <h1>+</h1>
                  <p>Click to upload image</p>
                </div>
              )}
            </label>

            <button onClick={handleAnalyze}>Analyze Image</button>
          </div>

          <div className="card">
            <h3>Prediction Result</h3>

            {result ? (
              <>
                <div className="result-row">
                  <span>Disease Class</span>
                  <strong>{result.disease}</strong>
                </div>

                <div className="result-row">
                  <span>Confidence</span>
                  <strong>{result.confidence}</strong>
                </div>

                <div className="result-row">
                  <span>Severity</span>
                  <strong>{result.severity}</strong>
                </div>

                <div className="grade-box">{result.grade}</div>
              </>
            ) : (
              <p className="empty">Prediction result will appear here.</p>
            )}
          </div>
        </div>

        <div className="output-grid">
          <div className="card">
            <h3>Segmentation Output</h3>
            <div className="segmentation-box">
              {preview ? (
                <img src={preview} alt="Segmentation placeholder" />
              ) : (
                <p>Segmentation overlay will appear here.</p>
              )}
            </div>
          </div>

          <div className="card">
            <h3>RAG-Based Advisory</h3>
            <p>{result ? result.advice : "Treatment advice will appear here."}</p>
          </div>
        </div>
      </section>

      <section className="about" id="about">
        <h2>About This System</h2>

        <div className="about-grid">
          <div className="card">
            <h3>Classification</h3>
            <p>EfficientNet-B0 detects the tea leaf disease class.</p>
          </div>

          <div className="card">
            <h3>Severity Estimation</h3>
            <p>SegFormer-B0 segments infected regions and estimates severity.</p>
          </div>

          <div className="card">
            <h3>Advisory Agent</h3>
            <p>RAG generates disease- and severity-based treatment advice.</p>
          </div>
        </div>
      </section>

      <footer>
        <p>
          AI-based advisory support only. Final treatment should be verified by
          agricultural experts.
        </p>
      </footer>
    </div>
  );
}

export default App;