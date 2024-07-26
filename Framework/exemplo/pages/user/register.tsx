// pages/register.tsx
import Head from "next/head";
import styles from '@/styles/register.module.css';
import { useState } from "react";
import Link from "next/link";


export default function Register() {

    const [ formData , setFormData ] = useState({
        
            name: "",
            email: "",
            username: "",
            password: "",
            ConfirmPassword: "" 
    }

    );

    function handleFormEdit(event:any , field:string) {
        setFormData({
            ...formData,
            [field]: event.target.value
        });

        console.log(formData);

    }

    async function formSubmit(event:any) {
        event.preventDefault();

        try {
            const response = await fetch(`/api/action/user/create` , {
                method: 'POST',
                headers: {'Content-type':'application/json'},
                body: JSON.stringify(formData)
            });

            const respondeJson = await response.json();

            alert(`${response.status} \n ${respondeJson}`);

        }
        catch (err) {
            console.log(err);
        }

    }


    return (
        <main id={styles.background} className="flex min-h-screen flex-col" >
            <Head>
                <title>Cadastro</title>
            </Head>

            <h1 className={styles.text}>PÁGINA  DE  CADASTRO</h1>

            <form className={styles.container} onSubmit={formSubmit}>
 
            
                <input className={styles.input} type="text" placeholder="Nome (Opcional)" onChange={(event) => {handleFormEdit(event , "name")}}  /><br />
                <input className={styles.input} type="email" placeholder="Email" onChange={(event) => {handleFormEdit(event , "email")}}  /><br />
                <input className={styles.input} type="text" placeholder="Nome de Usuário" onChange={(event) => {handleFormEdit(event , "username")}}  /><br />
                <input className={styles.input} type="password" placeholder="Senha" onChange={(event) => {handleFormEdit(event , "password")}}  /><br />
                <input className={styles.input} type="password" placeholder="Confirmação da senha" onChange={(event) => {handleFormEdit(event , "ConfirmPassword")}}  /><br />
 
                <input className={styles.CreateBtn} type="submit" value="Criar Conta" />
                <br />
                <Link className={styles.LoginBtn}   href={`/user/login`}>Já tenho uma conta</Link>
            </form>

            

        </main>
    );
}
