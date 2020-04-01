%
% Optimality properties of constrained optimization
% 
% Let x=[x1 x2]
%
% Optimize
% J(x)= x^Tx subject to x1+x2=1
% Introduce Lagrange multiplier m
%
% Unconstrained optimization criterion 
% J(x,m)=x1^2+x2^2 + m(x1+x2-1)
% Set gradient of J equal to zero and solve
%
% m=-2x1, x1=x2=1/2
%
% J(x,m)=x1^2+x2^2 -m(m+1)
%
% Note that J(x,m) has saddle point properties
%
for ii=1:100, xi=-5+ii/10; 
    for jj=1:100,  mj=-5+jj/10; X(ii,jj)=xi; Y(ii,jj)=mj;
        %J(ii,jj)=xi*xi-mj*(mj+1);
        J(ii,jj)=xi*xi+mj*(xi+xi-1);
    end 
end
figure, mesh(X,Y,J)
xlabel('x1'), ylabel('m'), zlabel('J(x1,m)')