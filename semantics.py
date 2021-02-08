"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formula import *
from functions import atoms


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    pass

    if isinstance(formula, Not):
        
        return None if truth_value(formula.inner, interpretation) is None else (not truth_value(formula.inner,interpretation))
    
    if isinstance(formula, Atom):
        for i in interpretation:
            if formula.__eq__(i):
                return interpretation[i]
        return None

    if isinstance(formula, Implies):
        
        left = truth_value(formula.left, interpretation)
        
        right = truth_value(formula.right, interpretation)

        return None if left is None else False if left is True and right is False else True
    
    if isinstance(formula, And):
        
        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return None if (left is None or right is None) else True if (left and right) else False

    if isinstance(formula, Or):

        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return True if left or right else None if left is None or right is None else False
    
        

def is_logical_consequence(premises: list, conclusion):
    
    # ======== YOUR CODE HERE ========

    pass

    return False if is_satisfiable(And(join_formula_and(premises),Not(conclusion))) else True



def join_formula_and(formulas_list: list):
    
    return formulas_list[0] if len(formulas_list) == 1 else And(formulas_list.pop(), join_formula_and(formulas_list.copy()))

def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========

    return True if is_satisfiable(Not(formula)) is False else False

def is_satisfiable(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========
    
    atoms_list = atoms(formula)
    partial_interpretation_ = partial_interpretation(formula)
    
    if partial_interpretation_:
        atoms_list = remove_atoms(atoms_list.copy(), partial_interpretation_)
        return sat(formula, atoms_list, partial_interpretation_)
    
    else:
        return sat(formula, atoms_list, {})


def sat(formula,atoms_list,interpretation):
    
    if len(atoms_list) == 0:
        
        result = truth_value(formula,interpretation)
        
        return interpretation if result else False

    
    atom_ = atoms_list.pop()
    
    interpretation1 = union_dict(interpretation, {atom_: True})
    interpretation2 = union_dict(interpretation, {atom_: False})

    result = sat(formula,atoms_list.copy(),interpretation1)
    
    if result:
        return result
    
    return sat(formula,atoms_list.copy(),interpretation2)

def partial_interpretation(formula):
    if isinstance(formula, Atom):
        
        return{formula: True}
    
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            
            return {formula.inner: False}
    
    if isinstance(formula, And):
        
        left = partial_interpretation(formula.left)
        right = partial_interpretation(formula.right)

        if (left and right):
            return union_dict(left,right)
    
    return None

def remove_atoms(formula, interpretation):
    atoms_list = []
    for atom in atoms_list:
        if atom not in interpretation:
            atoms_list.append(atom)
    return atoms_list
    

def union_dict(interpretation1: dict, interpretation2: dict):
    
    return {**interpretation1,**interpretation2}