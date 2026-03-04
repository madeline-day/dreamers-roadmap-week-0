export default function HomePage() {
  const scholarships = [
    { id: 1, name: "Golden Door Scholars Program" },
    { id: 2, name: "TheDream.US National Scholarship" },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-green-700 text-white px-8 py-4 flex items-center justify-between shadow-md">
        <h1 className="text-xl font-bold">DREAMers Roadmap Admin</h1>
        <span className="text-sm opacity-80">Welcome, Admin</span>
      </nav>

      <main className="max-w-4xl mx-auto px-6 py-10">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-semibold text-gray-800">Scholarships</h2>
          <button className="bg-green-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-green-700 transition-colors">
            + Add Scholarship
          </button>
        </div>

        <div className="bg-white rounded-xl shadow overflow-hidden">
          <table className="w-full text-sm text-left">
            <thead className="bg-gray-100 text-gray-600 uppercase text-xs">
              <tr>
                <th className="px-6 py-3">#</th>
                <th className="px-6 py-3">Scholarship Name</th>
              </tr>
            </thead>
            <tbody>
              {scholarships.map((s) => (
                <tr key={s.id} className="border-t border-gray-100 hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-gray-400">{s.id}</td>
                  <td className="px-6 py-4 font-medium text-gray-800">{s.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}