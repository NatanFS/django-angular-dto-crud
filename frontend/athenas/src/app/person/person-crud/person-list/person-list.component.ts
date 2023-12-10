import { Component, OnInit } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { Person } from '../../person.model';
import { PersonService } from '../../person.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-person-list',
  templateUrl: './person-list.component.html',
  styleUrl: './person-list.component.scss'
})
export class PersonListComponent implements OnInit{
  persons$: Observable<Person[]>;
  displayedColumns = ['id', 'name', 'sex', 'weight', 'height', 'birth_date', 'cpf',];

  searchForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private personService: PersonService,
    private router: Router
  ) {
    this.persons$ = this.personService.list();
    this.searchForm = this.formBuilder.group({
      name: [''],
      sex: [''],
      weight: [''],
      height: [''],
      birth_date: [''],
      cpf: [''],
    });
  }
  
  ngOnInit() {
    this.listPersons();
  }

  listPersons() {
    const searchParams = this.searchForm.value;
    
    this.persons$ = this.personService.search(searchParams)
      .pipe(
        catchError(error => {
          alert("Ocorreu um erro ao buscar pessoas." + JSON.stringify(error));
          throw error;
        })
      );
  }



  onPersonClick(row: any){
    this.router.navigateByUrl('/persons/' + row.id);
  }

}
