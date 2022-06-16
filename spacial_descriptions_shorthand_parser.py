shorthand_string_ex = 'CACB&CASBSG-SACG&CASBCG+SASG\\\\' \
                      'SACB&SASBSG+CACG&SASBCG-CASG\\\\' \
                      '-SB&CBSG&CBCG'

def get_latex_string(shorthand_string):
    
    return shorthand_string.replace( 'A'         , '\\alpha'        ) \
                           .replace( 'B'         , '\\beta'         ) \
                           .replace( 'G'         , '\\gamma'        ) \
                                                                      \
                           .replace( 'S'         , '\\mathrm{s}\\,' ) \
                           .replace( 'C'         , '\\mathrm{c}\\,' ) \
                                                                      \
                           .replace( 'a\\mathrm' , 'a\\,\\mathrm'   )

latex_string_ex = get_latex_string(shorthand_string_ex)

from numpy import array, sin, cos

def get_python_string(shorthand_string):
    
    return 'array([[' + shorthand_string.replace( 'A'    , '(alpha)' ) \
                                        .replace( 'B'    , '(beta)'  ) \
                                        .replace( 'G'    , '(gamma)' ) \
                                                                       \
                                        .replace( ')S'   , ')*S'     ) \
                                        .replace( ')C'   , ')*C'     ) \
                                                                       \
                                        .replace( 'S'    , 'sin'     ) \
                                        .replace( 'C'    , 'cos'     ) \
                                                                       \
                                        .replace( ')+'   , ') + '    ) \
                                        .replace( ')-'   , ') - '    ) \
                                                                       \
                                        .replace( '&'    , ', '      ) \
                                        .replace( '\\\\' , '], ['    ) + ']])'

python_string_ex = get_python_string(shorthand_string_ex)

# alpha = ...
#  beta = ...
# gamma = ...

# print(eval(python_string_ex))

def parse(expression, **kwargs):
    
    python_string = get_python_string(shorthand_string = expression)
    return eval(python_string)
