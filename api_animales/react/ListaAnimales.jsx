import { useEffect, useState } from "react";
export default function ListaAnimales() {
  const [animales, setAnimales] = useState([]);
  const [error, setError] = useState("");
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/animales/")
      .then(r => { if (!r.ok) throw new Error("Error HTTP"); return r.json(); })
      .then(setAnimales).catch(() => setError("No se pudo cargar la lista"));
  }, []);
  if (error) return <p>{error}</p>;
  return <ul>{animales.map(a =>
    <li key={a.id}>{a.nombre} - {a.especie} - {a.raza} - {a.edad} años</li>
  )}</ul>;
}
