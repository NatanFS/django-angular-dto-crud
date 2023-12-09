import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Person } from '../../person.model';
import { PersonService } from '../../person.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrl: './person-list.component.scss'
})
export class PersonListComponent implements OnInit{
  persons$: Observable<Person[]>;
  displayedColumns = ['id', 'name', 'sex', 'weight', 'height', 'birth_date', 'cpf',];

  constructor(
    private personService: PersonService,
    private router: Router
  ) {
    this.persons$ = this.personService.list();
  }
  
  ngOnInit() {
    this.listPersons();
  }

  listPersons() {
    this.persons$ = this.personService.list();
  }


  onPersonClick(row: any){
    this.router.navigateByUrl('/persons/' + row.id);
  }

}
