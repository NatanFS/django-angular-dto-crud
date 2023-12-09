import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PersonCrudRoutingModule } from './person-crud-routing.module';
import { PersonListComponent } from './person-list/person-list.component';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';

@NgModule({
  declarations: [
    PersonListComponent
  ],
  imports: [
    CommonModule,
    PersonCrudRoutingModule,
    
    MatProgressSpinnerModule,
    MatTableModule,
    MatButtonModule,
    MatToolbarModule
  ]
})
export class PersonCrudModule { }
