%constants
C_alpha = 30;  %equilibrium extracellular K+ concentration
C_0 = 4;      %initial extracullar K+ concentration
C_t1 = 5.18; %extracellular K+ concentration at time 1
C_t2 = 6.23; %extracellular K+ concentration at time 2

%time range
t0_1 = 0;     %initial time 1
t0_2 = 10;    %initial time 2

%calculate rate constant k
k = (1 / (t0_2 - t0_1)) * log((C_alpha - C_t1) / (C_alpha - C_t2)); 

% Concentration range
C_t0 = linspace(C_0, C_alpha, 100);  %vary C_t0 from C_0 to C_alpha

%calculate time using the equation
time = -(1/k) * log((C_alpha - C_t0) / (C_alpha - C_0));

%plot the graph 
plot(time, C_t0,'linewidth',01.5)
xlabel('Time since death (minutes)')  
ylabel('Extracellular concentration of K+ (mM)') 
title('Extracellular concentration of K+ vs. Time since death')
grid on
