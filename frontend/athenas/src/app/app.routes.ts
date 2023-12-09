import { Routes } from '@angular/router';

export const routes: Routes = [
    { path: '', redirectTo: 'persons', pathMatch: 'full' },
    { path: 'persons', loadChildren: () => import('./person/person-crud/person-crud.module').then(m => m.PersonCrudModule) }
];
