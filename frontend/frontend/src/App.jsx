import { useState } from "react";
import axios from "axios";

export default function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const analyze = async () => {
    if (!url.trim()) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await axios.post(
        "https://page-pulse-backend-4ank.onrender.com/api/analyze",
        { url }
      );

      setResult(response.data.data);
    } catch (err) {
      setError(
        err.response?.data?.detail || "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  };

  const scoreLabel =
  result?.seo_score >= 90
    ? "Excellent"
    : result?.seo_score >= 70
    ? "Good"
    : "Needs Improvement";

const scoreColor =
  result?.seo_score >= 90
    ? "bg-green-500"
    : result?.seo_score >= 70
    ? "bg-yellow-500"
    : "bg-red-500";

  const Card = ({ title, value }) => (
    <div className="bg-white rounded-2xl shadow-lg p-5 border">
      <p className="text-gray-500 text-sm">{title}</p>
      <h2 className="text-xl font-bold mt-2 break-words">
        {value}
      </h2>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">

      <div className="max-w-6xl mx-auto">

        <h1 className="text-5xl font-extrabold text-center text-blue-700">
          Page Pulse
        </h1>

        <p className="text-center text-gray-600 mt-3 mb-10">
          Website SEO & Accessibility Analyzer
        </p>

        <div className="bg-white rounded-2xl shadow-xl p-6 flex flex-col md:flex-row gap-4">

          <input
            className="flex-1 border rounded-xl p-4 text-lg outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="https://example.com"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />

          <button
            onClick={analyze}
            className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition"
          >
            Analyze
          </button>

        </div>

        {loading && (
          <div className="text-center mt-10 text-blue-600 text-xl font-semibold">
            Analyzing Website...
          </div>
        )}

        {error && (
          <div className="bg-red-100 text-red-700 rounded-xl p-4 mt-8">
            {error}
          </div>
        )}

        {result && (
          <>
            <div className={`${scoreColor} rounded-3xl shadow-xl text-white p-8 mt-10`}>

  <p className="uppercase tracking-widest opacity-80">
    SEO Score
  </p>

  <h1 className="text-7xl font-extrabold mt-2">
    {result.seo_score}/100
  </h1>

  <p className="text-2xl font-semibold mt-2">
    {scoreLabel}
  </p>

  <p className="mt-4 text-sm break-all opacity-90">
    {result.url}
  </p>

</div>

            {/* Metrics */}

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">

              <Card title="HTTP Status" value={result.http_status} />

              <Card
                title="Response Time"
                value={`${result.response_time_ms} ms`}
              />

              <Card
                title="Word Count"
                value={result.word_count}
              />

              <Card
                title="H1 Count"
                value={result.h1_count}
              />

              <Card
                title="Images Missing ALT"
                value={result.images_missing_alt}
              />

              <Card
                title="Title"
                value={result.title || "Not Available"}
              />

              <div className="md:col-span-2 lg:col-span-3">
                <Card
                  title="Meta Description"
                  value={result.meta_description || "Not Available"}
                />
              </div>

            </div>

            {/* Recommendations */}

            <div className="bg-white rounded-2xl shadow-xl p-6 mt-8">

              <h2 className="text-2xl font-bold mb-5">
                Recommendations
              </h2>

              <ul className="space-y-3">

                {result.recommendations.map((item, index) => (

                  <li
                    key={index}
                    className="border-b pb-3"
                  >
                    {item}
                  </li>

                ))}

              </ul>

            </div>
          </>
        )}

           </div>

      <footer className="text-center text-gray-500 text-sm py-6 mt-10">
        Built for{" "}
        <a
          href="https://digitalheroesco.com"
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 hover:underline"
        >
          Digital Heroes Training Task
        </a>
      </footer>

    </div>
  );
}