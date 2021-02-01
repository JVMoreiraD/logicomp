"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formula import *
from functions import atoms


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    pass
    # ======== YOUR CODE HERE ========
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return not formula.innner
        else:
            return not truth_value(formula.inner, interpretation)
    
    if isinstance(formula, Atom):
        for i in interpretation:
            if formula.__eq__(i):
                return interpretation[i]
        return None
    
    if isinstance(formula, Implies):
        
        left = truth_value(formula.left, interpretation)
        
        right = truth_value(formula.right, interpretation)

        
        if left is None:
            return None
        
        if left is True and right is False:
            return False
        
        else:
            return True

    
    if isinstance(formula, And):
        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        if left is None or right is None:
            return None

        if (left and right):
            return True
        
        return False

    if isinstance(formula, Or):

        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return True if left or right else None if left is None or right is None else False
    
        

def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def is_satisfiable(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========
#    list_atoms = atoms(formula)
#    interpretation = None
#    return sat(formula,list_atoms,interpretation)

#def sat(formula,atoms_list,interpretation):
#    if len(atoms_list) == 0:
#        if truth_value(formula,interpretation):
#            return interpretation
#        else:
#            return False
#    atom_list = atoms_list.pop()
#    interpretation1 = {interpretation}.union(atom_list,True)
#    interpretation2 = {interpretation}.union(atom_list,False)
#    result = sat(formula,atoms_list,interpretation1) or sat(formula,atoms_list,interpretation2)
#    if result!= False:
#       return result
#    return sat(formula,atoms_list,interpretation2)

