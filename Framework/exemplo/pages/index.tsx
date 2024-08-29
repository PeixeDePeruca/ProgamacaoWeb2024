import { checkToken } from "@/services/tokenConfig";
import { getCookie, deleteCookie } from "cookies-next";
import styles from "@/styles/home.module.css";
import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();
  const [data, setData] = useState<any>(undefined);

  async function fetchData() {
    try {
      const response = await fetch('/api/action/movie/select', {
        method: 'GET'
      });
      const responseJson = await response.json();
      setData(responseJson.data);
    } catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  function logOut() {
    deleteCookie('authorization');
    router.push(`/user/login`);
  }

  function movieClick(movieName: string) {
    router.push(`/movie/` + movieName);
  }

  return (
    <main id={styles.mainContainer} className="flex min-h-screen flex-col">
      {/* Barra superior de navegação */}
      <nav className={styles.navBar}>
        <h1 className={styles.Header}>Olá Treinador, Bem vindo ao site aí :D </h1>

        <Link href={`/movie/create`} className= {styles.createMovie}>Criar Filme</Link>
        <button className={styles.logoutBtn} onClick={logOut}>Logout</button>
      </nav>

      {/* Container principal. Ele vai conter o GRID */}
      <div className={styles.mainContainer}>
        {/* Painel esquerdo */}
        <div className={styles.leftContainer}>
          {/*<img src="/Haunter.png" alt="" />*/}
          <img src="/Cynthia_totosa.png" alt="" />
          <h1 className={styles.leftText}>
            TREINADORAS POKÉMON SOLTEIRAS PERTO DE SUA ÁREA➡️
            <a href="https://i.imgur.com/QRahrvn.jpeg" target="_blank" rel="noopener noreferrer">
              <span className={styles.leftText2}> CLIQUE AQUI E CONFIRA! </span>
            </a>
            ⬅️
          </h1>
        </div>

        {/* Painel direito */}
        <div className={styles.rightContainer}>
          {data != undefined && Array.isArray(data) ? (
            data.map((movie: any) => (
              <div key={movie.name} onClick={() => { movieClick(movie.name) }} className={styles.card}>
                <img src={movie.img} className={styles.cardImg} alt="" />
                {/*<iframe src= {movie.videoURL} className={styles.cardImg} ></iframe>*/}
                <div className={styles.cardInfos}>
                  <h2>{movie.name}</h2>
                  <p>{movie.releaseDate}</p>
                  <p>Gêneros do Filme</p>
                  <p>{movie.description}</p>
                </div>
              </div>
            ))
          ) : (
            <p>No movies Found</p>
          )}
        </div>
      </div>
    </main>
  );
}

export async function getServerSideProps({ req, res }: any) {
  try {
    const token = getCookie('authorization', { req, res });

    if (!token) {
      throw new Error('Invalid Token');
    } else {
      checkToken(token);
    }

    return {
      props: {}
    };
  } catch (err) {
    return {
      redirect: {
        permanent: false,
        destination: '/user/login'
      },
      props: {}
    };
  }
}
