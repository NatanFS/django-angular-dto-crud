import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PersonCrudRoutingModule } from './person-crud-routing.module';
import { PersonListComponent } from './person-list/person-list.component';


@NgModule({
  declarations: [
    PersonListComponent
  ],
  imports: [
    CommonModule,
    PersonCrudRoutingModule
  ]
})
export class PersonCrudModule { }
