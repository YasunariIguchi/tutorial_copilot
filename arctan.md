*arctan z のテーラー展開*
$$
\arctan z = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} z^{2n+1}
$$
*arctan z のテーラー展開の証明*
$$
\begin{aligned}
\frac{d}{dz} \arctan z &= \frac{d}{dz} \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} z^{2n+1} \\
&= \sum_{n=0}^\infty \frac{d}{dz} \frac{(-1)^n}{2n+1} z^{2n+1} \\
&= \sum_{n=0}^\infty (-1)^n z^{2n} \\
&= \frac{1}{1+z^2}
\end{aligned}
$$
$$
\begin{aligned}
\therefore \arctan z &= \int \frac{1}{1+z^2} dz \\
&= \int \frac{1}{1+z^2} \frac{1}{1+z^2} (1+z^2) dz \\
&= \int \frac{1}{(1+z^2)^2} (1+z^2) dz \\
&= \int \frac{1}{(1+z^2)^2} dz + \int \frac{z^2}{(1+z^2)^2} dz \\
&= \int \frac{1}{(1+z^2)^2} dz + \int \frac{1}{1+z^2} dz - \int \frac{1}{1+z^2} dz \\
&= \int \frac{1}{(1+z^2)^2} dz + \arctan z - \int \frac{1}{1+z^2} dz \\
&= \int \frac{1}{(1+z^2)^2} dz + \arctan z - \frac{1}{2} \int \frac{1}{1+z^2} d(1+z^2) \\
&= \int \frac{1}{(1+z^2)^2} dz + \arctan z - \frac{1}{2} \log (1+z^2) \\
&= \int \frac{1}{(1+z^2)^2} dz + \arctan z - \frac{1}{2} \log (1+z^2) + C
\end{aligned}
$$
$$
\begin{aligned}
\therefore \arctan z &= \int \frac{1}{(1+z^2)^2} dz + \arctan z - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\arctan z &= \int \frac{1}{(1+z^2)^2} dz - \frac{1}{2} \log (1+z^2) + C \\
\end{aligned}
$$
