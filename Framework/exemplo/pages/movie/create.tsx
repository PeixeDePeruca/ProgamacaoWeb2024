


import Head from "next/head";
import styles from "@/styles/createMovie.module.css";

export default function createMovie() {
    return (
        <main className={`flex min-h-screen flex-col ${styles.mainContainer}`}>
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={styles.formContainer}>
                    
                    <input className={styles.Menu} type="text" placeholder="Nome" />

                    <p>Data de Lançamento</p>

                    
                    <input className={styles.Menu} type="date" />
                   
                    <p>Imagem do filme</p>
                    

                    <input className={styles.Menu} type="file" 
                     accept=".png, .jpg, .jpeg, .jfif" />

                    
                    <br /><textarea className={styles.Menu} placeholder="Descrição" />

                    <br /><input className={styles.SendBtn} type="submit" value="Enviar" />
                </form>
            </div>
        </main>
    );
}
