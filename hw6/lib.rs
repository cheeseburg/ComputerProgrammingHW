#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Operator {
    // `+`
    Add,
    // `-`
    Sub,
    // `*`
    Mul,
    // `/`
    Div,
}

#[derive(Debug, PartialEq)]
pub enum InfixToken {
    Operator(Operator),
    Operand(isize),
    LeftParen,
    RightParen,
}

#[derive(Debug, PartialEq)]
pub enum PostfixToken {
    Operator(Operator),
    Operand(isize),
}

/// Transforms an infix expression to a postfix expression.
///
/// If the infix expression is valid, outputs `Some(_)`; 
/// otherwise, outputs `None`.
pub fn infix_to_postfix(tokens: &[InfixToken]) -> Option<Vec<PostfixToken>> {
    let mut s2 = vec![];///for num
    let mut s1 = vec![];///for Operand
    let mut s3:Vec<PostfixToken> = vec![];
    let mut s0:Vec<&InfixToken> = vec![];
    let mut i6 = 0;
    let mut done = false;
    let mut count = 0;
    let mut gg = false;
    if {tokens}.len() == 0{
        return None
    }else{
        for g in {tokens}{
            s0.push(g);
        }
        let count1 = s0.len()-1;
        let mut count2 = 0;
        let mut count3 = 0;
        for i in {tokens}{
            if i == &InfixToken::RightParen{
                count2 = count2 + 1;
            }else if i == &InfixToken::LeftParen{
                count3 = count3 + 1;
            }
            if s0[0] == &InfixToken::RightParen{
                return None;
            }else if s0[0] == &InfixToken::Operator(Operator::Add){
                return None;
            }else if s0[0] == &InfixToken::Operator(Operator::Sub){
                return None;
            }else if s0[0] == &InfixToken::Operator(Operator::Mul){
                return None;
            }else if s0[0] == &InfixToken::Operator(Operator::Div){
                return None;
            }else if s0[count1] == &InfixToken::LeftParen{
                return None;
            }else if s0[count1] == &InfixToken::Operator(Operator::Add){
                return None;
            }else if s0[count1] == &InfixToken::Operator(Operator::Sub){
                return None;
            }else if s0[count1] == &InfixToken::Operator(Operator::Mul){
                return None;
            }else if s0[count1] == &InfixToken::Operator(Operator::Div){
                return None;
            }else{
                match i {
                    &InfixToken::Operator(ref operator) => {
                        if count+1 < s0.len(){
                            if s0[count+1] == &InfixToken::Operator(Operator::Add){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Sub){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Mul){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Div){
                                return None;
                            }else if s0[count+1] == &InfixToken::RightParen{
                                return None;
                            }else{
                                    match operator {
                                        &Operator::Add|&Operator::Sub => {
                                            if s0[count+1] == &InfixToken::RightParen{
                                                return None;
                                            }else{
                                                if s1.len() == 0{
                                                    s1.push(i);
                                                }else{
                                                    let mut ss = s1.len()-1;
                                                    if let Some(mut i3) = Some(s1[ss]){
                                                        match i3 {
                                                            &InfixToken::LeftParen => s1.push(i),
                                                            &InfixToken::Operator(Operator::Mul) => {
                                                                s2.push(s1.pop());
                                                                if let Some(mut a) = s1.pop(){
                                                                    match a {
                                                                        &InfixToken::LeftParen => {
                                                                            s1.push(a);
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Mul) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Sub) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Div) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Add) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        }, 
                                                                        _ => continue,
                                                                    }
                                                                }
                                                            },
                                                            &InfixToken::Operator(Operator::Sub) => {
                                                                s2.push(s1.pop());
                                                                if s1.len() == 0{
                                                                    s1.push(i);
                                                                }else{
                                                                    if let Some(mut a) = s1.pop(){
                                                                        match a {
                                                                            &InfixToken::LeftParen => {
                                                                                s1.push(a);
                                                                                s1.push(i);
                                                                            },
                                                                            &InfixToken::Operator(Operator::Mul) => {
                                                                                s2.push(Some(a));
                                                                                s1.push(i);
                                                                            },
                                                                            &InfixToken::Operator(Operator::Sub) => {
                                                                                s2.push(Some(a));
                                                                                s1.push(i);
                                                                            },
                                                                            &InfixToken::Operator(Operator::Div) => {
                                                                                s2.push(Some(a));
                                                                                s1.push(i);
                                                                            },
                                                                            &InfixToken::Operator(Operator::Add) => {
                                                                                s2.push(Some(a));
                                                                                s1.push(i);
                                                                            }, 
                                                                            _ => continue,
                                                                        }
                                                                    }
                                                                }
                                                            },
                                                            &InfixToken::Operator(Operator::Div) => {
                                                                s2.push(s1.pop());
                                                                if let Some(mut a) = s1.pop(){
                                                                    match a {
                                                                        &InfixToken::LeftParen => {
                                                                            s1.push(a);
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Mul) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Sub) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Div) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Add) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        }, 
                                                                        _ => continue,
                                                                    }
                                                                }
                                                            },
                                                            &InfixToken::Operator(Operator::Add) => {
                                                                s2.push(s1.pop());
                                                                if let Some(mut a) = s1.pop(){
                                                                    match a {
                                                                        &InfixToken::LeftParen => {
                                                                            s1.push(a);
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Mul) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Sub) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Div) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        },
                                                                        &InfixToken::Operator(Operator::Add) => {
                                                                            s2.push(Some(a));
                                                                            s1.push(i);
                                                                        }, 
                                                                        _ => continue,
                                                                    }
                                                                }
                                                            }, 
                                                            _ => continue,
                                                        }
                                                    }
                                                }
                                                if s1.len() == 0 {
                                                    s1.push(i)
                                                }
                                            }
                                        }
                                        &Operator::Mul|&Operator::Div => {
                                            if s0[count+1] == &InfixToken::RightParen{
                                                return None;
                                            }else{
                                                if s1.len() == 0{
                                                    s1.push(i);
                                                }else{
                                                    let mut sss = s1.len()-1;
                                                    if let Some(mut i4) = Some(s1[sss]){
                                                        match i4 {
                                                            &InfixToken::LeftParen => s1.push(i),
                                                            &InfixToken::Operator(Operator::Add) => s1.push(i),
                                                            &InfixToken::Operator(Operator::Sub) => s1.push(i),
                                                            &InfixToken::Operator(Operator::Mul) => {
                                                                s2.push(s1.pop());
                                                                s1.push(i);
                                                            },
                                                            &InfixToken::Operator(Operator::Div) => {
                                                                s2.push(s1.pop());
                                                                s1.push(i);
                                                            },
                                                            _ => continue,
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                            }
                        }else{

                        }
                    }
                    &InfixToken::Operand(anum) => {
                        if count+1 < s0.len(){
                            if s0[count+1] == &InfixToken::Operator(Operator::Add){
                                s2.push(Some(i));
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Sub){
                                s2.push(Some(i));
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Mul){
                                s2.push(Some(i));
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Div){
                                s2.push(Some(i));
                            }else if s0[count+1] == &InfixToken::LeftParen{
                                s2.push(Some(i));
                            }else if s0[count+1] == &InfixToken::RightParen{
                                s2.push(Some(i));
                            }else{
                                return None
                            }
                        }else{
                            s2.push(Some(i));
                        }
                    }
                    &InfixToken::LeftParen => {
                        if count+1 < s0.len(){
                            if s0[count+1] == &InfixToken::Operator(Operator::Add){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Sub){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Mul){
                                return None;
                            }else if s0[count+1] == &InfixToken::Operator(Operator::Div){
                                return None;
                            }else if s0[count+1] == &InfixToken::RightParen{
                                return None;
                            }else{
                                s1.push(i);
                            }
                        }else{
                            s1.push(i);
                        }
                    }
                    &InfixToken::RightParen =>{
                        if count+1 < s0.len(){
                            if s0[count+1] == &InfixToken::LeftParen{
                                return None
                            }else{
                                while !done{
                                    if let Some(mut i1) = Some(s1.pop()){
                                        match i1{
                                            Some(&InfixToken::LeftParen) => done = true,
                                            Some(&InfixToken::Operator(Operator::Mul)) => s2.push(i1),
                                            Some(&InfixToken::Operator(Operator::Div)) => s2.push(i1),
                                            Some(&InfixToken::Operator(Operator::Add)) => s2.push(i1),
                                            Some(&InfixToken::Operator(Operator::Sub)) => s2.push(i1),
                                            _ => continue,
                                        }
                                    }
                                }
                                done = false;
                            }
                        }else{
                            while !done{
                                if let Some(mut i1) = Some(s1.pop()){
                                    match i1{
                                        Some(&InfixToken::LeftParen) => done = true,
                                        Some(&InfixToken::Operator(Operator::Mul)) => s2.push(i1),
                                        Some(&InfixToken::Operator(Operator::Div)) => s2.push(i1),
                                        Some(&InfixToken::Operator(Operator::Add)) => s2.push(i1),
                                        Some(&InfixToken::Operator(Operator::Sub)) => s2.push(i1),
                                        _ => break,
                                    }
                                }
                            }
                            done = false;
                        }
                    },
                }
            }
            count = count + 1;
        }
        if count2 == count3{
            done = false;
        }else{
            return None;
        }
        loop {
            let mut n = s1.len();
            if n == 0{
                break;
            }else{
                s2.push(s1.pop());
            }
        }
        while i6 < s2.len(){
            if let Some(mut i5) = s2[i6]{
                match i5{
                    &InfixToken::Operator(operator) => s3.push(PostfixToken::Operator(operator)),
                    &InfixToken::Operand(uu) => s3.push(PostfixToken::Operand(uu)),
                    _ => break,
                }
            i6 = i6 + 1
            }
        }
        if eval(&s3) == None{
            return None
        }else{
            return Some(s3)
        }
    }
}

pub fn eval(tokens: &[PostfixToken]) -> Option<isize> {
    // TODO
    let mut i1: Vec<isize> = vec![];
    let mut i2: isize;
    let mut i3: isize;
    for i in {tokens}{
        match i {
            &PostfixToken::Operator(ref operator) => {
                if i1.len() >= 2{
                    if let Some(i3) = i1.pop(){
                        if let Some(i2) = i1.pop(){
                            match operator{
                                &Operator::Add => i1.push(i2 + i3),
                                &Operator::Sub => i1.push(i2 - i3),
                                &Operator::Mul => i1.push(i2 * i3),
                                &Operator::Div => i1.push(i2 + i3),
                            }
                        }
                    }
                }else{
                    return None
                }
            }
            &PostfixToken::Operand(ab) => i1.push(ab),
        }
    }
    if i1.len() == 1{
        return Some(i1[0])
    }else{
        return None
    }
}

