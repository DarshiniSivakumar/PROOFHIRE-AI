import axios from "axios";

export const getCandidates = async () => {
  const res = await axios.get("http://127.0.0.1:5000/api/candidates");
  return res.data;
};