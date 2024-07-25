// pages/register.tsx
import Head from "next/head";
import styles from '@/styles/register.module.css';

export default function Register() {
    return (
        <main className={styles.background}>
            <Head>
                <title>Cadastro</title>
            </Head>
            <h1 className={styles.text}>PÁGINA  DE  CADASTRO</h1>
            <form className={styles.container}>
 
                <input className={styles.input} type="text" placeholder="Nome" /><br />
                <input className={styles.input} type="email" placeholder="Email" /><br />
                <input className={styles.input} type="text" placeholder="Nome de Usuário" /><br />
                <input className={styles.input} type="password" placeholder="Senha" /><br />
                <input className={styles.input} type="password" placeholder="Confirmação da senha" /><br />
 
            </form>
 

        </main>
    );
}
