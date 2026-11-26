from sympy import symbols
from sympy.logic.inference import satisfiable

P, Q = symbols('P Q')

knowledge = P & (P >> Q)

result = satisfiable(knowledge & ~Q)

if result is False:
    print("Q is True")
else:
    print("Inference failed")
