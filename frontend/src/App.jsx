import { BrowserRouter, Routes, Route } from "react-router-dom";
import RecruiterDashboard from "./pages/RecruiterDashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RecruiterDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}