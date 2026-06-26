import  test_packing.module_a
import  test_packing.module_b
from  test_package.module_a import Module_a, module_a_fuc,
moule_var_a

def main():
    print(module_a())
    print(module_a_fuc())
    print(moule_var_a)
    print(test_packing.module_b.module_b)
    print(test_packing.module_b.module_b_fuc())
    print(test_packing.module_b.moule_var_b) 