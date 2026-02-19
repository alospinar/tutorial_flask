export class Cancion {
    constructor(
        public titulo: string,
        public minutos: number,
        public segundos: number,
        public interprete: string,
        public id?: number,
        public albumes?: any[]
    ) {

     }
}
