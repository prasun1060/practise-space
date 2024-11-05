import { Injectable } from "@angular/core";
import { type UserData } from "./user.model";

@Injectable({
    providedIn: 'root'
})
export class UserService {

    private users: UserData[] = []

    registerUser(userData: UserData) {
        this.users.push(userData);
    }

    loginUser(userId: string, password: string) {
        let user = this.users.filter((user)=>{user.id === userId})[0]
        if (user.password === password) {
            return user
        } else {
            return null
        }
    }

}