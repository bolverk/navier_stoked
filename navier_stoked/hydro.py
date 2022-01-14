import sympy
from sympy.vector import CoordSys3D, gradient, curl, divergence
from argparse import ArgumentParser

geometries = ['cartesian',
              'cylindrical',
              'spherical']

aesthetic = {'cartesian':sympy.symbols('x y z'),
             'cylindrical':sympy.symbols('r phi z'),
             'spherical':sympy.symbols('r theta phi')}

def make_eqns(geometry='cartesian'):

    S = CoordSys3D('S',
                   transformation=geometry,
                   variable_names='xyz')
    t = sympy.Symbol('t')
    zeta, mu = sympy.symbols('zeta mu', positive=True)
    args = (t,S.x,S.y,S.z)
    v_1, v_2, v_3, rho, p = [f(*args) for f
                          in sympy.symbols('v_{1:4} rho p', cls=sympy.Function)]
    v = sum((v_n*vec for v_n, vec in zip((v_1, v_2, v_3),(S.i,S.j,S.k))), 0*S.i)
    res = v.diff(t)
    res += gradient(v.dot(v)/2) - (v^curl(v))
    res += gradient(p)/rho
    res -= (zeta+4*mu/3)*gradient(divergence(v))
    res += mu*curl(curl(v))
    res = res.subs({old_var:new_var for old_var, new_var in zip((S.x, S.y, S.z), aesthetic[geometry])})
    return {'equations':res,
            'velocity':v,
            'pressure':p,
            'density':rho,
            'mu':mu,
            'zeta':zeta,
            'coordinate system':S,
            'time':t,
            'coordinates vars':aesthetic[geometry]}

def get_input():

    parser = ArgumentParser()
    parser.add_argument('func_name',
                        help='name of function',
                        type=str)
    args = parser.parse_args()
    return args.func_name

def main():

    func_name = get_input()
    assert(func_name != 'main')
    sympy.pprint(eval(f'{func_name}()'))

if __name__ == '__main__':

    main()

    
    
