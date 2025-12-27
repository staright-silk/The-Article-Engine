'use client';

import { useState } from 'react';
import styles from './page.module.css';

export default function Home() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<{ title: string, content: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setHasSearched(true);
    try {
      const res = await fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}`);
      if (!res.ok) throw new Error('Failed to fetch');
      const data = await res.json();
      setResults(data.results || []);
    } catch (err) {
      console.error(err);
      // Optional: set error state
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1 className={styles.title}>The Article Writer</h1>
          <p className={styles.subtitle}>Explore the depths of knowledge</p>
        </header>

        <form onSubmit={handleSearch} className={styles.searchForm}>
          <div className={styles.inputWrapper}>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search for articles..."
              className={styles.searchInput}
            />
            <button type="submit" className={styles.searchButton} disabled={loading}>
              {loading ? (
                <span className={styles.loader}></span>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              )}
            </button>
          </div>
        </form>

        <section className={styles.resultsSection}>
          {hasSearched && results.length === 0 && !loading && (
            <div className={styles.noResults}>
              <p>No articles found matching "{query}"</p>
            </div>
          )}

          <div className={styles.grid}>
            {results.map((r, i) => (
              <article key={i} className={styles.card}>
                <h2 className={styles.cardTitle}>{r.title}</h2>
                <div className={styles.cardContent}>
                  {r.content}
                </div>
              </article>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
