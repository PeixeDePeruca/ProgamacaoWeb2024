import { checkToken } from "@/services/tokenConfig";
import { getCookie } from "cookies-next";
import styles from "@/styles/home.module.css";

export default function Home() {
  return (
    <main id={styles.mainContainer} className="flex min-h-screen flex-col">
      {/* Barra superior de navegação */}
      <nav className={styles.navBar}>

      <h1 className={styles.Header}>Olá Treinador, Bem vindo a o site aí :D </h1>
      
      </nav>

      {/* Container principal. Ele vai conter o GRID */}
      <div className={styles.mainContainer}>

        {/* Painel esquerdo */}
        <div className={styles.leftContainer}>
        {/*<img src="/Haunter.png" alt="" />*/}
        <img src="/Cynthia_totosa.png" alt="" />
        <h1 className={styles.leftText}>TREINADORAS POKÉMON SOLTEIRAS PERTO DE SUA ÁREA➡️<a href="https://i.imgur.com/QRahrvn.jpeg" target="_blank" rel="noopener noreferrer"><span className={styles.leftText2}> CLIQUE AQUI E CONFIRA! </span></a>⬅️</h1>

        </div>

        {/* Painel direito */}
        <div className={styles.rightContainer}>

        </div>

      </div>

    </main>
  );
}

export function getServerSideProps({ req, res }: any) {
  try {
    const token = getCookie('authorization', { req, res });

    if (!token) {
      throw new Error('Invalid Token');
    }
    else {
      checkToken(token);
    }

    return {
      props: {}
    }

  }
  catch (err) {
    return {
      redirect: {
        permanent: false,
        destination: '/user/login'
      },
      props: {}
    }
  }
}
 


