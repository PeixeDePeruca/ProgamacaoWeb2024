import { NextApiRequest , NextApiResponse } from "next";
import { createUserController } from "../../controller/userController";

export default async ( req:NextApiRequest , res:NextApiResponse ) =>{
    if ( req.method != 'POST' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    const { name , email , username , password , ConfirmPassword } = req.body;


    // Enviar para o controller
    const response = await createUserController(name , email , username , password , ConfirmPassword);

    return res.status(response.status).json(response.message);
}