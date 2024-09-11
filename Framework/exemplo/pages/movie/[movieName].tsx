import { checkToken } from '@/services/tokenConfig';
import styles from '@/styles/MovieName.module.css'
import { getCookie } from 'cookies-next';
import { useRouter } from 'next/router';
import { comment } from 'postcss';
import { useState, useEffect } from 'react';

export default function movie({ movieName }: any) {
    const router = useRouter();

    // Formulário de avaliação

    const [ratingForm, setRatingForm] = useState(
        {
            value: 0,
            comment: ''
        }
    );

    const [data, setData]: any = useState(undefined);

    function handleFormEdit(event: any, field: string) {
        setRatingForm({
            ...ratingForm,
            [field]: event.target.value
        })
    }

    async function formSubmit(e: any) {
        e.preventDefault();

        try {
            const cookieAuth = getCookie('authorization');

            const tokenInfos = checkToken(cookieAuth);

            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify({
                    value: Number(ratingForm.value),
                    comment: ratingForm.comment,
                    email: tokenInfos.email,
                    movieName: movieName
                })
            });

            const responseJson = await response.json();

            alert(responseJson.message);
            router.reload();

        }
        catch (err) {
            console.log(err);
            alert(err);
        }
    }

    async function fetchData() {
        try {
            const response = await fetch(`/api/action/movie/find?name=` + movieName, {
                method: 'GET'
            });

            const responseJson = await response.json();

            setData(responseJson.data);
        }
        catch (err) {
            console.log(err);
            alert('Algo deu Errado');
        }
    }

    useEffect(() => {

        fetchData();
    }, [])

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            {
                data != undefined ?

                    <div className={styles.page}>
                        <div className={styles.movie}>
                            <img src={data.imageURL} alt="" className={styles.img} />
                            <div className={styles.movieInfos}>
                                <h2>{data.name}</h2>
                                <p>{data.relaseDate}</p>
                                <p>{data.description}</p>
                                <p>Generos: TALES</p>
                            </div>
                        </div>

                        <iframe className={styles.video} height="800" src={"https://www.youtube.com/embed/" + data.videoURL}>
                        </iframe>

                        <form className={styles.formRating} onSubmit={formSubmit}>
                            <h2>Digite uma nota (0 a 5)</h2>
                            <input onChange={(e) => { handleFormEdit(e, 'value') }} className={styles.value} type="number" /><br />
                            <textarea onChange={(e) => { handleFormEdit(e, 'comment') }} className={styles.comment} placeholder='Digite seu Comentário'></textarea>
                            <input className={styles.submitBtn} type="submit" />

                        </form>

                        <div className={styles.ratings}>

                            {

                                data.ratings.map((rating: any) => (
                                    <div className={styles.ratingsCard}>
                                        <div className={styles.rInfos}>
                                            <label className={styles.rUser}>{rating.user.userName}</label>
                                            <label className={styles.rValue}>{rating.value} /5 Recomendação</label><br />
                                        </div>
                                        <div className={styles.rComment}>
                                            <label>{rating.comment}</label>
                                        </div>
                                    </div>
                                ))


                            }

                        </div>



                    </div>

                    :

                    <p>Erro 404 Filme não encontrado</p>
            }
        </main>
    );
}


export function getServerSideProps(context: any) {

    const { movieName } = context.query;

    return {
        props: { movieName }
    }
}