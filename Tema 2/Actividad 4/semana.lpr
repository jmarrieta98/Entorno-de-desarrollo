PROGRAM semana;
 USES CRT;
 VAR num:INTEGER;
BEGIN
 ClrScr;
 WRITE ('Escriba un numero para ver con que dia corresponde: ');
 READLN (num);
 IF num=1 THEN
 WRITE ('Lunes')
 ElSE IF num=2 THEN
 WRITE ('Martes')
 ELSE IF num=3 THEN
 WRITE ('Miercoles')
 ELSE IF num=4 THEN
 WRITE ('Jueves')
 ELSE IF num=5 THEN
 WRITE ('Viernes')
 ELSE IF num=6 THEN
 WRITE ('Sabado')
 ELSE IF num=7 THEN
 WRITE ('Domingo')
 ELSE
 WRITE ('Error al introducir el numero, debe de estar entre 1 y 7 ');
 Readln;
 ClrScr;
END.

