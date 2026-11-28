import "./App.css";
import Menu from "./menu";


const WHATSAPP = "503XXXXXXXX";

const destacadas = [
  { id: 1, titulo: "Promo de temporada", texto: "Conoce lo que preparamos este mes.", enlace: "#menu" },
  { id: 2, titulo: "Café de maíz", texto: "Una bebida que tienes que probar.", enlace: "#menu" },
  { id: 3, titulo: "Visítanos", texto: "Ven a conocer el local.", enlace: "#visitanos" },
];

export default function App() {
  return (
    <>
      <header className="nav">
        <a href="#inicio" className="logo">mamá Julia</a>
        <nav className="nav-links">
          <a href="#inicio">Inicio</a>
          <a href="#menu">Menú</a>
          <a href="#historia">Historia</a>
          <a href="#visitanos">Visítanos</a>
        </nav>
        <a className="btn" href={`https://wa.me/${WHATSAPP}`} target="_blank" rel="noreferrer">
          WhatsApp
        </a>
      </header>

      <main>
        <section id="inicio" className="hero">
          <div className="hero-texto">
            <p className="hero-etiqueta">Café, postres y buen rato</p>
            <h1>Una pausa para compartir</h1>
            <p className="hero-sub">Café de maíz, pasteles y más. Ven a probarlos.</p>
            <div className="hero-botones">
              <a className="btn" href="#menu">Ver menú</a>
              <a className="btn btn-claro" href="#visitanos">Visítanos</a>
            </div>
          </div>
          <img className="hero-foto" src="/negocio/hero.png" alt="Pie de calabaza y café de maíz de Mamá Julia" />
        </section>

        <section className="destacadas">
          {destacadas.map((d) => (
            <article key={d.id} className="tarjeta">
              <div className="tarjeta-foto" role="img" aria-label={d.titulo}></div>
              <h3>{d.titulo}</h3>
              <p>{d.texto}</p>
              <a href={d.enlace}>Ver más</a>
            </article>
          ))}
        </section>

        <Menu />

        <div className="banda">
          <div className="banda-interior">
            <section id="historia">
              <h2>Nuestra historia</h2>
              <p>Aquí va la historia de Mamá Julia Café.</p>
              <p>Escríbela con calma junto a tu madrina.</p>
            </section>

            <section id="visitanos">
              <h2>Visítanos</h2>
              <p>Dirección del local</p>
              <p>Horarios de atención</p>
              <a className="btn btn-lima" href={`https://wa.me/${WHATSAPP}`} target="_blank" rel="noreferrer">
                Escribir por WhatsApp
              </a>
            </section>
          </div>
        </div>
      </main>

      <footer className="pie">
        <span>Mamá Julia Café</span>
        <a href="https://www.instagram.com/mama_julia_cafe/" target="_blank" rel="noreferrer">
          Instagram
        </a>
      </footer>
    </>
  );
}