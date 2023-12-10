import { NgModule } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';

import { PersonCrudRoutingModule } from './person-crud-routing.module';
import { PersonListComponent } from './person-list/person-list.component';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { PersonDetailComponent } from './person-detail/person-detail.component';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MAT_DATE_LOCALE, MatNativeDateModule, MatOptionModule } from '@angular/material/core';
import { MatSelectModule } from '@angular/material/select';

@NgModule({
  declarations: [
    PersonListComponent,
    PersonDetailComponent
  ],
  imports: [
    CommonModule,
    PersonCrudRoutingModule,

    MatProgressSpinnerModule,
    MatTableModule,
    MatButtonModule,
    MatToolbarModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDatepickerModule, 
    MatOptionModule,
    MatNativeDateModule,
    MatSelectModule

  ],
  providers: [
    { provide: MAT_DATE_LOCALE, useValue: 'pt-BR' },
    DatePipe
  ]
})
export class PersonCrudModule { }
