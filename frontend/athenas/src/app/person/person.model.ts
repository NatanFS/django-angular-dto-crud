export interface Person {
    id: number;
    name: string;
    birth_date: Date;
    cpf: string;
    sex: 'M' | 'F';
    height: number;
    weight: number;
}