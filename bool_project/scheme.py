# elementary base class
class KS_Methods(object):
    # conjunction
    def con(self, a: bool | int, b: bool | int) -> bool | int:
        return a and b

    # desjunction
    def des(self, a: bool | int, b: bool | int) -> bool | int:
        return a or b

    # inverter
    def inv(self, a: bool | int) -> bool | int:
        return not a


class KSchemes(KS_Methods):
    # schemes
    def emergency_exit(self, x: bool | int, y: bool | int, z: bool | int) -> bool | int:
        left_side_of_equation = self.con(self.inv(self.des(x, y)), self.con(x, y))
        right_side_of_equation = self.con(self.con(x, self.inv(y)), z)
        return int(self.des(left_side_of_equation, right_side_of_equation))

    def decoder(self, x: bool | int, y: bool | int) -> list[bool | int]:
        responce = []
        responce.append(int(self.con(self.inv(x), self.inv(y))))
        responce.append(int(self.con(self.inv(x), y)))
        responce.append(int(self.con(x, self.inv(y))))
        responce.append(int(self.con(x, y)))
        return responce

    def encoder(self, x: bool | int, y: bool | int, z: bool | int, f: bool | int) -> list[bool | int]:
        responce = []
        responce.append(int(self.des(z, f)))
        responce.append(int(self.des(y, f)))
        return responce

    def mltpx(self, p1, p2, p3, p4, x0, x1) -> str:
        data_dc = self.decoder(x0, x1)
        #1
        b1 = self.con(p1, data_dc[0])
        #2
        b2 = self.con(p2, data_dc[1])
        #3
        b3 = self.con(p3, data_dc[2])
        #4
        b4 = self.con(p4, data_dc[3])
        #5 
        return b1 or b2 or b3 or b4

    def multiplexor_formula(p1, p2, p3, p4, x0, x1):
        y = not x0 and not x1 and p1 or not x0 and not x1 and p2 or not x0 and not x1 and p3 or not x0 and not x1 and p4
        return y

solver = KSchemes()
# print(solver.emergency_exit(1, 0, 1))

# print(solver.decoder(1, 1))
# print(solver.decoder(1, 0))
# print(solver.decoder(0, 1))
# print(solver.decoder(0, 0))

# print(solver.encoder(0, 0, 0, 1))
# print(solver.encoder(0, 0, 1, 0))
# print(solver.encoder(0, 1, 0, 0))
# print(solver.encoder(1, 0, 0, 0))

print(solver.mltpx(1, 0, 0, 0, 0, 0))
