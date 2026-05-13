export default function CandidateCard({ candidate }) {
  return (
    <div className="border p-4 rounded-lg shadow">
      <h2 className="font-bold">{candidate.name}</h2>
      <p>{candidate.role}</p>
      <p>Score: {candidate.overall_score}</p>
    </div>
  );
}