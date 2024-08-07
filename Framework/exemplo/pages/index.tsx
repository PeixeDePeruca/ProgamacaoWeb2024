import { checkToken } from "@/services/tokenConfig";
import { getCookie } from "cookies-next";
import styles from "@/styles/home.module.css";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col">
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
        <h1 className={styles.leftText}>TREINADORAS POKEMON SOLTEIRAS PERTO DE SUA ÁREA ➡️CLIQUE AQUI E CONFIRA!⬅️</h1>

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
 


