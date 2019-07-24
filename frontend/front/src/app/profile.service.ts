import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor() { }

  // getProfiles(){
  //   let url = ${environment.profileUrl}/api/profile/;
  //   return axios.get(url).then(response => data)
  // }
}
