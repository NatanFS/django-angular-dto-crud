import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { PersonService } from '../../person.service';
import { catchError } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { Person } from '../../person.model';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrl: './person-detail.component.scss'
})
export class PersonDetailComponent implements OnInit{

  formGroup: FormGroup;
  person?: Person;

  constructor(
    private formBuilder: FormBuilder,
    private personService: PersonService,
    private router: Router,
    private route: ActivatedRoute,
    private datePipe: DatePipe
  ) {
    this.formGroup = this.formBuilder.group({
      id: [''],
      name: ['', Validators.required],
      sex: [''],
      birth_date: [''], 
      cpf: [''],
      weight: [''],
      height: [''],
    });
  }
  
  ngOnInit() {
    const personId = this.route.snapshot.paramMap.get('id');
  
    if (personId) {
      

      this.personService.findById(+personId).subscribe((person) => {
        this.person = person;

        this.formGroup.patchValue({
          id: person.id,
          name: person.name,
          sex: person.sex,
          birth_date: person.birth_date,
          cpf: person.cpf,
          weight: person.weight,
          height: person.height,
        });
  
        console.log(this.formGroup.value);
      });
    }
  }

  save() {
    console.log(this.formGroup.value)
    console.log(this.person)
    if (this.person && this.person.id) {
      this.personService.update(this.formGroup.value)
        .pipe(
          catchError(error => {
            alert("Ocorreu um erro ao atualizar a pessoa." + JSON.stringify(error));
            throw error; 
          })
        )
        .subscribe(updatedPerson => {
          this.router.navigateByUrl('/persons');
        });
    } else {
      this.personService.create(this.formGroup.value)
        .pipe(
          catchError(error => {
            alert("Ocorreu um erro ao cadastrar a pessoa." + JSON.stringify(error));
            throw error;
          })
        )
        .subscribe(createdPerson => {
          this.router.navigateByUrl('/persons');
        });
    }
  }

  delete() {
    if (!this.person){
      return
    }

    if(confirm("Deseja deletar a pessoa " + this.person.name)) {
      this.personService.delete(this.person.id)
        .pipe(
          catchError(error => {
            alert("Ocorreu um erro ao deletar a pessoa." + JSON.stringify(error));
            throw error; // Rethrow para manter o erro propagado
          })
        )
        .subscribe(() => {
          this.router.navigateByUrl('/persons');
        });
    }
  }

  getIdealWeight(){
    if (!this.person){
      return
    }

    this.personService.getIdealWeight(this.person.id).subscribe((idealWeight) => {
      alert('Seu peso ideal é: ' + idealWeight['ideal_weight']);
    });
  }

  onlyNumbers(e: any) {
    let charCode = e.charCode ? e.charCode : e.keyCode;
    if (charCode != 8 && charCode != 9) {
      let max = 11;      
      if ((charCode < 48 || charCode > 57)||(e.target.value.length >= max)) return false;
    }
    return true
  }

}
