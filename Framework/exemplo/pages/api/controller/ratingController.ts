import { findMovieByName } from "../model/movie";
import { createRatingModel } from "../model/rating";
import { findUserByEmail } from "../model/user";

export async function createRating(_value: number, _email: string, _movieName: string, _comment = " ") {
    try {
        const userByEmail = await findUserByEmail(_email);

        if (userByEmail == undefined) {
            return { status: 404, message: 'User not found' };
        }

        const movieByName = await findMovieByName(_movieName);

        if (movieByName == undefined) {
            return { status: 404, message: 'Movie not found' };
        }

        const response = await createRatingModel(_value, _comment, userByEmail.id, movieByName.id);

        return { status: 201, message: 'Rating created', data: response };

    }
    catch (err) {
        return { status: 500, message: 'Something went wrong' };
    }
}