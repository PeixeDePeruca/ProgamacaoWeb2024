// pages/register.tsx
import Head from "next/head";
import styles from '@/styles/register.module.css';

export default function Register() {
    return (
        <main>
            <Head>
                <title>Cadastro</title>
            </Head>
            <h1 className={styles.text}>Página de Cadastro</h1>
        </main>
    );
}
