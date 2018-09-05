pub enum Operator {
    // `+`
    Add, 
    // `-`
    Sub,
    // `*`
    Mul,
}

pub enum Token {
    Operator(Operator),
    Operand(isize),
}

/// Evaluates the postix expression.
///
/// Input: a postfix expression, where each element contains an operator or operand.
/// Returns: if the postfix expression is valid, returns `Some(value)`;
///     otherwise, returns `None`.
pub fn eval(tokens: &[Token]) -> Option<isize> {
    // TODO
    let mut i1: Vec<isize> = vec![];
    let mut i2: isize;
    let mut i3: isize;
    for i in {tokens}{
        match i {
        	&Token::Operator(ref operator) => {
                if i1.len() >= 2{
            		if let Some(i3) = i1.pop(){
            			if let Some(i2) = i1.pop(){
            				match operator{
            					&Operator::Add => i1.push(i2 + i3),
            					&Operator::Sub => i1.push(i2 - i3),
            					&Operator::Mul => i1.push(i2 * i3),
            				}
            			}
            		}
                }else{
                    return None
                }
        	}
        	&Token::Operand(ab) => i1.push(ab),
        }
    }
    if i1.len() == 1{
        return Some(i1[0])
    }else{
        return None
    }
}
