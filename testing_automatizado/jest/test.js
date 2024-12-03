const funciones = require('./index.js')


test('La suma de 3 + 5 es 8', function(){
    let result = funciones.miFuncion(3, 5);
    
    expect( result ).toBe( 8 );  // Compara si el resultado es 8
});

test('La suma de 2 + 2 es 5', function(){
    let result = funciones.miFuncion(2, 2);
    
    expect( result ).toBe( 5 );  // Compara si el resultado es 5
});