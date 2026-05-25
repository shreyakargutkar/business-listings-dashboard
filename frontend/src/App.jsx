import { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  PieChart,
  Pie,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";

const API_BASE = "http://127.0.0.1:8000";

const COLORS = [
  "#3b82f6",
  "#10b981",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6",
  "#06b6d4",
];

function App() {
  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);
  const [loading, setLoading] = useState(true);
git push -u origin main
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const cityRes = await axios.get(
        `${API_BASE}/city-wise-count`
      );

      const categoryRes = await axios.get(
        `${API_BASE}/category-wise-count`
      );

      const sourceRes = await axios.get(
        `${API_BASE}/source-wise-count`
      );

      setCityData(
        Array.isArray(cityRes.data)
          ? cityRes.data
          : []
      );

      setCategoryData(
        Array.isArray(categoryRes.data)
          ? categoryRes.data
          : []
      );

      setSourceData(
        Array.isArray(sourceRes.data)
          ? sourceRes.data
          : []
      );
    } catch (error) {
      console.error(error);
      alert(
        "Backend not running or API issue"
      );
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div
        style={{
          height: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: "28px",
        }}
      >
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          marginBottom: "30px",
        }}
      >
        Business Listings Dashboard
      </h1>

      <div
        style={{
          display: "flex",
          gap: "20px",
          justifyContent: "center",
          marginBottom: "40px",
        }}
      >
        <div
          style={{
            border: "1px solid gray",
            padding: "20px",
            borderRadius: "10px",
            width: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Cities</h3>
          <h2>{cityData.length}</h2>
        </div>

        <div
          style={{
            border: "1px solid gray",
            padding: "20px",
            borderRadius: "10px",
            width: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Categories</h3>
          <h2>{categoryData.length}</h2>
        </div>

        <div
          style={{
            border: "1px solid gray",
            padding: "20px",
            borderRadius: "10px",
            width: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Sources</h3>
          <h2>{sourceData.length}</h2>
        </div>
      </div>

      <h2 style={{ textAlign: "center" }}>
        City Wise Business Count
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <BarChart data={cityData}>
          <XAxis dataKey="city" />
          <YAxis />
          <Tooltip />
          <Bar
            dataKey="count"
            fill="#3b82f6"
          />
        </BarChart>
      </ResponsiveContainer>

      <h2
        style={{
          textAlign: "center",
          marginTop: "50px",
        }}
      >
        Category Wise Count
      </h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <PieChart>
          <Pie
            data={categoryData}
            dataKey="count"
            nameKey="category"
            outerRadius={120}
            label
          >
            {categoryData.map(
              (entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={
                    COLORS[
                      index %
                        COLORS.length
                    ]
                  }
                />
              )
            )}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>

      <h2
        style={{
          textAlign: "center",
          marginTop: "50px",
        }}
      >
        Source Wise Count
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <BarChart data={sourceData}>
          <XAxis dataKey="source" />
          <YAxis />
          <Tooltip />
          <Bar
            dataKey="count"
            fill="#10b981"
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;