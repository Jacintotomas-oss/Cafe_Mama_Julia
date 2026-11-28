import { useEffect, useState } from "react";

const API = "http://127.0.0.1:8000/api";

export default function Menu(){
    //const solo declara variables pero quien guarda todo es useState
    const [activa, setActiva] = useState(0);
    const [categorias, setCategorias] = useState([]);

    useEffect(() => {
        // Fetch categories from API
        fetch(`${API}/menu/`)
            .then((response) => response.json())
            .then((data) => setCategorias(data));
    }, []);
    const productos = categorias[activa]?.productos ?? [];


return (
  <section id="menu" className="menu">
    <h2>Nuestro menú</h2>

    <div className="pills">
      {categorias.map((c, i) => (
        <button
          key={c.id}
          className={i === activa ? "pill on" : "pill"}
          onClick={() => setActiva(i)}
        >
          {c.nombre}
        </button>
      ))}
    </div>

    <div className="productos">
      {productos.map((p) => (
        <article key={p.id} className="producto">
          <div className="producto-foto">
            {p.foto && <img src={p.foto} alt={p.nombre} />}
          </div>
          <h3>{p.nombre}</h3>
          {p.descripcion && <p className="producto-desc">{p.descripcion}</p>}
          <strong className="producto-precio">${p.precio}</strong>
        </article>
      ))}
    </div>

    {productos.length === 0 && (
      <p className="menu-vacio">Pronto habrá productos aquí.</p>
    )}
  </section>
);
}