class Solution:

    def encode(self, strs: List[str]) -> str:
        cantCadenas = len(strs)
        cadena1Cod = str(cantCadenas) + ","
        cadena2Cod = ''
        for cadena in strs:
            cadena1Cod = cadena1Cod + str(len(cadena)) + ","
            cadena2Cod = cadena2Cod + cadena

        cadenaCod = cadena1Cod + cadena2Cod

        return cadenaCod

    def decode(self, s: str) -> List[str]:
        # cantCadenas = primer num. hasta primera ,
        coma = s.index(",")
        cantCadenas = int(s[:coma])

        arrDeco = []
        if cantCadenas == 0:
            return arrDeco

        # s = s - primer num. hasta primera ,
        s = s[coma + 1:]

        # cadenaTamCad = contamos cantCadenas ,'s y cortamos ahí
        pos = -1
        for _ in range(cantCadenas):
            pos = s.index(",", pos + 1)
        cadenaTamCad = s[:pos]

        # cadenaCadenas = lo que queda después de cadenaTamCad
        cadenaCadenas = s[pos + 1:]

        for i in range(cantCadenas):
            # tamCadAct = num. antes de la primera coma
            tamCadAct = int(cadenaTamCad.split(",", 1)[0])

            # arrDeco.append(cadenaCadenas cortada hasta tamCadAct)
            arrDeco.append(cadenaCadenas[:tamCadAct])

            # cadenaTamCad = cadenaTamCad - número hasta primera ,
            coma = cadenaTamCad.find(",")
            cadenaTamCad = cadenaTamCad[coma + 1:] if coma != -1 else ""

            # cadenaCadenas = cadenaCadenas - tamCadAct-ésimos caracteres
            cadenaCadenas = cadenaCadenas[tamCadAct:]

        return arrDeco