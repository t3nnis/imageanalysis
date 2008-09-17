from numpy import *
def snakedeform(x,y,alpha,beta,gamma,kappa,fx,fy,ITER):
# SNAKEDEFORM2  Deform snake in the given external force field without
#     pressure force
#     [x,y] = snakedeform(x,y,alpha,beta,gamma,kappa,fx,fy,ITER)
#
#     alpha:   elasticity parameter
#     beta:    rigidity parameter
#     gamma:   viscosity parameter
#     kappa:   external force weight
#     fx,fy:   external force field

#      Chenyang Xu and Jerry L. Prince, 4/1/95, 6/17/97
#      Copyright (c) 1995-97 by Chenyang Xu and Jerry L. Prince
#      Image Analysis and Communications Lab, Johns Hopkins University


# generates the parameters for snake

    N = x.shape[1]

    alpha = alpha*ones((1,N),Float) 
    beta = beta*ones((1,N),Float)

# produce the five diagnal vectors
    alpham1 = concatenate((alpha[1:N-1], alpha[0]))
    alphap1 = concatenate((alpha[N-1], alpha[0:N-2]))
    betam1 = concatenate((beta[1:N-1], beta[0]))
    betap1 = concatenate((beta[N-1], beta[0:N-2]))

    a = betam1;
    b = -alpha - 2*beta - 2*betam1
    c = alpha + alphap1 +betam1 + 4*beta + betap1
    d = -alphap1 - 2*beta - 2*betap1
    e = betap1

# generate the parameters matrix
    A = diag(a[0:N-3],-3) + diag(a[N-2:N-1],N-3);
    A = A + diag(b[0:N-2],-2) + diag(b[N-1], N-2);
    A = A + diag(c);
    A = A + diag(d[0:N-2],0) + diag(d[N-1],-(N-2))
    A = A + diag(e[0:N-3],1) + diag(e[N-2:N-1],-(N-3));

    invAI = linalg.inv(A + gamma * diag(ones(1,N),Float));

    for count in arange(0,ITER):
        vfx = interp2(fx,x,y,'*linear')
        fy = interp2(fy,x,y,'*linear')
        
        # deform snake
        x = invAI * (gamma* x + kappa*vfx);
        y = invAI * (gamma* y + kappa*vfy);
    return [x,y]
