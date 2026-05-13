export default function ScoreChart({ score }) {
  return (
    <div className="mt-4">
      <div className="w-full bg-gray-200 rounded h-5">
        <div
          className="bg-blue-500 h-5 rounded"
          style={{ width: `${score}%` }}
        />
      </div>

      <p className="mt-2">
        Overall Score: {score}
      </p>
    </div>
  );
}