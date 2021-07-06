tokens=('number','plus','minus','mul','division','positive','nagative','lpar','rpar')
t_plus=r'\+'
t_minus=r'\-'
t_mul=r'\*'
t_division=r'\/'
def t_number(t):
    r'[0-9]+'
    t.value=int(t.value)
    return t
t_ignore="\t"
def t_errore(t):
    print("|||egal character %s"%t.values[0])
    t.lexer.skip(1)
    import ply.lex as lex;lex.lex()
    def p_s(p):
        'S:E'
        print(p[1])
        def p_e_e_a(p):
            'E:E plus number'
            p[0]=p[1]+p[3]
            def p_e_e_a1(p):
                'E:E minus number'
                p[0]=p[1]-p[3]
                def p_e_e_a2(p):
                    'E:T mul number'
                    p[0] = p[1] * p[3]
                    def p_e_e_a3(p):
                    'E:T division number'
                    p[0] = p[1] / p[3]
                    def p_e_a(p):
                        'E:number'
                        p[0] = p[1]
                        def p_e_e_a4(p):
                            'E:E positive number'
                            p[0] = p[1] + p[3]
                            def p_e_e_a5(p):
                                'E:E nagative number'
                                p[0] = p[1] _ p[3]
                                def p_e_e_a6(p):
                                    'F:F lpar number'
                                    p[0] = p[6]
                                    def p_e_e_a7(p):
                                        'F:F rpar number'
                                        p[0] = p[8]
                                def p_errore(p):
                                    print("syntax error at '%s'"%t p.value)
                                    import ply.yacc as yacc;
                                    yacc.yacc()
                                    while true:
                                        s=input('calc>')
                                        if s.strip()=="":
                                            break
                                            yacc.parse(s)



