import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { Person } from './person.model';

@Injectable({
  providedIn: 'root'
})
export class PersonService {

  private baseURL = "http://localhost:8000";
  private endpoint = "persons";

  constructor(private httpClient: HttpClient) { 
    
  }

  list(): Observable<Person[]> {
    return this.httpClient.get<Person[]>(`${this.baseURL}/${this.endpoint}/`);
  }

  create(person: Person): Observable<Person>{
    return this.httpClient.post<Person>(`${this.baseURL}/${this.endpoint}/`, person);
  }

  findById(id: number): Observable<Person> {
    return this.httpClient.get<Person>(`${this.baseURL}/${this.endpoint}/${id}/`);
  }

  update(person: Person): Observable<Person> {
    console.log(person)
    return this.httpClient.put<Person>(`${this.baseURL}/${this.endpoint}/${person.id}/`, person);
  }

  delete(id: number): Observable<any> {
    return this.httpClient.delete(`${this.baseURL}/${this.endpoint}/${id}/`);
  }

  getIdealWeight(id: number): Observable<any> {
    return this.httpClient.get(`${this.baseURL}/${this.endpoint}/${id}/ideal-weight/`);
  }

  search(criteria: any): Observable<Person[]> {
    let params = new HttpParams();
    Object.keys(criteria).forEach(key => {
      if (criteria[key]) {
        params = params.set(key, criteria[key]);
      }
    });

    return this.httpClient.get<Person[]>(`${this.baseURL}/${this.endpoint}/`, { params })
      .pipe(
        catchError(error => {
          console.error('Error during search:', error);
          throw error;
        })
      );
  }

}
